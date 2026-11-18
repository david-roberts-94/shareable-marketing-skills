# Build the composition

One HyperFrames project per video, in `edit/<video>/hf/`. Read the `hyperframes-core` skill for
the composition contract before you write it. This file says what goes in a talking-head Reel.

## Set up

```bash
cd edit/<video>
npx hyperframes init hf --non-interactive --resolution portrait --skip-skills
```

(`--skip-skills` stops `init` from changing the HyperFrames skills that are already installed.)

Copy `work/base.mp4`, the plan's assets, and the brand fonts into `hf/assets/`. Fonts go in
`hf/assets/fonts/` and load with `@font-face`: a render cannot fetch a font from the web.

Write the composition with a script (for example `work/build.py`) that reads `work/words-cut.json`,
`work/captions.json`, and `plan.md`, and writes `hf/index.html`. Then a re-cut or a plan change is
one command, not a hand edit.

## The layers

The root is 1080 x 1920, with `data-duration` equal to the length of `base.mp4` and `data-fps`
equal to the rate that `base.py` printed.

| Track | What | Notes |
|---|---|---|
| 0 | `<video>` of `base.mp4`, muted | A direct child of the root. Layouts move and crop this element on the main timeline. |
| 1 to 5 | Graphics, one clip per plan beat | Each starts at its word's time from `words-cut.json`, minus 0.05 s. |
| 6 | Captions | From `captions.json` (see below). |
| 10 | `<audio>` of `base.mp4` | The voice, volume 1. |
| 11 | `<audio>` of the music bed | Volume from the brand sheet (about 0.08 is a quiet bed). Fade in and out. |
| 12+ | Sound effects | One `<audio>` per effect, on the plan's words. |

Video must be muted and inline. The voice is a separate `<audio>` element of the same file.

**Sound effects:** take the files from the `hyperframes-media` skill's bundled library
(`assets/sfx/`) or from a free library you are allowed to use, copy them to `hf/assets/sfx/`, and
place them as `<audio>` clips. You do not need its `audio.mjs` engine for this.

## Layouts

All layout changes animate the base video on the main timeline in `index.html`:

- **Full face:** the video fills the frame.
- **Split:** the graphic panel fills the top half (y 0 to 960). Move the video down so the face is
  in the bottom half (for example `y: 480`), with the eyes about y 1250.
- **Full-screen graphic:** the graphic panel covers the frame. Keep the voice playing.
- **Picture in picture:** scale the video to about 35% and put it in a corner, with a rounded
  frame.

Change layouts on a word, and make the change fast (0.15 to 0.25 s) or a hard cut. Slow slides
look like slop.

## Captions

Build one clip per caption from `work/captions.json`. Never type captions by hand.

- Style from the brand sheet: font, size, case, color, outline or shadow, and the highlight for
  key words.
- Width: `left: 60px; width: 880px; text-align: center`. Shrink the font before you wrap to a
  second line.
- **Full face:** at the brand sheet's y (often about y 1150 to 1300, on the chest, under the
  mouth).
- **Split:** at the bottom edge of the graphic panel (center about y 900), on the panel, **never on
  the face**. Check that the caption does not cover the forehead or eyes.
- **Full-screen graphic:** hide the caption when the graphic already shows the same words.
- Use the creator's spelling for names (from `words.json`), not Whisper's.

## Graphics

- One clip per graphic, on its own track, `data-start` = the word time − 0.05 s.
- **Fill the panel.** A graphic uses 60 to 85% of the panel's width. Logos are at least 140 px
  tall, text in a graphic at least 56 px. A small logo in a big empty panel looks unfinished.
- Build each graphic with HTML and CSS: text cards, logo pills, app windows, icons, arrows,
  simple charts, screenshots in a frame. Animate with the paused GSAP timeline.
- Come in fast (0.2 to 0.35 s, ease out). Hold still while the words are spoken. Go out fast or
  cut on the next graphic.
- Build lists step by step: each item comes in on its word.
- Prompt windows: a dark app window with a title bar, the prompt in a 34 to 40 px font,
  placeholders in a highlight color, and the reply lines coming in one by one. Keep it on screen at
  least 2.5 s. A typing caret sits at the end of the typed text, not in the middle of the box.
- Use the brand sheet's colors and fonts. Nothing bounces, spins, or wobbles unless the brand
  sheet says so.

## Before the full render

```bash
cd edit/<video>/hf
npx hyperframes lint
npx hyperframes check
npx hyperframes snapshot --at <the middle second of each graphic, comma separated>
```

- `lint` warns that a long `index.html` should use sub-compositions. For a short Reel, one file is
  fine: ignore these warnings.
- `check` warns that captions of 2 or 3 words are on screen too short to read (`line_unread`).
  That is the style: ignore it for captions only. Its safe zones are stricter than the brand
  sheet's; the brand sheet wins.

Look at every snapshot. Check: the graphic is the one in the plan, it fills the panel, the text is
readable at phone size, nothing covers the eyes or mouth, and nothing sits in the safe-zone margins
(`references/checks.md`). Fix and snapshot again.

## Render

From `edit/<video>/hf/`:

```bash
npx hyperframes render --quality high --output ../final.mp4
```
