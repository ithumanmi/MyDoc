# Catalog for agents & RAG

| File | Purpose |
| --- | --- |
| [topics.yaml](./topics.yaml) | topic id → canonical path + aliases |
| [FRONTMATTER.md](./FRONTMATTER.md) | YAML schema for markdown |
| [rag-exclude.txt](./rag-exclude.txt) | Globs to skip when embedding |

Validate: `python scripts/check_agent_catalog.py`

Human routing twin: [`../routing.md`](../routing.md)  
Meta hub: [`../README.md`](../README.md)
