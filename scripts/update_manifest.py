#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from datetime import datetime


def main() -> int:
    parser = argparse.ArgumentParser(description="Update topic manifest")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--new-items", type=int, required=True)
    parser.add_argument("--kept-topics", type=int, required=True)
    parser.add_argument("--used-tokens-est", type=int, required=True)
    parser.add_argument("--max-tokens", type=int, default=3000)
    parser.add_argument("--root", default=".")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    manifest = root / "knowledge" / args.topic / "manifest.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)

    day = datetime.now().astimezone().strftime("%Y-%m-%d")
    payload = {
        "day": day,
        "new_items": args.new_items,
        "kept_topics": args.kept_topics,
        "used_tokens_est": args.used_tokens_est,
        "max_tokens": args.max_tokens,
        "style": "topic-card",
    }

    manifest.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"updated: {manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
