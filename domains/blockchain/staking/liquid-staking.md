---
title: "Liquid Staking Ecosystem"
description: "Lido, Rocket Pool, Frax, tích hợp DeFi và quản trị rủi ro."
tags:
  - staking
  - liquid-staking
  - ethereum
updated: 2026-03-11
---

# 🌊 Liquid Staking Ecosystem

## 1. Concept

- Stake ETH/SOL... nhận token đại diện (LST) có thể giao dịch/DeFi.
- APR = base staking reward - protocol fee.
- Peg stability phụ thuộc thanh khoản LST/ETH.

## 2. Protocol Comparison

| Protocol | Model | Fee | Notes |
| --- | --- | --- | --- |
| **Lido (stETH)** | Curated node operator | 10% | Largest TVL, DAO governance risk |
| **Rocket Pool (rETH)** | Permissionless minipool (8 ETH + RPL collateral) | 15% commission | Decentralized operator, slower liquidity |
| **Frax (sfrxETH/frxETH)** | Dual token (frxETH pegged, sfrxETH yield) | 10% | Use Curve pools, incentives |
| **Coinbase cbETH** | Custodial exchange | Variable | Institutional friendly, centralized |
| **Ether.fi / StakeWise v3** | Liquid restaking, operator NFTs | TBD | Modular operator marketplace |

## 3. LSTfi Use Cases

- Lending collateral (Aave stETH, Morpho, Spark).
- LP pair (stETH/ETH Curve) to maintain peg.
- Leverage staking (Loop stETH/ETH on Aave → borrow ETH → restake).
- Restaking on EigenLayer (if LST supported).

## 4. Risk Factors

- **Depeg:** khi stETH liquidity thấp hoặc market panic.
- **Smart contract risk:** bug trong staking contracts.
- **Operator centralization:** curated set big share.
- **Leverage loop risk:** cascading liquidations.

## 5. Due Diligence Checklist

- [ ] Fee structure, DAO control, insurance fund.
- [ ] TVL distribution (whales vs retail).
- [ ] Liquidity depth trên Curve/Balancer.
- [ ] Integrations (Aave, Maker, EigenLayer ready?).
- [ ] Governance token alignment (LDO, RPL incentives).