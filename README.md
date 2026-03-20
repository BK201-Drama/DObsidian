# DObsidian

DObsidian is a compact personal knowledge repository for OpenClaw-style memory workflows.

## Goals

- Keep Git clean: only compact/curated knowledge is tracked.
- Keep raw logs local-only for privacy and traceability.
- Support daily capture, long-term memory, and topic-based knowledge cards.

## Structure

```text
knowledge/
  github/
    memory_compact.md
    manifest.json
  openclaw/
    memory_compact.md
    manifest.json
  projects/
    memory_compact.md
    manifest.json

memory/
  YYYY-MM-DD.md

scripts/
  init_topic.py
  update_manifest.py

docs/
  local-logs.md
```

## Tracked in Git

- `knowledge/*/memory_compact.md`
- `knowledge/*/manifest.json`
- `MEMORY.md`
- docs and scripts

## Local-only (ignored)

- `local_logs/<topic>/messages-YYYY-MM.jsonl`
- transient scratch/output files

## Quick Start

```bash
# 1) Initialize a new topic card
python3 scripts/init_topic.py --topic ideas

# 2) Update manifest for a topic
python3 scripts/update_manifest.py --topic github --new-items 3 --kept-topics 2 --used-tokens-est 180
```

## Memory Layers

1. Daily raw notes: `memory/YYYY-MM-DD.md`
2. Long-term stable memory: `MEMORY.md`
3. Topic knowledge cards: `knowledge/<topic>/memory_compact.md`

## License

MIT
