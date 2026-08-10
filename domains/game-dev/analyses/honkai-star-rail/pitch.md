---
title: "Honkai: Star Rail — Pitch / one-pager (reconstructed)"
description: "Reconstructed pitch: turn-based combat puzzle + GaaS collection for Hoyoverse stack."
updated: "2026-08-10"
canonical: false
tags: [game-design, pitch, gaas, analysis-pack]
audience: [intermediate, advanced]
related:
  - ./README.md
  - ./gdd.md
  - ../../game-design/templates/game-pitch-one-pager.md
sensitivity: public
---

# Honkai: Star Rail — Pitch / one-pager

> [← Pack](./README.md) · Skill: `game-design-docs` · Mode: `pitch`  
> Pitch **tái dựng** từ game đã ship — không phải deck nội bộ miHoYo.

| Field | Value |
| --- | --- |
| Working title | Honkai: Star Rail |
| Owner | Docs study (reconstructed) |
| Status | `(locked)` as shipped reference |
| Date | 2026-08-10 |
| Audience | design study / GaaS TB RPG greenlight exercise |

---

## 0. Hook (1 câu)

Bạn là Trailblazer trên đoàn tàu Astral Express — **ghép đội 4 người đánh theo lượt**, phá Toughness và xoay Skill Point như puzzle, trong vũ trụ aeon/Path — dưới áp lực **stamina ngày và banner limited** của GaaS. `(observed)`

---

## 1. Player & occasion

- **Target player:** Fan Hoyoverse / gacha RPG; thích story anime + combat có depth; chơi mobile/PC session ngắn hoặc grind endgame. `(assumed)`
- **Occasion:** Commute / couch / desk — dailies 10–20p hoặc MoC block dài hơn. `(assumed)`
- **Session length target:** Daily ~15–30p; story/endgame 45–90p `(assumed)`

---

## 2. Core loop (1 chuỗi)

`Enter fight → Read weakness → Manage SP → Break Toughness → Burst / Ult window → Clear → Spend TB Power / upgrade roster → Next content gate`

---

## 3. USP / role inversion

- **Comps:** Genshin Impact (same studio open-world action); other gacha TB (e.g. classic SRPG gacha); premium TB like Persona on time. `(observed)` / `(genre pattern)`
- **We flip:** Trong stack Hoyoverse, **bỏ aim/i-frame** → combat-as-puzzle (Break/SP); giữ máy GaaS (Power, pity, cycles) để retention tháng. `(inferred)`

---

## 4. Pillars (≤3)

| # | Pillar | Playtestable signal |
| --- | --- | --- |
| 1 | **Every Skill spends a shared SP** | Players vocalize “need battery” / Basic to breathe `(observed)` |
| 2 | **Break opens the real damage window** | Elite fights punish ignore-Toughness `(observed)` |
| 3 | **Roster breadth > one eternal team** | New MoC cycle forces swaps / new covers `(observed)` |

**Anti‑goals:** Pure idle clicker; pay-to-skip story beat tường minh; combat chỉ ATK number không puzzle. `(assumed)`

---

## 5. Scope slice (MVP / study)

- **In:** FTUE fight dạy weakness+SP → one gacha-feel recruit moment → one stamina-gated farm → one endgame-lite timer clear. `(proposed)`
- **Out:** Full SU variants, all Paths, multi-year banner archive.
- **Shipped North Star:** Continuously updated story worlds + rotating endgame + collection meta. `(observed)`

---

## 6. Business model

- **Model:** GaaS freemium / gacha `(observed)`
- **Primary lever:** Limited character/LC banners + BP + packs; pity softens variance `(observed)`
- **Non‑goals (ethics tension):** Avoid selling direct stage skip; friction = time/roster ceiling `(inferred)` — still extractive via FOMO `(genre pattern)`

---

## 7. Risks & ask

| Risk | Mitigation |
| --- | --- |
| “Just Genshin TB” narrative | Market Break/SP puzzle + Auto farm honesty `(assumed)` |
| Relic RNG burnout | Pity-adjacent crafting / loadout QoL over time `(observed)` / evolving |
| Power creep one-unit meta | Cycle buffs + multi-mode endgame (MoC/PF/AS) `(observed)` |

**Ask (exercise):** Greenlight vertical slice “SP puzzle + one stamina day + one banner fantasy” trước khi commit LiveOps calendar.

---

## 8. Early success signals

- Qualitative: “Break cảm giác sướng”; nhớ Path identity; muốn clear MoC star. `(assumed)`
- Measurable `(TBD — không bịa)`: D1 tutorial Break completion; % enable Auto by day 7; first pity conversion; MoC attempted rate.

---

Pack: [gdd.md](./gdd.md) · [systems-teardown.md](./systems-teardown.md) · Theory: [game-economics-monetization.md](../../game-design/game-economics-monetization.md)
