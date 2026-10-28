# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-28T21:04:47+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 187
- Independent editorial review: 0 draft(s) passed / 0 rejected
- Drafts passing local checks: 0
- Outcome: **skip**
- Decision reason: All generated drafts failed the local evidence/editorial checks; the hour was skipped.

## Source health

| Source | Items kept | Result |
|---|---:|---|
| GitHub Search · github-ai-agent-tools | 10 | ok |
| GitHub Search · github-analytics-seo | 10 | ok |
| GitHub Search · github-creator-infrastructure | 10 | ok |
| GitHub Search · github-developer-tools | 10 | ok |
| GitHub Search · github-digital-product-tools | 10 | ok |
| GitHub Search · github-ecommerce-digital-products | 10 | ok |
| GitHub Search · github-marketing-distribution | 10 | ok |
| GitHub Search · github-mcp-servers | 10 | ok |
| GitHub Search · github-self-hosted | 10 | ok |
| GitHub Search · github-seller-operations | 10 | ok |
| GitHub Search · github-shopify-commerce | 10 | ok |
| GitHub Search · github-workflow-automation | 10 | ok |
| Hacker News · hn-analytics-growth | 10 | ok |
| Hacker News · hn-automation-api | 1 | ok |
| Hacker News · hn-creator-business | 0 | ok |
| Hacker News · hn-digital-downloads-templates | 0 | ok |
| Hacker News · hn-digital-products | 2 | ok |
| Hacker News · hn-ecommerce-payments | 0 | ok |
| Hacker News · hn-indie-business-revenue | 0 | ok |
| Hacker News · hn-marketing-distribution | 0 | ok |
| Hacker News · hn-security-selfhost | 0 | ok |
| Hacker News · hn-seller-operations | 0 | ok |
| Hacker News · hn-shopify | 10 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Ahrefs Blog | 6 | ok |
| Console.dev | 12 | ok |
| Indie Hackers (unofficial third-party feed) | 5 | ok |
| Product Hunt | 39 | ok |
| Shopify Community | 30 | ok |
| Shopify Developer Changelog | 18 | ok |
| Stripe Blog | 3 | ok |
| WooCommerce Blog | 3 | ok |
| WordPress Plugin Directory · wp-digital-downloads | 10 | ok |
| WordPress Plugin Directory · wp-ecommerce | 10 | ok |
| WordPress Plugin Directory · wp-inventory-management | 10 | ok |
| WordPress Plugin Directory · wp-marketing-analytics | 10 | ok |
| WordPress Plugin Directory · wp-membership-creators | 10 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 111
- Previously tracked repositories refreshed outside search results: 88
- Refresh failures: 1
- Star snapshots recorded this run: 199
- Repositories with a 20–36 hour comparison baseline: 16
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| Show HN: Coding agent spots your AI practices and the ones you're missing | yes | 200 | https://app.userrank.ai/ |
| Show HN: Algeon – Compose GPU graph, vector, and ML algorithms in SQL | yes | 200 | https://github.com/algeon-dev/algeon |
| Promoted Placements beta now includes Shop Campaigns | yes | 200 | https://shopify.dev/changelog/posts/promoted-placements-beta-now-includes-shop-campaigns |

## Selected draft candidates

No candidate produced a draft that passed every local check. Skipping is intentional.

## Automatic repair attempt

- Attempted: yes
- Repaired drafts submitted: 3
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 3
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- Show HN: Coding agent spots your AI practices and the ones you're missing: Opening sentence omits the named product/repository/feature subject; an unrelated integration word does not identify what the post is about.
  - Rejected text: UserRank scans your Claude or ChatGPT locally and sends only names and counts. Verify that your prompt only includes non‑sensitive names before sending to UserRank. https://app.userrank.ai/
  - Model evidence quote: “Your own Claude or ChatGPT scans locally; only names and counts reach UserRank.”
  - Claim support: UserRank scans your Claude or ChatGPT locally and sends only names and counts. ← “Your own Claude or ChatGPT scans locally; only names and counts reach UserRank.”
