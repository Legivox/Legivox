# Legivox Automation

Zero-budget GitHub Actions workflow for multidomain research, quality-gated source-grounded X publishing, GitHub star tracking, and evidence-led digital-product market research.

## Schedule
- 06:00 IST: prepare the curated research plan and manual-engagement shortlist.
- 08:00–23:00 IST, every hour: attempt one quality-gated post using the latest approved multidomain report.
- Discovery refresh: 07:17–22:17 IST, hourly, so the following hour's publishing slot has a recent report.

For scheduled posts, a random target is chosen inside the first 45 minutes of each one-hour window. If a workflow starts late, it can post immediately while the window remains open; if the window has expired, the post is skipped. GitHub can delay scheduled runs, so these are windows, not guaranteed exact times. Each hour may be skipped when discovery is stale, no candidate clears every source/editorial gate, model quota is exhausted, or publisher duplicate checks reject the copy. The discovery draft cap is 16 per IST date, matching the 16 publishing windows. Manual workflow dispatch defaults to preparing the curated plan only. For a deliberate live test, set the boolean publish_now input to true; it attempts one quality-gated multidomain post immediately when the latest report is fresh. This uses the production X session and can publish publicly.

## What is and isn't automated
- Topic selection uses a public, no-key Hacker News Algolia search endpoint. Discussion activity is a prioritisation signal, not proof of market demand.
- The legacy curated-plan workflow still uses individually written copy in data/ideas.json; the scheduled publishing slots now generate source-led news posts through the RSS + Groq pipeline.
- A reviewed starter library contains 20 topics and 60 copy variations for the curated plan. Hashes prevent intentional text reuse.
- The image step for curated posts searches Wikimedia Commons and attaches only relevant candidates marked CC0 or public domain. Scheduled RSS/Groq news posts default to text-only rather than attaching a generic category image.
- X search results for the day's niches are saved to output/engagement-shortlist.md for manual review. The workflow does not automate likes, replies, follows or reposts.

## Experimental multidomain discovery

The automated discovery queue is **research-only** and now covers useful digital products, creator tools, online-business workflows, commerce operations, marketing/distribution tactics and technology people can act on. Current editorial lanes include:
- Developer tools and infrastructure.
- AI, agents and automation.
- Digital products, templates, downloads and creator commerce.
- Online seller and small-business operations.
- Ecommerce, storefronts, payments and subscriptions.
- Creator tools, independent businesses and monetization.
- Search, SEO, marketing and distribution.
- Analytics, data and growth.
- Security, privacy and self-hosting.

The source registry is data/discovery_sources.json. Current automated discovery includes GitHub repository search, Hacker News/Show HN, Product Hunt, Console.dev, Shopify Developer Changelog, Shopify Community, Stripe Blog, Ahrefs Blog, WooCommerce Blog, an unofficial Indie Hackers RSS mirror, and WordPress.org's public Plugin Directory API. Indie Hackers is marked as an unofficial feed; generated claims still require primary-source verification. The research report records per-source health, and a source failure should not be mistaken for evidence that a market is quiet.

These sources serve different purposes: changelogs and blogs explain what changed; community posts surface problems and workarounds; marketplace listings/reviews show competitors and prices; search data helps compare demand with supply; and plugin installs/reviews show usage and feedback. None of these signals alone proves willingness to pay.

The research script is scripts/discover_candidates.py. Run the command *python scripts/discover_candidates.py --lookback-days 14 --limit 30* from the repository root to fetch a live preview. It writes output/discovery/discovery-report.md and output/discovery/discovery-candidates.json. No extra Python packages are required. An optional GITHUB_TOKEN environment variable improves GitHub API rate-limit headroom; do not commit any token.

The separate GitHub Actions workflow **Legivox multidomain discovery preview** runs tests and a read-only discovery preview on matching pull requests. Once the workflow is available on the default branch, it can also be run manually with a 7-, 14- or 30-day lookback. The report appears in the Actions run summary. It does not load the X session cookie or Groq API key, write to the production plan, or publish/interact on X.

## Market-first digital-product research

Our own product research is a separate track from the public X content queue. Read [the market-validation playbook](docs/market-validation-playbook.md), the [market research source map](data/market_research_sources.json), and the [unvalidated hypothesis backlog](data/market_validation_hypotheses.json).

