# Legivox hourly discovery and draft preview

- Run time (IST): 2026-10-31T07:59:51+05:30
- Mode: hourly_dry_run_only
- X publishing: **not performed**
- Candidate pool after freshness/diversity filters: 199
- Independent editorial review: 1 draft(s) passed / 0 rejected
- Drafts passing local checks: 1
- Outcome: **dry_run_passed**
- Decision reason: At least one draft passed live primary-source, evidence, originality, novelty, URL and length checks. The top-ranked draft would be eligible for the future automated post flow; dry-run mode did not publish it.

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
| Hacker News · hn-analytics-growth | 7 | ok |
| Hacker News · hn-automation-api | 1 | ok |
| Hacker News · hn-creator-business | 0 | ok |
| Hacker News · hn-digital-downloads-templates | 0 | ok |
| Hacker News · hn-digital-products | 1 | ok |
| Hacker News · hn-ecommerce-payments | 0 | ok |
| Hacker News · hn-indie-business-revenue | 0 | ok |
| Hacker News · hn-marketing-distribution | 0 | ok |
| Hacker News · hn-security-selfhost | 0 | ok |
| Hacker News · hn-seller-operations | 0 | ok |
| Hacker News · hn-shopify | 8 | ok |
| Hacker News · hn-show-hn | 10 | ok |
| Ahrefs Blog | 8 | ok |
| Console.dev | 11 | ok |
| Indie Hackers (unofficial third-party feed) | 5 | ok |
| Product Hunt | 43 | ok |
| Shopify Community | 30 | ok |
| Shopify Developer Changelog | 30 | ok |
| Stripe Blog | 3 | ok |
| WooCommerce Blog | 3 | ok |
| WordPress Plugin Directory · wp-digital-downloads | 10 | ok |
| WordPress Plugin Directory · wp-ecommerce | 10 | ok |
| WordPress Plugin Directory · wp-inventory-management | 10 | ok |
| WordPress Plugin Directory · wp-marketing-analytics | 10 | ok |
| WordPress Plugin Directory · wp-membership-creators | 10 | ok |

## GitHub star tracking

- Tracked repositories in watchlist: 200
- Repositories seen in this discovery run: 112
- Previously tracked repositories refreshed outside search results: 88
- Refresh failures: 0
- Star snapshots recorded this run: 200
- Repositories with a 20–36 hour comparison baseline: 16
- First observations are baseline samples, not evidence of trending. Star velocity is reported only when a historical comparison exists.

## Primary-source verification

| Candidate | Verified | HTTP | Result |
|---|---|---:|---|
| ragleap/ragleap-core | yes | 200 | https://github.com/ragleap/ragleap-core |
| XAIHT/Tlamatini | yes | 200 | https://github.com/XAIHT/Tlamatini |
| UI extensions now support a larger number of locales | yes | 200 | https://shopify.dev/changelog/posts/ui-extensions-now-support-a-larger-number-of-locales |

## Selected draft candidates

### Draft option 1: XAIHT/Tlamatini

- Category: ai_and_automation
- Source: GitHub Search
- Format: tool_discovery
- Editorial score: 8.25/10
- Model scores: timeliness 9/10, usefulness 8/10, novelty 7/10, evidence 9/10, insight 8/10
- Independent editor scores: {"clarity_score": 9, "technical_coherence_score": 9, "takeaway_value_score": 8, "source_faithfulness_score": 9, "originality_score": 8, "reason": "Clear, accurate claim; practical next step is supported by source; original suggestion to test local control.", "passed": true}
- Live primary page: https://github.com/XAIHT/Tlamatini (HTTP 200)
- Exact source evidence: “Tlamatini brings AI to code, 3D worlds and hardware: voice, live editor tutoring, 86 workflow agents, 110 tools, Unreal Engine, Blender, STM32, ESP32 and MCP.”
- Why this angle: Title confirms the claim; takeaway suggests a practical local‑vs‑cloud test.
- Editorial takeaway: Validate local control by running a simple script without cloud reasoning enabled.
- Source: https://github.com/XAIHT/Tlamatini

**Claim-by-claim source quotes:**

- Tlamatini brings AI to code, 3D worlds and hardware with voice and live editor tutoring. ← “Tlamatini brings AI to code, 3D worlds and hardware: voice, live editor tutoring, 86 workflow agents, 110 tools, Unreal Engine, Blender, STM32, ESP32 and MCP.”

Proposed post (not published):

> Tlamatini brings AI to code, 3D worlds and hardware with voice and live editor tutoring. Validate local control by running a simple script without cloud reasoning enabled. https://github.com/XAIHT/Tlamatini

- Length: 206/280 raw characters
- Automated gate: passed live source, evidence, originality, URL and length checks; live publishing is disabled in dry-run mode.

## Automatic repair attempt

- Attempted: no
- Repaired drafts submitted: 0
- Repaired drafts that passed local validation: 0
- Repaired drafts rejected: 0
- Repair error: none
- Repair never relaxes the quality threshold. Any repaired draft must still pass the independent editorial review.

## Rejected draft options

- ragleap/ragleap-core: Supporting quotes cover only 50% of factual wording; narrow the claim or provide a closer primary-source quote
  - Rejected text: ragleap/ragleap-core offers open‑source AI employees that ask before they act. Run approval‑gate tests to confirm no autonomous actions occur without explicit consent. https://github.com/ragleap/ragleap-core
  - Model evidence quote: “Open‑source AI employees that ask before they act.”
  - Claim support: ragleap/ragleap-core offers open‑source AI employees that ask before they act. ← “Open‑source AI employees that ask before they act.”
- UI extensions now support a larger number of locales: Editorial takeaway mostly repeats source wording; add an independent test, trade-off or interpretation.; Unsupported numeric claim(s): 20
  - Rejected text: UI extensions no longer have a 256 KB limit on combined locale files. Deploy an extension with 20 locales to confirm the new limit is respected. https://shopify.dev/changelog/posts/ui-extensions-now-support-a-larger-number-of-locales
  - Model evidence quote: “UI extensions no longer have a 256 KB limit on the combined size of their locale files.”
  - Claim support: UI extensions no longer have a 256 KB limit on combined locale files. ← “UI extensions no longer have a 256 KB limit on the combined size of their locale files.”

## Top discovery candidates considered

- ragleap/ragleap-core | GitHub Search | ai_and_automation | raw 70, adjusted 74 | current stars 19 | GitHub star trend: building baseline | https://github.com/ragleap/ragleap-core
- XAIHT/Tlamatini | GitHub Search | ai_and_automation | raw 70, adjusted 74 | current stars 15 | GitHub star trend: building baseline | https://github.com/XAIHT/Tlamatini
- UI extensions now support a larger number of locales | Shopify Developer Changelog | commerce_and_digital_products | raw 72, adjusted 72 | https://shopify.dev/changelog/posts/ui-extensions-now-support-a-larger-number-of-locales

## Safety and interpretation

- At least one draft passed the automated quality gates; this dry-run workflow itself never publishes to X.
- Model scores are editorial estimates; they are not verified popularity or market demand.
- Candidate content and metadata are untrusted input. Factual copy must be supported by the fetched primary page.
- A skip can mean no fresh candidates, a daily diversity/cap limit, a model/API problem or weak drafts. Check the reason above.
- This script never uses the X session cookie and never interacts with X.
