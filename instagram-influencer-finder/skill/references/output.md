# The artifact and the CSV

The user gets two things: one **artifact** (the brief and the creator shortlist) and one **CSV** (the creator table).

## The artifact

Use `assets/shortlist-template.html`. Copy it as it is. Change **only** the `DATA` object at the top of the `<script>`. The page draws everything from `DATA`, so you do not write any HTML.

- **Claude Desktop or claude.ai:** make an HTML artifact from the filled template. Title it "{Brand} — Instagram creator shortlist".
- **No artifacts (for example Claude Code):** write the filled file as `{brand-slug}-creator-shortlist.html` in the working folder, and give the user the path.

### Two times you write it

1. **Step 5 (while Klint works):** fill `brand`, `brief`, `painPoints`, and `competitors`. Set `status` to `"searching"` and `creators` to `[]`. The page shows "Klint is searching Instagram…".
2. **Step 7 (after ranking):** add the creators, set `status` to `"done"`, and fill `summary`. If an angle failed, put it in `missingAngles`. Update the same artifact; do not make a second one.

For TikTok results (step 8), put the creators in `tiktokCreators` with the same fields. The page shows them in a separate section.

### The DATA fields

```js
const DATA = {
  status: "searching",            // "searching" or "done"
  generated: "2026-11-17",        // today's date
  brand: { name: "", url: "", instagram: "" },
  brief: {
    sells: "", priceRange: "", customer: "", whyBuy: "", angle: "",
    country: "", size: ""
  },
  painPoints: [ { label: "", phrase: "", quote: "", quoteUrl: "" } ],
  competitors: [ { name: "", instagram: "" } ],
  summary: "",                    // the 3–4 lines from ranking.md step 6, as one short paragraph
  missingAngles: [],              // e.g. ["Pain"]
  creators: [ {
    rank: 1, handle: "", name: "", url: "", photo: "", followers: 0, country: "",
    angles: ["Category", "Pain"], // any of "Category", "Pain", "Customer"
    alreadyFan: false,
    whyFit: "", painPoint: "",    // painPoint = the brief label it matches
    proof: [ { url: "", note: "" } ],
    sponsored: "6 of last 20", brands: ["Our Place"],
    lastPost: "", contact: "", redFlags: []
  } ],
  tiktokCreators: []
};
```

Use `""` or `[]` for anything you do not have. Do not invent values to fill a field.

### Profile photos

Each card shows the creator's profile photo. The Klint record gives a "Profile photo" URL.

- Klint photo links expire within hours to days. So **download each photo at once and put it in `photo` as a `data:` URI** (`data:image/jpeg;base64,…`). Then the page keeps its photos when the user shares it next week.
- **Claude Code:** download with `curl -sL "<url>" -o <handle>.jpg`, check that the file is an image (not an error page), and base64-encode it.
- **Claude Desktop or claude.ai:** use code execution to download and encode the photos if the sandbox can reach the image host. If it cannot, put the URL itself in `photo`. The page shows initials when a photo stops loading.
- If a URL returns an error (often HTTP 403), the signature is missing. Ask the same Klint agent once with `klint_message_agent`: "Give the complete, unshortened profile picture URL with every query parameter for: {handles}, in one plain code block." Do not get photos from Instagram pages yourself.
- If there is still no photo, leave `photo` empty. The page shows initials.

## The CSV

Make one CSV file with one row for each creator in the shortlist, in rank order. Name it `{brand-slug}-instagram-creators.csv` (and `{brand-slug}-tiktok-creators.csv` for TikTok).

- **Claude Desktop or claude.ai:** create the file so the user can download it.
- **Claude Code:** write it in the working folder.

Columns, in this order:

```
rank,platform,handle,profile_url,name,followers,country,angles,already_a_fan,why_they_fit,pain_point,proof_post_1,proof_post_2,proof_post_3,sponsored_last_20,brands_promoted,last_post,contact,red_flags
```

- `angles`: separated by ` | ` (for example `Category | Pain`)
- `already_a_fan`: `yes` or `no`
- Put quotes around any value that has a comma, and double any quote inside it.

## After you deliver

Give the user the lines from `ranking.md` step 6, then the offer from SKILL.md step 8.
