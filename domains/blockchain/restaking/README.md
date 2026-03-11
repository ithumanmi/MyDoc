---
title: "Restaking & EigenLayer"
description: "EigenLayer, AVS, risk isolation và checklist tích hợp."
tags:
  - restaking
  - eigenlayer
  - ethereum
updated: 2026-03-11
---

# ♻️ Restaking & AVS

> **Goal:** Tận dụng ETH đã stake để cung cấp bảo mật cho dịch vụ mới (AVS) thông qua EigenLayer.
> **Deliverables:** Restaking architecture, AVS onboarding checklist, slashing/risk analysis.
> **Success Criteria:** Yield tăng thêm nhưng vẫn kiểm soát risk, AVS có bảo mật đủ mạnh, event slashing rõ ràng.

## 1. Overview

- **Restaking:** dùng LST (stETH, rETH, cbETH) hoặc native ETH stake lại cho AVS (Actively Validated Services).
- **EigenLayer:** middleware cho phép operator opt-in bảo vệ dịch vụ (oracle, DA, bridges...).
- **AVS:** dịch vụ yêu cầu trust (Oracle, DA layer, shared sequencer) → thuê bảo mật từ restakers.

## 2. Components

| Role | Description |
| --- | --- |
| Restaker | Người khóa ETH/LST vào EigenLayer, delegate cho operator |
| Operator | Chạy AVS client, ký messages, chịu slashing |
| AVS | Dịch vụ (EigenDA, Espresso sequencer, oracle...) |

## 3. Yield & Incentive

- Base staking reward + EigenLayer reward (AVS trả bằng token/fee).
- Incentive token: EigenLayer points, AVS token airdrop.
- Need to price risk vs reward.

## 4. Risk

1. **Slashing Multiplication:** Nếu AVS slash do lỗi, mất cả stake gốc.
2. **Smart Contract:** EigenLayer contracts upgradeable.
3. **Coordination:** Operator offline → slash.
4. **Liquidity:** Unlock period, withdrawal queue.

## 5. AVS Examples

- **EigenDA:** Data availability layer.
- **Restaked rollup sequencer (Espresso).**
- **Oracle network** (e oracle).

## 6. Operator Flow

1. **Register:** run EigenLayer operator, set metadata.
2. **Accept Delegation:** restakers delegate stake.
3. **Opt-in AVS:** run AVS-specific client, sign contract.
4. **Monitoring:** uptime, slash alert.

## 7. Checklist

- [ ] Xác định stake asset (ETH vs LST) và risk tolerance.
- [ ] Đánh giá AVS: client maturity, slashing condition, reward.
- [ ] Thiết lập operator infra (keys, monitoring, redundancy).
- [ ] Theo dõi EigenLayer upgrade & governance.
- [ ] Kế hoạch rút stake khi có sự cố (withdraw queue, partial exit).