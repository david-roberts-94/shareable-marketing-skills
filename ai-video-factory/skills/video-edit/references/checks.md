# Checks before the creator sees a video

Run the script, then the checks that need your eyes. Fix what fails and render again. Do not show
the creator a video that failed a check.

```bash
python3 <skill>/scripts/checks.py edit/<video>
```

It runs checks 1 to 6, makes the contact sheets for check 9, and writes `work/checks.md`.

| # | Check | Pass |
|---|---|---|
| 1 | Size and frame rate | 1080 x 1920, at the take's rate |
| 2 | Length | Equal to `base.mp4` within 0.15 s |
| 3 | Loudness | Integrated −14 LUFS ± 1, true peak ≤ −1 dB |
| 4 | Captions | Every spoken word is in a caption, once, in order |
| 5 | Black frames | None, except at a planned fade |
| 6 | Frozen frames | None longer than 0.5 s, unless a still graphic covers the frame |
| 7 | Sync (your eyes) | Take a frame at three words with "p", "b", or "m": the lips close on the word |
| 8 | Safe zones (your eyes) | No caption or key graphic above y 220, below y 1540, or right of x 940 |
| 9 | Every frame (your eyes) | Look at every sheet in `work/sheets/`: no blank panel, no graphic in the wrong place, no caption on the face, no small graphic in an empty panel. Black tiles at the end of the last sheet are padding. |
| 10 | The plan (your eyes) | Every approved beat is there, on its word |

## Fix the loudness without a new render

When check 3 fails (the music bed or the sound effects moved the level):

```bash
ffmpeg -y -i final.mp4 -c:v copy -af "loudnorm=I=-14:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 256k final_fixed.mp4
```

`-ar 48000` matters: without it, loudnorm writes 192 kHz audio. Replace `final.mp4` with
`final_fixed.mp4` and run the checks again.
