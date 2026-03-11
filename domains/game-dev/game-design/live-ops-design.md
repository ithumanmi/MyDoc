---
title: "Live Ops Design"
description: "Event cadence, limited-time content, FOMO ethics cho Live Service/GaaS."
tags:
  - game-design
  - live-ops
updated: 2026-03-11
---

# 📅 Live Ops Design

## 1) Event Cadence
- Macro cadence: Seasonal (3 tháng), Major event (monthly), Minor event (weekly), Micro (daily quests).
- Cadence matrix: align với content production, marketing beat.
- Buffer sprint dành cho QA/rollback.

## 2) Event Types
- **Score Chase**: leaderboard, PvP tournament.
- **Collection**: limited currency, shop rotation.
- **Narrative**: story event, VO scenes.
- **Co-op**: guild raid, community goal.
- Mix: Tạo event pack (Mission + Store + Cosmetics).

## 3) Limited-Time Content & FOMO Ethics
- Dùng thông báo rõ ràng (timer, preview reward) để tránh gây stress.
- Re-run policy: cho phép rerun sau X tháng để tránh “forever miss”.
- Alternate acquisition: token craft sau khi event kết thúc.
- Consider accessibility: timezone-friendly, offline catch-up.

## 4) Live Ops Pipeline
1. Ideation (theme + KPI).
2. Spec (design doc, economy impact, art requirements).
3. Build branch + automated tests.
4. Event config + localization.
5. Dry run (internal) → soft launch (region nhỏ) → global go-live.
6. Post-mortem + telemetry review.

## 5) KPI & Telemetry
- Track: Participation %, conversion, ARPDAU uplift, retention delta.
- Real-time dashboard: concurrency, server load, monetization.
- Alerting: threshold cho bug (mission không ghi nhận, reward fail).

## 6) Tooling & Automation
- Live config server (Remote Config) để bật/tắt event.
- Template script: generate calendar, sync với marketing.
- Localization pipeline: string bundle + VO scheduling.
- Use RenderDoc/CI screenshot automation cho asset QA (lệch hue, UI glitch).

## ✅ Apply it
- [ ] Lập event cadence chart + KPI gắn với business goal.
- [ ] Thiết kế event pack (mission, store, cosmetics) và policy rerun.
- [ ] Documentation pipeline (spec → build → dry run → post-mortem).
- [ ] Thiết lập dashboard + alerting cho Live Ops.
- [ ] Rà soát FOMO ethics: thông báo minh bạch, catch-up path.