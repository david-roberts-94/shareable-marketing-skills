# Prompt 5: watch Claude edit your video

Film your video the way you normally would. Drop the raw file in `sources/`. If your mic records
its own audio file, drop that in too, with a similar name.

```text
Use the video-edit skill to edit my new video:
- Raw footage: sources/[FILE NAME]
- Script: edit/[VIDEO NAME]/script.md

Cut every silence, keep the energy up, and add captions and motion graphics on the words I say,
in my brand sheet's style. Use real screenshots and logos, never fake ones.
Show me the edit plan first. Don't render anything until I approve it.
```

## What you should see

1. Claude transcribes the take and cuts the silences, the breaths, and the retakes.
2. It shows you a numbered **edit plan** in the chat: each beat with its words, its layout, the
   graphic, and the word the graphic lands on.
3. You reply with changes ("drop 4", "make 7 a screenshot of the pricing page", "approved").
4. It renders a draft, checks it (size, sound level, captions, flashes, safe zones), and gives you
   the file in `edit/[VIDEO NAME]/`.
5. You leave notes. Every note becomes a rule in your brand sheet, so the next video needs fewer.

A 60-second video usually takes 10 to 20 minutes to render and check.
