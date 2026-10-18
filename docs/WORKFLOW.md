# Legivox publishing workflow

## Scheduled execution
The workflow makes one publish attempt per day at 14:00 IST (08:30 UTC). GitHub Actions can delay scheduled starts. Keep the cadence low until the account has enough audience feedback to judge which posts are useful.

## Required secret
Set repository Actions secret `X_SESSION_COOKIE` to the raw X cookie value for @Legivox. Include `auth_token`, `ct0`, and `twid`; do not include the literal `Cookie:` header label. The publisher verifies the session user ID against the @Legivox profile ID before posting. Never put the cookie in Git or chat.

## Exact behaviour
1. Install upstream `tweetkit-x` source from commit `d42503a936f80eb0af2e9856a0fbd392cc4a750c` in the temporary hosted runner.
2. Verify the session is for @Legivox.
3. Read the latest 100 non-reply posts to check for exact duplicates.
4. Choose the next unused, individually written `publish_text` from `data/ideas.json`, post once and append an audit record.
5. Commit `output/` state even when the publishing step fails, where state changes were produced.

## Content quality guardrails
- Each post must be explicitly written in `publish_text`; the publisher no longer converts internal problem and solution labels into public copy.
- Starter records are unverified hypotheses, not validated market research. Add source links and evidence before making factual demand claims.
- Each post must fit within 280 characters.
- The workflow stops when all reviewed drafts are used instead of looping through generic templates.

## Failure handling
Unauthenticated sessions, account mismatches, timeline-read failures and confirmed post errors stop the job. Uncertain post requests are not retried automatically. Check the profile before manually rerunning a failed job to avoid duplicate publication.

## Risk
`tweetkit-x` uses internal X website endpoints. X's automation rules prohibit website scripting and mention possible permanent suspension. This implementation does not use proxies or attempt to evade rate limits, and does not automate social interactions.
