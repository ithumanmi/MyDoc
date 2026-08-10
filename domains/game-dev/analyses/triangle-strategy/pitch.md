---
title: "Triangle Strategy — Pitch / one-pager (reconstructed)"
description: "Reconstructed pitch from shipped HD-2D tactical RPG: Convictions, Scales, political SRPG."
updated: "2026-08-10"
canonical: false
tags: [game-design, pitch, tactical-rpg, case-study]
audience: [intermediate, advanced]
related:
  - ./README.md
  - ./gdd.md
  - ./systems-teardown.md
  - ../../game-design/templates/game-pitch-one-pager.md
sensitivity: public
---

# Triangle Strategy — Pitch / one-pager

> [← Pack](./README.md) · Skill: `.cursor/skills/game-design-docs/` · Mode: `pitch`  
> **Loại doc:** Pitch **tái dựng** từ game đã ship (Square Enix / Artdink, HD-2D) — không phải deck nội bộ thật.  
> Claims: `(observed)` từ design lộ thiên · `(assumed)` khi suy từ product.

| Field | Value |
| --- | --- |
| Working title | Triangle Strategy |
| Owner | (reconstructed exercise) |
| Status | `(locked)` as shipped reference · pitch text = teaching artifact |
| Date | 2026-08-10 |
| Audience for this doc | team kickoff / design study — “làm sao pitch một political SRPG” |

---

## 0. Hook (1 câu)

Bạn là lãnh đạo trẻ nhà Wolffort, **cân bằng chiến tranh liên minh trên bàn cờ từng ô** trong khi **mọi lựa chọn đạo đức đẩy vận nước** trên ba Trục Niềm tin — dưới áp lực muối, sắt và phản bội. `(observed)`

---

## 1. Player & occasion

- **Target player:** Fan Fire Emblem / Tactics Ogre / FFT — thích đọc dialogue chính trị, chấp nhận combat chậm, replay route. `(assumed)`
- **Occasion:** Couch / desktop evening sessions; story-heavy blocks, không “một trận Metro”. `(assumed)`
- **Session length target:** ~45–90 phút (1 chapter segment hoặc 1 battle lớn) `(assumed)`

---

## 2. Core loop (1 chuỗi)

`Explore / dialogue → Collect conviction lean → Scales of Conviction (vote) → Deploy squad → Grid battle (height · weather · flanking) → Story branch + character loyalty → Next chapter pressure`

Combat và narrative **cùng một currency niềm tin**: lựa chọn tăng Utility / Morality / Liberty, mở unit và ending path. `(observed)`

---

## 3. USP / role inversion

- **Comps:** Fire Emblem (modern social + map); Tactics Ogre / FFT (politics + grid); Octopath (HD-2D production language). `(observed)`
- **We flip:** Không lấy “avatar warlord + support dating” làm xương sống. Xương sống là **công lý tranh chấp trên hội đồng (Scales)** — player thường *không* độc quyền quyết định; conviction ẩn + vote tạo cảm giác chính trị thật. HD-2D bán fantasy “board game sống” thay vì anime hero expedition. `(inferred)`

---

## 4. Pillars (≤3)

| # | Pillar | Playtestable signal |
| --- | --- | --- |
| 1 | **No clean war** | Sau major Scales choice, người chơi tranh luận “có đúng không” với nhau / trong notes — không có NH đường xanh rõ. `(assumed)` |
| 2 | **Position is the skill** | Battles thắng nhờ cao độ, thời tiết, kẹp flank, Quietuses — không chỉ stat check. `(observed)` |
| 3 | **Belief routes roster** | Khác conviction path → khác character join / story nodes; NG+ có lý do. `(observed)` |

**Anti‑goals:** Open-world padding; gacha live cadence; combat auto “skip story”; moral binary good/evil UI. `(assumed)`

---

## 5. Scope slice (MVP / vertical slice)

*(Nếu greenlight lại / học scope — mirror structure đã ship.)*

- **In:** 1 political vignette (resource dispute) → 1 Scales vote với kết quả thoại phân nhánh → 1 battle dạy height/weather → 1 recruit/lockout do conviction. `(proposed)` as slice design
- **Out:** Full multi-route ending web; all late Quietuses; remaster QoL stack.
- **Content boundary (shipped North Star):** Multi-path campaign trên một lục địa Norzelia (muối/sắt), roster lớn, difficulty modes — không phải live service map. `(observed)`

---

## 6. Business model

- **Model:** Premium (full purchase); later multiplat / enhanced edition — không GaaS. `(observed)`
- **Primary monetization lever:** Upfront sale + edition/DLC adjacent catalog trong hệ Square JRPG. `(assumed)`
- **Non‑goals (ethics):** Không gắn tiến độ câu chuyện với IAP; không battle pass. `(observed)`

---

## 7. Risks & ask

| Risk | Mitigation |
| --- | --- |
| Pace “quá nhiều thoại” mất tactical audience | Chapter clarity; battle frequency; skip/fast-forward UX `(observed)` / `(assumed)` |
| Conviction cảm giác black-box → bất công | Surface lean hints; Scales ceremony làm moment; wiki-friendly but playable blind `(observed)` |
| Bị đọc như “FE clone HD-2D” | Market Scales + politics first; combat pillars in trailer beats `(assumed)` |

**Ask / next decision (exercise):** Greenlight vertical slice “one Scales + one signature battle” trước khi commit full branch graph — hoặc (nghiên cứu) viết GDD module Convictions. Mode tiếp: `gdd`.

---

## 8. Early success signals

- **Qualitative:** Người chơi nhớ *một* quyết định Scales và hậu quả nhân vật; replay “để thấy bên kia”. `(assumed)`
- **Measurable `(TBD — không bịa số ship)`:** % players hoàn thành chapter dạy Scales; % start NG+ / second route; combat abandon mid-battle; average session length vs story:battle ratio. `(proposed)`

---

## Theory footer

[core-loop-mastery.md](../../game-design/core-loop-mastery.md) · [advanced-core-loops.md](../../game-design/advanced-core-loops.md) · [narrative-toolkit.md](../../game-design/narrative-toolkit.md) · Template: [game-pitch-one-pager.md](../../game-design/templates/game-pitch-one-pager.md)  
Pack: [gdd.md](./gdd.md) · [systems-teardown.md](./systems-teardown.md) · [systems-economy.md](./systems-economy.md)
