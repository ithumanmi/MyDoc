---
title: "Game systems teardown template"
description: "Fillable essay template: loop physics, systems map, axes, tiers, economy, UX"
updated: "2026-08-10"
canonical: true
tags: [game-design, template, teardown, systems]
audience: [intermediate, advanced]
related:
  - ../advanced-core-loops.md
  - ../core-loop-mastery.md
  - ../economy-systems.md
  - ../game-economics-monetization.md
  - ../player-psychology.md
  - ../checklist-game-review.md
  - ../genre-deep-dives/README.md
sensitivity: public
---

# Game systems teardown — template

> [← Game Design](../README.md) · Skill: `.cursor/skills/game-systems-teardown/`  
> Quality bar: systems essay (named mechanisms + tradeoffs), not a feature list.  
> Forward docs (pitch/GDD/economy/…): skill `game-design-docs` · [templates/](./)

**Title:** …  
**Platform / model:** … (mobile arcade · GaaS · premium · …)  
**Genre family:** …  
**Sources:** play / VOD / wiki / patch notes — mark claims `(observed)` · `(inferred)` · `(genre pattern)`

---

## 0. Thesis (1–2 câu)

Game này **đảo / nhấn** điều gì so với chuẩn thể loại?  
→ …

## 1. Loop physics & nhịp agency

### Core actions (chuỗi)
`A → B → C → …` (tên hành động cụ thể)

### Feedback
- Positive: …
- Negative / brake: …

### Phases (bắt buộc)

| Phase | Player agency | Hệ thống đang làm gì | Cảm xúc mục tiêu |
| --- | --- | --- | --- |
| Early (micro) | High control | … | … |
| Mid (tipping / expand) | … | … | … |
| Late (macro / spectacle hoặc endurance) | … | … | … |

### Vì sao nhịp này khớp platform?
…

## 2. Systems map

| Layer | Loop / modes | Job |
| --- | --- | --- |
| **Core** (trong màn) | … | Instant skill / risk-reward |
| **Meta** (ngoài màn) | … | Long-horizon motive / identity |
| **Live / modes** | … | Diversify session length / retention |

## 3. Decision axes (1–3 xung lực trái chiều)

### Axis 1 — `<Name A>` vs `<Name B>`

| | A | B |
| --- | --- | --- |
| Làm gì | … | … |
| Được | … | … |
| Mất / rủi ro | … | … |
| Khi nào chọn | … | … |

*(Lặp Axis 2…)*

## 4. Escalation & anti power-creep

| Tier / gate | Vai trò | Cách trả lời power của player |
| --- | --- | --- |
| T0 … | … | … |
| T1 … | … | … |
| T2 … | … | … |
| Boss / soft wall | … | … |

## 5. Economy & monetization friction

| | Chi tiết |
| --- | --- |
| Sources | … |
| Sinks (stat / content) | … |
| Grinding wall / friction point | … |
| Premium → freemium pattern? | … |
| Ethics / feel of fair | … |

## 6. UI/UX & psychology

| Topic | Phân tích |
| --- | --- |
| Controls / FTUE | … |
| Friction điểm | … |
| Visual hierarchy khi mật độ cao / phức tạp | … |
| Quality-of-life gap | … |

## 7. Transfer (mang đi game khác)

| Pattern portable | Đừng copy mù |
| --- | --- |
| … | … |

## 8. Open questions / verify

- [ ] Telemetry hoặc replay cần để cứng hóa claim …
- [ ] So sánh 1–2 competitor cùng family: …

## Theory refs (Docs)

- Core/meta: [`advanced-core-loops.md`](../advanced-core-loops.md)
- Economy: [`economy-systems.md`](../economy-systems.md) · [`game-economics-monetization.md`](../game-economics-monetization.md)
- Psyche: [`player-psychology.md`](../player-psychology.md)
- Genre pillars: [`genre-deep-dives/`](../genre-deep-dives/README.md)
- Build QA scoring (khác teardown): [`checklist-game-review.md`](../checklist-game-review.md)
