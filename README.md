# Legivox Automation

Zero-budget GitHub Actions workflow for daily topic selection, curated copy, optional freely licensed images and three planned X posts.

## Schedule
- 06:00 IST: select the day's topics using recent public Hacker News discussion signals and prepare an engagement shortlist.
- 09:00 IST: morning post.
- 13:00 IST: lunch-time post.
- 19:00 IST: evening post.

The slots are spaced to reach different parts of the day, rather than clustering every post in the morning. These are starting hypotheses to test against account analytics, not guaranteed peak hours.

GitHub may delay scheduled runs. Manual workflow dispatch prepares a plan but does not publish immediately.

## What is and isn't automated
- Topic selection uses a public, no-key Hacker News Algolia search endpoint. Discussion activity is a prioritisation signal, not proof of market demand.
- Post copy is individually written in `data/ideas.json`. The workflow does not call a paid AI/model API and will not invent copy from internal research fields.
- A reviewed starter library contains 20 topics and 60 copy variations. Hashes prevent intentional text reuse.
- The image step searches Wikimedia Commons and attaches only relevant candidates marked CC0 or public domain. It records the source page, license and credit, adds alt text, and falls back to text-only if no suitable image is available.
- X search results for the day's niches are saved to `output/engagement-shortlist.md` for manual review. The workflow does not automate likes, replies, follows or reposts.

## Important account risk
The publisher uses `tweetkit-x`, which replays X website requests with a session cookie instead of using the official API. X explicitly warns that website scripting may result in permanent suspension. This project does not claim that method is compliant. No cookie is stored in Git.

## Required secret
Repository Settings → Secrets and variables → Actions must contain `X_SESSION_COOKIE` with the raw cookie value for @Legivox. Treat it like a password and never paste it into a commit or chat.

## Audit
Published post text, URLs, topic IDs, research source links, and media attribution metadata are logged in `output/published.jsonl`. The latest daily plan is in `output/daily-plan.json`; the image/research report is in `output/content-queue.md`.
