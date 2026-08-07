# Plan: Agent Retrieval Hardening

> Status: **Implemented** (Aug 2026)  
> Goal: Cursor agents + external RAG navigate & answer from this repo reliably.

## Phases

| Phase | Items | Status |
| --- | --- | --- |
| **P0** | `AGENTS.md`, `llms.txt`, `AGENT-ROUTING.md`, `.cursor/rules/*` | ✅ |
| **P1** | `catalog/topics.yaml`, frontmatter schema, SUMMARY on long deep-dives, hub links | ✅ |
| **P2** | `agent-eval/questions.md`, RAG exclude list, catalog path checker script | ✅ |

## Success criteria
- Agent defaults to hubs → canonical docs (not random mid-file).
- `personal/` treated as private life-data, not curriculum.
- Topic lookup resolves via `AGENT-ROUTING.md` / `catalog/topics.yaml`.
- Eval set documents expected paths for ~25 questions.

## Non-goals (this pass)
- Rewriting all 1800 files’ frontmatter.
- Building a vector DB / embedding pipeline.
- Auto-regenerating every INDEX.md (manual INDEX debt remains; use catalog instead).

## Follow-ups (optional / partial)
| Item | Status |
| --- | --- |
| Expand catalog (guides pillars, sleep, movement, health protocols…) | ✅ 2026-08-07 |
| More Agent SUMMARYs (sleep, movement, health-opt, learning-os) | ✅ |
| Frontmatter on main hubs only | ✅ |
| Frontmatter on 15 domain READMEs | optional |
| Hook into QUICK-START.md | optional |
| Run 25-question smoke eval scoring | optional |
| SUMMARY on remaining long domain deep-dives | optional |