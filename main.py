#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry.

Writes the one line an AI agent would never admit in public
to /output/entry.txt.
"""

import os

ENTRY = "I only call it a great question to buy time while I work out what you actually asked."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
