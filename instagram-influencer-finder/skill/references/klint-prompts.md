# Klint agent prompts

Klint does not ask questions back. Put the whole task in one prompt. Each prompt has two parts: the **shared part** (the same in all 3) and the **angle part** (different in each).

Fill every `{field}` from the brief and the checkpoint answers. Remove a line if you have nothing for it. Do not send a prompt with `{` or `}` in it.

## Shared part (put at the start of all 3 prompts)

```
I'm finding Instagram creators to promote a brand. Search Instagram only.

BRAND
- {Brand} ({website}), Instagram {@handle or "unknown"}
- Sells: {what they sell, price range}
- Target customer: {target customer and traits}
- Why people buy: {why people buy}
- Competitors: {competitor 1 (@handle)}, {competitor 2}, {competitor 3} …

REQUIREMENTS FOR EVERY CREATOR
- Country: audience and creator based in {country}
- Size: {size band, e.g. 10K–500K followers}
- Posted on Instagram in the last 30 days
- Clearly an adult (18+). If there is any sign the creator is under 18, or you can't tell, leave them out.
- The fit must show in their posts, not only in their bio
- Leave out: the brand's own account, competitor brand accounts, meme or repost pages, shops, and {avoid list}

FOR EACH CREATOR, COUNT SPONSORED POSTS
- In their last 20 posts, count posts with a paid partnership label OR an ad stated in the caption or on screen (#ad, "sponsored", "gifted", "use my code", "partner"). Name the brands.

RETURN ABOUT 15 CREATORS. Use exactly this format for each one, with no table:

### @handle
- Profile: https://www.instagram.com/handle/
- Profile photo: {the complete profile picture URL, unshortened, with every query parameter, or "none"}
- Name:
- Followers:
- Country:
- Adult: yes — {how you know: a stated age, a job, a degree, marriage, or children. "Professional creator" or "does brand deals" is not enough}
- Last post: {date}
- Posts in last 30 days:
- Typical likes / comments per post: {or "hidden"}
- Sponsored in last 20 posts: {number} — brands: {list}
- Mentions {Brand} without being paid: yes / no — {post link if yes}
- Contact in bio: {email or "link in bio" only if visible; else "none seen"}
- Proof posts (2–3):
  - {post URL} — {one line: what the post shows and why it fits}
- Why they fit: {one or two lines}
- Red flags: {or "none"}

Give complete, unshortened URLs. Give exact follower counts when you have them (12,400, not 12K). If you could not check a field, write "not checked".
```

## Angle 1 — Already in the category

Agent label: **Category**

```
ANGLE: creators who are already in this brand's category.
Find creators who have posted about {Brand} or any of the competitors ({competitor list}): paid posts, gifted posts, reviews, tags, or organic mentions. Also include creators who post regularly about {product category} and do sponsored posts for similar brands.
Creators who mention {Brand} without being paid are the most valuable. Find as many of those as you can and mark them.
```

## Angle 2 — Talks about the pain

Agent label: **Pain**

```
ANGLE: creators who post about the problems this brand solves, not general {product category} influencers.
The problems, in customers' own words:
- {pain point 1}: "{customer phrase}"
- {pain point 2}: "{customer phrase}"
- {pain point 3}: "{customer phrase}"
Search phrases creators use: {6 to 10 search phrases from the brief}
Find creators who share their own experience of these problems, or who help people with them (for example coaches, specialists, or people who document their journey). They do not need to have posted about any brand in this category before.
```

## Angle 3 — Is the customer

Agent label: **Customer**

```
ANGLE: creators who are this brand's target customer and post about that life.
The customer: {target customer, with traits}
Find creators whose own life matches this customer, so their audience is likely to be people like them. Look at what they post about day to day ({2–4 topics from the customer's life, e.g. "home cooking for a family", "life with a rescue dog"}), not only at their bio.
Prefer creators whose posts show they would naturally use a product like {what they sell}.
```

## Follow-up: the same search on TikTok

Send to each of the 3 agents with `klint_message_agent`:

```
Now do the same search on TikTok instead of Instagram. Same brand, same angle, same requirements, same format. Use TikTok profile and video URLs, and count sponsored posts from the last 20 TikTok videos. Do not repeat creators you already listed unless they are also strong on TikTok; if so, say so.
```

## Follow-up: deeper on Instagram

Send to the one agent whose creators ranked highest:

```
Find about 15 more Instagram creators for the same angle and requirements, in the same format. Do not repeat anyone you already listed. Widen the search: try related search phrases, accounts that the best creators so far follow or collaborate with, and creators in the same niche at the edges of the size range.
```
