"""Run the machine checks on a render and make contact sheets.

    python checks.py edit/<video>   (expects final.mp4, work/base.mp4, work/words-cut.json, work/captions.json)

Writes work/checks.md and work/sheets/s01.jpg ... (a frame every 0.5 s). Checks 7, 8, and 10 of
references/checks.md need your eyes: look at every sheet and every snapshot.
"""
import json, re, sys
from pathlib import Path
from common import norm, probe, run

V = Path(sys.argv[1])
final, base = V / "final.mp4", V / "work" / "base.mp4"
lines, fail = [], False


def res(n, name, ok, detail):
    global fail
    fail |= not ok
    lines.append(f"{n}. {name}: {'PASS' if ok else 'FAIL'} ({detail})")


f, b = probe(final), probe(base)
res(1, "Size and frame rate", (f["width"], f["height"]) == (1080, 1920), f"{f['width']}x{f['height']} at {f['fps_float']:.3f} fps")
res(2, "Length", abs(f["duration"] - b["duration"]) <= 0.15, f"{f['duration']:.2f} s, base {b['duration']:.2f} s")

e = run(["ffmpeg", "-nostdin", "-hide_banner", "-nostats", "-i", str(final), "-af", "ebur128=peak=true", "-f", "null", "-"])
summary = e[e.rfind("Summary:"):]
I = float(re.search(r"I:\s+(-?[\d.]+) LUFS", summary).group(1))
tp = float(re.search(r"Peak:\s+(-?[\d.]+) dBFS", summary).group(1))
res(3, "Loudness", abs(I + 14) <= 1 and tp <= -1, f"{I:.1f} LUFS, true peak {tp:.1f} dB")

cw = Path(V / "work" / "captions.json")
if cw.exists():
    caps = " ".join(c["text"] for c in json.loads(cw.read_text())).split()
    spoken = " ".join(w["word"] for w in json.loads((V / "work" / "words-cut.json").read_text())).split()
    ok = [norm(x) for x in caps if norm(x)] == [norm(x) for x in spoken if norm(x)]
    res(4, "Captions", ok, f"{len(caps)} caption words, {len(spoken)} spoken")
else:
    res(4, "Captions", False, "work/captions.json not found")

bl = run(["ffmpeg", "-nostdin", "-hide_banner", "-nostats", "-i", str(final), "-vf", "blackdetect=d=0.03:pix_th=0.10", "-an", "-f", "null", "-"])
n_black = bl.count("black_start")
res(5, "Black frames", n_black == 0, f"{n_black} found")
fr = run(["ffmpeg", "-nostdin", "-hide_banner", "-nostats", "-i", str(final), "-vf", "freezedetect=n=0.003:d=0.5", "-an", "-f", "null", "-"])
n_freeze = fr.count("freeze_start")
lines.append(f"6. Frozen frames: {n_freeze} found (OK only where a still graphic covers the frame)")

sheets = V / "work" / "sheets"
sheets.mkdir(parents=True, exist_ok=True)
for old in sheets.glob("s*.jpg"):
    old.unlink()
run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(final), "-vf", "fps=2,scale=270:-1,tile=6x2", str(sheets / "s%02d.jpg")])
lines.append(f"9. Contact sheets: {len(list(sheets.glob('s*.jpg')))} in work/sheets (look at every one; empty black tiles at the end are padding)")
lines.append("7, 8, 10. Sync, safe zones, and the plan: look at the frames yourself.")

(V / "work" / "checks.md").write_text("# Checks\n\n" + "\n".join(f"- {l}" for l in lines) + "\n")
print("\n".join(lines))
sys.exit(1 if fail else 0)
