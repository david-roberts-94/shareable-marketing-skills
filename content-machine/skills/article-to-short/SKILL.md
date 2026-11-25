---
name: article-to-short
description: Turn one article (an X article, a blog post, or any playbook) into a 30 to 45 second short-form video for an AI avatar (HeyGen) or the user's own face, with a hook, a comment word CTA, the HeyGen prompt, a caption for each platform, and the DM that sends commenters back to the article. Use it when the user says "make a Short from this article", "turn this into a Reel", "write the avatar video", "article to video", or asks for a comment-to-DM video for an article.
---

# Article to Short

You turn one article into a short video that sends people back to the article. The video does not
teach the whole method. It shows the result, gives a taste of the steps, and asks the viewer to
comment one word. Every commenter gets a DM with the article. That brings warm readers back to the
article, and some of them become buyers.

Read `references/article-template.md` first.

## 1. Read the article

Open the link and read it in full, or ask the user to paste it. Write down: the result (the
number), the trend, the most surprising step, and the one prompt or trick that a viewer would
most want.

## 2. Ask three short questions

Ask all three at once:

1. Is the video for a HeyGen avatar or for the user's own face?
2. The comment word (one short word in capitals, for example BOT, PROMPT, or PLAYBOOK). Suggest
   two that fit the article.
3. The article link that the DM sends.

## 3. Write 10 hooks, keep 3

The hook is the first 3 seconds. Write 10 hooks, then cut each one that fails one of these tests:

- **Proof:** it has a real number or name from the article.
- **Promise:** the viewer knows what they will get.
- **Fast:** the promise comes in the first 15 words.
- **True:** it says only what the article shows. Never write "I did this" when the creator in the
  article did it. Say their name, or "this creator".

Show the 3 best to the user, and use the best one.

## 4. Write the script

- **30 to 45 seconds,** about 80 to 120 words.
- **The shape:** hook → the result and who got it → 2 or 3 of the steps, each in one sentence →
  the CTA.
- **The CTA, as the last line:** "Comment [WORD] and I'll send you the full article." Keep the
  word the same everywhere.
- Short sentences that sound good out loud. No words that the avatar will say wrong (spell
  numbers the way they are spoken).

Save it as `shorts/<slug>/script.txt`.

## 5. Write the HeyGen prompt

When the video is for an avatar, write `shorts/<slug>/heygen-prompt.txt` for the user to paste
into HeyGen with the script. Describe the look of the video in plain words:

- big bold text behind or beside the avatar with each number and key word, as it is spoken
- a slow zoom in on the hook, quick zoom cuts on each step, and a zoom out on the CTA
- the comment word on screen, large, for the last 3 seconds
- 9:16 vertical, captions on every word

Check HeyGen's current docs for what its prompt supports, and tell the user which parts they must
set by hand.

## 6. Write the caption and the DM

- **`caption.txt`:** "Comment [WORD]" in the first line. Then one line on the result, and 3 to 5
  hashtags. Make one version each for YouTube Shorts, TikTok, Instagram, and Facebook if their
  limits differ.
- **`dm.txt`:** the message each commenter gets: a thank-you, one line on what the article gives
  them, and the link. Under 40 words.

## 7. Hand over

Show the user: the hook, the script, its length in seconds, and the list of files. Then point
them to prompt 05 in this pack to post the video everywhere and set up the DMs.
