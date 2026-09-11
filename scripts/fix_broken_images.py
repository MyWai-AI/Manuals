#!/usr/bin/env python3
"""Repair MDX image markdown broken by newline insertion inside filenames with parentheses."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ![](/images/image%20(1)\n\n.png)  ->  ![](/images/image%20(1).png)
# The ')' after the number was wrongly treated as the markdown link closer.
SPLIT_IMG = re.compile(
    r"!\[([^\]]*)\]\((/images/[^\n]+?)\)\s*\n+\s*(\.[A-Za-z0-9]+)\)",
    re.MULTILINE,
)

# Ensure a blank line after a complete image when text follows immediately
AFTER_IMG = re.compile(
    r"(!\[[^\]]*\]\(/images/.+?\.(?:png|svg|jpg|jpeg|gif|webp|PNG|SVG)\))(?=\S)"
)


def fix_text(text: str) -> str:
    # Re-insert the filename ')' that was consumed as the markdown closer
    text = SPLIT_IMG.sub(r"![\1](\2)\3)", text)
    # Also repair already-broken forms: image%20(1.png -> image%20(1).png
    text = re.sub(
        r"(/images/[^\s\n)]+)\((\d+)\.(png|svg|jpg|jpeg|gif|webp)",
        r"\1(\2).\3",
        text,
        flags=re.IGNORECASE,
    )
    text = AFTER_IMG.sub(r"\1\n\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*.mdx"):
        if "user-manual" in path.parts:
            continue
        original = path.read_text(encoding="utf-8")
        fixed = fix_text(original)
        if fixed != original:
            path.write_text(fixed, encoding="utf-8")
            changed += 1
            print(path.relative_to(ROOT))
    print(f"updated {changed} files")


if __name__ == "__main__":
    main()
