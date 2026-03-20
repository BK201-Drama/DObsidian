# Memory Compact

- updated_at: 2026-03-20T18:25:00+08:00
- source_day: 2026-03-20
- style: 主题 -> 结论 -> 证据 -> 后续动作 -> 风险 -> 状态

### 主题：DObsidian bootstrap
- 结论：知识库基础结构已搭建完成并已推送到远程仓库。
- 证据：`https://github.com/BK201-Drama/DObsidian` 已可访问。
- 后续动作：持续补充主题卡片并执行定期去重。
- 风险：早期 topic 分类可能随实践调整。
- 状态：tracking
- 更新时间：2026-03-20T18:25:00+08:00

### 主题：Dual-repo capability mapping
- 结论：当前能力分为两条主线：代码能力与文本转视频能力，并已形成统一调度 skill。
- 证据：
  - 代码能力仓库：`https://github.com/BK201-Drama/Base-Boilerplate`
  - 文本转视频仓库：`https://github.com/BK201-Drama/brainstorm`（`video_story_generator`）
  - OpenClaw skill：`skills/dual-repo-ops`（已打包 `dist/dual-repo-ops.skill`）
- 后续动作：新增 `novel-style-generator` skill，用于按风格生成章节 txt，再接视频流水线。
- 风险：跨仓流程若无统一命令入口，容易出现维护分裂。
- 状态：open
- 更新时间：2026-03-20T19:26:00+08:00

### 主题：TXT-first novel-to-video decision
- 结论：故事生产采用“先 txt、后视频”的单一真源策略。
- 证据：章节规范已落地为 `stories/<小说名>/chapter-xxx.txt`，并支持按章节/范围生成视频。
- 后续动作：增加章节批量重试与质量校验报告（时长对齐、字幕末尾边界）。
- 风险：若 TTS 文本与字幕文本走不同清洗链路，可能产生语义不一致。
- 状态：open
- 更新时间：2026-03-20T19:26:00+08:00

### 主题：Audio-tail truncation fix
- 结论：已修复“音频长于底视频导致尾部被截断”的问题。
- 证据：`brainstorm` 提交 `821e7ad`；修复后实测 video/audio 时长约 `22.166s/22.180s`，尾部对齐可接受。
- 后续动作：将时长差阈值（如 0.3s）纳入自动检查脚本。
- 风险：不同编码器和平台可能造成轻微漂移，需要阈值容忍。
- 状态：tracking
- 更新时间：2026-03-20T19:26:00+08:00
