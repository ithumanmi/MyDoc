---
title: "Liquid Staking"
description: "Lido, Rocket Pool, cbETH, risk/architecture/checklist."
tags:
  - staking
  - ethereum
  - defi
updated: 2026-03-11
---

# 💧 Liquid Staking (LST)

> **Goal:** Tối ưu vốn khi staking (ETH, SOL...) nhưng vẫn thanh khoản.
> **Deliverables:** Protocol comparison, risk matrix, integration checklist.
> **Success Criteria:** APR ~ staking yield - fee, peg ổn định, không slash hàng loạt.

## 1. Concept

- Lock coin (ETH) → nhận receipt token (stETH, rETH, cbETH).
- Receipt có thể dùng DeFi (lending, LP) nhưng đại diện staked ETH.
- Yield = base staking reward - protocol fee.

## 2. Main Protocols

| Protocol | Model | Fee | Key Points |
| --- | --- | --- | --- |
| **Lido (stETH)** | Liquid staking pool, node operator set | 10% fee (split DAO/NOP) | Lớn nhất (~30% ETH staked), risk centralization |
| **Rocket Pool (rETH)** | Permissionless mini pool 8ETH + 24ETH from stakers | 15% commission + RPL staking | Decentralized node operator, higher collateral |
| **Coinbase cbETH** | Centralized exchange | Coinbase fee | Custodial, easy for institutions |
| **Frax ETH, StakeWise V3** | LSD + modular pool | Variable | Experiment decentralization |

## 3. Risk

1. **Peg Deviation:** withdrawal queues, liquidity; watch Curve stETH/ETH.
2. **Smart Contract:** multi-sig, upgradeable proxies.
3. **Validator Risk:** slash, correlated client bug.
4. **Centralization:** Lido dominance → governance capture.

## 4. Integration Patterns

- Accept LST as collateral (Aave v3, Maker sDAI).
- Use `rebasing` vs `non-rebasing` tokens (stETH rebasing, rETH vs wstETH).
- Treasuries hold LST for yield.
- Need price oracle for LST/ETH ratio.

## 5. Monitoring

- **Metrics:** TVL, APR, share of staked ETH, peg price.
- **Risk alert:** withdrawal queue length, validator slash event, DAO votes.

## 6. Checklist

- [ ] Chọn LST phù hợp (stETH/rETH/cbETH) theo risk appetite.
- [ ] Theo dõi peg & liquidity pool depth (Curve, Balancer).
- [ ] Kiểm tra smart contract audit, multi-sig control.
- [ ] Định nghĩa strategy cho rebasing vs wrapped token (wstETH) nếu tích hợp DeFi.
- [ ] Chuẩn bị plan khi Shanghai/withdrawal event hoặc slashing hàng loạt.