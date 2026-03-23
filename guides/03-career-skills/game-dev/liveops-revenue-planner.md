---
title: "LiveOps Revenue Planner"
description: "Framework 90 ngày để align retention, content cadence và doanh thu cho mobile/PC live service."
tags:
  - liveops
  - monetization
  - planning
updated: 2026-03-23
---

# 📈 LiveOps Revenue Planner (90D Cycle)

> **Goal:** Lập kế hoạch LiveOps 90 ngày đảm bảo engagement, economy guardrail và doanh thu target.
> **Deliverables:** LiveOps calendar, KPI sheet, economy guardrail dashboard, retro doc.

## 1. Inputs cần chuẩn bị
- KPIs hiện tại: DAU, D1/D7 retention, ARPDAU, payer %, whale %, churn.
- Content inventory: battle pass tiers, cosmetic backlog, events.
- Tech constraints: feature flag, build cadence, server capacity.
- Marketing beats: UA campaigns, store featuring, collab.

## 2. Planning cadence

| Phase | Week | Output |
|-------|------|--------|
| Strategy Sync | Week -4 | Objectives, revenue target, guardrails |
| Content Align | Week -3 | Event themes, rewards, art brief |
| Economy Modeling | Week -2 | Currency sinks, pricing, LTV forecast |
| Finalization | Week -1 | Publish calendar, lock config |
| Execution | Week 0-12 | Launch + monitor |
| Retro | Week 13 | KPI review, learnings |

## 3. KPI Model Template

| Metric | Target | Actual | Delta |
|--------|--------|--------|-------|
| DAU | 500k | 520k | +4% |
| Participation rate | 55% | 48% | -7% |
| ARPDAU | $0.35 | $0.37 | +0.02 |
| Payer % | 2.5% | 2.8% | +0.3% |
| Currency inflation | <+8% | +6% | ✅ |

**Formula:** `Revenue = DAU * ARPDAU`. Break ARPDAU = payer% * ARPPU + ad revenue per DAU.

## 4. Calendar layout (sample)

| Week | Beat | Objective | Reward | Notes |
|------|------|-----------|--------|-------|
| 1 | Battle Pass Season 5 | Retention, monetization | Cosmetics, hard currency | Feature flag rollout 10% → 100% |
| 3 | Mini Event “Lunar Siege” | Midcore engagement | Token shop | Sync marketing x influencer |
| 6 | Double XP Weekend | Reactivate churned | XP boost | Trigger if D7 drop >3% |
| 8 | Collab Drop | Monetization spike | Limited skin bundle | Bundle price $19.99 |
| 11 | Economy Sink Event | Balance soft currency | Auction house | Guardrail: inflation <8% |

## 5. Economy Guardrails
- Hard currency inflation < +8% per season
- Token sink ratio ≥ 0.9 (spent/earned)
- Battle Pass completion target 60%
- Gacha pity protection < 120 pulls
- Whale spend % < 35% total revenue (diversify payer base)

## 6. Telemetry Dashboard (Notion/Tableau)
- Engagement: DAU, participation, session length
- Monetization: Revenue, payer %, ARPPU, top SKU
- Economy: Currency balances, sink/source ratio
- Reliability: Crash rate, error rate, queue length

Set alerts (PagerDuty/Slack): error >0.5%, revenue -10% day/day, whale churn.

## 7. Retro Template
1. **Goal vs Result** (KPI table)
2. **What worked:** e.g. “Token shop drove +20% ARPPU”
3. **Issues:** e.g. “Server latency >200ms in SEA”
4. **Player Sentiment:** CS ticket trends, social listening.
5. **Action Items:** Owner + deadline.
6. **Experiment Backlog:** ideas ranked by ICE (Impact, Confidence, Effort).

## 8. Tooling
- Spreadsheet model (Google Sheets) linkable to BI.
- JIRA/Linear for event tasks.
- Remote config system (UGS, PlayFab) with versioning.
- Slack command `/event-status` pull metrics.

## 9. Checklist
- [ ] Objectives & KPIs defined
- [ ] Calendar 90 ngày approved
- [ ] Economy simulation run (base/optimistic/pessimistic)
- [ ] LiveOps config reviewed (QA, rollback plan)
- [ ] Dashboards + alerting ready
- [ ] Retro scheduled (Week 13)

## 🔗 References
- [LiveOps Event Loop Playbook](../../../domains/game-dev/live-service/liveops-event-loop.md)
- [Mobile Monetization Traps](./mobile-monetization-traps.md)
- [Publisher Financial Model](./publisher-financial-model.md)