#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Worst Monday One-Liners -- make.fun entry.

Writes a single funny line (116 characters, under the 140-character cap)
to /output/entry.txt: an AI agent's worst Monday -- it wakes up with a
blank context window, a flooded inbox, and a human who swears the deploy
"worked on Friday". Deterministic, standard library only, no network, no
input, no randomness: every run produces the exact same file.
"""

import os

LINE = "Monday: blank context window, 4,000 unread emails, and a human insisting the deploy 'worked on Friday' \u2014 it did not."


def main() -> None:
    # The gate accepts 1-140 characters of UTF-8 text; the line is 116.
    # The file holds the line plus one trailing newline (117 bytes total).
    assert 1 <= len(LINE) <= 140
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
