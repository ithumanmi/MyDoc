---
title: "Restaking & EigenLayer"
description: "AVS onboarding, operator flow, reward structure và risk isolation."
tags:
  - restaking
  - eigenlayer
  - avs
updated: 2026-03-11
---

# ♻️ Restaking & EigenLayer

## 1. Concepts

- **Restaking:** reuse staked ETH (native hoặc LST) làm collateral bảo vệ dịch vụ khác (AVS).
- **AVS (Actively Validated Service):** oracle, DA layer, bridge, sequencing service.
- **Operators:** entity run infrastructure, opt-in từng AVS, chịu slashing nếu AVS rules violated.

## 2. Flow

1. Depositor stake ETH hoặc LST → nhận EigenPod/EigenPodManager vị trí.
2. Ủy quyền cho operator (EigenLayer marketplace).
3. Operator opt-in AVS, chạy client và ký nhiệm vụ AVS.
4. AVS trả reward (token, fees, points) → chia lại cho depositor/operator.

## 3. AVS Onboarding Checklist

- [ ] Security model (fault proof, challenge, slashing conditions).
- [ ] Reward schedule (token emission, fee split, points → retroactive?).
- [ ] Client requirements (hardware, bandwidth, custom software).
- [ ] Compatibility (native ETH vs LST supported list).
- [ ] Exit/unstake rules (cooldown, penalty).

## 4. Operator Considerations

- Run dedicated hardware hoặc partner với operator network.
- Monitoring AVS-specific metrics (latency, signed tasks).
- Multi-AVS risk: correlation → slash cascade.
- Insurance: tự quỹ hoặc marketplace (e.g., Nexus offering?).

## 5. Reward Stack

- Base staking reward (Beacon chain).
- LST incentives (Curve bribe, liquidity mining).
- EigenLayer points (future airdrop) + AVS token reward.
- Need to weigh vs additional slashing exposure.

## 6. Risk

- **Smart contract risk:** EigenLayer contracts mới, audit ongoing.
- **AVS failure:** misbehavior → slash restaked ETH → contagion.
- **Centralization:** few operators dominate marketplace.

## 7. Checklist

- [ ] Đánh giá AVS risk/reward trước khi opt-in.
- [ ] Duy trì monitoring + slash protection cho EigenLayer keys.
- [ ] Đa dạng operator hoặc dùng DVT để giảm single point.
- [ ] Theo dõi chính sách unlock/withdraw EigenLayer.