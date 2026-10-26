# Legivox Market Validation Playbook

## Purpose

Legivox has two related but separate jobs:

1. **Public content discovery:** find useful digital products, creator tools, online-business workflows, commerce operations, practical marketing/distribution lessons and technology people can act on.
2. **Our own product research:** identify a specific buyer, a painful recurring job, evidence that money is already being spent, a credible gap in the existing solutions, and a channel where we can reach buyers before building a product.

A topic appearing in a launch feed is a content lead. It is not automatically a market opportunity. Do not treat GitHub stars, upvotes, forum mentions, search interest or a model-generated score as proof of willingness to pay.

## What counts as evidence?

Use a hierarchy rather than one blended popularity score:

1. **Strongest:** real paid purchases, paid competitors, pre-orders/deposits from unrelated target buyers, and renewal/retention evidence where available.
2. **Strong:** marketplace search counts and listing competition; many independent buyers describing the same problem; detailed competitor reviews showing a repeated, specific failure or missing workflow.
3. **Supporting:** Google Trends, active installations, downloads, ratings, forum activity, Product Hunt votes, GitHub stars and Hacker News comments.
4. **Weak by itself:** launch announcements, lifetime star counts, one enthusiastic comment, generic trend articles, founder claims without evidence, or friends saying they would pay.

Signals must retain their source, date, market/geography, and limitation. Do not combine unlike quantities into a fake "market demand score".

## Research sources

### Search and marketplace evidence

- **Etsy Marketplace Insights** — https://help.etsy.com/hc/en-us/articles/35122361353239-How-Do-I-Use-Etsy-s-Marketplace-Insights-Tool  
  Use buyer keyword search counts and listing counts over the last 30 days to compare demand with competition. The current help page says the free tier allows 15 keyword searches per week. This requires access to Etsy Shop Manager, so record the values manually instead of scraping a signed-in account. Search terms must be narrow and buyer-oriented.

- **Etsy Seller Handbook / Trend Reports** — https://www.etsy.com/in-en/seller-handbook  
  Use official trend reports as contextual evidence, not as proof that a particular digital download will sell. Some report metrics are marketplace-specific, time-bound, and based on US signed-in users.

- **AppSumo marketplace and reviews** — https://appsumo.com/  
  Track paid offer prices, product positioning, review counts, recurring objections in negative reviews, and claims about purchases where a partner story discloses them. Deal buyers may be unusually price-sensitive, and review/purchase figures are not comparable across products. It is useful for finding categories where people pay, plus complaints to investigate.

- **Gumroad Discover** — https://gumroad.com/help/article/79-gumroad-discover  
  Inspect real digital product offers, formats, prices, positioning and customer reviews where visible. Do not infer sales volume from a listing alone. Gumroad's current eligibility guidance requires at least USD 100 in genuine seller balance plus review/verification before a creator is eligible for Discover; therefore Discover examples are selected toward creators who already achieved some sales.

- **Shopify digital products and merchant ecosystem** — https://help.shopify.com/en/manual/products/digital-service-product/digital-downloads and https://community.shopify.com/latest.rss  
  Use the official help pages to understand product formats and delivery constraints; use community discussions for repeated merchant problems, workarounds and app requests. The Developer Changelog remains useful for platform changes, but it must not stand in for research into digital-product selling or merchant demand.

- **Shopify App Store / WordPress.org Plugin Directory** — https://apps.shopify.com/ and https://wordpress.org/plugins/  
  Review competing paid tools and recurring low-star complaints. WordPress.org's public Plugin Directory API provides adoption and feedback metadata (including active installations, downloads, rating and number of ratings). These are usage/feedback signals, not proof that customers pay for the plugin; many are free.

- **Google Trends** — https://trends.google.com/trends/explore  
  Compare several related phrases across markets and time. Google explains that Trends is normalized to a 0–100 relative scale and is not an absolute search-volume report. Treat spikes as a clue, not as a sales forecast.

### Problem and competitor discovery

- **Shopify Community, app reviews, Etsy seller discussions and Reddit communities** — collect concrete examples of repeated work, failed workarounds, complaints and current tool costs. One post is anecdotal; several independent reports from different users and dates are a stronger pattern.
- **Indie Hackers** — https://indiehackers.com/ and its community's unofficial RSS mirror, https://feed.indiehackers.world/ . Use transparent founder case studies and reported revenue to generate questions, then verify the original post. Treat revenue anecdotes as self-reported and subject to survivorship bias.
- **Hacker News / Show HN / Product Hunt** — use launch discussions and comments to find new tools and objections. They overrepresent technology audiences, and launches/votes are not evidence of paying demand.
- **Stripe, WooCommerce, and Ahrefs blogs** — useful for changes in payments, commerce workflows, SEO and distribution. They are context and content sources, not customer-demand measurements.

## The Shopify change

The source registry should distinguish at least three separate Shopify signals:

1. **Developer Changelog:** product/platform releases, API changes and documentation changes.
2. **Merchant Community:** repeated seller problems, workarounds, requested features and questions.
3. **App Store reviews:** competing solutions, prices, complaints and potential gaps.

