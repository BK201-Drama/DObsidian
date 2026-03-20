# Local Raw Message Logs (Local-only)

## Goal

- Keep GitHub repo clean: only compact knowledge.
- Store raw logs locally for traceability and re-compaction.

## Path & Naming

- `local_logs/<topic>/messages-YYYY-MM.jsonl`

## Suggested JSON fields

```json
{
  "ts": "2026-03-20T16:55:00+08:00",
  "topic": "github",
  "channel": "feishu",
  "chat_id": "chat:xxx",
  "message_id": "om_xxx",
  "role": "user",
  "sender": "name",
  "text": "...",
  "meta": {}
}
```

## Cleanup policy

- Keep current month and 1 previous month buffer.
- Delete older files periodically.
