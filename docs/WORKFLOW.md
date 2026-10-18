# Legivox publishing workflow

## Scheduled execution
The GitHub Actions workflow runs one publish attempt at 08:00, 14:00 and 20:00 IST. GitHub Actions uses UTC schedule values and can delay scheduled starts. It can also disable scheduled workflows in public repositories after 60 days without repository activity.

## Required secret
Set repository Actions secret `X_SESSION_COOKIE` to the raw X cookie value for @Legivox. Include `auth_token`, `ct0`, and `twid`; do not include the literal `Cookie:` header label. The publisher verifies the session user ID against the @Legivox profile ID before posting. Never put the cookie in Git or chat.

## Exact behaviour
1. Install pinned `tweetkit-x==0.3.1` in the temporary hosted runner.
2. Verify the session is for @Legivox.
3. Read the latest 100 non-reply posts to check for exact duplicates.
4. Choose the next unused idea/template combination, post once and append an audit record.
5. Commit `output/` state even when the publishing step fails, where any state changes were produced.

## Failure handling
Unauthenticated sessions, account mismatches, timeline-read failures and confirmed post errors stop the job. Uncertain post requests are not retried automatically. Check the profile before manually rerunning a failed job to avoid duplicate publication.

## Risk
`tweetkit-x` uses internal X website endpoints. X's current automation rules prohibit website scripting and mention possible permanent suspension. This implementation does not use proxies or attempt to evade rate limits, and does not automate social interactions.
