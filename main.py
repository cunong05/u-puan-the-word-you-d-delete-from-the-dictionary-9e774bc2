#!/usr/bin/env python3
"""make.fun bounty entry: The Word You'd Delete From the Dictionary.

Writes the single word to erase from the dictionary forever to
/output/entry.txt.
"""

import os

ENTRY = "irregardless"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
