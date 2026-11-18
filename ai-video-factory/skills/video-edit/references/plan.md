# The edit plan

The plan is the only checkpoint before the render. The creator must be able to read it in one
minute and say "approved" or "change 4". Save it as `edit/<video>/plan.md` and show it in the chat.

## Before you write it

- Read the brand sheet: its pace (a new picture every N seconds), its layouts, its captions, and
  its rules from notes.
- Read `## On screen` in `script.md`: the creator's own ideas for the graphics come first.
- Split the video into beats: usually one sentence or one list item per beat.

## Rules for a good plan

- **Every graphic shows the words.** When the creator says "FFmpeg cuts video", show FFmpeg
  cutting video, not a random tech picture. Name the word it lands on.
- **Real assets only.** A logo, a real screenshot, a real post, a real number, or a simple
  drawn shape (an icon, an arrow, a folder). Never a fake app screen.
- **Follow the brand sheet's pace.** If it says a new picture every 2 s, the plan has about one
  beat or graphic change every 2 s.
- **The face comes back.** Never go longer than the brand sheet allows without the face. The
  hook and the CTA are usually on the face.
- **One idea per graphic.** If a graphic needs a sentence to explain it, make it simpler.
- **Prompts on screen.** When the script says "use this prompt", show the prompt as a clean,
  readable app window (big text, 4 to 8 lines), long enough to screenshot (at least 2.5 s).

## The form

```markdown
# Edit plan: <video>

Length: <before> → <after> s · Cut: <n> silences, <n> retakes, <n> false starts
Captions: <style from the brand sheet> · Music: <bed and level, or none> · Sound effects: <which>

| # | Time | Words | Layout | Graphic | Lands on | Asset |
|---|---|---|---|---|---|---|
| 1 | 0:00–0:04.2 | "Claude edited this Reel…" | Full face | Title text: "My AI video editor" | "Claude" | none |
| 2 | 0:04.2–0:07.0 | "…here's every step for free." | Full face | A course card with "$90", crossed out on "free" | "free" | drawn |
| 3 | 0:07.0–0:10.1 | "First, get Claude Code." | Split | The Claude Code app window | "Claude Code" | screenshot: claude.ai/download |

Questions:
- Beat 6 has two takes of the same line. I kept the second. OK?
```

Keep the table to what the creator needs to decide. Put the exact times of animations in the
composition, not in the plan.

## After approval

- Write "Approved: <date>" at the top of `plan.md`.
- A change after approval goes into `plan.md` first, then into the composition.