None of these alone proves demand for a digital download. To research digital-product creation and selling itself, use marketplaces, search-demand data, and creator/seller discussions alongside them.

## Product research loop: market first, build second

### Stage 1 — Choose buyer segments, not products

Start with a small number of buyer groups:

- People already selling digital downloads, templates, courses, assets or software.
- Small online sellers who manage pricing, inventory, listings, orders, refunds and customer support.
- Independent creators, freelancers and tiny agencies with repeatable operational work.
- Small businesses with a specific, spreadsheet-heavy task that existing software handles poorly.

Do not start by choosing "an app", "an AI tool", or "a template". Choose a buyer and a job they already need to complete.

### Stage 2 — Collect evidence

For each candidate problem, record:

- Who experiences it and in what circumstances.
- What the buyer currently uses or pays for.
- The last real occasion it caused extra work, lost revenue, errors or risk.
- The workaround and its cost in time or money.
- At least two independent source types that point to the same problem.
- Competitors, prices, recent product activity, distribution channels and the recurring themes in low-star reviews.
- What evidence would disprove the hypothesis.

For the initial research pass, gather at least 20 distinct problem reports across at least three source groups for each serious candidate. Deduplicate copies of the same complaint and do not mistake a popular thread for 20 independent buyers.

### Stage 3 — Inspect competitors for the gap

Study at least 10 competing products or substitutes where available. Record price, intended buyer, core workflow, delivery format, marketplace visibility, reviews and obvious limits. Read negative and middle-rated reviews, not only testimonials.

Existing competition is usually useful evidence that buyers understand the category. The opportunity is not "no competitors"; it is a narrower buyer or workflow that existing products underserve. A missing feature is only a hypothesis until buyer behaviour shows that it matters.

### Stage 4 — Prove reachability

Because Legivox is starting without an established audience, a product idea also needs an acquisition path. Favor buyers who already search marketplaces or specific problem keywords, or who participate in reachable specialist communities. Direct outreach to a narrowly defined group is a valid low-cost test. Do not assume that a product page, an X account, or an app launch will create demand by itself.

Record the exact query, marketplace, community or partner path through which a stranger could plausibly discover the offer. If the only distribution plan is "post on social media and hope", the candidate has not passed.

### Stage 5 — Validate before building

1. Make a one-page offer that names the buyer, painful job, outcome, scope, exclusions, price and delivery date.
2. Show a concrete sample, mock-up, spreadsheet tab, screenshot or manually delivered result. Do not build a full app.
3. Contact 30 relevant prospective buyers or use a marketplace/channel where buyers already search.
4. Ask about recent behaviour and current costs, not hypothetical enthusiasm.
5. Where appropriate, ask for a paid pilot or pre-order with clear terms and a refund policy.

**Suggested go/no-go gate:** proceed to a small build only after (a) recurring problem evidence from multiple independent sources, (b) existing paid spending or comparable paid competitors, (c) a specific visible gap, (d) a plausible non-ad distribution path, and (e) at least three unrelated prospective buyers actually pay/pre-order or another comparably strong commitment is observed. If buyers will not commit, revise or discard the hypothesis rather than adding features.

### Stage 6 — Build the smallest paid solution

Deliver the smallest artifact that solves the job: a spreadsheet/workbook, template pack, guide with operational tools, script, small automation, plugin or micro-utility. Start with manual fulfilment if it tests the buyer outcome. Automate only the part whose value has been demonstrated.

## Starter hypothesis backlog (not recommendations yet)

These are research directions only. None has passed validation:

| Hypothesis | What we need to verify | Main risk |
|---|---|---|
| Digital-product seller operations | Do specific seller segments struggle with margin/fees, listing data, refunds/support, product updates or multi-channel reconciliation? Which exact keyword has buyer searches relative to listings? | Generic seller spreadsheets are crowded and often priced low. |
| Small online-business workflow tools | Which one repeated task in orders, inventory, pricing, reporting or follow-up is currently handled in brittle spreadsheets or by manual copying? | Broad operations suites already exist; distribution and trust are hard. |
| Creator/freelancer repeatable workflows | Are there narrow, recurring jobs in proposals, client handoff, content repurposing, lead tracking or reporting with clear paid alternatives and dissatisfied users? | Lots of free templates and creator tools; discovery can depend on audience. |
| Marketplace-specific product research helpers | Will a specific seller pay to reduce a recurring research/analysis task using data they are allowed to access? | Marketplace data access, terms, data quality and competition may block the product. |

For each candidate, score evidence quality, pain frequency/severity, spending, differentiation, distribution and build/maintenance cost separately. Keep unknowns as unknowns. Do not declare a "validated niche" until the evidence is in the research log.

## Operating principles

- Market research and content discovery are separate queues; a topic can be interesting to publish about without being a business opportunity for us.
- The hourly X pipeline must not publish product-demand claims based only on launches, GitHub stars, search trends, review counts or anecdotes.
- Manual marketplace values should be dated and saved with their source URL and context.
- Respect official APIs and source terms; do not automate scraping of signed-in dashboards such as Etsy Marketplace Insights.
- Report null/insufficient data explicitly. Never fill a blank metric with a guess.