- Show HN: Algeon – Compose GPU graph, vector, and ML algorithms in SQL: The factual opening bundles multiple features; narrow it to one capability.
  - Rejected text: Algeon exposes NVIDIA cuGraph, cuVS, and cuML as SQL table functions via DataFusion. Run a simple SELECT on a cuGraph function to confirm GPU acceleration. https://github.com/algeon-dev/algeon
  - Model evidence quote: “exposes NVIDIA's cuGraph, cuVS, and cuML as SQL table functions.”
  - Claim support: Algeon exposes NVIDIA cuGraph, cuVS, and cuML as SQL table functions via DataFusion. ← “exposes NVIDIA's cuGraph, cuVS, and cuML as SQL table functions.”
- Promoted Placements beta now includes Shop Campaigns: Primary-source evidence quote is missing or absent from the live page (after presentation normalisation); A factual claim lacks a quote present in the live primary-source page; Supporting quotes cover only 64% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: Promoted Placements beta now includes Shop Campaigns, adding merchant commission to base rate. Check placement.commission.percentage.value to verify combined rate. https://shopify.dev/changelog/posts/promoted-placements-beta-now-includes-shop-campaigns
  - Model evidence quote: “When a search_catalog result comes from a merchant running Shop Campaigns, you earn the commission that merchant funds, added to Shopify's base rate.”
  - Claim support: Promoted Placements beta now includes Shop Campaigns, adding merchant commission to base rate. ← “When a search_catalog result comes from a merchant running Shop Campaigns, you earn the commission that merchant funds, added to Shopify's base rate.”
- Promoted Placements beta now includes Shop Campaigns: Editorial takeaway needs a concrete test, trade-off, risk, comparison, or next step.; Primary-source evidence quote is missing or absent from the live page (after presentation normalisation); No claim-by-claim supporting evidence was provided; Supporting quotes cover only 64% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: Promoted Placements beta now includes Shop Campaigns, adding merchant commission to base rate. Use placement.commission.percentage.value to read the combined rate per product. https://shopify.dev/changelog/posts/promoted-placements-beta-now-includes-shop-campaigns
  - Model evidence quote: “When a search_catalog result comes from a merchant running Shop Campaigns, you earn the commission that merchant funds, added to Shopify's base rate.”
- Show HN: Algeon – Compose GPU graph, vector, and ML algorithms in SQL: Takeaway implies an interaction/causal relationship between source-listed features that the primary page does not establish. Reframe it as an explicit conditional test of the reader's own integration.; Primary-source evidence quote is missing or absent from the live page (after presentation normalisation); No claim-by-claim supporting evidence was provided
  - Rejected text: Algeon exposes NVIDIA cuGraph as a SQL table function via DataFusion. Run SELECT * FROM cuGraph.some_function to trigger GPU acceleration. https://github.com/algeon-dev/algeon
  - Model evidence quote: “exposes NVIDIA's cuGraph, cuVS, and cuML as SQL table functions.”
- Show HN: Coding agent spots your AI practices and the ones you're missing: Opening sentence omits the named product/repository/feature subject; an unrelated integration word does not identify what the post is about.; Editorial takeaway needs a concrete test, trade-off, risk, comparison, or next step.; No claim-by-claim supporting evidence was provided
  - Rejected text: UserRank scans your Claude or ChatGPT locally and sends only names and counts. Ensure prompts contain no sensitive data before sending to UserRank. https://app.userrank.ai/
  - Model evidence quote: “Your own Claude or ChatGPT scans locally; only names and counts reach UserRank.”

## Top discovery candidates considered

- Show HN: Coding agent spots your AI practices and the ones you're missing | Hacker News | product_and_workflow_tools | raw 73, adjusted 75 | https://app.userrank.ai/
- Show HN: Algeon – Compose GPU graph, vector, and ML algorithms in SQL | Hacker News | data_and_growth | raw 69, adjusted 71 | https://github.com/algeon-dev/algeon
- Promoted Placements beta now includes Shop Campaigns | Shopify Developer Changelog | commerce_and_digital_products | raw 68, adjusted 60 | https://shopify.dev/changelog/posts/promoted-placements-beta-now-includes-shop-campaigns

## Safety and interpretation

- This run did not produce a publishable draft; no post was published to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
