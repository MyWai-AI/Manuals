#!/usr/bin/env python3
"""Convert GitBook Git Sync export to Mintlify (MDX + docs.json)."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "user-manual"
OUT = ROOT  # Mintlify content at repo root
IMAGES_DIR = OUT / "images"
SUMMARY = SRC / "SUMMARY.md"

HINT_MAP = {
    "info": "Info",
    "success": "Check",
    "warning": "Warning",
    "danger": "Danger",
}


def decode_gitbook_entities(text: str) -> str:
    text = text.replace("&#x20;", " ")
    text = text.replace("&#x49;", "I")
    text = re.sub(r"&#x([0-9A-Fa-f]+);", lambda m: chr(int(m.group(1), 16)), text)
    return text


def path_to_nav(path: str) -> str:
    """Convert SUMMARY path like administration/README.md -> administration/index"""
    p = path.replace("\\", "/")
    if p.endswith(".md"):
        p = p[:-3]
    if p.endswith("/README"):
        p = p[: -len("/README")] + "/index"
    elif p == "README":
        p = "index"
    return p


def parse_summary(summary_text: str) -> list:
    """Parse SUMMARY.md into Mintlify navigation groups/pages."""
    lines = [ln.rstrip() for ln in summary_text.splitlines() if ln.strip() and not ln.startswith("#")]
    items: list[dict] = []
    stack: list[tuple[int, list]] = [(-1, items)]

    link_re = re.compile(r"^\s*\*\s+\[([^\]]+)\]\(([^)]+)\)\s*$")

    for line in lines:
        m = link_re.match(line)
        if not m:
            continue
        title, href = m.group(1), m.group(2)
        indent = len(line) - len(line.lstrip(" "))
        # GitBook uses 2 spaces per level
        level = indent // 2

        while stack and stack[-1][0] >= level:
            stack.pop()
        parent = stack[-1][1]

        nav_path = path_to_nav(href)
        node = {"title": title, "path": nav_path, "children": []}
        parent.append(node)
        stack.append((level, node["children"]))

    return items


def to_mintlify_nav(nodes: list[dict]) -> list:
    """Convert parsed tree to Mintlify navigation pages array."""
    result = []
    for node in nodes:
        if not node["children"]:
            result.append(node["path"])
            continue
        # Group with optional root page (README)
        group = {"group": node["title"], "pages": []}
        # If node itself is a page (has README), include as first page via root
        # Mintlify supports "root" for overview pages that also have children
        group["pages"].append(node["path"])
        group["pages"].extend(to_mintlify_nav(node["children"]))
        # Prefer nested groups for deeper structure:
        # Flatten first-level children that themselves have children as subgroups
        nested_pages = []
        for child in node["children"]:
            if child["children"]:
                nested_pages.append(
                    {
                        "group": child["title"],
                        "pages": [child["path"]] + to_mintlify_nav(child["children"]),
                    }
                )
            else:
                nested_pages.append(child["path"])
        group["pages"] = [node["path"]] + nested_pages
        result.append(group)
    return result


def extract_title(content: str, fallback: str) -> tuple[str, str]:
    """Return (title, content_without_first_h1). Prefer first H1."""
    m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if m:
        title = decode_gitbook_entities(m.group(1).strip())
        # Remove first H1 only
        content = re.sub(r"^#\s+.+\n?", "", content, count=1, flags=re.MULTILINE).lstrip("\n")
        return title, content
    return fallback, content


def strip_gitbook_frontmatter(content: str) -> str:
    if content.startswith("---\n"):
        end = content.find("\n---\n", 4)
        if end != -1:
            return content[end + 5 :].lstrip("\n")
    return content


def convert_hints(content: str) -> str:
    def repl(m: re.Match) -> str:
        style = (m.group(1) or "info").lower()
        body = m.group(2).strip()
        component = HINT_MAP.get(style, "Info")
        return f"<{component}>\n{body}\n</{component}>"

    return re.sub(
        r"\{%\s*hint\s+style=\"([^\"]+)\"\s*%\}(.*?)\{%\s*endhint\s*%\}",
        repl,
        content,
        flags=re.DOTALL,
    )


def convert_code_wrappers(content: str) -> str:
    # Remove {% code ... %} / {% endcode %} wrappers; keep inner fences
    content = re.sub(r"\{%\s*code\b[^%]*%\}\s*", "", content)
    content = re.sub(r"\s*\{%\s*endcode\s*%\}", "", content)
    return content


def convert_content_refs(content: str, src_file: Path) -> str:
    def repl(m: re.Match) -> str:
        url = m.group(1).rstrip("/")
        inner = m.group(2).strip()
        link_m = re.search(r"\[([^\]]+)\]\(([^)]+)\)", inner)
        if link_m:
            label, href = link_m.group(1), link_m.group(2)
        else:
            label = Path(url).name.replace("-", " ").replace("_", " ").title()
            href = url
        # Resolve relative to current file directory
        target = (src_file.parent / href).resolve()
        try:
            rel = target.relative_to(SRC.resolve())
        except ValueError:
            rel = Path(href)
        # Directory refs -> index
        if rel.suffix == "" and (SRC / rel / "README.md").exists():
            nav = path_to_nav(str(rel / "README.md").replace("\\", "/"))
        elif str(rel).endswith(".md") or rel.suffix == ".md":
            nav = path_to_nav(str(rel).replace("\\", "/"))
        else:
            candidate = str(rel).replace("\\", "/")
            if not candidate.endswith(".md"):
                if (SRC / f"{candidate}.md").exists():
                    nav = path_to_nav(f"{candidate}.md")
                elif (SRC / candidate / "README.md").exists():
                    nav = path_to_nav(f"{candidate}/README.md")
                else:
                    nav = path_to_nav(candidate if candidate.endswith(".md") else f"{candidate}.md")
            else:
                nav = path_to_nav(candidate)
        # Prefer human titles from SUMMARY-like text when content-ref has poor labels
        pretty = {
            "gds-installation-v3.0": "GDS Installation (v3.0)",
            "edge-installation-v2.1": "Edge Installation (v2.1)",
            "edge-installation-v3.0": "Edge Installation (v3.0)",
        }
        if label in pretty:
            label = pretty[label]
        elif label.endswith(".md") or re.fullmatch(r"[\w.-]+", label):
            # Keep explicit link labels; only prettify filename-like labels
            if "." in label or label == url or label == Path(url).name:
                label = pretty.get(Path(url).name, Path(url).name.replace("-", " ").replace("_", " ").title())
        return f'<Card title="{label}" href="/{nav}" />'

    return re.sub(
        r"\{%\s*content-ref\s+url=\"([^\"]+)\"\s*%\}(.*?)\{%\s*endcontent-ref\s*%\}",
        repl,
        content,
        flags=re.DOTALL,
    )


def convert_file_embeds(content: str) -> str:
    def repl(m: re.Match) -> str:
        src = m.group(1)
        name = Path(src).name
        # Normalize to /images/...
        asset = re.sub(r"^(\.\./)*\.gitbook/assets/", "", src)
        asset = asset.replace(".gitbook/assets/", "")
        safe = sanitize_asset_name(asset)
        return f"[{name}](/images/{safe})"

    return re.sub(r"\{%\s*file\s+src=\"([^\"]+)\"\s*%\}", repl, content)


def sanitize_asset_name(name: str) -> str:
    """Turn 'image (1).png' into 'image-1.png' for stable Mintlify URLs."""
    path = Path(name)
    stem = re.sub(r"\s*\((\d+)\)\s*", r"-\1", path.stem)
    stem = stem.replace(" ", "-")
    return stem + path.suffix


def asset_to_url(asset: str) -> str:
    asset = re.sub(r"^(\.\./)*\.gitbook/assets/", "", asset)
    asset = asset.replace(".gitbook/assets/", "")
    asset = asset.strip("<>").strip()
    return sanitize_asset_name(asset)


def convert_figures(content: str) -> str:
    def repl(m: re.Match) -> str:
        src = m.group(1)
        caption = (m.group(2) or "").strip() if m.lastindex and m.lastindex >= 2 else ""
        caption = re.sub(r"</?p>", "", caption).strip()
        img = f"![](/images/{asset_to_url(src)})"
        if caption:
            return f"{img}\n\n*{caption}*\n\n"
        return f"{img}\n\n"

    # Optional wrapping <div ...>
    content = re.sub(
        r"(?:<div[^>]*>\s*)?<figure>\s*<img\s+[^>]*src=\"([^\"]+)\"[^>]*>\s*"
        r"(?:<figcaption>(.*?)</figcaption>)?\s*</figure>\s*(?:</div>)?",
        repl,
        content,
        flags=re.DOTALL,
    )
    # Markdown images: GitBook uses <path with spaces/parens>
    content = re.sub(
        r"!\[([^\]]*)\]\(<((?:\.\./)*\.gitbook/assets/[^>]+)>\)",
        lambda m: f"![{m.group(1)}](/images/{asset_to_url(m.group(2))})\n\n",
        content,
    )
    content = re.sub(
        r"!\[([^\]]*)\]\(((?:\.\./)*\.gitbook/assets/[^)\s]+)\)",
        lambda m: f"![{m.group(1)}](/images/{asset_to_url(m.group(2))})\n\n",
        content,
    )
    # Any remaining <img ... src=".gitbook/assets/...">
    content = re.sub(
        r"<img\s+[^>]*src=\"(?:\.\./)*\.gitbook/assets/([^\"]+)\"[^>]*>",
        lambda m: f"![](/images/{asset_to_url(m.group(1))})\n\n",
        content,
    )
    return content


def convert_asset_links(content: str) -> str:
    content = re.sub(
        r"\]\(<((?:\.\./)*\.gitbook/assets/[^>]+)>\)",
        lambda m: f"](/images/{asset_to_url(m.group(1))})",
        content,
    )
    content = re.sub(
        r"\]\(((?:\.\./)*\.gitbook/assets/[^)\s]+)\)",
        lambda m: f"](/images/{asset_to_url(m.group(1))})",
        content,
    )
    return content


def convert_md_links(content: str, src_file: Path) -> str:
    """Rewrite relative .md links to Mintlify paths without extension."""

    def repl(m: re.Match) -> str:
        label, href = m.group(1), m.group(2)
        if href.startswith(("http://", "https://", "mailto:", "#", "/")):
            return m.group(0)
        if ".gitbook/assets/" in href or href.startswith("/images/"):
            return m.group(0)

        anchor = ""
        path = href
        if "#" in href:
            path, anchor = href.split("#", 1)
            anchor = f"#{anchor}"

        if not path:
            return m.group(0)

        if path.endswith(".md") or path.endswith("/"):
            resolved = (src_file.parent / path).resolve()
            try:
                rel = resolved.relative_to(SRC.resolve())
            except ValueError:
                return m.group(0)
            if resolved.is_dir() or path.endswith("/"):
                nav = path_to_nav(str(rel / "README.md").replace("\\", "/"))
            else:
                nav = path_to_nav(str(rel).replace("\\", "/"))
            return f"[{label}](/{nav}{anchor})"
        return m.group(0)

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, content)


def convert_content(raw: str, fallback_title: str, src_file: Path) -> str:
    content = strip_gitbook_frontmatter(raw)
    content = decode_gitbook_entities(content)
    title, content = extract_title(content, fallback_title)
    content = convert_hints(content)
    content = convert_code_wrappers(content)
    content = convert_content_refs(content, src_file)
    content = convert_file_embeds(content)
    content = convert_figures(content)
    content = convert_asset_links(content)
    content = convert_md_links(content, src_file)
    # MDX requires self-closing void elements
    content = content.replace("<br>", "<br />")
    content = content.replace("<hr>", "<hr />")
    # Leftover {% ... %} tags (best-effort strip)
    leftover = re.findall(r"\{%.*?%\}", content, flags=re.DOTALL)
    if leftover:
        print(f"  WARN leftover tags: {leftover[:5]}")
    frontmatter = f'---\ntitle: "{title.replace(chr(34), chr(92)+chr(34))}"\n---\n\n'
    return frontmatter + content.strip() + "\n"


def out_path_for(src_file: Path) -> Path:
    rel = src_file.relative_to(SRC)
    parts = list(rel.parts)
    if parts[-1] == "README.md":
        if len(parts) == 1:
            return OUT / "index.mdx"
        return OUT.joinpath(*parts[:-1]) / "index.mdx"
    if parts[-1] == "SUMMARY.md":
        return None  # type: ignore
    stem = parts[-1]
    if stem.endswith(".md"):
        parts[-1] = stem[:-3] + ".mdx"
    return OUT.joinpath(*parts)


def copy_images() -> None:
    src_assets = SRC / ".gitbook" / "assets"
    if not src_assets.exists():
        return
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    for f in src_assets.iterdir():
        if f.is_file():
            shutil.copy2(f, IMAGES_DIR / sanitize_asset_name(f.name))
    print(f"Copied assets -> {IMAGES_DIR}")


def build_docs_json(nav_items: list[dict]) -> dict:
    pages = to_mintlify_nav(nav_items)
    # Top-level: Welcome + Access as pages, rest as groups already
    # parse_summary already nested; to_mintlify_nav wraps groups.
    # Flatten so Welcome/Access stay top-level pages and sections are groups.
    navigation_pages = []
    for node in nav_items:
        if not node["children"]:
            navigation_pages.append(node["path"])
        else:
            nested = []
            for child in node["children"]:
                if child["children"]:
                    nested.append(
                        {
                            "group": child["title"],
                            "pages": [child["path"]] + flatten_pages(child["children"]),
                        }
                    )
                else:
                    nested.append(child["path"])
            navigation_pages.append(
                {"group": node["title"], "pages": [node["path"]] + nested}
            )

    return {
        "$schema": "https://mintlify.com/docs.json",
        "name": "MYW.AI - User Manual",
        "theme": "mint",
        "colors": {"primary": "#0B6BCB", "light": "#3B8DD9", "dark": "#084A8A"},
        "navigation": {
            "groups": [
                {"group": "User Manual", "pages": navigation_pages},
            ]
        },
    }


def flatten_pages(nodes: list[dict]) -> list:
    result = []
    for node in nodes:
        if node["children"]:
            result.append(
                {
                    "group": node["title"],
                    "pages": [node["path"]] + flatten_pages(node["children"]),
                }
            )
        else:
            result.append(node["path"])
    return result


def title_from_path(path: Path) -> str:
    name = path.stem
    if name == "README":
        name = path.parent.name if path.parent != SRC else "Welcome"
    return name.replace("-", " ").replace("_", " ").title()


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Source not found: {SRC}")

    summary = SUMMARY.read_text(encoding="utf-8")
    nav_items = parse_summary(summary)
    docs = build_docs_json(nav_items)
    (OUT / "docs.json").write_text(json.dumps(docs, indent=2) + "\n", encoding="utf-8")
    print("Wrote docs.json")

    copy_images()

    md_files = [p for p in SRC.rglob("*.md") if ".gitbook" not in p.parts and p.name != "SUMMARY.md"]
    for src_file in sorted(md_files):
        dest = out_path_for(src_file)
        if dest is None:
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        raw = src_file.read_text(encoding="utf-8")
        converted = convert_content(raw, title_from_path(src_file), src_file)
        dest.write_text(converted, encoding="utf-8")
        print(f"Converted {src_file.relative_to(SRC)} -> {dest.relative_to(OUT)}")

    print("Done.")


if __name__ == "__main__":
    main()
