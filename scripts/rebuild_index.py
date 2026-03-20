#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def main() -> int:
    root = Path('knowledge')
    rows = []
    for topic_dir in sorted([p for p in root.iterdir() if p.is_dir() and not p.name.startswith('_')]):
        m = topic_dir / 'manifest.json'
        day = 'unknown'
        if m.exists():
            data = json.loads(m.read_text(encoding='utf-8'))
            day = data.get('day', 'unknown')
        status = 'open'
        priority = 'medium'
        if topic_dir.name in {'github', 'openclaw'}:
            priority = 'high'
        rows.append((topic_dir.name, day, status, priority))

    out = ["# Knowledge Index", "", "| Topic | Last Updated | Status | Priority |", "|---|---|---|---|"]
    out += [f"| {t} | {d} | {s} | {p} |" for (t, d, s, p) in rows]
    out += ["", "## Notes", "- Status: open / tracking / done / archived", "- Priority: high / medium / low", ""]
    (root / '_index.md').write_text("\n".join(out), encoding='utf-8')
    print('updated knowledge/_index.md')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
