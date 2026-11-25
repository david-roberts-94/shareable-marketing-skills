# The Content Machine

The three-step content machine behind Postiz, the social media scheduler whose founder says it
reached 5 million dollars in ARR. From David Roberts's Reel on the Postiz playbook (comment
MACHINE).

1. **Experiment articles:** creators run real experiments on the newest trend and write them up
   as X articles.
2. **The repost network:** paid creators repost every article, so every one gets views.
3. **The repurpose agents:** every article becomes an SEO blog post, a LinkedIn article, a dev.to
   post, a Reddit post, and short videos that send commenters back to the article.

**Needs:** Claude (the desktop app, claude.ai, or Claude Code) with code execution turned on, on a Mac or a Windows computer.
The trend, writer, and reposter prompts need [Klint AI](https://tryklint.ai) (new accounts get
free credits). The SEO step works best with a DataForSEO, Ahrefs, or SEMrush connector and Google
Search Console, and it still works with web search alone. The videos use
[HeyGen](https://www.heygen.com) or your own camera.

## What's inside

```text
content-machine/
  prompts/
    01-trend-check.md      this week's trends → 5 experiment ideas (Klint AI)
    02-find-writers.md     creators who really get views in your niche (Klint AI)
    03-article-draft.md    the creator's notes → the article draft
    04-find-reposters.md   the X accounts whose followers are your buyers (Klint AI)
    05-cross-post.md       post the Short everywhere and set up the DMs
  skills/
    article-repurpose/     X article → blog, LinkedIn, dev.to, and Reddit versions
    article-to-short/      article → avatar video script, HeyGen prompt, caption, and DM
  templates/
    article-template.md    the title formula, the structure, and the rules
    creator-brief.md       the brief you send to a writer
    tracker.csv            every writer, reposter, price, and result in one place
```

## How to install the skills

Each skill has its own upload-ready zip: [article-repurpose.zip](https://github.com/david-roberts-94/shareable-marketing-skills/releases/download/content-machine-v1/article-repurpose.zip) and
[article-to-short.zip](https://github.com/david-roberts-94/shareable-marketing-skills/releases/download/content-machine-v1/article-to-short.zip). Each one has the article template inside.

- **Claude desktop app or claude.ai:** open **Settings → Capabilities** and turn on **Code
  execution and file creation**. Then open **Customize → Skills**, click **+**, then **Create
  skill → Upload a skill**, and choose the zip. Do not unzip it. Do this for both skills.
- **Claude Code:** copy the two folders in `skills/` into `~/.claude/skills/`.

Then say "use the article-repurpose skill on [link]" or "use the article-to-short skill on [link]".

The prompts are plain text: open a file in `prompts/` and paste its text block into Claude.

## Good to know

- Every article must be a real experiment with real numbers. That is the rule the whole machine
  stands on.
- Every paid repost uses X's paid-partnership label.
- The skills never post for you. You check every piece before it goes live.

Made by [David Roberts](https://www.instagram.com/davi.d_roberts/), co-founder of
[Klint AI](https://tryklint.ai). The method is from Nevo David's public video on how Postiz runs
its content. These prompts and skills are new; they are not Postiz's own files.
