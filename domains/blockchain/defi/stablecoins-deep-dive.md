---
title: "Stablecoins Deep Dive"
description: "CDP, algorithmic, fractional models, risk assessment."
tags:
  - defi
  - stablecoins
  - risk
updated: 2026-03-11
---

# ⚖️ Stablecoins Deep Dive

## 1. Models

- **CDP-backed:** MakerDAO (DAI), Liquity (LUSD).
- **Custodial fiat:** USDC, USDT.
- **Algorithmic:** FRAX (fractional), Terra (failed UST).

## 2. CDP Mechanics

- Lock collateral (ETH, stETH) → mint stablecoin.
- Stability fee, liquidation ratio.
- Peg stability modules (PSM) for swap at $1.

## 3. Algorithmic/Fractional

- Supply adjusts via mint/burn incentives.
- Frax: collateral ratio + FXS seigniorage.
- Risk: bank run if confidence drops.

## 4. Risk Analysis

- Collateral volatility.
- Liquidity + redemption depth.
- Governance/blacklist risk (USDC freeze).

## 5. Checklist

- [ ] Understand backing (on-chain collateral, fiat reserves).
- [ ] Track collateral ratio + oracle sources.
- [ ] Evaluate redemption process + fees.
- [ ] Stress test scenario (peg deviation, regulatory action).

## 🧪 Lab: Peg Stress Test

**Goal:** mô phỏng stress scenario cho stablecoin (DAI/FRAX).

1. Fork Maker/Frax repo + run local simulation.
2. Shock collateral price (-20%) và đo CR, surplus buffer.
3. Evaluate PSM capacity + redemption queue.
4. Viết report đề xuất hành động (raise SF, adjust CR).

**Deliverables:** simulation notebook, charts, policy recommendation memo.