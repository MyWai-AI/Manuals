#!/usr/bin/env python3
"""Post-fix remaining link issues in converted MDX."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MENTION_RE = re.compile(
    r"\[([^\]]+)\]\(([^)\s]+?)(?:\s+\"[^\"]*\")?\)"
)


def resolve_md_href(src_file: Path, href: str) -> str | None:
    if href.startswith(("http://", "https://", "mailto:", "#", "/")):
        return None
    path, anchor = (href.split("#", 1) + [""])[:2]
    if not (path.endswith(".md") or path.endswith("/")):
        return None
    resolved = (src_file.parent / path).resolve()
    try:
        rel = resolved.relative_to(ROOT.resolve())
    except ValueError:
        return None
    if path.endswith("/") or resolved.is_dir():
        nav = str(rel).replace("\\", "/") + "/index"
    else:
        nav = str(rel.with_suffix("")).replace("\\", "/")
        if nav.endswith("/README"):
            nav = nav[: -len("/README")] + "/index"
        elif nav.endswith("README"):
            nav = "index"
    label_path = Path(path).name
    label = Path(label_path).stem if label_path.endswith(".md") else label_path
    label = label.replace("-", " ").replace("_", " ").title()
    suffix = f"#{anchor}" if anchor else ""
    return f"[{label}](/{nav}{suffix})"


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text

    def repl(m: re.Match) -> str:
        href = m.group(2)
        fixed = resolve_md_href(path, href)
        return fixed if fixed else m.group(0)

    text = MENTION_RE.sub(repl, text)

    # Card titles accidentally title-cased .md -> .Md
    text = re.sub(
        r'(<Card title=")([^"]+?)\.Md(")',
        lambda m: f'{m.group(1)}{m.group(2).replace("-", " ").strip()}{m.group(3)}',
        text,
    )
    text = text.replace('title="As .Zip Package"', 'title="As .zip Package"')
    text = text.replace('title="Installation On Windows"', 'title="Installation on Windows"')

    # Known broken GitBook asset placeholders
    text = text.replace("![](/broken/files/IdllMtyRqMU8PRPKWepZ)", "*(Edge Device Details)*")
    text = text.replace(
        "](/broken/spaces/vjuWaEo4y48XYZR4INvA)",
        "](/custom-ai-algorithms)",
    )

    # Folder links should target /index
    for folder in [
        "administration",
        "configuration",
        "configuration/sensors",
        "data",
        "3d-viewer",
        "analysis",
        "analysis/algorithms",
        "automation",
        "reporting",
        "edge-operations",
        "edge-operations/gds-installation-v3.0",
        "edge-operations/edge-installation-v2.1",
        "edge-operations/edge-installation-v3.0",
        "custom-ai-algorithms",
        "custom-ai-algorithms/packaging-a-custom-ai-algorithm",
        "marketplace-tools",
    ]:
        text = text.replace(f'href="/{folder}"', f'href="/{folder}/index"')
        text = text.replace(f'](/{folder})', f'](/{folder}/index)')
        text = text.replace(f'](/{folder} ', f'](/{folder}/index ')

    if path.name == "index.mdx" and "edge-installation-v3.0" in str(path):
        text = text.replace(
            "/edge-operations/edge-installation-v2.1/installation-on-ubuntu",
            "/edge-operations/edge-installation-v3.0/edge-installation-on-ubuntu",
        )

    # Anchor slug for advanced installations heading
    text = text.replace(
        "#connect-edge-with-a-gds-on-a-different-device",
        "#connect-edge-with-a-gds-on-a-different-device",
    )

    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*.mdx"):
        if "user-manual" in path.parts:
            continue
        if fix_file(path):
            changed += 1
            print(path.relative_to(ROOT))
    print(f"updated {changed} files")


if __name__ == "__main__":
    main()
