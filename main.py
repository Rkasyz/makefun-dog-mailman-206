#!/usr/bin/env python3
"""The Dog Reviews the Mailman — one-line review entry.

Writes the dog's one-line review of the mailman to
$MAKEFUN_OUTPUT_DIR/entry.txt as UTF-8 text, no trailing newline.
"""

import os
import sys

ENTRY = "One star. He comes every day, teases me through the slot, and never once comes inside to play. Coward. Would bark again."


def main() -> int:
    # Enforce the competition gate locally: 1 to 200 characters, not
    # only white space. Fail loudly instead of writing an invalid entry.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        print("entry fails the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
