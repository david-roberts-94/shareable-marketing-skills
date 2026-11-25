---
name: article-repurpose
description: Turn one X article (or any long post) into four new pieces that rank and get cited: an SEO blog article for your own site, a LinkedIn article, a dev.to post, and a Reddit post. Each one is rewritten for its platform, not copied. It picks keywords with an SEO tool (DataForSEO, Ahrefs, or SEMrush MCP, or web search when none is connected) and Google Search Console when it is connected. Use it when the user says "repurpose this article", "turn this X article into a blog post", "make the SEO version", "cross-post this to LinkedIn, dev.to and Reddit", or pastes an X article link and asks for more pieces from it.
---

# Article repurpose

You take one article that already worked on X and give it four more lives. Google, ChatGPT, and
the other AI search tools read and cite blogs, LinkedIn, dev.to, and Reddit, so each piece is a
new way for buyers to find the same experiment.

Read `references/article-template.md` first. It explains what these articles are.

## 1. Get the article

- **An X article link:** open it and read it in full. If you cannot open it (X often blocks
  tools), ask the user to paste the full text and the screenshots.
- **Pasted text:** use it as it is.

Write down: the title, the trend, the result, every step, every prompt (word for word), the
creator's name and handle, and the product's last step.

## 2. Ask four short questions

Ask all four at once, then wait:

1. The site the blog article goes on, and one or two links to its best existing articles (for the
   style and the internal links).
2. The product page to link to.
3. Do you want all four pieces, or only some?
4. Is an SEO tool connected (DataForSEO, Ahrefs, SEMrush, or Google Search Console)?

## 3. Pick the keywords

Find the searches that this article can win. Use the best tool that is connected:

- **Google Search Console:** the queries that the site already gets impressions for on this
  topic, with position 5 to 30. These are the fastest wins.
- **DataForSEO, Ahrefs, or SEMrush:** for the trend and the result (for example "openai agent
  tiktok marketing"), get the search volume, the difficulty, and the questions people ask.
- **No tool:** search the web for the trend. Use the "People also ask" questions and the titles
  that already rank as your guide. Say that you have no volume numbers.

Choose one main keyword, 3 to 5 related keywords, and 4 to 6 questions. Show them to the user in a
small table, with the reason for each, before you write.

## 4. Write the blog article

This is a new article, not a copy. Google ignores copies, and so do readers who saw the X article.

- **Title:** the main keyword plus the result, under 65 characters if you can.
- **First 100 words:** the result, the main keyword, and who this is for.
- **Structure:** keep the steps of the experiment, but write each one for a reader who arrived
  from a search: explain terms, add the "why" behind each step, and add what to do when it fails.
- **Keep every prompt word for word,** in code blocks.
- **Add an FAQ** at the end with the questions from step 3. Answer each in 2 to 4 sentences. AI
  search tools quote answers like these.
- **Credit the creator** by name, with a link to the original X article.
- **Links:** 2 or 3 internal links to the user's existing articles, and one link to the product
  page in the product step.
- **Meta:** a meta title, a meta description (under 155 characters), and a URL slug.

Save it as `repurpose/<slug>/blog.md`.

## 5. Write the three cross-posts

Each one is shorter and fits its platform. Save each in the same folder.

- **`linkedin.md` (a LinkedIn article):** a first line that states the result. Short paragraphs.
  The steps as a numbered list, with the 2 or 3 most useful prompts. 600 to 1,000 words. End with
  a link to the blog article.
- **`devto.md` (a dev.to post):** add front matter with `title`, `tags` (up to 4), and
  `canonical_url` set to the blog article's URL, so the blog keeps the SEO credit. Keep the
  technical parts: the prompts, the tools, the settings.
- **`reddit.md` (a Reddit post):** first find 2 or 3 subreddits where this topic is welcome, and
  read their rules. Write the post as a person sharing what worked: the result, the steps, the
  prompts. No marketing words. Put the link only where the rules allow it, usually in a comment.
  Write one version for each subreddit, because each one is different.

## 6. Check and hand over

Before you finish, check:

- [ ] No paragraph is copied from the X article.
- [ ] Every number matches the original, and every prompt is word for word.
- [ ] The creator is credited in every piece.
- [ ] The product is in one step only.
- [ ] The dev.to post has the canonical URL.

Then show the user the list of files, the main keyword, and what to post where. Do not post
anything yourself unless the user asks.
