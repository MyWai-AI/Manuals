#!/usr/bin/env python3
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PRE_RE = re.compile(
    r"<pre[^>]*>\s*<code[^>]*>(.*?)</code>\s*</pre>",
    re.DOTALL | re.IGNORECASE,
)
LANG_FROM_PRE = re.compile(r'class="language-(\w+)"')
LANG_FROM_CODE = re.compile(r'class="lang-(\w+)"')


def convert_pre_block(full: str, match: re.Match) -> str:
    block = full[match.start() : match.end()]
    lang_m = LANG_FROM_PRE.search(block) or LANG_FROM_CODE.search(block)
    lang = lang_m.group(1) if lang_m else ""
    body = match.group(1)
    body = re.sub(r"</?strong>", "", body, flags=re.I)
    body = html.unescape(body)
    lines = body.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    body = "\n".join(lines)
    return f"```{lang}\n{body}\n```"


def main() -> None:
    for path in ROOT.rglob("*.mdx"):
        if "user-manual" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        out: list[str] = []
        last = 0
        changed = False
        for match in PRE_RE.finditer(text):
            out.append(text[last : match.start()])
            out.append(convert_pre_block(text, match))
            last = match.end()
            changed = True
        if changed:
            out.append(text[last:])
            path.write_text("".join(out), encoding="utf-8")
            print(f"fixed {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
