---
name: docs-navigation
description: >-
  Navigate the Docs knowledge library via AGENTS.md read order, meta/routing,
  topics.yaml, and hub READMEs (domains, Games OS, Health OS, career). Use when
  answering from this repo, finding canonical docs, resolving tech vs career
  overlaps, Games OS make/play/earn/follow, hormones/lifestyle theory, adding
  canonical topics, or writing Vietnamese context/content (đúng ngữ cảnh, dễ đọc).
---

# Docs navigation

## Read order (mandatory)

Before broad grep/search:

1. `AGENTS.md`
2. `OVERVIEW.md`
3. `meta/routing.md` (or `meta/catalog/topics.yaml`)
4. Hub README (`domains/README.md`, `guides/…/README.md`, `personal/README.md`)
5. Canonical deep-dive — **cite markdown paths** in the answer

If routing fails, then search. Prefer Stable domains (`domains/README.md`) unless asked for Drafting.

## Intent → hub

| Intent | Start |
| --- | --- |
| How to build / implement (tech) | `domains/<x>/README.md` → modules |
| Career / freelance / monetize | `guides/03-career-skills/<x>/` |
| Overlap tech ↔ career | `meta/domain-guide-map.md` |
| Everything games | `guides/05-games-os/README.md` → `games-os-map.md` |
| Make game (design/Unity/netcode) | `domains/game-dev/` (+ `challenges/game-dev/`) |
| Phân tích title / full-pack / pitch+GDD+teardown | `domains/game-dev/analyses/` · skill `game-design-docs` mode `full-pack` |
| Systems teardown essay only | `domains/game-dev/game-design/templates/game-systems-teardown.md` · skill `game-systems-teardown` (prefer inside pack) |
| Earn from games | `guides/03-career-skills/game-dev/` |
| Play / leisure / backlog | `guides/05-games-os/play/` |
| Game news (culture + industry) | `guides/05-games-os/follow/` |
| Learning how to learn | `guides/03-career-skills/productivity/meta-skills/learning-os-framework.md` |
| Hormones / health theory | `guides/04-lifestyle-os/health/` (map → interactions → rhythm → control playbook → one `*-system.md` per hormone) |
| Luật Việt Nam / VBQPPL / số hiệu đạo luật | `guides/06-vn-law/README.md` → `catalog.yaml` |
| HĐLĐ / NDA / thuế DN thực hành | `guides/02-wealth-business/legal/` |
| User’s own logs/metrics | `personal/` **only if asked** |

## Answer rules

- Cite paths (and `##` headings when useful). Prefer map/README/playbook over mid-file walls.
- Conflict: `*-map.md` / hub README → playbook → deep-dive → older duplicate.
- Long files: Agent SUMMARY first, then jump to needed `##`. Do not dump whole files.
- Prefer markdown guides over `resources/**/*.pdf`. Prefer `meta/` over root stubs.
- Educational lifestyle only — no fabricated diagnosis; clinical symptoms → professional care.
- GitHub wishlist/clone catalog is local `GitClone/PROJECTS.md` (gitignored). Non-GitHub links: `resources/collected_links/`.

## Editing (when creating/changing canonical docs)

1. Kebab-case paths; frontmatter per `meta/catalog/FRONTMATTER.md`.
2. New canonical topic → update `meta/routing.md` **and** `meta/catalog/topics.yaml`.
3. New domain → update `domains/README.md` maturity table.
4. Validate: `python scripts/check_agent_catalog.py`

## Vietnamese content (mandatory)

Khi tạo **context** hoặc **content** tiếng Việt: phải **đúng ngữ cảnh**, **đọc dễ hiểu**.

- Viết như người Việt nói/đọc được hết một mạch — câu đủ, ý rõ, không dịch cứng từ tiếng Anh.
- Thuật ngữ Anh chỉ giữ khi cần (tên bài, tên riêng). Lần đầu **giải thích bằng tiếng Việt**; sau đó dùng tiếng Việt.
- Cấm chồng viết tắt / jargon không giải thích (`T1`, `PE`, `PMF`, `dry-run`, `prior`, `vá T4`…) trong đoạn người đọc.
- Bảng và gạch đầu dòng cũng phải đọc được; không nhồi một ô toàn từ Anh rút gọn.
- Filename tiếng Anh được; **thân bài tiếng Việt** thì ngữ cảnh tiếng Việt.

## Anti-patterns

- Grep random long files before routing
- Answer from stale `guides/INDEX.md` alone without checking hub/fs
- Mix `personal/` CSV into general advice
- Put play/news into `domains/game-dev/`
- Scatter pitch/GDD/teardown for one title outside `domains/game-dev/analyses/<slug>/` (use `full-pack`)
- Put GitHub repos into `resources/collected_links/` (use `GitClone/PROJECTS.md` locally)
- Dump Luật VN corpus into `guides/02-wealth-business/legal/` (catalog/notes → `guides/06-vn-law/`)
- Viết body tiếng Việt kiểu dịch Anh / Vietlish / viết tắt chồng (người đọc phải dịch ngược mới hiểu)

## Quick examples

**User:** “Unity netcode / how do I build multiplayer?”  
→ `domains/game-dev/README.md` → networking hub; career only if they ask rates/freelance.

**User:** “full-pack / phân tích Honkai Star Rail đủ models”  
→ `domains/game-dev/analyses/` · skill `game-design-docs` mode `full-pack` (not Games OS Play).

**User:** “Games OS / chơi game bền / tin industry tuần này?”  
→ `guides/05-games-os/` → play or follow; not `domains/game-dev`.

**User:** “Hormone / cortisol checklist”  
→ `endocrine-hormone-map.md` then `endocrine-control-playbook.md` under health hub.
