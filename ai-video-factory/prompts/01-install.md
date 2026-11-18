# Prompt 1: install the five tools

Paste this into the **Code** tab of the Claude desktop app (or into Claude Code in a terminal). Open
the folder where you want your factory to live first, for example your Documents folder.

```text
I want you to be my video editor. Install these five tools on my computer, then test each one:

1. Whisper (speech to text with a timestamp on every word): github.com/openai/whisper
   On a Mac with Apple silicon, also install mlx-whisper, which is much faster.
2. FFmpeg (cuts, joins, and mixes video): ffmpeg.org
3. HyperFrames (captions and motion graphics as code): github.com/heygen-com/hyperframes
   Also install its agent skills with: npx skills add heygen-com/hyperframes
4. yt-dlp (downloads any Reel so you can watch it): github.com/yt-dlp/yt-dlp
5. Klint AI (finds what's going viral on Instagram): add the MCP connector https://mcp.tryklint.ai

Use my computer's normal package manager (Homebrew on a Mac, winget on Windows) and install
anything they need first, like Python or Node.js. Don't use sudo unless I say yes.

Then test each tool:
- Whisper: transcribe a 3-second test clip and show me the word timestamps.
- FFmpeg: make a 3-second 1080x1920 test video.
- HyperFrames: run npx hyperframes doctor.
- yt-dlp: print its version.
- Klint AI: tell me if the connector is connected, and if not, tell me exactly how to sign in.

Give me a checklist of what works, and tell me when you're ready.
```

## What you should see

A checklist with five ticks. Klint asks you to sign in once in your browser (new accounts get free
credits at https://tryklint.ai).

## If something fails

- **"command not found" after an install:** close and reopen the Claude app so it sees the new
  tools, then say "test the tools again".
- **Whisper is slow:** that is normal on the first run (it downloads a model). On a Mac, use
  mlx-whisper. On Windows with an NVIDIA card, ask Claude to install the CUDA build of PyTorch.
- **Klint does not show up:** in Claude Code, run `claude mcp add --transport http klint
  https://mcp.tryklint.ai`, then type `/mcp` and sign in. In the desktop app, add it under
  Settings → Connectors.
