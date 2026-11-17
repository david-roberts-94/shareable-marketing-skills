---
name: instagram-influencer-finder
description: Find Instagram influencers who fit a brand. The user gives a company website. The skill researches the brand (its website, reviews, and the web), writes a short brand brief, and then uses Klint agents to find and check Instagram creators. It returns a ranked shortlist with proof posts as an artifact and a CSV. Use it when the user asks to find influencers or creators for a brand, company, product, or website, asks who should promote their product on Instagram, or gives a URL and says "influencers". The creator search needs the Klint connector; the brand research works without it.
---

# Instagram Influencer Finder

Version: v1

You find Instagram creators who are a good fit to promote one brand. You research the brand first, with free tools. You stop one time to check your understanding with the user. Then you start Klint agents to find the creators, and you give the user a ranked shortlist.

## Klint cost

> **Keep every cost figure and Klint link in this block only. Other sections refer to it.**

| Setting | Value |
|---|---|
| Klint agents in a standard run | **3** (one for each angle) |
| Time for a run | 10 to 25 minutes (the Topicals test run took about 22) |
| Free allowance text | New Klint accounts come with free credits. A full run can use most or all of them. |
| Sign up | https://tryklint.ai |
| Connector URL | https://mcp.tryklint.ai |
| Check credits | {KLINT_BILLING_URL} |

Rules:

- Start exactly **3** Klint agents in a standard run. Do not start more unless the user asks for more.
- Before you start any agent, tell the user the cost (from this block) and wait for "go".
- If the Check credits value is still `{KLINT_BILLING_URL}`, say "check your credits in your Klint account" and do not show the placeholder.

## The run

1. Get the website. Check for Klint.
2. Research the brand. Write the brief.
3. Checkpoint: the user corrects the brief, sets preferences, and says "go".
4. Start the 3 Klint agents.
5. Build the artifact with the brief while Klint works.
6. Wait for Klint (or give control back to the user).
7. Merge, filter, and rank the creators. Finish the artifact and the CSV.
8. Offer the next step: TikTok, or more Instagram creators.

### 1. Get the website. Check for Klint.

- If the user did not give a website, ask for it. That is the only input you need.
- If the user pasted a **resume block** (from step 3 or step 6 of an earlier chat), skip to the step that the block names.
- Look at your tools. Klint is connected if you have a tool whose name contains `klint_start_agent`.
- If Klint is **not** connected, say this one line and continue:
  > I'll research your brand now. To find the creators at the end, you'll need Klint connected (free). I'll show you how when we get there.

Do not stop. The brief comes first, with or without Klint.

### 2. Research the brand. Write the brief.

Follow `references/brief.md`. It tells you which pages to read, what to search, where to find customers' own words, and the fields of the brief.

Do not research Reddit. Claude's web tools cannot read reddit.com.

Use only web search and web fetch for this step. Do not use Klint for research.

### 3. Checkpoint

Send **one** message. Use this form:

