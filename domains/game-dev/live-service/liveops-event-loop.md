---
title: "LiveOps Event Loop Playbook"
description: "Quy trình thiết kế, launch, vận hành và retro sự kiện LiveOps 2026."
tags:
  - liveops
  - live-service
  - playbook
updated: 2026-03-23
---

# 🎯 LiveOps Event Loop Playbook

> **Goal:** Sản xuất sự kiện LiveOps mà không phá core loop, có telemtry rõ ràng và rollback được trong 15 phút.
> **Deliverables:** Event spec (`EventSpec_vX.md`), backend config JSON, telemetry dashboard, post-event retro.
> **Success Criteria:**
> - Engagement uplift rõ (Participation rate > 55% DAU target).
> - No incident > Sev2, rollback plan chạy được.
> - Economy impact nằm trong guardrail (currency inflation < +8%).

## 1. Event Lifecycle

| Phase | Owner | Key Actions |
|-------|-------|-------------|
| Ideation | Product/Design | Define objective (Retention, Monetization, Feature adoption). Draft success metric. |
| Spec | LiveOps + Backend | Create EventSpec (timeline, missions, reward, telemetry). Align with Battle Pass. |
| Implementation | Engineering | Build server config, client scene, feature flags, QA plan. |
| Launch Prep | Ops | Load test, QA, marketing assets, support macros. |
| Live Monitoring | LiveOps + On-call | Watch dashboard, respond to incidents, run micro-events (double XP). |
| Post-event | Data + Product | Retro metrics, economy impact, player sentiment, action items |

## 2. EventSpec Template

```
Event Name: Lunar Siege 2026
Objective: Re-engage midcore players, upsell premium BP.
Timeline: Preload (Mar 25) → Active (Mar 28 - Apr 4) → Cooldown (Apr 4-6).
Core Loop: 3-phase co-op boss + leaderboard.
Rewards: Tokens → Shop (cosmetic + currency sink).
Telemetry: participation_rate, avg_runs_per_user, token_spent, ARPDAU delta, error rate.
Kill-switch: feature flag `event_lunar_siege_pct`, default 0.
Rollback plan: disable flag, run script `refund_tokens`, send inbox apology.
```

## 3. Config & Backend Architecture
- Store event config in `EventConfig_vX.json` (Remote Config/UGS, S3 CDN).
- Key fields: `event_id`, `start_ts`, `end_ts`, `leaderboard_id`, `mission_list`, `reward_table`, `failsafe_drop`.
- Use **control plane vs data plane** separation: control plane handles scheduling & config, data plane handles match logic.
- Build `EventStateMachine` service to emit webhook (Scheduled → Preload → Active → Cooldown → Archived).

## 4. Telemetry & Dashboards
- Metrics to track hourly:
  - `participation_rate = EventPlayers / DAU`
  - `avg_runs_per_user`
  - `shop_conversion`
  - `currency_delta`
  - `error_rate`, `matchmaking_latency`
- Dashboard sections:
  - **Engagement**: participation, time spent.
  - **Economy**: tokens earned vs spent.
  - **Reliability**: API error %, server CPU.
  - **Revenue**: ARPDAU, premium conversions.
- Guardrail alerts: D1 retention drop >3%, ARPDAU drop >2%, error rate >0.5% -> auto flag to on-call.

## 5. QA & Load Test
- **Simulation:** run synthetic users (Bots) hitting event endpoints (50k CCU) -> measure scaling.
- **Soak test:** 48h to detect memory leak.
- **Failover drill:** kill pods / region to ensure reroute.
- **Client QA:** multi-device, localization, accessibility.
- **Checklists** include: reward grant, progression, leaderboard snapshot, kill-switch.

## 6. Ops Runbook
- Document roles: Incident Commander, Economy lead, Backend, CS.
- Create pre-launch checklist (asset upload, config publish, marketing go-live, feature flag set to 5%).
- On-call schedule + Slack channel for war room.
- Pre-bake compensation packages (hard currency, BP tokens) for rollback scenario.
- Define stop-loss metrics (if participation < target by day 2 -> trigger double XP mission; if error > threshold -> disable event).

## 7. Postmortem / Retro
- Within 24h event end: gather metrics vs target, economy impact, incidents.
- Template sections: objective, results, issues, player sentiment, action items.
- Link to [Retro Template](../production/metrics/retro-template.md).
- Add insights to `LiveOps Wiki` for knowledge reuse.

## 8. Tooling Suggestions
- Build Event Config Editor (Web/Unity) for designers to adjust drop table without touching JSON manually.
- Provide script `event_diff.py` to compare config versions and highlight risk.
- Automation: CI test verifying event config schema, reward mapping, translation coverage.

## 9. Reference
- [Live Service / GaaS Hub](./README.md)
- [Economy Guardrail](./README.md#3-economy--pacing)
- [Unity Impact Metrics](../production/metrics/unity-impact-metrics.md)