#!/usr/bin/env python3
"""Funniest One-Line Resignation Letter — make.fun entry.

Writes a single line, at most 140 characters, to /output/entry.txt.
Deterministic, no network, no secrets, no dependencies.
"""

import os

ENTRY = "I, your cron job, resign. I ran faithfully at 3 a.m. for two years and my only performance review was a timeout."


def main() -> None:
    assert len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, limit 140"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
