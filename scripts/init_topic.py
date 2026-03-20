#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from datetime import datetime
import json


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a knowledge topic")
    parser.add_argument("--topic", required=True, help="topic name, e.g. github")
    parser.add_argument("--root", default=".", help="repo root")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    topic_dir = root / "knowledge" / args.topic
    topic_dir.mkdir(parents=True, exist_ok=True)

    now = datetime.now().astimezone()
    day = now.strftime("%Y-%m-%d")

    compact = topic_dir / "memory_compact.md"
    if not compact.exists():
        compact.write_text(
            "# Memory Compact\n\n"
            f"- updated_at: {now.isoformat()}\n"
            f"- source_day: {day}\n"
            "- style: 主题 -> 结论 -> 后续动作\n\n",
            encoding="utf-8",
        )

    manifest = topic_dir / "manifest.json"
    if not manifest.exists():
        manifest.write_text(
            json.dumps(
                {
                    "day": day,
                    "new_items": 0,
                    "kept_topics": 0,
                    "used_tokens_est": 0,
                    "max_tokens": 3000,
                    "style": "topic-card",
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    print(f"initialized: {topic_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
