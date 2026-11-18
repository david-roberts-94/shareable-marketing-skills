"""Group the kept words into captions.

    python captions.py work/words-cut.json work/captions.json [--max-words 3] [--pause 0.3]

Each caption: {text, start, end, words}. A new caption starts at a sentence end, at a pause longer
than --pause, or when it reaches --max-words. A caption ends at the next caption's start, or
0.3 s after its last word at a pause. Use --max-words from the brand sheet. Build the caption
clips in HyperFrames from this file; never type captions by hand.
"""
import argparse, json, re
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("words"); ap.add_argument("out")
ap.add_argument("--max-words", type=int, default=3)
ap.add_argument("--pause", type=float, default=0.3)
a = ap.parse_args()
W = json.loads(Path(a.words).read_text())

groups, cur = [], []
for i, w in enumerate(W):
    cur.append(w)
    nxt = W[i + 1] if i + 1 < len(W) else None
    if (nxt is None or len(cur) >= a.max_words or re.search(r"[.?!,:;]$", w["word"])
            or nxt["start"] - w["end"] > a.pause):
        groups.append(cur); cur = []

caps = []
for k, g in enumerate(groups):
    nxt = groups[k + 1][0]["start"] if k + 1 < len(groups) else None
    end = g[-1]["end"] + 0.3
    if nxt is not None:
        end = nxt if nxt - g[-1]["end"] <= a.pause else min(end, nxt)
    text = " ".join(w["word"] for w in g)
    caps.append({"text": re.sub(r"[.,;:]$", "", text), "start": g[0]["start"], "end": round(end, 3),
                 "words": [{"word": w["word"], "start": w["start"], "end": w["end"]} for w in g]})
Path(a.out).write_text(json.dumps(caps, indent=1))
print(f"{len(caps)} captions from {len(W)} words -> {a.out}")
