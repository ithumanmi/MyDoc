---
title: "MEV Strategies & Bots"
description: "Arbitrage, liquidation, cross-chain MEV và tooling."
tags:
  - mev
  - bot
  - arbitrage
updated: 2026-03-11
---

# 🤖 MEV Strategies & Bots

## 1. Arbitrage Bot

- Monitor price diff giữa DEX (Uniswap v3, Curve) hoặc CEX vs DEX.
- Simulation: `eth_call` với state override, ensure profit > gas.
- Bundle submission: Flashbots 

```python
bundle = [tx_buy, tx_sell]
flashbots.send_bundle(bundle, target_block)
```

## 2. Liquidation Bot

- Watch lending protocol (Aave, Compound) health factor.
- Khi HF < 1, call `liquidateBorrow`.
- Use Keeper network (Gelato) hoặc run bot riêng.
- Optimize gas: use `flashLoan` để trả nợ rồi nhận collateral.

## 3. Cross-chain MEV

- Monitor bridge queue (LayerZero, Wormhole) → arbitrage latency.
- Risks: need capital trên nhiều chain, bridging delay.

## 4. Tools

- **Searchers:** `mev-share`, `suave`, mev-inspect.
- **Sim engines:** Tenderly, Foundry `fork`, Reth.
- **Infra:** QuickNode Archive, Erigon.

## 5. Strategy Development Loop

1. Idea → Identify invariant (price mismatch, liquidation threshold).
2. Data collection → mempool, on-chain data.
3. Simulation → ensure profitability + minimal reverts.
4. Deployment → use `mev-sendBundle`. Set alerts for revenue.

## 6. Checklist

- [ ] Viết bot modular (data, simulation, executor).
- [ ] Thêm risk control (max gas, stop-loss).
- [ ] Theo dõi outcome (PNL, inclusion rate).
- [ ] Tối ưu latency (co-locate node, use websockets).