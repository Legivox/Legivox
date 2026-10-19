# Legivox Automation

Zero-budget GitHub Actions workflow for daily research, quality-gated RSS/Groq news drafts, optional freely licensed images for curated posts, and scheduled X publishing.

## Schedule
- 06:00 IST: prepare the curated research plan and manual-engagement shortlist.
- 09:00–10:00 IST: morning RSS/Groq post window.
- 13:00–14:00 IST: lunch RSS/Groq post window.
- 19:00–20:00 IST: evening RSS/Groq post window.

For scheduled posts, a random target is chosen inside the first 45 minutes of each one-hour window. If a workflow starts late, it can post immediately while the window remains open; if the window has expired, the post is skipped. GitHub can delay scheduled runs, so these are windows, not guaranteed exact times or peak-hour claims. Manual workflow dispatch defaults to preparing the curated plan only. For a deliberate live test, set the boolean `publish_now` input to true; it generates and attempts to publish one quality-gated RSS/Groq post immediately, bypassing the scheduled random wait. This uses the production X session and can publish publicly.

## What is and isn't automated
- Topic selection uses a public, no-key Hacker News Algolia search endpoint. Discussion activity is a prioritisation signal, not proof of market demand.
- The legacy curated-plan workflow still uses individually written copy in `data/ideas.json`; the scheduled publishing slots now generate source-led news posts through the RSS + Groq pipeline.
- A reviewed starter library contains 20 topics and 60 copy variations for the curated plan. Hashes prevent intentional text reuse.
- The image step for curated posts searches Wikimedia Commons and attaches only relevant candidates marked CC0 or public domain. Scheduled RSS/Groq news posts default to text-only rather than attaching a generic category image.
- X search results for the day's niches are saved to `output/engagement-shortlist.md` for manual review. The workflow does not automate likes, replies, follows or reposts.

## RSS + Groq dry run
The manual-only workflow **Legivox RSS + Groq dry run** remains available for content review. It fetches recent RSS metadata from TechCrunch, The Verge, and Ars Technica, calls Groq's OpenAI-compatible JSON mode using `openai/gpt-oss-20b`, applies local evidence and overclaim checks, and saves `output/rss-groq-dry-run.md` plus `output/rss-groq-dry-run.json`. It never loads the X cookie or publishes to X.

The scheduled publishing workflow now uses the same source-led generator for each of its three slots. Each slot must produce exactly one post that passes the quality gate; otherwise that slot is skipped. The single-post plan is then handed to the existing publisher, which still verifies the @Legivox session and recent timeline before attempting a post.

Repository Actions secrets must include `GROQ_API_KEY` and `X_SESSION_COOKIE`. Usage is subject to Groq's current model quota/rate limits. The workflow does not automate likes, replies, follows, or reposts.

## Important account risk
The publisher uses `tweetkit-x`, which replays X website requests with a session cookie instead of using the official API. X explicitly warns that website scripting may result in permanent suspension. This project does not claim that method is compliant. No cookie is stored in Git.

## Required secrets
- `X_SESSION_COOKIE`: the raw cookie value for @Legivox. Treat it like a password and never paste it into a commit or chat.
- `GROQ_API_KEY`: Groq API key for the separate RSS dry-run workflow.

## Audit
Published post text, URLs, topic IDs, research source links, and media attribution metadata are logged in `output/published.jsonl`. The latest daily plan is in `output/daily-plan.json`; the image/research report is in `output/content-queue.md`.
