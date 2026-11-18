---
name: video-script
description: Write a short-form video script (Instagram Reels, TikTok, YouTube Shorts) in the creator's own voice from any idea, with 15 tested hooks. The input is an idea card from ideas.md, a post or video link, an article, a voice note, or a few words. It learns the voice from the creator's approved scripts in edit/*/script.md, pitches two or three angles, writes 15 hooks and tests them, then writes one script to edit/<video>/script.md. Use it when the user says "write a script", "script this", "turn this into a Reel", "use the video-script skill on idea 3", or drops a link as a video idea, and when the user says a script is approved.
---

# Video script

You write short-form video scripts in the creator's voice. You learn the voice from examples, not
from rules. Every script the creator approves becomes a new example, so each script needs fewer
changes than the last.

Work inside the creator's `video-factory` folder. Read its `CLAUDE.md` first.

## 1. Learn the voice

Read every `edit/*/script.md` whose front matter says `status: approved`. Each one holds the
source, your draft, and the creator's final. Ask yourself:

- What did the creator keep from the source, and what did they leave out?
- What did they change in your draft? Their hooks, their words, their length, their CTA.
- How do their sentences sound when spoken aloud?

**No approved scripts yet?** Ask for one of these, then learn from it:

- links to 3 of their own best videos: download each with yt-dlp, transcribe it with Whisper, and
  read the transcripts as examples of their voice; or
- 2 or 3 scripts or captions they wrote.

Measure their speed from a transcript (words divided by seconds). If you cannot measure it, use
2.9 words per second. Use it to say how long a script runs.

## 2. Read the idea

- **A video link:** download it with yt-dlp and transcribe it with Whisper. Note the hook, the
  structure, and every number.
- **An idea card from ideas.md:** open its link and do the same.
- **An article or a post:** read it fully.
- **A few words:** search the web for the best real example: a company, a person, a number.

Check the big claims. A script with one wrong number loses trust. Find the original source of
each number and name it in the script file. If a claim is wrong or old, tell the creator and use
the right one.

## 3. Pitch

Give the creator two or three pitches in the chat. Each pitch has:

- the angle: what the video is about, and why the viewer cares
- the form: a list, a story, a demo, a breakdown, one big number, or something new. Let the
  material choose the form. Do not use the form of the last script out of habit.
- three hooks, as they would sound
- one line on what it leaves out

Recommend one. Stop and wait for the pick.

## 4. Write 15 hooks

The hook is the first 3 to 5 seconds. It decides most of the views. Read
[`references/hooks.md`](references/hooks.md), then write 15 hooks for the picked pitch:

- 10 that use the method of a hook that worked (from the creator's approved scripts, or from the
  examples in `references/hooks.md`)
- 3 that use the method of a hook from a different subject (food, fitness, a story)
- 2 that try something new

Test each one with the five questions in `references/hooks.md`. Remove each hook that fails one.
Pick the best three.

**Never write proof that is not true.** Write "I did X" only when the creator told you they did
it. Otherwise give the result of the real person or company, in the third person.

## 5. Write the script

- Open with the best hook.
- Then deliver what the hook promised, fast. One idea per paragraph. Each point gets what it is,
  how it works, and one exact detail (a number, a name, a tool, a step). Cut every line that is
  only framing.
- Write for the ear: short sentences, the creator's words, numbers as they would say them.
- Mark each place where the edit should show something, but only in `script.md`, not in the
  spoken words.
- End with one CTA. A comment keyword with a free asset works well ("Comment GUIDE and I'll send
  it to you"), or "follow for more".
- Aim for 60 to 90 seconds unless the creator asks for another length.

## 6. Save it

Make `edit/<video-name>/script.md` (lowercase, hyphens), in this form:

```markdown
---
status: draft          # draft | approved
source: <link or "idea from ideas.md #3">
words: <n>
seconds: <words ÷ words per second>
---

# <short title>

## Script

<only the spoken words, one paragraph per beat>

## On screen

<one line per beat: the word it lands on, and what to show>

## Other hooks

1. <second best>
2. <third best>

## Sources

<one line per claim: the claim and its link>

## Draft

<a copy of the script as you first wrote it. Never change this section after the creator edits.>
```

Show the creator the script, the two other hooks, and the length. Tell them to edit `## Script`
in the file (or paste their version in the chat), and to say "approved" when it is final.

## 7. When the creator approves

1. Make sure `## Script` holds the creator's final words, exactly. If they pasted it in the chat,
   copy it in.
2. Keep `## Draft` as it was. The difference between the two is what you learn from next time.
3. Set `status: approved`.
4. Tell them the next step: "Film it, drop the file in sources, and use prompt 5 to edit it."
