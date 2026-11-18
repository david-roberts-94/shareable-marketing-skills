"""Render the cut take: one clip per kept part, joined, framed to 1080 x 1920, voice at -14 LUFS.

    python base.py sources/take.mp4 work/audio.wav work/cut-list.json work/base.mp4 [--crop-x auto|<px>]

- Keeps the take's frame rate (29.97 becomes 30). Prints the rate: set data-fps to it in HyperFrames.
- A landscape take is cropped to a vertical frame. --crop-x is the left edge of the crop in the
  scaled frame; "auto" centres it. Look at a frame and move it so the face is in the middle.
- 10 ms fades at each join stop clicks. The voice is brought to about -14 LUFS (compressor + loudnorm).
"""
import argparse, json, re, shutil, tempfile
from pathlib import Path
from common import output_fps, probe, run

ap = argparse.ArgumentParser()
ap.add_argument("take"); ap.add_argument("audio"); ap.add_argument("cutlist"); ap.add_argument("out")
ap.add_argument("--crop-x", default="auto")
ap.add_argument("--words", help="work/words-cut.json: re-time it to the real part lengths (frames round each part)")
a = ap.parse_args()

info = probe(a.take)
fps = output_fps(info["fps"])
w, h = info["width"], info["height"]
scale = max(1080 / w, 1920 / h)
sw = int(round(w * scale / 2) * 2)
x = (sw - 1080) // 2 if a.crop_x == "auto" else int(a.crop_x)
vf = f"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920:{x}:(ih-1920)/2,fps={fps}"
if w > h:
    print(f"Landscape take ({w}x{h}): scaled {scale:.2f}x, crop x={x} of {sw}. The picture will be softer.")

parts = json.loads(Path(a.cutlist).read_text())
tmp = Path(tempfile.mkdtemp(prefix="parts_"))
lines = []
for n, p in enumerate(parts, 1):
    s, e = p["start"], p["end"]
    L = e - s
    f = tmp / f"part_{n:03d}.mov"
    # Seek each input (not the output), so the part starts at t=0 and the fades land right.
    # With re-encoding, input seeking is frame-accurate.
    run(["ffmpeg", "-nostdin", "-v", "error", "-y",
         "-ss", f"{s:.3f}", "-to", f"{e:.3f}", "-i", a.take,
         "-ss", f"{s:.3f}", "-to", f"{e:.3f}", "-i", a.audio,
         "-map", "0:v:0", "-map", "1:a:0", "-vf", vf,
         "-af", f"afade=t=in:d=0.01,afade=t=out:st={max(0, L - 0.01):.3f}:d=0.01",
         "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p",
         "-c:a", "pcm_s16le", "-ar", "48000", str(f)])
    lines.append(f"file '{f.as_posix()}'")
    p["real"] = probe(f)["duration"]
(tmp / "list.txt").write_text("\n".join(lines) + "\n")
joined = tmp / "joined.mov"
run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(tmp / "list.txt"),
     "-c", "copy", str(joined)])

# The voice to about -14 LUFS: a gentle speech compressor, then loudnorm (alone, it lands about 2 dB quiet on peaky speech).
run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(joined), "-c:v", "libx264", "-crf", "17",
     "-preset", "medium", "-pix_fmt", "yuv420p",
     "-af", "acompressor=threshold=-24dB:ratio=3:attack=5:release=120:makeup=4,loudnorm=I=-14:TP=-1.5:LRA=11",
     "-ar", "48000", "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", a.out])
shutil.rmtree(tmp, ignore_errors=True)

total = sum(p["real"] for p in parts)
if a.words:
    # Move each word by the difference between the planned and the real part starts.
    W = json.loads(Path(a.words).read_text())
    plan_acc = real_acc = 0.0
    bounds = []
    for p in parts:
        bounds.append((plan_acc, plan_acc + p["end"] - p["start"], real_acc - plan_acc))
        plan_acc += p["end"] - p["start"]; real_acc += p["real"]
    for w in W:
        shift = next((d for lo, hi, d in bounds if lo - 0.001 <= w["start"] < hi), bounds[-1][2])
        w["start"] = round(w["start"] + shift, 3); w["end"] = round(w["end"] + shift, 3)
    Path(a.words).write_text(json.dumps(W, indent=1))
    print(f"re-timed {len(W)} words in {a.words}")
got = probe(a.out)["duration"]
print(f"base: {a.out}  {got:.2f} s (parts {total:.2f} s)  fps={fps}")
if abs(got - total) > 0.06:
    print("WARNING: the length differs from the parts by more than 0.06 s. Check the joins.")
