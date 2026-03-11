---
title: "Player Psychology"
description: "Flow state, Self-Determination Theory (SDT), loss aversion và ứng dụng game design."
tags:
  - game-design
  - psychology
updated: 2026-03-11
---

# 🧠 Player Psychology

## 1) Flow State
- **Điều kiện**: (1) Mục tiêu rõ ràng, (2) Feedback tức thời, (3) Thử thách cân bằng với kỹ năng.
- **Tuning**: dùng matchmaking, difficulty scaling, hoặc adaptive AI để giữ người chơi ở “channel” flow.
- **Flow blockers**: UI clutter, grind vô nghĩa, latency cao.
- Checklist: mỗi loop phải trả lời “mục tiêu gì?”, “feedback nào?”, “thử thách tăng ra sao?”.

## 2) Self-Determination Theory (SDT)
- **Autonomy**: cho phép lựa chọn meaningful (build path, loadout, narrative choice).
- **Competence**: cung cấp mastery curve + scaffolding (tutorial → advanced loop).
- **Relatedness**: social layer (guild, co-op, asynchronous interaction).
- Map SDT vào features: ví dụ Battle Pass (autonomy = pick track, competence = missions, relatedness = party boost).

## 3) Motivation Mix
- Intrinsic: discovery, mastery, storytelling.
- Extrinsic: rewards, streak, achievements.
- Hybrid model: align extrinsic reward để boost intrinsic (ví dụ cosmetic unlocks reinforce identity).
- Beware burnout: overjustification effect khi extrinsic lấn át intrinsic.

## 4) Loss Aversion & Prospect Theory
- Người chơi sợ mất hơn thích được → design retention hooks (daily streak) nhưng cần cân bằng đạo đức.
- Dùng framing: “Giữ bonus” vs “Nhận bonus mới”.
- Soft fail state (lose progress) vs hard loss (mất item) → calibrate friction.
- Monetization: cho phép “insurance” hoặc comeback mechanic để giảm frustration.

## 5) Emotional Loop Mapping
- Mapping cảm xúc theo session: onboarding (curiosity) → mid-session (challenge) → end-session (satisfaction/longing).
- Tool: Journey map (moment-to-moment) + Emotion KPI (fun, frustration, surprise).
- Telemetry: log rage quit (Alt+F4), fail streak, churn reason.

## 6) Practical Framework
1. Chân dung player archetype (Achiever, Socializer, etc.).
2. Ánh xạ SDT needs → feature list.
3. Flow tuning: build difficulty ramp + gating.
4. Loss aversion test: A/B messaging “Bạn sắp mất buff” vs “Nhận buff nếu đăng nhập”.
5. Review onboarding > D7 progression > D30 meta để tránh psychological fatigue.

## ✅ Apply it
- [ ] Xây Persona + SDT canvas cho dự án.
- [ ] Đảm bảo mỗi loop có mục tiêu/feedback/thử thách rõ.
- [ ] Lập bảng mapping feature ↔ emotional payoff.
- [ ] Chạy playtest/telemetry track session emotion KPI.
- [ ] Audit retention hook để tránh lạm dụng loss aversion.