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

The priority score is only a queue-sorting heuristic made from recency, source type, public signals, technical specificity and description detail. It is not a quality rating, validation of claims, evidence of market demand, or a measurement of popularity. GitHub stars are cumulative; the first version does not yet calculate daily star growth. Every candidate is marked as needing primary-source review. Verify the original product/project page, docs or changelog; confirm price, licence, free-tier limits, integrations and privacy/security implications; then decide whether a practical demonstration or honest comparison is worth publishing.

**Production publishing has not been changed by this experimental branch.** Discovery candidates remain separate from output/daily-plan.json and the scheduled RSS/Groq publishing steps. Do not merge the branch until its test and live preview results have been reviewed.

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
