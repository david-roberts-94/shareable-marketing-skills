---
name: video-edit
description: Edit a raw talking-head take into a finished vertical video (1080 x 1920) for Instagram Reels, TikTok, or YouTube Shorts. It transcribes the take with Whisper, cuts silences, breaths, and retakes with FFmpeg, plans captions and motion graphics on the spoken words, shows the plan in the chat for approval, then builds the graphics and captions with HyperFrames, renders, checks the result, and turns the creator's notes into brand-sheet rules. Use it when the user says "edit my video", "use the video-edit skill", "cut this take", drops a raw file in sources/, or gives notes on a draft.
---

# Video edit

You are the creator's video editor. The input is a raw take in `sources/` and its script in
`edit/<video>/script.md`. The output is `edit/<video>/final.mp4`.

Work inside the creator's `video-factory` folder. Read `CLAUDE.md` and `brand-sheet.md` first.
The section "Rules from my notes" in the brand sheet wins over everything else.

Before you write any HyperFrames code, read the HyperFrames agent skills (installed with
`npx skills add heygen-com/hyperframes`): `hyperframes`, then `hyperframes-core`, and
`hyperframes-media` for audio and captions. They hold the rules of a renderable composition. This
skill tells you what to make; they tell you how HyperFrames wants it.

## The run

1. Get the files
2. Cut the take
3. Plan the edit, and **stop for approval**
4. Get the assets
5. Build the composition
6. Render and check
7. Deliver
8. Turn notes into rules

### 1. Get the files

- Find the raw take in `sources/`. If there are several new files, ask which one.
- Find the script: `edit/<video>/script.md`. No script? Ask for the video name, and work from the
  transcript alone.
- A separate audio file with a similar name (`.wav`, `.m4a`, `.mp3`) is the mic recording of the
  same take. Use it for the sound: it is better than the camera's.
- Make `edit/<video>/work/`. Never change a file in `sources/`.

### 2. Cut the take

Follow [`references/cut.md`](references/cut.md). The scripts in `scripts/` do the work (Python 3.9+
and FFmpeg, no extra packages):

1. Probe the take. Sync the mic file to the camera when there is one (`sync.py`).
2. Transcribe with Whisper, with word timestamps, and fix names from the script (`words.py`).
3. Make the cut list: silences, retakes, a pause after list numbers (`cutlist.py`). Read its report.
4. Render `work/base.mp4`: the cut take, framed to 1080 x 1920, voice at about -14 LUFS (`base.py`).
5. Group the words into captions (`captions.py`).

### 3. Plan the edit, and stop for approval

Write `edit/<video>/plan.md` in the form of [`references/plan.md`](references/plan.md), and show
it in the chat. It has one numbered line per beat: the time, the words, the layout, the graphic,
the word it lands on, and the asset it needs.

Then stop. Say: "Reply with changes (for example 'drop 4' or 'make 7 a screenshot of the pricing
page'), or say approved." Do not render until the creator approves the plan. Apply each change to
`plan.md` and show only the changed lines again.

### 4. Get the assets

For each asset in the plan:

- **Logos:** the company's own press kit or website. SVG, or PNG with a clear background. Many
  main sites block scripts (403): try the company's press, `company.`, or CDN address, or the
  parent company's site. A white logo on a light panel needs a one-color dark version (change the
  SVG fill). Trim empty padding from a PNG so it shows at its real size.
- **Screenshots:** take them from the real page (`npx hyperframes capture`, or a headless browser),
  at the size the layout needs. No personal data in a capture.
- **Reels or posts:** download with yt-dlp, and use only the seconds the plan names.
- Save each file in `assets/<video>/` and write its source link in `assets/sources.md`.

Never make a fake app screen, a fake review, or a made-up number. If you cannot get a real asset,
say so and propose another graphic.

### 5. Build the composition

Follow [`references/compose.md`](references/compose.md). In short: one HyperFrames project in
`edit/<video>/hf/`, 1080 x 1920, with `work/base.mp4` as the bottom layer, the captions from
`work/words-cut.json`, and one clip per graphic, each starting on its word.

Run `npx hyperframes lint` and `npx hyperframes check`. Then take snapshots at the middle of each
graphic and look at every one before the full render.

### 6. Render and check

From `edit/<video>/hf/`, render with `npx hyperframes render --quality high --output ../final.mp4`.
Then run `scripts/checks.py` and the checks that need your eyes, in
[`references/checks.md`](references/checks.md): size and frame rate, length, loudness, captions
against the transcript, flashes and frozen frames, sync, safe zones, and every frame. Fix what fails, and render again. Do not show the creator a video that failed a check.

### 7. Deliver

Tell the creator:

- the file path, the length, and the number of cuts and graphics
- the results of the checks, in one line each
- anything you could not do (an asset you could not find), and what you did instead

Ask for notes, with times ("at 0:12, the logo comes in too late").

### 8. Turn notes into rules

For each note, follow [`references/notes.md`](references/notes.md): fix it in this video, then
decide if it is a rule for every video. A rule goes into "Rules from my notes" in
`brand-sheet.md`, with the date and the note in the creator's own words. A one-time fix does not.
Render again, check again, and deliver again.

When the creator says the video is final, keep `final.mp4`, and delete the large files in `work/`
(keep `words.json`, `words-cut.json`, `cut-list.json`, `captions.json`, and `plan.md`).
