# Instagram Influencer Finder

Give Claude your website. Get a ranked list of Instagram creators who fit your brand, with the posts that prove it.

**What it does**

1. **Reads your brand.** Claude reads your website, finds your competitors, and reads reviews to learn your customers' problems in their own words.
2. **Checks with you once.** You see a short brand brief. Fix anything it got wrong, set your country and creator size, and say "go".
3. **Finds creators from three angles.** Three [Klint](https://tryklint.ai) agents search Instagram at the same time:
   - **Already in the category:** creators who post about you or your competitors, or are already paid by them
   - **Talks about the pain:** creators who post about the problems your product solves
   - **Is the customer:** creators whose life matches your customer, so their audience does too
4. **Ranks them.** Creators found by more than one angle move up. Creators who already mention you without being paid get an "Already a fan" tag.

**What you get**

- A shareable page with your brand brief and 15–25 ranked creators. Each creator comes with why they fit, 2–3 proof posts, their past brand deals, and red flags
- A CSV of the same list
- Optional: the same search on TikTok, or more Instagram creators

## What you need

- **Claude** (the desktop app or claude.ai) with Skills turned on
- **A free Klint account.** This skill uses Klint to search Instagram. The brand research works without it. Klint is only needed for the creator search.

## Install (about 3 minutes)

**1. Download the skill**

Download [`instagram-influencer-finder.zip`](https://github.com/david-roberts-94/shareable-marketing-skills/releases/download/instagram-influencer-finder-v1/instagram-influencer-finder.zip). Do not unzip it.

**2. Add it to Claude**

- In Claude, open **Settings → Capabilities** and turn on **Code execution and file creation**. (Newer layouts call it **Create and edit files**.)
- Open **Customize → Skills**. Click **+**, then **Create skill → Upload a skill**, and choose the zip.

<!-- screenshot: customize-skills.png -->

**3. Connect Klint**

- Make a free account at [tryklint.ai](https://tryklint.ai).
- In Claude, open **Customize → Connectors**. Click **+ Add**, then **Add custom connector**.
- Name: `Klint` · URL: `https://mcp.tryklint.ai`
- Click **Continue**. Choose **Sign in now**, click **Add**, and sign in to Klint.

You add Klint one time. It then works in the Claude app, in Cowork, and in Claude Code when you sign in to Claude Code with your Claude account.

<!-- screenshot: add-connector.png -->

## Use it

Open a **new chat** and type:

> Find Instagram influencers for yourbrand.com

Answer the one checkpoint question, then reply **go**. In Claude Desktop, Klint takes 10–25 minutes. When Claude says so, reply **check** to pull in the creators.

## What it costs

The brand research is free. The creator search uses Klint credits: one run starts 3 Klint agents. New Klint accounts come with free credits, and one full run can use most or all of them. The skill tells you the cost and waits for your "go" before it spends anything.

## Claude Code

```bash
mkdir -p ~/.claude/skills && unzip instagram-influencer-finder.zip -d ~/.claude/skills/
```

If you sign in to Claude Code with your Claude account, the Klint connector from step 3 is already there (type `/mcp` to see it). If you use an API key, add Klint with this command, then sign in through `/mcp`:

```bash
claude mcp add --transport http klint https://mcp.tryklint.ai
```

Then ask: `Find Instagram influencers for yourbrand.com`. In Claude Code the skill waits for Klint by itself.

## Good to know

- Every creator comes from live public Instagram data that Klint checked. Claude does not add creators from memory.
- Only adult creators are included.
- Each card shows the creator's profile photo and links to the profile.
- Contact details appear only when they are public in the creator's bio.
