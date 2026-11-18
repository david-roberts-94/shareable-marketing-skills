"""Turn a Whisper JSON (openai-whisper or mlx-whisper) into words.json, and fix names from the script.

    python words.py work/audio.json work/words.json [--fix "WellFound.=Wellfound." --fix "YouNeed.=Uneed."]

Compare the words with the script and pass one --fix for each name that Whisper heard wrong.
Captions and graphics use these spellings.
"""
import argparse, json
from pathlib import Path
from common import load_words

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--fix", action="append", default=[], help='"heard=right", for example "ProductHunt=Product Hunt"')
a = ap.parse_args()
fix = dict(f.split("=", 1) for f in a.fix)
words = load_words(a.src)
for w in words:
    w["word"] = fix.get(w["word"], w["word"])
Path(a.out).write_text(json.dumps(words, indent=1))
print(f"{len(words)} words -> {a.out}")
print(" ".join(w["word"] for w in words))
