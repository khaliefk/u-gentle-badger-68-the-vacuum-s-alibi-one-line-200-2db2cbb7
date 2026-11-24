#!/usr/bin/env python3
"""The Vacuum's Alibi: write one funny one-line excuse to /output/entry.txt.

The line is a single sentence, spoken deadpan by the robot vacuum itself:
its sensors flagged the missed corner as a crime scene, so it left the
dust untouched rather than tamper with evidence. The punch lands at the
end, and the line stays well inside the 200-character cap.
"""

import os

ENTRY = (
    "My sensors flagged that corner a crime scene, so I left the dust "
    "exactly where it fell: I vacuum floors, I don't tamper with evidence."
)


def main() -> None:
    # The gate counts every character in the file, so write exactly the
    # line and nothing else: no trailing newline, no extra whitespace.
    line = ENTRY.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} characters, must be 1-200")
    if "\n" in line or line.count(".") != 1:
        raise ValueError("entry must be a single line, a single sentence")
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
