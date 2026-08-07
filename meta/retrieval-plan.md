# Plan: Agent Retrieval Hardening

> Status: **Implemented** (Aug 2026) · relocated under [`meta/`](./README.md)  
> Goal: Cursor agents + external RAG navigate & answer from this repo reliably.

## Phases

| Phase | Items | Status |
| --- | --- | --- |
| **P0** | `AGENTS.md`, `llms.txt`, `meta/routing.md`, `.cursor/rules/*` | ✅ |
| **P1** | `meta/catalog/topics.yaml`, frontmatter schema, SUMMARY on long deep-dives, hub links | ✅ |
| **P2** | `meta/eval/questions.md`, RAG exclude list, catalog path checker script | ✅ |
| **Meta reorg** | Agent/RAG artifacts under `meta/` (Phase 1 folder plan) | ✅ |

## Success criteria
- Agent defaults to hubs → canonical docs (not random mid-file).
- `personal/` treated as private life-data, not curriculum.
- Topic lookup resolves via `meta/routing.md` / `meta/catalog/topics.yaml`.
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
| Frontmatter on 15 domain READMEs | ✅ |
| Hook into QUICK-START.md | ✅ |
| SUMMARY on top long domain deep-dives (~8) | ✅ |
| Harden agent-eval (full paths + path checker + scorecard) | ✅ |
| Routing smoke auto-score (`smoke_agent_routing.py`) | ✅ |
| Meta folder reorganization | ✅ |
| Health path shorten (`well-being/biohacking` → `health/`) | ✅ |
| Manual 25-question live Cursor turns | optional (routing smoke >=20/25 already) |
| Vector DB / sync INDEX tu dong | non-goal |
