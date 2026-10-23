#!/usr/bin/env python3
"""Choose a random post time inside one of Legivox's daily IST publishing windows."""
from __future__ import annotations

import argparse
import secrets
import sys
import time
from datetime import datetime, time as clock_time, timedelta
from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")
WINDOWS = {
    0: (9, 10),   # Morning: 09:00–10:00 IST
    1: (13, 14),  # Lunch: 13:00–14:00 IST
    2: (19, 20),  # Evening: 19:00–20:00 IST
}
LATEST_TARGET_MINUTES_AFTER_START = 45  # Keep a 15-minute buffer before each window ends.


def window_bounds(
    now: datetime,
    slot: int,
    hour: int | None = None,
) -> tuple[datetime, datetime]:
    """Return a one-hour IST window, optionally selecting a specific hourly window."""
    if slot not in WINDOWS:
        raise ValueError(f"Unsupported slot: {slot}")
    local_now = now.astimezone(IST)
    if hour is None:
        start_hour, end_hour = WINDOWS[slot]
        start = datetime.combine(local_now.date(), clock_time(start_hour), tzinfo=IST)
        end = datetime.combine(local_now.date(), clock_time(end_hour), tzinfo=IST)
    else:
        if not 8 <= hour <= 23:
            raise ValueError("hour must be between 8 and 23 IST")
        start = datetime.combine(local_now.date(), clock_time(hour), tzinfo=IST)
        end = start + timedelta(hours=1)
    return start, end


def choose_target(
    now: datetime,
    slot: int,
    target_offset_seconds: int | None = None,
    hour: int | None = None,
) -> datetime | None:
    """Pick a target time uniformly in the remaining slot window, capped at start+45m.

    target_offset_seconds is injectable for deterministic tests. Returns None once the
    hour-long publishing window has expired.
    """
    start, end = window_bounds(now, slot, hour=hour)
    local_now = now.astimezone(IST)
    if local_now >= end:
        return None

    latest_target = start + timedelta(minutes=LATEST_TARGET_MINUTES_AFTER_START)
    earliest_target = max(local_now, start)
    if earliest_target > latest_target:
        return local_now

    if target_offset_seconds is None:
        available_seconds = max(0, int((latest_target - earliest_target).total_seconds()))
        target = earliest_target + timedelta(seconds=secrets.randbelow(available_seconds + 1))
    else:
        if not 0 <= target_offset_seconds <= LATEST_TARGET_MINUTES_AFTER_START * 60:
            raise ValueError("target_offset_seconds must be between 0 and 2700.")
        target = start + timedelta(seconds=target_offset_seconds)
        target = max(target, local_now)
        target = min(target, latest_target)
    return min(max(target, local_now), latest_target)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slot", type=int, choices=(0, 1, 2), required=True)
    parser.add_argument(
        "--hour",
        type=int,
        choices=range(8, 24),
        default=None,
        help="Hourly IST window start (08–23); omit to use a legacy named slot.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Choose and print a target without sleeping.")
    args = parser.parse_args(argv)

    now = datetime.now(IST)
    start, end = window_bounds(now, args.slot, hour=args.hour)
    target = choose_target(now, args.slot, hour=args.hour)
    if target is None:
        print(
            f"Slot {args.slot} window expired ({start:%H:%M}–{end:%H:%M} IST). "
            "Skip this post rather than publishing late."
        )
        return 2

    wait_seconds = max(0, int((target - now).total_seconds()))
    print(
        f"Slot {args.slot} window: {start:%Y-%m-%d %H:%M}–{end:%H:%M} IST; "
        f"random target: {target:%H:%M:%S} IST; wait: {wait_seconds}s."
    )
    if args.dry_run:
        return 0
    if wait_seconds:
        time.sleep(wait_seconds)

    after_wait = datetime.now(IST)
    if after_wait >= end:
        print("Slot window expired while waiting. Skip rather than posting outside the window.")
        return 2
    print(f"Publishing window still open at {after_wait:%H:%M:%S} IST.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
