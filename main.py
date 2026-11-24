#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — make.fun entry.

Writes one line to entry.txt in the output directory: a software patch
note for a bug in real life. Pure standard library only.

Output directory, first match wins:
  1. $MAKEFUN_OUTPUT_DIR (the grader's contract)
  2. /output              (the kit's stated path)
  3. the folder this script lives in (local runs)
"""

import os
import sys

LINE = (
    "v34.9.0: Fixed a bug where the tongue finds the exact spot inside "
    "your cheek that you bit at lunch and returns to it hourly for "
    "quality assurance."
)


def output_dir():
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    return os.path.dirname(os.path.abspath(__file__))


def checked_line():
    """Mirror the kit's sealed gate: UTF-8 text of 1 to 160 characters,
    a single line, and not only white space. Refuse to ship an entry the
    gate would mark invalid."""
    if not (1 <= len(LINE) <= 160):
        raise ValueError(f"entry must be 1..160 characters, got {len(LINE)}")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not LINE.strip():
        raise ValueError("entry must not be only white space")
    LINE.encode("utf-8")  # raises if it ever stops being encodable
    return LINE


def main():
    line = checked_line()
    folder = output_dir()
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {target} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
