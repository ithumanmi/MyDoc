---
title: "Uniswap v4 Deep Dive"
description: "Hooks, custom AMM logic, singleton architecture."
tags:
  - defi
  - amm
  - uniswap
updated: 2026-03-11
---

# 🌀 Uniswap v4

## 1. Architecture

- **Singleton contract:** all pools in one contract.
- **Hooks:** contracts executed before/after swaps/liquidity updates.
- **Custom LP logic:** dynamic fees, time-weighted positions.

## 2. Hooks Explained

- `beforeInitialize`, `afterInitialize`.
- `beforeAddLiquidity`, `afterAddLiquidity`.
- Use cases: fee switch, oracle updates, MEV-resistant logic.

## 3. Building Custom Hooks

```solidity
contract AutoFeeHook is IHook {
  function beforeSwap(...) external override returns (bytes4) {
    // adjust fee based on volatility
    return IHook.beforeSwap.selector;
  }
}
```

- Deploy hook contract + register in pool parameters.

## 4. Risk & Considerations

- Hook security critical (reentrancy, griefing).
- Gas overhead vs benefits.
- Governance to approve hook lists.

## 5. Checklist

- [ ] Define hook purpose (fee, risk management, automation).
- [ ] Security review for hook contract.
- [ ] Backtest hook logic on historical data.
- [ ] Monitor pool metrics (fee APY, volume).

## 🧪 Lab: Build a Volatility Hook

**Goal:** viết hook điều chỉnh fee theo volatility.

1. Fork Uniswap v4 repo + enable hook dev tooling.
2. Implement hook đọc TWAP để set fee tiers.
3. Deploy hook + pool config trên testnet.
4. Run Foundry tests + simulate swaps.

**Deliverables:** hook contract repo, deployment params, test report.