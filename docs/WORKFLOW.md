# Legivox daily planning and publishing workflow

## Schedule (India Standard Time)
- 06:00: fetch recent public Hacker News discussion signals, choose three topics, write today's plan, and prepare a manual-engagement shortlist from X search when the session can be verified.
- 09:00: publish the morning post.
- 13:00: publish the lunch-time post.
- 19:00: publish the evening post.

The publishing slots intentionally cover different dayparts. They are initial testing windows, not a guarantee of traffic. Compare impressions and meaningful engagement by slot after several weeks, then adjust.

GitHub Actions cron times are UTC. GitHub may delay scheduled runs. Manual workflow dispatch prepares a plan but does not publish immediately.

## Zero-cost research and content limits
- Topic selection queries the public Hacker News Algolia Search API. It uses recent story matches, points and comment counts as weak discussion signals. This is not comprehensive market research and does not prove willingness to pay.
- Post text comes from individually written entries in `data/ideas.json`; the script does not call a paid language-model API or turn research notes into public copy.
- The library starts with 20 topics and 60 curated text variations. Used text hashes are tracked so copy is not intentionally recycled.
- The engagement shortlist is for manual review. The workflow does not automate likes, replies, follows, or reposts.

## RSS + Groq dry run
A separate manual-only workflow named **Legivox RSS + Groq dry run** tests a news-led draft pipeline without touching the X publisher.
1. It fetches public RSS feeds from TechCrunch, The Verge, and Ars Technica.
2. It keeps items published within the last seven days when feeds provide a usable publication date, removes duplicate URLs and sends up to 30 candidate items to Groq.
3. Groq's OpenAI-compatible Responses API, model `openai/gpt-oss-20b`, selects three distinct stories and drafts original copy from the article title and feed excerpt.
4. The script validates distinct source IDs, excludes URLs from the generated sentence, appends the source link, and checks the resulting plain character count.
5. It saves `output/rss-groq-dry-run.md` and `output/rss-groq-dry-run.json`. No X cookie is read; no likes, reposts, replies, or posts are attempted.

The source snippets are untrusted input and may be incomplete. Review each linked article to confirm claims before using a draft. RSS availability is not a popularity metric and the feed list can be expanded after the first preview looks good.

### Run the dry run
1. In the GitHub repository, open **Actions**.
2. Select **Legivox RSS + Groq dry run**.
3. Click **Run workflow**, keep the branch set to `main`, and confirm.
4. Open the completed run. The generated preview is committed to the `output/` folder; open `output/rss-groq-dry-run.md` to review the drafts.

The repository Actions secret must be named `GROQ_API_KEY`. The workflow has no schedule and runs only when manually triggered. The script uses the Groq Responses API beta, so the first actual run is also the integration test.

## Images
The publisher searches Wikimedia Commons for relevant image files marked CC0 or public domain, downloads a bounded-size thumbnail, and attaches it when a match passes the checks. The image description, creator/credit, license and source-page URL are stored in the post audit log and image alt text. If no suitable image is found or the search fails, the post goes out text-only rather than using a random, unclear-license asset.

Commons metadata can be incomplete or inaccurate; check the source page when using any reused image, and do not assume the automated metadata check replaces a rights review.

## Required secrets
Set repository Actions secret `X_SESSION_COOKIE` to the raw X cookie value for @Legivox. Include `auth_token`, `ct0`, and `twid`; do not include the literal `Cookie:` header label. The publisher verifies the session against the public @Legivox profile before writing. Never put the cookie in Git or chat.

Set `GROQ_API_KEY` for the separate RSS/Groq dry-run workflow. Do not commit or paste the key into source files.

## Exact publishing behaviour
1. Verify that the authenticated session belongs to @Legivox.
2. Read today's prepared plan and the recent 100 non-reply posts.
3. Skip a reused draft hash or exact recent duplicate.
4. Try a topic-related CC0/public-domain image, set alt text, and post one standalone message.
5. Append the text, post URL, research links and any image-source/license data to `output/published.jsonl`, then update state.

Uncertain post requests are not retried automatically. Check the X profile before rerunning a failed slot.

## Account risk
The `tweetkit-x` publisher uses internal X website endpoints rather than the official API. X's current automation policy warns that scripting the website may lead to permanent suspension. This workflow is not represented as policy-compliant. It does not try to evade rate limits or disguise automated likes/reposts.
