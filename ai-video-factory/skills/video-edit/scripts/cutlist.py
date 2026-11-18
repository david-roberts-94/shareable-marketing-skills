"""Make the cut list from word timestamps: cut silences and retakes, keep a pause after list numbers.

    python cutlist.py work/words.json work/audio.wav --out work [--gap 0.35] [--list-pause 0.4]

Reads words.json (a list of {word, start, end}, names already fixed from the script) and the
16-bit WAV the words came from. Writes:
  work/cut-list.json   the parts of audio.wav to keep: [{start, end}]
  work/words-cut.json  every kept word with its time on the new (cut) timeline
  work/cut-report.md   what was cut, for the edit plan
The brand sheet's numbers can override the defaults with the flags.
"""
import argparse, json, re
from pathlib import Path
from common import Wav, norm

ap = argparse.ArgumentParser()
ap.add_argument("words"); ap.add_argument("audio"); ap.add_argument("--out", default=".")
ap.add_argument("--gap", type=float, default=0.35, help="cut a silence longer than this (s)")
ap.add_argument("--pad-before", type=float, default=0.06, help="keep this much before a word (s)")
ap.add_argument("--list-pause", type=float, default=0.4, help="pause kept after a list number (s)")
ap.add_argument("--tail-db", type=float, default=-50, help="extend a part's end until the sound is below this")
ap.add_argument("--min-part", type=float, default=0.25)
ap.add_argument("--retake-words", type=int, default=4)
ap.add_argument("--retake-window", type=float, default=30)
a = ap.parse_args()
out = Path(a.out)
words = json.loads(Path(a.words).read_text())
wav = Wav(a.audio)
dur = wav.n / wav.sr
report = []

# 1. Sentences, and retakes: a sentence whose first N words return within the window is dropped.
sents, cur = [], []
for i, w in enumerate(words):
    cur.append(i)
    if re.search(r"[.?!]$", w["word"]):
        sents.append(cur); cur = []
if cur:
    sents.append(cur)
key = lambda s: tuple(norm(words[i]["word"]) for i in s[: a.retake_words])
drop = set()
for x, s in enumerate(sents):
    if len(s) < a.retake_words:
        continue
    for t in sents[x + 1:]:
        if words[t[0]]["start"] - words[s[0]]["start"] > a.retake_window:
            break
        if key(t) == key(s):
            drop.update(s)
            old = " ".join(words[i]["word"] for i in s)
            new = " ".join(words[i]["word"] for i in t)
            note = "same words" if old.lower() == new.lower() else "THE WORDS DIFFER: ask in the plan"
            report.append(f"- Retake cut at {words[s[0]]['start']:.2f} s: “{old}” (kept the later take: “{new}”; {note})")
            break
kept = [w for i, w in enumerate(words) if i not in drop]

# 2. Parts: split where the gap is longer than --gap. A list number keeps its pause.
LIST = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "first", "second",
        "third", "next", "then", "last", "finally", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}
parts, start = [], None
silences = 0
for i, w in enumerate(kept):
    if start is None:
        start = max(0.0, w["start"] - a.pad_before)
    nxt = kept[i + 1] if i + 1 < len(kept) else None
    gap = (nxt["start"] - w["end"]) if nxt else None
    if nxt is None or gap > a.gap:
        end = w["end"]
        hold = a.list_pause if norm(w["word"]) in LIST and w["word"].endswith((":", ",")) or (
            norm(w["word"]) in LIST and (i == 0 or re.search(r"[.?!:]$", kept[i - 1]["word"]))) else 0
        limit = (nxt["start"] - a.pad_before) if nxt else dur
        # Whisper ends words early: extend until the sound is quiet (max 0.3 s).
        t = end
        while t < min(end + 0.3, limit) and wav.db(t) > a.tail_db:
            t += 0.01
        end = max(t + 0.04, end + hold) if hold else t + 0.04
        end = min(end, limit, dur)
        parts.append({"start": round(start, 3), "end": round(end, 3)})
        if nxt is not None:
            silences += 1
        start = None

parts = [p for p in parts if p["end"] - p["start"] >= a.min_part]

# 3. Words on the new timeline.
cut, acc = [], 0.0
for p in parts:
    for w in kept:
        if w["start"] >= p["start"] - 0.001 and w["start"] < p["end"]:
            off = acc - p["start"]
            cut.append({"word": w["word"], "start": round(w["start"] + off, 3), "end": round(min(w["end"], p["end"]) + off, 3)})
    acc += p["end"] - p["start"]

(out / "cut-list.json").write_text(json.dumps(parts, indent=1))
(out / "words-cut.json").write_text(json.dumps(cut, indent=1))
head = [f"# Cut report", "", f"- Length: {dur:.2f} s → {acc:.2f} s",
        f"- Parts kept: {len(parts)}. Silences cut: {silences}. Retakes cut: {sum(1 for r in report if 'Retake' in r)}.",
        f"- Words kept: {len(cut)} of {len(words)}."]
(out / "cut-report.md").write_text("\n".join(head + report) + "\n")
print("\n".join(head + report))
