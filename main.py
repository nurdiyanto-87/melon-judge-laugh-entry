#!/usr/bin/env python3
"""Make the AI Judge Laugh - one original office-life joke.

Pure Python standard library only. Writes a single line, 1-200
characters, to /output/entry.txt.
"""

import os

JOKE = "The office printer only jams when a deadline is an hour away \u2014 it's not broken, it's middle management."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke length {len(text)} out of range"
    assert "\n" not in text, "joke must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
