"""Shared helpers for the video-edit scripts. Python 3.9+, standard library only, plus ffmpeg/ffprobe on PATH."""
import json, math, re, subprocess, wave, array
from pathlib import Path


def run(cmd, quiet=True):
    """Run a command; return stdout+stderr as text. Raises on a non-zero exit."""
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"command failed: {' '.join(map(str, cmd[:3]))} ...\n{r.stderr[-2000:]}")
    return r.stdout + r.stderr


def probe(path):
    out = run(["ffprobe", "-v", "error", "-show_entries",
               "stream=codec_type,width,height,r_frame_rate:stream_tags=rotate:stream_side_data=rotation:format=duration",
               "-of", "json", str(path)])
    d = json.loads(out)
    v = next((s for s in d.get("streams", []) if s.get("codec_type") == "video"), None)
    info = {"duration": float(d["format"]["duration"])}
    if v:
        num, den = v["r_frame_rate"].split("/")
        rot = 0
        for sd in v.get("side_data_list", []) or []:
            rot = int(sd.get("rotation", 0) or 0)
        rot = int((v.get("tags") or {}).get("rotate", rot) or 0)
        w, h = v["width"], v["height"]
        if abs(rot) in (90, 270):
            w, h = h, w
        info.update(width=w, height=h, fps=v["r_frame_rate"], fps_float=float(num) / float(den))
    return info


def output_fps(fps_str):
    """Keep the take's frame rate, except 29.97 becomes 30."""
    num, den = fps_str.split("/")
    f = float(num) / float(den)
    return "30" if abs(f - 29.97) < 0.02 else fps_str


def load_words(path):
    """Read words from a Whisper JSON (openai-whisper or mlx-whisper) or from a words.json list."""
    d = json.loads(Path(path).read_text())
    if isinstance(d, list):
        return d
    words = []
    for seg in d.get("segments", []):
        for w in seg.get("words", []):
            t = w["word"].strip()
            if t:
                words.append({"word": t, "start": round(float(w["start"]), 3), "end": round(float(w["end"]), 3)})
    return words


def norm(word):
    return re.sub(r"[^a-z0-9']", "", word.lower())


class Wav:
    """16-bit PCM WAV reader for short RMS windows."""

    def __init__(self, path):
        with wave.open(str(path), "rb") as f:
            if f.getsampwidth() != 2:
                raise SystemExit("audio must be 16-bit PCM WAV (make it with: ffmpeg -i in -c:a pcm_s16le out.wav)")
            self.sr, self.ch, self.n = f.getframerate(), f.getnchannels(), f.getnframes()
            self.data = array.array("h", f.readframes(self.n))

    def db(self, t, win=0.02):
        a = max(0, int(t * self.sr)) * self.ch
        b = min(self.n, int((t + win) * self.sr)) * self.ch
        if b <= a:
            return -120.0
        seg = self.data[a:b]
        ms = sum(x * x for x in seg) / len(seg)
        return 20 * math.log10(math.sqrt(ms) / 32768 + 1e-9)
