#!/usr/bin/env python3
"""Publish one unique Legivox post using a user-supplied X session cookie.

This uses tweetkit-x's unofficial web-session integration. It is intentionally
restricted to original standalone posts and verifies the authenticated account
before any write. Never print or persist the cookie.
"""
from __future__ import annotations
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from tweetkit_x import TweetKit

ROOT = Path(__file__).resolve().parents[1]
IDEAS_PATH = ROOT / 'data' / 'ideas.json'
OUTPUT_DIR = ROOT / 'output'
STATE_PATH = OUTPUT_DIR / 'queue-state.json'
REPORT_PATH = OUTPUT_DIR / 'content-queue.md'
PUBLISHED_PATH = OUTPUT_DIR / 'published.jsonl'
EXPECTED_USERNAME = 'Legivox'
TEMPLATES = 4

def fail(message: str) -> None:
    print('Legivox publisher: ' + message, file=sys.stderr)
    raise SystemExit(1)

def clean(value: str) -> str:
    return ' '.join(str(value).split())

def clip(value: str, limit: int) -> str:
    value = clean(value)
    if len(value) <= limit:
        return value
    trimmed = value[:limit - 1].rsplit(' ', 1)[0].rstrip('.,;: ')
    return (trimmed or value[:limit - 1]).rstrip() + '…'

def make_draft(item: dict, variant: int) -> str:
    niche = clip(item['niche'], 38)
    problem = clip(item['problem'], 110)
    solution = clip(item['solution_hypothesis'], 110)
    endings = [
        'What evidence would show people will pay for this?',
        'I would validate willingness to pay before building.',
        'Repeated behaviour matters more than compliments.',
        'The first step is checking whether people already spend time or money on it.',
    ]
    starts = [
        'A problem to test in ' + niche + ': ' + problem + ' Product hypothesis: ' + solution + ' ',
        'For ' + niche + ', one friction point is ' + problem + ' A possible tool: ' + solution + ' ',
        'Product idea to validate, not assume: ' + problem + ' For ' + niche + ', perhaps ' + solution + ' ',
        'Before building for ' + niche + ', validate this: ' + problem + ' One possible solution is ' + solution + ' ',
    ]
    problem_limit = 110
    solution_limit = 110
    draft = starts[variant] + endings[variant]
    while len(draft) > 275:
        if problem_limit >= solution_limit and problem_limit > 32:
            problem_limit -= 8
        elif solution_limit > 32:
            solution_limit -= 8
        else:
            fail('A draft exceeds the X character limit after safe shortening.')
        problem = clip(item['problem'], problem_limit)
        solution = clip(item['solution_hypothesis'], solution_limit)
        starts = [
            'A problem to test in ' + niche + ': ' + problem + ' Product hypothesis: ' + solution + ' ',
            'For ' + niche + ', one friction point is ' + problem + ' A possible tool: ' + solution + ' ',
            'Product idea to validate, not assume: ' + problem + ' For ' + niche + ', perhaps ' + solution + ' ',
            'Before building for ' + niche + ', validate this: ' + problem + ' One possible solution is ' + solution + ' ',
        ]
        draft = starts[variant] + endings[variant]
    return draft

def write_state(state: dict) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + '\n', encoding='utf-8')

def write_report(item: dict, draft: str, message: str, result: dict | None = None) -> None:
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    lines = [
        '# Legivox content queue', '', 'Generated: ' + now, '',
        '> Automated posting is enabled for this workflow. Starter records are hypotheses, not verified market research.', '',
        '## Latest draft', '', draft, '',
        '## Research record', '',
        '- Niche: ' + clean(item['niche']),
        '- Problem: ' + clean(item['problem']),
        '- Evidence status: ' + clean(item['evidence']),
        '- Solution hypothesis: ' + clean(item['solution_hypothesis']),
        '- Idea ID: ' + clean(item['id']),
        '- Result: ' + message,
    ]
    if result and result.get('url'):
        lines += ['- Published URL: ' + result['url']]
    lines += ['', '## Review reminder', '',
        'This workflow posts a standalone message without replies, likes, follows, reposts, or DMs.',
        'The source records must be refreshed with researched and verified evidence before claims are made about market demand.', '']
    REPORT_PATH.write_text('\n'.join(lines), encoding='utf-8')