> **Here's what I found about {Brand}**
> {Two-line summary: what they sell, to whom, and why people buy.}
>
> **Target customer:** {one line}
> **Pain points:** {3 to 5, each with a short customer phrase from a review}
> **Competitors:** {3 to 5}
> **Country:** {from the site's currency and shipping} · **Creator size:** {default: micro and mid, 10K–500K followers}
>
> Tell me anything I got wrong, and any preferences:
> - **Country** to search
> - **Creator size:** nano (1K–10K), micro (10K–100K), mid (100K–500K), macro (500K+)
> - **Creators or brands to avoid**
>
> {Cost line from the Klint cost block: "This starts 3 Klint agents and takes 10–25 minutes. New Klint accounts come with free credits; a full run can use most or all of them."}
>
> Reply **go** to start.

If Klint is not connected, add the connection steps before "Reply go":

> **To find the creators, connect Klint (free, about 2 minutes):**
> 1. Make a free account at {Sign up}.
> 2. In Claude, open **Customize → Connectors**. Click **+ Add**, then **Add custom connector**. Name it **Klint** and paste **{Connector URL}**. Click **Continue**, choose **Sign in now**, click **Add**, and sign in.
> 3. Come back here and reply **go**.

Then wait. Apply every correction the user gives before step 4. If the user changes the brief a lot, show the changed lines once, then continue when they say "go".

### 4. Start the 3 Klint agents

- Check for the Klint tools again. If they are still missing, a new connector sometimes shows only in a **new chat**. Give the user a resume block (see "Resume blocks" below) and tell them to paste it into a new chat.
- Write the 3 prompts from `references/klint-prompts.md`. Fill every field from the brief and the checkpoint answers.
- Start all 3 agents in the same turn with `klint_start_agent`. Do not wait for one before you start the next.
- Write the agent IDs in the chat, so they are not lost if the chat pauses:
  > Klint agents started: **Category** `{id}` · **Pain** `{id}` · **Customer** `{id}`

### 5. Build the artifact while Klint works

Follow `references/output.md`. Make the artifact now with the full brief, and put a "Klint is searching Instagram…" note where the creators will go. The user sees real work while Klint searches.

### 6. Wait for Klint

Use `klint_get_agent_status` for each agent ID.

**If you have a shell tool (for example Bash in Claude Code):** you can wait. Run `sleep 120` between checks. If a foreground `sleep` is blocked, run it as a background command and check when it finishes. Continue until each agent is done, has failed, or has worked for 20 minutes. Do not give control back to the user.

**If you do not have a shell tool (Claude Desktop, claude.ai):** you cannot wait. Do not call the status tool again and again in a loop. Do this:

1. Check each agent's status one time, after you build the artifact.
2. Read the reply of each agent that is done (`klint_get_agent_reply`).
3. If any agent is still working, end your turn with:
   > Klint is still searching Instagram. This usually takes 10–25 minutes. Reply **check** and I'll pull in the creators.
4. When the user replies "check", do steps 1 to 3 again. Add creators to the artifact as each agent finishes.

An agent that is still working is not stuck until it has worked for 20 minutes.

### 7. Merge, filter, and rank

When all 3 agents are done (or failed, or stuck), follow `references/ranking.md`. Then finish the artifact and make the CSV as `references/output.md` says.

Do not wait for a perfect set. If one agent failed, build the list from the other two, and tell the user which angle is missing.

### 8. Offer the next step

After the shortlist, say:

> Want more? **(1) The same search on TikTok**, or **(2) go deeper on Instagram**, on the angle that found your best creators. Either one uses more Klint credits.

- **TikTok:** send the TikTok follow-up from `references/klint-prompts.md` to the **same 3 agents** with `klint_message_agent`. A follow-up is cheaper than a new agent. Put TikTok creators in a separate section of the artifact and in a separate CSV.
- **Deeper on Instagram:** send the "deeper" follow-up to the **one** agent whose creators ranked highest.
- Use steps 6 and 7 again for the follow-up replies.

## When something fails

| What happens | What you do |
|---|---|
| One agent fails, and other agents are still working or done | Klint sometimes fails a long first search ("Something went wrong") and then succeeds on a retry. Retry it **one time** at once, with `klint_message_agent` on the same agent ID: "The last request failed. Please try again with the same brief, requirements, and format. If you already found creators, return those first. Aim for 10–15 creators; fewer is fine if they are well checked." Tell the user in one line. If the retry fails too, build the list from the other agents and name the missing angle. |
| All agents fail at the same time, or a retry fails at once | Say it is most likely the Klint credits. Tell the user to check their credits (Klint cost block). Give a resume block so they can continue after a top-up. |
| An agent works for more than 20 minutes | Call it stuck. Continue without it. |
| A follow-up fails | Send it again one time. If it fails again, treat it as a failed agent. |
| A Klint reply has fewer creators than you asked for | Use what it gave. Do not add creators from anywhere else. |

## Resume blocks

When the user must continue in a new chat, give one fenced block that they can paste:

```
Find Instagram influencers — resume at step {4 or 6}
Website: {url}
Brief: {the full brief, compact}
Checkpoint: country {…}; size {…}; avoid {…}; user said go
Klint agents (only at step 6): Category {id} · Pain {id} · Customer {id}
```

## Rules

- **Every creator comes from a Klint reply.** Never add a creator, handle, follower count, or post from memory or from web search. If Klint did not give it, it is not in the list.
- **Every fit has proof.** Each creator needs at least one post link that shows the fit. A bio alone is not proof.
- **Adults only.** If anything suggests a creator is under 18, or you cannot tell, remove the creator.
- **Sponsored posts are a good sign.** A creator who has done paid posts knows how deals work. Only flag a creator when nearly every recent post is an ad.
- **Profile photos, saved into the page.** Klint photo links expire, so download each photo and put it in the page as a `data:` URI (`references/output.md`). Use initials when there is no photo.
- **No made-up contact details.** Show an email or "contact in bio" only if Klint returned it.
- **Short quotes only.** Quote reviewers in 25 words or fewer, with a link.
- **Plain words about data.** Say "public posts" or "the public internet". Do not say "scrape".
