#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

CARD_RE = re.compile(r"(^### 主题：.*?)(?=^### 主题：|\Z)", re.M | re.S)


def normalize(card: str) -> str:
    title = ""
    conclusion = ""
    for line in card.splitlines():
        if line.startswith("### 主题："):
            title = line.strip()
        elif line.strip().startswith("- 结论："):
            conclusion = line.strip()
            break
    return f"{title}|{conclusion}"


def dedupe_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    cards = CARD_RE.findall(text)
    if not cards:
        return 0

    seen: set[str] = set()
    kept: list[str] = []
    removed = 0

    for c in cards:
        key = hashlib.sha1(normalize(c).encode("utf-8")).hexdigest()
        if key in seen:
            removed += 1
            continue
        seen.add(key)
        kept.append(c.strip() + "\n\n")

    if removed:
        header_end = text.find("### 主题：")
        header = text[:header_end] if header_end != -1 else text
        path.write_text(header.rstrip() + "\n\n" + "".join(kept).rstrip() + "\n", encoding="utf-8")

    return removed


def main() -> int:
    parser = argparse.ArgumentParser(description="Dedupe topic cards by title+conclusion")
    parser.add_argument("--root", default="knowledge", help="knowledge root")
    args = parser.parse_args()

    root = Path(args.root)
    total_removed = 0
    for p in sorted(root.glob("*/memory_compact.md")):
        removed = dedupe_file(p)
        total_removed += removed
        print(f"{p}: removed={removed}")

    print(f"total_removed={total_removed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
