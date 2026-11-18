# AI Video Factory

Turn Claude into your video editor. This pack has every prompt and skill from David Roberts's Reel
"Claude edited this Reel and my last 18": the five tools, the folder, your editing style, ideas from
what's going viral, scripts in your voice, and a full edit with captions and motion graphics.

**Needs:** the Claude desktop app (Code tab) or Claude Code, on a Mac or a Windows computer. The
ideas step needs [Klint AI](https://tryklint.ai) (new accounts get free credits). Everything else
is free and open source.

## What's inside

```text
ai-video-factory/
  prompts/
    01-install.md     install and test the five tools
    02-folder.md      make the video-factory folder
    03-style.md       teach Claude your editing style → brand-sheet.md
    04-ideas.md       find ideas with Klint AI → ideas.md
    05-edit.md        watch Claude edit your video
  skills/
    video-script/     writes scripts in your voice, with 15 tested hooks
    video-edit/       cuts, plans, adds captions and motion graphics, renders, and checks
  templates/
    brand-sheet.md    your style, with a number for every rule
    CLAUDE.md         tells Claude how your factory folder works
```

## The five tools

| Tool | What it does in the factory |
|---|---|
| [Whisper](https://github.com/openai/whisper) | Transcribes every word with a timestamp |
| [FFmpeg](https://ffmpeg.org) | Cuts, joins, and mixes the video |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | Builds the captions and motion graphics as code |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Lets Claude download and watch any Reel |
| [Klint AI](https://tryklint.ai) | Finds what's going viral on Instagram, so you never run out of ideas |

## How to use it

1. Unzip the pack somewhere you can find it.
2. Open the Claude desktop app, switch to the **Code** tab, and paste the prompts in order:
   01, 02, 03, 04. Each prompt file says what you should see and what to do if something fails.
3. For each video: pick an idea, say **"Use the video-script skill on idea 3"**, edit the script,
   say "approved", film it, drop the file in `sources/`, and paste prompt 05.
4. Give notes on the draft. Every note becomes a rule in your brand sheet, so the next video needs
   fewer.

## Good to know

- A 60-second video takes about 10 to 20 minutes to cut, render, and check.
- Claude shows you an edit plan first and renders nothing until you approve it.
- The factory uses only real screenshots, logos, and numbers. It never makes up an app screen.

Made by [David Roberts](https://www.instagram.com/davi.d_roberts/), co-founder of
[Klint AI](https://tryklint.ai).