The core rule is **market first, product second**. Pick a specific buyer and recurring job, look for independent evidence that people already search, spend money or use workarounds, study competing products and their negative reviews, prove that we can reach buyers without relying on paid ads or a pre-existing audience, and test a paid offer before building the full product.

Etsy Marketplace Insights is a manual research source because it requires seller-dashboard access; its official help page describes buyer search and listing counts over the previous 30 days and currently allows 15 free keyword searches per week. Google Trends gives normalized relative interest, not absolute search volume. AppSumo/Gumroad listings and reviews can reveal prices and competitors, but public listings alone do not expose reliable sales data. WordPress installs and ratings describe adoption and feedback, not payment. These distinctions are documented in the playbook and the source registry.

The starting hypothesis backlog covers digital-download seller operations, spreadsheet-heavy small-business work, and creator/freelancer distribution workflows. They are **unvalidated hypotheses**, not chosen products. No product should move to a build phase without evidence of a specific problem, existing spending, a credible market gap, an organic acquisition path, and a paid pilot or pre-order.

## Editorial quality standard: explain, don't announce

The source and creator list provided for Legivox is an editorial benchmark, not a request to imitate anyone's exact voice.

- **TLDR Dev:** concise, scannable summaries with a link to the original story.
- **Console.dev:** explain what a tool does, what is useful, and its limitations; consider documentation, self-service access, maintenance, and security/privacy.
- **ByteByteGo and engineering blogs:** explain how something works, which architectural choice matters, or what failure mode/trade-off readers should understand.
- **Dreams of Code, ThePrimeagen, Fireship and NetworkChuck:** prefer concrete workflows, demos and implementation details over launch announcements.
- **The Changelog and GitHub Release Radar:** use release context, maintainer/engineering perspective and what changed, without confusing repository activity with a new launch.
- **GitHub Trending, Show HN and OpenAlternative:** treat these as discovery signals. Stars, votes or a directory listing alone do not prove quality or market demand.

### Required post structure

1. **A specific supported fact:** the exact feature, tool behaviour, API change or engineering lesson described by the source.
2. **A candidate-specific editorial takeaway:** a concrete test, trade-off, limitation, implementation step, decision rule or failure mode. A generic audience tag such as "useful if you build apps" does not count.
3. **The primary source link:** placed at the end, with no unsupported claims about price, performance, adoption, release timing or security.

The post must name the product/platform/capability in its opening, state one live-source-backed fact, and add a candidate-specific test, trade-off, implementation detail or decision rule. The deterministic validator checks live-page quotes, length, title similarity, feature-list openings, numeric claims and undocumented capabilities. If the model omits a usable quote, the workflow may attach an exact contiguous excerpt from the already-fetched primary page only when its wording covers at least 65% of the factual sentence's specific tokens; it never paraphrases evidence to make the quote fit. If no first-pass draft passes, one automatic repair attempt uses the rejection reasons to shorten/narrow the copy; repaired drafts go through the same checks. A second independent Groq editor scores clarity, technical coherence, takeaway value, source faithfulness and originality; all five scores must be at least 7/10. The author's own novelty score is diagnostic only and cannot veto a draft; the separate editor decides originality. It rejects orphaned fragments, undocumented capability assumptions and mismatched tests such as using page-load timing to claim script byte size. If repair or the second review fails or returns invalid output, the flow fails closed and skips. Before drafting, the workflow fetches the candidate's primary page, checks HTTP status and title/content match, records the canonical redirect target, and uses only fetched page text for factual claims. Dead/mismatched pages are rejected. Passing drafts are labelled dry_run_passed_not_published: no human approval is required for the automated quality decision, but live publishing remains disabled during validation.

Preferred formats are release context, tool review, practical workflow, comparison/trade-off, and engineering lesson. A candidate that cannot support a useful angle should be skipped.

The automated source set is broader than the original developer-tool queue, but it still cannot access logged-in marketplace dashboards. Etsy Marketplace Insights, Google Trends exports, full competitor negative-review analysis, Shopify App Store reviews and Gumroad price comparisons are documented manual/market research inputs rather than falsely presented as connected APIs.

