# Brand research and the brief

Use web fetch and web search only. Keep this step to about 20 tool calls. The brief must be good enough to aim the Klint agents. It does not have to be a full report.

Do not research Reddit. Claude's web tools cannot read reddit.com, and Reddit mirror sites are not a source.

## A. Read the website (8 to 15 pages)

1. Fetch the home page. It usually gives the products, the prices, the currency, the Instagram handle, and the main links.
2. Try `{site}/sitemap.xml` only if the home page links are not enough. Many sitemaps are an index of other sitemaps; open only the product sitemap.
3. Choose pages in this order:
   - The 3 to 5 main product pages (best sellers first)
   - About or "our story"
   - How it works, ingredients, materials, or science
   - Shop or pricing (for the price range)
4. From each page, take only what the brief needs. Do not copy long text.

Many brand sites load FAQ answers and customer reviews with JavaScript, so a fetch shows only headings or star ratings. Do not fetch those pages again. Get reviews from other sites (part C).

Note the currency, the shipping countries, and any "as seen in" or creator content on the site.

## B. Search the web (4 to 6 searches)

- `{brand} {best-selling product} review` — finds review articles
- `{brand} vs` and `{brand} alternatives` or `{brand} dupes` — finds the competitors
- `best {product category}` — finds the competitors that buyers compare
- `{brand} founder` or `{brand} news` — finds the story, investors, and creator partnerships in the press

Competitors are direct-to-consumer peers that a buyer compares with this brand. They are not big retailers or mass-market drugstore brands, unless nothing else fits. Pick 3 to 5.

Check the dates of news results. Note anything big from the last year (a new owner, a new chief executive, a famous investor).

## C. Find the customers' own words

The Klint "pain" agent uses these words to find creators, so this part matters most. You want the words people use about their problem ("my dark spots won't fade"), not marketing words ("hyperpigmentation correction").

Good sources, in this order:

1. **Review articles** from part B. Reviewers often describe their problem before they describe the product.
2. **Review and comparison sites** for the category, for example product-review communities, "dupe" sites, and retailer review pages. Some block fetches; if one blocks, move on.
3. **The text in search results.** Search for the problem itself, such as `{main problem} nothing works` or `{main problem} what helped`, and read the result text. Do not open forum mirror sites.

Take:

- The problems people describe, **in their words**
- What they tried before and why it failed
- What they like or dislike about this brand or its competitors

Keep each quote to 25 words or fewer, and keep its link. If you cannot find a real quote for a pain point, write the customer phrase without a quote. Never make up a quote.

## D. Write the brief

Use these fields. Keep the whole brief short enough to read in one minute.

| Field | What to write |
|---|---|
| Brand | Name, website, Instagram handle if found |
| What they sell | One line, plus the price range |
| Target customer | One line, plus 2 or 3 traits (life stage, interests, values) |
| Pain points | 3 to 5. For each: a short label, the customer's own phrase, and one review quote with its link if you found one |
| Competitors | 3 to 5, with Instagram handles only if you saw them on a page |
| Why people buy | One or two lines: what the brand promises that the competitors do not |
| Instagram angle | One or two lines: what kind of post a creator would make for this brand |
| Country | From the currency and shipping. Default for the search |
| Creator size | Default: micro and mid (10K–500K followers), unless the brand is very small or very large |

## E. Words for the Klint prompts

At the end of research, also write (for yourself, not for the user) 6 to 10 **search phrases** that creators would use in captions about the pain points. Use the customers' words. For example, for an eczema brand: "eczema journey", "flare up", "eczema skincare routine", "TSW", "my skin story". You put these in the "pain" agent prompt.
