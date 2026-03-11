---
title: "Decentralized Oracles Landscape"
description: "Pyth, API3, UMA/Data Verification Mechanism và các mô hình oracle phi tập trung."
tags:
  - oracle
  - pyth
  - api3
  - uma
updated: 2026-03-11
---

# 🌐 Decentralized Oracles Landscape

## 1. Pyth Network

- **Model:** Publishers (exchanges, market makers) push price vào Pythnet (Solana-based), sau đó relay qua Wormhole.
- **Latency:** Sub-second, hữu ích cho trading.
- **Integration:** `PythContract.updatePriceFeeds(bytes[] calldata priceUpdateData)`.
- **Risk:** Guardian set, bridge dependency.

## 2. API3

- **First-party Oracle:** Data provider deploy Airnode (serverless) → sign data trực tiếp.
- **dAPI:** on-chain aggregated feed, update via DAO-managed contracts.
- **Economics:** API3 staking + insurance pool, slashing khi feed sai.
- **Use-case:** Khi cần trust trực tiếp vào data provider (airline, weather company).

## 3. UMA & DVM

- **Data Verification Mechanism (DVM):** Token holders vote giá trị đúng, economic guarantee.
- **Optimistic Oracle:** Proposer submit data, challenged trong dispute window.
- **Suitable for:** Long-tail data (custom KPI, KPI options, insurance claim).
- **Latency:** Minutes (depends on dispute window).

## 4. Chronicle / RedStone / DIA

- **Chronicle:** MakerDAO-run oracle, focus on ETH ecosystem.
- **RedStone:** Modular data delivery, pushes data just-in-time bằng calldata.
- **DIA:** Crowd-sourced data, open-source connectors.

## 5. Comparison

| Oracle | Latency | Sec Model | Ideal Use |
| --- | --- | --- | --- |
| Chainlink | Seconds | DON staking reputation | Lending, stablecoin |
| Pyth | Sub-second | Publisher + guardian | Perp DEX, HFT |
| API3 | Seconds | First-party provider | Off-chain data trusted source |
| UMA | Minutes | Token holder vote/slash | Custom settlement data |
| RedStone | On demand | Optimistic + calldata | DeFi protocols cần gas-optimize |

## 6. Checklist

- [ ] Xác định yêu cầu latency vs trust model của dApp.
- [ ] Chọn oracle phù hợp (low latency → Pyth, formal governance → UMA).
- [ ] Đánh giá economic security (stake, slashing, insurance).
- [ ] Plan integration path (SDK, relayer, calldata packing).
- [ ] Test dispute flow / fallback cho optimistic oracle.