---
title: "MEV Fundamentals"
description: "Sandwich, front-run, backrun và pipeline mempool → searcher → builder."
tags:
  - mev
  - fundamentals
  - ethereum
updated: 2026-03-11
---

# 📚 MEV Fundamentals

## 1. Pipeline Overview

1. User gửi tx vào public mempool.
2. Searcher lắng nghe mempool, tìm cơ hội → xây bundle.
3. Builder gom bundle + tx khác -> block proposal.
4. Proposer (validator) chọn block có giá trị MEV cao nhất.

## 2. Attack Types

| Type | Description | Impact |
| --- | --- | --- |
| **Front-run** | Searcher inject tx trước user để hưởng lợi | User bị mua giá xấu |
| **Back-run** | Searcher đặt tx sau user (e.g., LP arbitrage) | Extract arbitrage |
| **Sandwich** | Combo front + back → ép slippage | User mất tiền |
| **Liquidation** | Keeper thanh lý loan khi collateral < threshold | Duy trì solvency |
| **Time-bandit** | Validator reorganize chain để lấy MEV | Chain instability |

## 3. Sandwich Mechanics

- Bot theo dõi swap tx có slippage cao.
- Gửi 2 tx: trước (buy) và sau (sell) với gas cao.
- User chịu giá xấu + bot ăn spread.

## 4. Mitigations (User)

- `maxPriorityFee` thấp + `eth_sendPrivateTransaction`.
- MEV-protected RPC (Flashbots Protect, Eden, bloXroute).
- DEX route: Use aggregators có private order flow (1inch Fusion).

## 5. Opportunities (Positive MEV)

- **Arbitrage:** đồng bộ giá giữa DEX.
- **Liquidation:** giữ hệ thống lending an toàn.
- **Backrun Rebalance:** Provide liquidity chính xác.

## 6. Checklist

- [ ] Hiểu pipeline mempool → searcher → builder.
- [ ] Phân biệt attack vs utility MEV.
- [ ] Thiết kế UX để giảm sandwich (private tx, slippage guard).
- [ ] Theo dõi mempool/relay để phát hiện bot.