def main() -> int:
    cookie = os.environ.get('TWEETKIT_COOKIE', '').strip()
    if not cookie:
        fail('Missing Actions secret X_SESSION_COOKIE. Add it in repository Settings > Secrets and variables > Actions.')
    try:
        client = TweetKit(cookie=cookie, timeout=25)
        identity = client.whoami()
    except Exception:
        fail('Could not initialise the X session. Check that the cookie secret contains auth_token, ct0, and twid; details suppressed.')
    if not identity.get('ready') or not identity.get('user_id'):
        fail('Session cookie is incomplete. A valid auth_token, ct0, and twid are required; details suppressed.')
    try:
        profile = client.user_profile(EXPECTED_USERNAME)
    except Exception:
        fail('Could not verify the @Legivox X profile. No post was attempted.')
    if not profile.get('ok') or str(profile.get('username', '')).lower() != EXPECTED_USERNAME.lower():
        fail('Could not verify the public @Legivox profile. No post was attempted.')
    if str(identity.get('user_id')) != str(profile.get('id')):
        fail('The cookie belongs to a different X account, not @Legivox. No post was attempted.')

    try:
        ideas = json.loads(IDEAS_PATH.read_text(encoding='utf-8'))
        state = json.loads(STATE_PATH.read_text(encoding='utf-8')) if STATE_PATH.exists() else {}
    except Exception:
        fail('Could not read the idea queue or state JSON.')
    required = ('id', 'niche', 'problem', 'evidence', 'solution_hypothesis')
    ideas = [row for row in ideas if isinstance(row, dict) and all(row.get(key) for key in required)]
    if not ideas:
        fail('No complete ideas found in data/ideas.json.')

    try:
        recent = client.get_tweets(limit=100, include_replies=False)
    except Exception:
        fail('Could not safely check recent @Legivox posts for duplicates. No post was attempted.')
    recent_texts = {clean(row.get('text', '')) for row in recent if row.get('text')}
    used_hashes = set(state.get('used_draft_hashes', []))
    last_id = state.get('last_idea_id')
    last_variant = state.get('last_template_index', TEMPLATES - 1)
    idea_ids = [row['id'] for row in ideas]
    last_idea_index = idea_ids.index(last_id) if last_id in idea_ids else -1
    current_flat = last_idea_index * TEMPLATES + int(last_variant)
    total = len(ideas) * TEMPLATES

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for step in range(1, total + 1):
        flat = (current_flat + step) % total
        item = ideas[flat // TEMPLATES]
        variant = flat % TEMPLATES
        draft = make_draft(item, variant)
        digest = hashlib.sha256(draft.encode('utf-8')).hexdigest()
        if digest in used_hashes:
            continue
        if draft in recent_texts:
            used_hashes.add(digest)
            state.update({'last_idea_id': item['id'], 'last_template_index': variant, 'used_draft_hashes': sorted(used_hashes)})
            continue

        try:
            result = client.post(draft)
        except Exception:
            fail('The posting request failed. It was not retried to avoid accidental duplicate posts; check Actions logs and the X profile before retrying.')
        if not isinstance(result, dict) or not result.get('ok'):
            status = result.get('status') if isinstance(result, dict) else None
            fail('X did not confirm the post (HTTP status ' + str(status or 'unknown') + '). The request was not retried; check the profile before rerunning.')

        now = datetime.now(timezone.utc).isoformat(timespec='seconds')
        used_hashes.add(digest)
        state.update({
            'last_idea_id': item['id'],
            'last_template_index': variant,
            'used_draft_hashes': sorted(used_hashes),
            'published_count': int(state.get('published_count', 0)) + 1,
            'last_published_at': now,
            'last_published_url': result.get('url', ''),
        })
        with PUBLISHED_PATH.open('a', encoding='utf-8') as out:
            out.write(json.dumps({'timestamp': now, 'idea_id': item['id'], 'text': draft, 'tweet_id': result.get('id'), 'url': result.get('url')}, ensure_ascii=False) + '\n')
        write_state(state)
        write_report(item, draft, 'Published successfully', result)
        print('Published one original post for @Legivox: ' + str(result.get('url', 'URL unavailable')))
        print('Idea ID: ' + str(item['id']) + '; character count: ' + str(len(draft)))
        return 0

    state['used_draft_hashes'] = sorted(used_hashes)
    write_state(state)
    fail('All current idea/template combinations are already used. Add fresh, researched records to data/ideas.json before resuming.')

if __name__ == '__main__':
    raise SystemExit(main())
