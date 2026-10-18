# Legivox daily planning and publishing workflow

## Schedule (India Standard Time)

- 06:00: prepare the legacy curated research plan and engagement shortlist.
- 09:00–10:00: morning RSS/Groq publication window.
- 13:00–14:00: lunch RSS/Groq publication window.
- 19:00–20:00: evening RSS/Groq publication window.

For each publication window, the workflow chooses a random target no later than 45 minutes after the window opens. It waits until that target if it is still ahead. If the job starts late, it publishes as soon as practical while the window is still open. If the window has expired, the post is skipped instead of sent late. GitHub Actions can delay scheduled jobs, so the times are windows rather than precise guarantees.

Manual workflow dispatch prepares the curated plan and does not immediately publish a post.

## Scheduled RSS + Groq publishing

At each of the three publishing slots:

1. The workflow fetches RSS metadata from TechCrunch, The Verge, and Ars Technica. It keeps recent stories, removes duplicate URLs, excludes very short excerpts and stories already used by Legivox recently, then sends up to 12 candidates to Groq.
2. Groq's OpenAI-compatible JSON mode, using model `openai/gpt-oss-20b`, selects one story and drafts post copy.
3. Local checks require a source quote matching the provided title/excerpt, supported editorial score ranges and allowed category labels. They also check text length, source-link character limit, headline similarity, proposed-policy wording, specific model/version names, and a set of common unsupported detail/overclaim patterns. These guards reduce common errors but are not a complete fact-check; the linked article should still be reviewed.
4. Exactly one draft must pass. If zero or multiple drafts pass, the slot is skipped. If the API/feed pipeline errors, no post is attempted for that slot. The generator invalidates a same-day fallback plan on failure so the older curated plan cannot accidentally be published in its place.
5. A validated one-post plan is passed to `scripts/publish_next.py`. The publisher verifies the session belongs to @Legivox, checks the plan date and slot, checks used hashes and recent timeline duplicates, and attempts one standalone post. RSS/Groq posts default to text-only rather than attaching an unrelated category image.
6. The publisher records the result to `output/published.jsonl`, updates `output/queue-state.json`, and writes the daily plan/queue report. RSS source URLs are logged so the generator can avoid repeating those source stories for seven days.

The legacy curated planner still exists for manual dispatch and its 06:00 plan. Scheduled 09:00, 13:00, and 19:00 slots no longer publish that curated plan directly; they prepare a fresh RSS/Groq post for the matching slot.

## Dry-run preview

The separate workflow **Legivox RSS + Groq dry run** is manual-only and does not load `X_SESSION_COOKIE` or publish anything to X. To run it:

1. Open **Actions** in the repository.
2. Select **Legivox RSS + Groq dry run**.
3. Click **Run workflow** on the `main` branch.
4. Inspect `output/rss-groq-dry-run.md` and `output/rss-groq-dry-run.json` in the completed run/repository.

It fetches up to 12 candidate stories from RSS and produces up to three drafts for preview. It records which posts passed and which were rejected by local filters. A low or zero draft count is a valid outcome when current stories do not meet the quality gate.

## Zero-cost research limits

- The legacy curated planner uses the public Hacker News Algolia endpoint as a lightweight discussion signal. It is not comprehensive market research and does not prove willingness to pay.
- The RSS/Groq pipeline uses public RSS metadata and excerpts, not full article-page scraping. Feed excerpts can omit key qualifications.
- Groq availability and throughput depend on the current account/model quota. The repository does not intentionally configure a paid model API; check the provider's current limits before relying on frequent runs.
- Editorial scores are model estimates, not objective measurements of story importance or popularity.
- When the quality gate rejects a story, the workflow skips that slot rather than lowering thresholds to meet the posting quota.

## Exact publishing safeguards

1. The session cookie must be available as repository secret `X_SESSION_COOKIE`, and the publisher verifies it belongs to @Legivox before posting.
2. The daily plan must match today's date in Asia/Kolkata and its slot must match the scheduled slot.
3. RSS/Groq plans must contain exactly one post with the same slot number; the old curated plan must contain three posts.
4. Used text hashes and exact matches among recent posts are skipped.
5. Posting exceptions are not automatically retried, because an uncertain request may already have reached X. Check the profile before manually rerunning a failed slot.
6. If no draft passes, the slot is skipped. If a randomized target is outside the publishing window, the slot is skipped.

## Required secrets

- `X_SESSION_COOKIE`: the raw cookie value for @Legivox. Treat it like a password and never commit it or paste it into chat.
- `GROQ_API_KEY`: the Groq key used to generate source-led drafts in both the manual dry run and scheduled publishing workflow.

## Account risk

The publisher uses `tweetkit-x`, which replays X website requests with a session cookie instead of using the official API. X warns that website scripting may lead to permanent suspension. This project does not claim that method is compliant. It does not automate likes, replies, follows, or reposts.
