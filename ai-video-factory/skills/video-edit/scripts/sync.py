"""Find the offset between the camera sound and a separate mic file, from their transcripts.

    python sync.py work/camera.json work/mic.json

Both files are Whisper JSON transcripts of the FULL recordings (not the first seconds: Whisper
can invent words in a silent start). The script matches runs of the same words and prints the
median time difference. offset_s > 0 means a word in the mic file happens offset_s later in the
camera file, so shift the mic by +offset_s (ffmpeg: -itsoffset offset_s on the mic input, or
adelay). It also prints the spread: more than 0.04 s means the files may be different takes.
"""
import difflib, statistics, sys
from common import load_words, norm

cam, mic = load_words(sys.argv[1]), load_words(sys.argv[2])
a, b = [norm(w["word"]) for w in cam], [norm(w["word"]) for w in mic]
diffs = []
for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
    if blk.size >= 3:  # only runs of 3+ words, so one common word cannot fool it
        for k in range(blk.size):
            diffs.append(cam[blk.a + k]["start"] - mic[blk.b + k]["start"])
if len(diffs) < 10:
    raise SystemExit(f"only {len(diffs)} matching words: these may not be the same take")
off = statistics.median(diffs)
spread = statistics.median(abs(d - off) for d in diffs)
print(f"offset_s={off:.3f} matched_words={len(diffs)} spread_s={spread:.3f}")
if spread > 0.04:
    print("WARNING: the spread is high. Check that both files are the same take.")
