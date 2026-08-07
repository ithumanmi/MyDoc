# Agent eval

Smoke-test set for Cursor agents and external RAG over this repo.

| File | Purpose |
| --- | --- |
| [`questions.md`](./questions.md) | 25 Qs + expected canonical paths |
| [`scorecard.md`](./scorecard.md) | Manual pass/fail grid |

```bash
python scripts/check_agent_eval_paths.py   # paths exist
python scripts/smoke_agent_routing.py      # routing coverage → scorecard.md
python scripts/check_agent_catalog.py      # catalog topics exist
```

Agent instructions: [`../../AGENTS.md`](../../AGENTS.md)  
Meta hub: [`../README.md`](../README.md)
