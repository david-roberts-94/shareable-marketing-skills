# Cut the take

All files go in `edit/<video>/work/`. The scripts are in this skill's `scripts/` folder. They need
only Python 3.9 or newer and FFmpeg: no extra packages. Below, `S` is the path to that folder
(for example `.claude/skills/video-edit/scripts`) and `V` is `edit/<video>`.

On Windows, use `py` in place of `python3`, and run the commands in PowerShell (each command is on
one line, so there is nothing to change).

## 1. Probe

```bash
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate -of json sources/<take>
```

- **Frame rate:** the output keeps the take's rate (29.97 becomes 30). `base.py` prints it. Use
  the same rate for `data-fps` in HyperFrames.
- **A landscape take** (wider than tall) is cropped to a vertical frame. Take a frame
  (`ffmpeg -ss 5 -i sources/<take> -frames:v 1 V/work/frame.jpg`), look at it, and find the x of
  the face. Tell the creator that a landscape take looks softer than a vertical one.

## 2. Make the sound file

Extract the sound as a 16-bit WAV. With a separate mic file, use the mic: it sounds better.

```bash
ffmpeg -y -i sources/<take> -vn -ac 1 -ar 48000 -c:a pcm_s16le V/work/camera.wav
ffmpeg -y -i sources/<mic file> -vn -ac 1 -ar 48000 -c:a pcm_s16le V/work/mic.wav
```

With no mic file, copy `camera.wav` to `audio.wav` and go to step 4.

## 3. Sync the mic file (only when there is one)

1. Transcribe both **full** files (step 4 shows the command). Do not transcribe only the first
   seconds: Whisper can invent words in a silent start.
2. Find the offset:

   ```bash
   python3 S/sync.py V/work/camera.json V/work/mic.json
   ```

   It prints `offset_s` and `spread_s`. A spread above 0.04 s means the files may be different
   takes: ask the creator.
3. Shift the mic by the offset and cut it to the camera's length:

   ```bash
   # offset_s > 0: delay the mic. (ms = offset_s × 1000)
   ffmpeg -y -i V/work/mic.wav -af "adelay=<ms>:all=1,apad" -t <camera length> -c:a pcm_s16le V/work/audio.wav
   # offset_s < 0: trim the start of the mic.
   ffmpeg -y -ss <-offset_s> -i V/work/mic.wav -af apad -t <camera length> -c:a pcm_s16le V/work/audio.wav
   ```

## 4. Transcribe

Whisper with word timestamps:

```bash
# Any computer (openai-whisper)
whisper V/work/audio.wav --model medium --language en --word_timestamps True --output_format json --output_dir V/work

# Mac with Apple silicon (faster)
mlx_whisper V/work/audio.wav --model mlx-community/whisper-large-v3-turbo --word-timestamps True --output-format json --output-dir V/work
```

Then make `words.json`, and fix the names that Whisper heard wrong. Compare the words with the
script: brand names, tools, people.

```bash
python3 S/words.py V/work/audio.json V/work/words.json --fix "WellFound.=Wellfound." --fix "ProductHunt=Product Hunt"
```

## 5. Make the cut list

```bash
python3 S/cutlist.py V/work/words.json V/work/audio.wav --out V/work --gap 0.35 --list-pause 0.4
```

Use the brand sheet's numbers for `--gap` (the longest silence to keep) and `--list-pause` (the
pause after a list number). The script:

- cuts every silence longer than `--gap`, and keeps 0.06 s before each word;
- extends the end of each part until the sound is quiet, because Whisper ends words early;
- keeps the pause after a list number ("One:", "Next,", "Then");
- cuts a retake when the same sentence starts again within 30 s, and keeps the later take;
- writes `cut-list.json`, `words-cut.json`, and `cut-report.md`.

Read `cut-report.md`. **When a retake's words differ from the take it replaced** (the report says
"THE WORDS DIFFER"), keep the later take and ask the creator in the plan. Also cut, by hand, any
line that is not in the script and is not needed ("wait, let me do that again"): remove those
words from `words.json` and run the script again. Never cut a script line without asking.

## 6. Render the base

```bash
python3 S/base.py sources/<take> V/work/audio.wav V/work/cut-list.json V/work/base.mp4 --crop-x auto --words V/work/words-cut.json
```

- `--crop-x` is the left edge of the vertical crop in the scaled frame. `auto` centres it. For a
  landscape take, set it so the face is in the middle (the script prints the scaled width).
- `--words` moves the word times to the real part lengths (each part rounds to whole frames).
- The voice comes out at about -14 LUFS.

Check the base: watch the joins (take a frame on each side of each join, and listen to the second
around it). If the face is not in the middle, change `--crop-x` and run it again.

## 7. Captions

```bash
python3 S/captions.py V/work/words-cut.json V/work/captions.json --max-words 3
```

Use the brand sheet's words per caption for `--max-words`. The composition builds the caption
clips from `captions.json` (see `compose.md`).
