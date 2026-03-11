---
title: "Liquid Staking DeFi"
description: "LST/LRT DeFi strategies, leverage loops, risk controls."
tags:
  - defi
  - liquid-staking
  - leverage
updated: 2026-03-11
---

# 🌊 Liquid Staking DeFi

## 1. Landscape

- **LST:** stETH, rETH, cbETH.
- **LRT:** EigenLayer restaking tokens (ezETH, rsETH).
- **Restaking points + DeFi yield fusion.**

## 2. Leverage Loops

1. Deposit stETH into lending protocol.
2. Borrow ETH.
3. Swap to stETH and restake.
4. Repeat until safe health factor.

## 3. Risks

- stETH depeg vs ETH.
- Liquidation cascades.
- Restaking slashing events.

## 4. Strategies

- Delta-neutral: hedge via perps.
- Points farming: track EigenLayer/LRT incentives.
- Diversify across LST issuers.

## 5. Checklist

- [ ] Health factor monitoring script.
- [ ] Depeg alert (stETH/ETH price).
- [ ] Restaking slash insurance (ether.fi cover, Nexus Mutual).
- [ ] Exit plan when APR compresses.

## 🧪 Lab: Leverage Loop Simulation

**Goal:** set up leverage loop + monitor health.

1. Deploy local fork (Anvil) với Aave v3 + stETH oracle.
2. Script deposit stETH, borrow ETH, loop 3x.
3. Add monitoring bot (Foundry/Hardhat) to watch health factor.
4. Simulate price shock (-5% stETH) và observe liquidations.

**Deliverables:** script repo, monitoring dashboard screenshots, risk notes.