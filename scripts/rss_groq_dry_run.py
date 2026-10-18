#!/usr/bin/env python3
"""Backward-compatible entry point for the manual RSS/Groq dry-run workflow."""
from rss_groq import main

if __name__ == "__main__":
    raise SystemExit(main(["--dry-run"]))
