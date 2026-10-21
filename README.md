# Legivox Automation

Zero-budget GitHub Actions workflow for daily research, quality-gated RSS/Groq news drafts, optional freely licensed images for curated posts, and scheduled X publishing.

## Schedule
- 06:00 IST: prepare the curated research plan and manual-engagement shortlist.
- 09:00–10:00 IST: morning RSS/Groq post window.
- 13:00–14:00 IST: lunch RSS/Groq post window.
- 19:00–20:00 IST: evening RSS/Groq post window.

For scheduled posts, a random target is chosen inside the first 45 minutes of each one-hour window. If a workflow starts late, it can post immediately while the window remains open; if the window has expired, the post is skipped. GitHub can delay scheduled runs, so these are windows, not guaranteed exact times or peak-hour claims. Manual workflow dispatch defaults to preparing the curated plan only. For a deliberate live test, set the boolean publish_now input to true; it generates and attempts to publish one quality-gated RSS/Groq post immediately, bypassing the scheduled random wait. This uses the production X session and can publish publicly.

## What is and isn't automated
- Topic selection uses a public, no-key Hacker News Algolia search endpoint. Discussion activity is a prioritisation signal, not proof of market demand.
- The legacy curated-plan workflow still uses individually written copy in data/ideas.json; the scheduled publishing slots now generate source-led news posts through the RSS + Groq pipeline.
- A reviewed starter library contains 20 topics and 60 copy variations for the curated plan. Hashes prevent intentional text reuse.
- The image step for curated posts searches Wikimedia Commons and attaches only relevant candidates marked CC0 or public domain. Scheduled RSS/Groq news posts default to text-only rather than attaching a generic category image.
- X search results for the day's niches are saved to output/engagement-shortlist.md for manual review. The workflow does not automate likes, replies, follows or reposts.

## Experimental multidomain discovery

The feature branch feature/multidomain-discovery-v1 adds a **research-only** discovery queue for useful technology across six lanes:
- Developer tools and infrastructure.
- AI, agents and automation.
- Shopify, ecommerce, checkout, payments and digital products.
- Creator tools and indie-business infrastructure.
- Analytics, data and growth.
- Security, privacy and self-hosting.

The source registry is data/discovery_sources.json. The first adapters use GitHub repository search, Hacker News/Show HN, Console.dev RSS, Product Hunt RSS, and the official Shopify Developer Changelog. The goal is to discover technology people can build with, automate, use to launch, or use to sell online, not to limit Legivox to software engineering news.

The research script is scripts/discover_candidates.py. Run the command *python scripts/discover_candidates.py --lookback-days 14 --limit 30* from the repository root to fetch a live preview. It writes output/discovery/discovery-report.md and output/discovery/discovery-candidates.json. No extra Python packages are required. An optional GITHUB_TOKEN environment variable improves GitHub API rate-limit headroom; do not commit any token.

The separate GitHub Actions workflow **Legivox multidomain discovery preview** runs tests and a read-only discovery preview on matching pull requests. Once the workflow is available on the default branch, it can also be run manually with a 7-, 14- or 30-day lookback. The report appears in the Actions run summary. It does not load the X session cookie or Groq API key, write to the production plan, or publish/interact on X.

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

The draft validator now requires an explicit editorial_takeaway as the second sentence and an insight score of at least 7/10. It checks that the takeaway is present, actionable and tied to the candidate's technical/product details. It rejects generic endings and opening lines that merely repeat the source headline. The post body is preserved during URL cleanup; the code must not delete the model's analysis and replace it with a boilerplate category sentence.

Preferred formats are release context, tool review, practical workflow, comparison/trade-off, and engineering lesson. A candidate that cannot support a useful angle should be skipped.

The current automated source adapters are still limited to GitHub search, Hacker News/Show HN, Console.dev RSS, Product Hunt RSS, and Shopify Developer Changelog. The remaining creators/blogs/directories are editorial benchmarks and future integration candidates, not currently connected feeds.

The priority score is a queue-sorting heuristic, not a quality rating, validation of claims, proof of market demand, or popularity measurement. GitHub star counts are sampled hourly and the pipeline estimates growth from a stored sample roughly 20–36 hours old. New repositories begin with no measured velocity until enough history exists; lifetime stars alone should not be described as trending. Every candidate needs primary-source review of functionality, dates, price, licence, free-tier limits, integrations and privacy/security trade-offs.

The separate **Legivox hourly discovery and draft preview** workflow is configured for hourly checks at :17 IST from 08:17 through 23:17. It uses the same source registry, selects a diverse slate, asks Groq for candidate-specific copy, applies claim/evidence/URL/length and use-case checks, and records either a draft for human review or an explicit skip. Its daily cap is 10 passing draft proposals. The run summary and artifact contain the candidate list, proposed copy and rejection reasons; the audit state tracks cooldowns, recent proposals and GitHub star snapshots. This workflow does not load the X cookie or publish to X.

The hourly workflow is currently on this feature branch, so scheduled hourly runs are not active on the default branch yet. Push-triggered dry runs validate code and sources, but do not persist the star-history state. Once the workflow is enabled on the default branch, scheduled/manual runs retain state between hours. Inspect the draft PR and its CI results before merging.

**Production publishing has not been changed by this experimental branch.** Discovery candidates and hourly drafts remain separate from output/daily-plan.json and the scheduled RSS/Groq publishing steps.

## RSS + Groq dry run
The manual-only workflow **Legivox RSS + Groq dry run** remains available for content review. It fetches recent RSS metadata from TechCrunch, The Verge, and Ars Technica, calls Groq's OpenAI-compatible JSON mode using openai/gpt-oss-20b, applies local evidence and overclaim checks, and saves output/rss-groq-dry-run.md plus output/rss-groq-dry-run.json. It never loads the X cookie or publishes to X.

The scheduled publishing workflow now uses the same source-led generator for each of its three slots. Each slot must produce exactly one post that passes the quality gate; otherwise that slot is skipped. The single-post plan is then handed to the existing publisher, which still verifies the @Legivox session and recent timeline before attempting a post.

Repository Actions secrets must include GROQ_API_KEY and X_SESSION_COOKIE. Usage is subject to Groq's current model quota/rate limits. The workflow does not automate likes, replies, follows, or reposts.

## Important account risk
The publisher uses tweetkit-x, which replays X website requests with a session cookie instead of using the official API. X explicitly warns that website scripting may result in permanent suspension. This project does not claim that method is compliant. No cookie is stored in Git.

## Required secrets
- X_SESSION_COOKIE: the raw cookie value for @Legivox. Treat it like a password and never paste it into a commit or chat.
- GROQ_API_KEY: Groq API key for the separate RSS dry-run workflow.

## Audit
Published post text, URLs, topic IDs, research source links, and media attribution metadata are logged in output/published.jsonl. The latest daily plan is in output/daily-plan.json; the image/research report is in output/content-queue.md.
