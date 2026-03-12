---
title: "Live Service / GaaS"
description: "Season/battle pass, events architecture, economy pacing, live-ops safeguards."
tags:
  - live-service
  - gaas
  - liveops
  - game-dev
updated: 2026-03-11
---

# ⏳ Live Service / GaaS

> **Goal:** Vận hành season/battle pass, sự kiện lặp và nền kinh tế bền vững mà không phá cân bằng hay gây burnout.
> **Deliverables:** Season playbook (cadence, XP curve), event config spec (backend flags, reward tables), economy sink/source map, LiveOps runbook + telemetry dashboard.
> **Success Criteria:** Completion rate battle pass >70% (free track), ARPDAU không giảm khi rollout sự kiện, không có lạm phát currency (>10% tuần), rollback/killswitch <15 phút.
> **Focus Areas:** Season pacing (catch-up, pity), backend-driven event architecture, economy guardrail, LiveOps safeguards/telemetry.

## 1) Season & Battle Pass
- Track XP/Stars; free vs premium track; pity/guarantee.
- Duration & cadence: 4-8 tuần; buffer 1 tuần cho nội dung lỗi.
- Backfill/skip mechanic; catch-up quest; limit FOMO quá mức.
- Progression fairness: daily/weekly quest load nhẹ (<=20-30 phút); soft cap cho grind loop; không gate progression bằng pay-only node.
- Retroactive credit: nếu người chơi mua premium giữa mùa, unlock retroactive reward hợp lý.
- Expire policy: rõ ràng về grace period claim; avoid surprise wipe.
- **XP pacing toolkit:** mô phỏng XP curve bằng spreadsheet + script (input: daily minutes, quest completion rate) để đảm bảo 70% người chơi đạt max trước tuần cuối. Thêm `Catch-up Tokens` (double XP weekend, mission skip) và `Bonus banked XP` cho người bỏ lỡ.
- **Battle pass monetization:** phân tách free/premium/premium+ track; hiển thị ARPDAU impact vs retention. Thiết lập live config (`SeasonConfig_vX.json`) để chỉnh XP requirement, reward ID, shop rotation mà không cần patch.
- **Unity:** lưu progression server-side; dùng Addressables để update reward table; ScriptableObject chỉ làm config client. Dùng Cloud Save/UGS (hoặc backend riêng) để tránh gian lận; verify XP trên server.

## 2) Events Architecture
- Time-limited event server flags; config từ backend.
- Event types: score chase, co-op boss, rerun shop; rotation rõ.
- Synergy: event drop hỗ trợ goal của season/battle pass.
- Config-first: toàn bộ tham số (rewards, drop table, shop price, boss HP) ở backend; không hardcode client.
- Isolation: event logic có thể tắt qua kill-switch; không ảnh hưởng core loop nếu rollback.
- Scalability: tách matchmaker/leaderboard shard theo event; rate-limit để tránh DDOS tự gây ra.
- **Event orchestration:** xây `EventStateMachine` (Scheduled → Preload → Active → Cooldown → Archived) với webhook cho Ops + marketing. Logging per phase giúp xác định lỗi.
- **Battle pass tie-in:** map event reward → BP XP/Token, cho phép mission `Play Event X 3 lần` để boost engagement nhưng không bắt buộc.
- **Live config example:** `event_id`, `start_ts`, `end_ts`, `mission_list`, `reward_table`, `failsafe_drop`. Mọi thứ publish qua CDN/Remote Config với checksum + signature.
- **Unity:** Remote Config/UGS cho tham số; Addressables cho asset event; Scene additive cho event hub; tách netcode event (Netcode for GameObjects/Photon/Mirror) khỏi core scene để rollback nhanh.

## 3) Economy & Pacing
- Sink/Source map; kiểm soát lạm phát; soft cap/day.
- Reward fairness: không ép paywall; cap RNG bad-luck.
- Progress tempo: daily/weekly quest load nhẹ; avoid chore list.
- Currency hygiene: định nghĩa hard/soft currency, cap tồn kho; lịch reset (daily/weekly/seasonal) rõ.
- Store & pricing: anchor price theo region, thuế, platform fee; bundle phải minh bạch tỉ lệ RNG.
- Anti-exploit: server validate reward, chống macro/autoplay farm event.
- **Telemetry:** real-time dashboard `CurrencyInflation = (TotalCurrencyWeek / ActiveUsers)`; alert nếu >10% tuần. Dùng quantile (P95) thay vì average để bắt whale abuse.
- **Unity:** tất cả grant/reward validate server; client chỉ hiển thị. Dùng Cloud Code/Functions để tính reward; lưu inventory trong Cloud Save/DB. UI shop dùng Addressables để cập nhật giá/rules mà không cần rebuild.

## 4) Safeguards & Ops
- Kill-switch cho feature; rollout theo %; A/B.
- Telemetry: retention D1/D7/D30, revenue ARPDAU, event participation.
- Live incident playbook: rollback, comp package, comms template.
- Experimentation guardrail: define metric stop-loss (ví dụ -3% D1, -2% ARPDAU) để auto-stop A/B khi xấu.
- Moderation: nếu có UGC/chat trong event, kiểm soát report/ban; rate-limit spam.
- Runbook: checklist deployment, pre/post-metrics review, on-call schedule cho event launch.
- **Battle pass/event operations board:** Kanban (Prep → RC → Live → Postmortem) + owner. Checklist: asset patch, telemetry validation, economy check, CS macros.
- **Rollback tooling:** snapshot economy/inventory trước sự kiện (DB backup + diff). Có script `grant_compensation` và `disable_event` chạy <15 phút.
- **Unity:** dùng Analytics/UGS hoặc pipeline custom để log event với player/session ID; A/B qua Remote Config + experiment targeting; kill-switch qua feature flag server-side. Dùng Cloud Diagnostics/Crashlytics để theo dõi error spike khi rollout.

## ✅ Apply it
- [ ] Thiết kế battle pass với pity/catch-up + buffer tuần.
- [ ] Xây event config server-side + rotation rõ ràng.
- [ ] Vẽ sink/source map và cap daily để tránh lạm phát.
- [ ] Thêm kill-switch/rollout % và A/B với guardrail metric (stop-loss).
- [ ] Theo dõi D1/D7/D30, ARPDAU, event participation, và kinh tế (sink/source) để điều chỉnh.
- [ ] Thiết lập retroactive premium claim và grace period khi hết season.
- [ ] Unity: dùng Remote Config/Cloud Save/Analytics; Addressables cho asset event; Scene additive/feature flag để rollback nhanh.

## 🔗 Cross-reference
- [Unity Impact Metrics](../metrics/unity-impact-metrics.md)
- [Playtest Framework](../game-design/playtest-framework.md)