The priority score is a queue-sorting heuristic, not a quality rating, validation of claims, proof of market demand, or popularity measurement. Every run samples current stars for GitHub repositories returned by discovery and refreshes a bounded watchlist of up to 200 previously tracked public repositories through the GitHub REST API, even when they no longer appear in that hour's search results. Samples and repository IDs are persisted in output/discovery/hourly-state.json; the trend delta is calculated from a sample 20–36 hours old, and can be positive or negative. The first sample is only a baseline, not evidence of a trend; lifetime stars alone should never be described as trending. Primary-page fetch and quote validation do not replace careful interpretation of pricing, licence, limits, integrations and privacy/security trade-offs.

The separate **Legivox hourly discovery and draft preview** workflow is configured for hourly checks at :17 IST from 07:17 through 22:17, ahead of the next hourly publishing slot. It selects a diverse slate, verifies live primary pages, generates source-grounded copy, applies deterministic claim/editorial checks, makes at most one evidence-constrained rewrite if the first pass fails, and runs an independent automated editor on the highest-ranked local pass. Originality is an explicit independent score, not the draft model's self-rating. A post passes only if every gate passes; otherwise the hour is skipped. The default daily cap is 16 passing dry-run drafts. Reports include primary-source checks, star counts/deltas, original rejection reasons, any repair attempt and both quality-gate outcomes. The bounded GitHub star watchlist is sampled hourly, including tracked repositories missing from the latest discovery results; a trend delta is calculated only after a 20–36-hour baseline exists. Scheduled, manual, and feature-branch push-triggered hourly runs persist star and audit state on the dedicated `legivox-hourly-state` branch. A shared concurrency group serializes those state writers. The separate multidomain discovery preview workflow uploads read-only candidate reports without modifying star-history state. This workflow does not load the X cookie or publish to X.

The hourly research workflow is active on the default branch. It persists reports and star history to the dedicated `legivox-hourly-state` branch, separately from production code, and remains research-only; it does not load the X session cookie or publish to X.

The production publisher consumes the multidomain handoff by default after rollout; the repository Actions variable `LEGIVOX_MULTIDOMAIN_PUBLISHING_ENABLED` can be explicitly set to `false` to retain the legacy RSS/Groq path. Scheduled slots consume only a fresh (at most 90-minute-old) report that passed primary-source, evidence, independent-editor, character-limit, unpublished-status, and star-baseline checks. A missing, stale, failed, or incomplete report skips the slot; there is no RSS fallback while the flag is enabled. The feature branch must pass its full test suite before merge; hourly schedules only activate once this workflow is on the default branch.

## RSS + Groq dry run
The manual-only workflow **Legivox RSS + Groq dry run** remains available for content review. It fetches recent RSS metadata from TechCrunch, The Verge, and Ars Technica, calls Groq's OpenAI-compatible JSON mode using openai/gpt-oss-20b, applies local evidence and overclaim checks, and saves output/rss-groq-dry-run.md plus output/rss-groq-dry-run.json. It never loads the X cookie or publishes to X.

The scheduled publishing workflow uses the source-led generator for up to 16 hourly slots per IST date. Each slot must produce exactly one post that passes all quality gates; otherwise that slot is skipped. The single-post plan is then handed to the existing publisher, which still verifies the @Legivox session and recent timeline before attempting a post.

Repository Actions secrets must include GROQ_API_KEY and X_SESSION_COOKIE. Usage is subject to Groq's current model quota/rate limits. The workflow does not automate likes, replies, follows, or reposts.

## Important account risk
The publisher uses tweetkit-x, which replays X website requests with a session cookie instead of using the official API. X explicitly warns that website scripting may result in permanent suspension. This project does not claim that method is compliant. No cookie is stored in Git.

## Required secrets
- X_SESSION_COOKIE: the raw cookie value for @Legivox. Treat it like a password and never paste it into a commit or chat.
- GROQ_API_KEY: Groq API key for the separate RSS dry-run workflow.

## Audit
Published post text, URLs, topic IDs, research source links, and media attribution metadata are logged in output/published.jsonl. The latest daily plan is in output/daily-plan.json; the image/research report is in output/content-queue.md.
