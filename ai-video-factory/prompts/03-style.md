# Prompt 3: teach it your style

Pick three to five Reels whose editing you want to copy. Pick creators who edit cleanly. Skip the
ones that look like AI slop: images that bounce and spin for no reason, italic serif fonts
everywhere, and camera moves that don't serve the words.

```text
Learn my editing style from these Reels:
[REEL LINK 1]
[REEL LINK 2]
[REEL LINK 3]

1. Download each one with yt-dlp into assets/references/.
2. Transcribe each one with Whisper, with word timestamps.
3. Measure each one, with real numbers:
   - cuts per 10 seconds and the shortest, median, and longest shot (use FFmpeg scene detection)
   - how often the face comes back, and how long the longest stretch without it is
   - captions: font style, size, position on screen, words per caption, upper or lower case,
     and how key words are highlighted
   - motion graphics: what kinds (text, logos, screenshots, icons, charts), how often, where on
     the screen, and how they come in and go out
   - the layouts: full face, split screen, picture in picture, full-screen graphic
   - music: is there a bed, and how loud it is under the voice; sound effects and when they play
   - colors, and the words per second of the speaker
   Look at a frame every half second so you don't miss anything.
4. Avoid AI slop: no over-animated images, no italic serif fonts, no camera moves that don't
   serve the words, and no fake app screens.
5. Fill in brand-sheet.md in my video-factory folder with what all the Reels have in common.
   Write a number for every rule, like "2 to 3 words per caption" or "a cut every 1.5 to 2.5 s".

Show me the brand sheet. Once I approve it, follow it every time you edit for me.
```

## What you should see

A filled-in `brand-sheet.md` with numbers, not adjectives. Read it and change anything you don't
like before you say "approved". Claude reads this file on every edit.

## If something fails

- **yt-dlp can't download an Instagram Reel:** Instagram sometimes asks for a login. Tell Claude:
  "use yt-dlp with --cookies-from-browser chrome" (or your browser), and be signed in to Instagram
  in that browser.
