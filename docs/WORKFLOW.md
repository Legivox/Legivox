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

## Images
The publisher searches Wikimedia Commons for relevant image files marked CC0 or public domain, downloads a bounded-size thumbnail, and attaches it when a match passes the checks. The image description, creator/credit, license and source-page URL are stored in the post audit log and image alt text. If no suitable image is found or the search fails, the post goes out text-only rather than using a random, unclear-license asset.

Commons metadata can be incomplete or inaccurate; check the source page when using any reused image, and do not assume the automated metadata check replaces a rights review.

## Required secret
Set repository Actions secret `X_SESSION_COOKIE` to the raw X cookie value for @Legivox. Include `auth_token`, `ct0`, and `twid`; do not include the literal `Cookie:` header label. The publisher verifies the session against the public @Legivox profile before writing. Never put the cookie in Git or chat.

## Exact publishing behaviour
1. Verify that the authenticated session belongs to @Legivox.
2. Read today's prepared plan and the recent 100 non-reply posts.
3. Skip a reused draft hash or exact recent duplicate.
4. Try a topic-related CC0/public-domain image, set alt text, and post one standalone message.
5. Append the text, post URL, research links and any image-source/license data to `output/published.jsonl`, then update state.

Uncertain post requests are not retried automatically. Check the X profile before rerunning a failed slot.

## Account risk
The `tweetkit-x` publisher uses internal X website endpoints rather than the official API. X's current automation policy warns that scripting the website may lead to permanent suspension. This workflow is not represented as policy-compliant. It does not try to evade rate limits or disguise automated likes/reposts.
