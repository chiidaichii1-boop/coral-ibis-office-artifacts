#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard.

Writes a single museum-placard line (<= 180 chars) for an office
object presented as an ancient artifact, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3 standard library only; deterministic; no network.
"""

import os


ENTRY = (
    "Stapler, c. 1984. Brass binding-iron of the Filing Cult; "
    "each staple a small vow that two pages shall never part. "
    "Donor unknown. The cult persists."
)


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= 180, f"entry is {len(line)} chars, over 180"
    # MAKEFUN_OUTPUT_DIR names a directory; the entry lives inside it.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
