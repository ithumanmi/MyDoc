---
title: "Lending Protocols"
description: "Aave v3, Morpho, isolated pools, risk parameters."
tags:
  - defi
  - lending
  - aave
updated: 2026-03-11
---

# 💸 Lending Protocols

## 1. Aave v3 Highlights

- **Isolation mode:** onboard long-tail assets with capped debt.
- **Efficiency mode (eMode):** higher LTV for correlated assets.
- **Portal:** cross-chain liquidity via CCIP.

## 2. Morpho Architecture

- Peer-to-peer matching on top of Compound/Aave.
- Optimizes rates for suppliers/borrowers.
- Morpho Blue: permissionless isolated vaults with oracle selection.

## 3. Risk Parameters

- LTV, liquidation threshold, reserve factor.
- Oracle source (Chainlink, Pyth).
- Collateral factor per asset.

## 4. Isolated Pools Strategy

- Create custom vault for specific collateral pair.
- Set curator to manage risk (oracle, IRM).
- Useful for RWA, LST, niche tokens.

## 5. Checklist

- [ ] Define collateral asset + oracle source.
- [ ] Choose isolation vs shared pool.
- [ ] Configure LTV & liquidation incentives.
- [ ] Simulate stress scenarios (price drop, oracle failure).

## 🧪 Lab: Launch an Isolated Vault

**Goal:** tạo pool isolated cho tài sản mới.

1. Fork Morpho Blue/Aave deployment scripts.
2. Chọn collateral (VD: wstETH) + oracle feed.
3. Set parameters (LTV, LT, IRM) và deploy vault testnet.
4. Run liquidation simulation + monitor HF dashboards.

**Deliverables:** config file, deployment tx, risk report.