---
title: "Oracle Problem & Attack Vectors"
description: "Tại sao smart contract cần oracle đáng tin cậy, mô tả rủi ro và phòng thủ."
tags:
  - oracle
  - security
  - defi
updated: 2026-03-11
---

# ⚠️ Oracle Problem

> Smart contract không thể tự gọi HTTP API hoặc đọc dữ liệu ngoài chain, nên phải dựa vào oracle → điểm yếu hệ thống.

## 1. Why Oracles Matter

- **Price Feeds:** AMM, lending cần giá collateral.
- **Settlement Data:** Prediction market, insurance cần dữ liệu ngoài (weather, flight, sports).
- **Cross-chain communication:** Bridge, restaking AVS cần messaging.
- **Automation:** Keepers, cron job.

## 2. Attack Vectors

| Vector | Description | Example |
| --- | --- | --- |
| **Price manipulation** | Flash loan khiến DEX TWAP bị lệch, oracle lấy giá đó | bZx 2020, Mango Markets 2022 |
| **Stale data** | Oracle không cập nhật, contract dùng giá cũ | Synthetix iETH 2019 |
| **Sybil / Collusion** | Publisher collude đưa giá sai | Custom oracle ít node |
| **Infrastructure downtime** | DON offline, relayer fail | Chainlink incident Feb 2022 (gas spike) |
| **Bridge compromise** | Oracle data gửi qua bridge bị hack | Wormhole 2022 |
| **API tampering** | First-party API bị hack, trả dữ liệu giả | Centralized feed |

## 3. Defense Strategies

- **Multiple Data Sources:** median aggregator, Chainlink + Pyth dual feed.
- **Bounds Check:** reject price nếu deviates > X% vs previous block.
- **Heartbeat & Staleness:** require timestamp < current - heartbeat.
- **Circuit Breaker:** freeze protocol nếu deviation > threshold.
- **Economic security:** incentivize honest publishers, slashable stake.
- **Continuous monitoring:** alert channel, failover manual update.

## 4. Checklist

- [ ] Map dữ liệu nào cần oracle (price, random, cross-chain message).
- [ ] Xác định attack surface và tolerance (deviation %, latency).
- [ ] Thiết kế fallback (secondary feed, manual override, TWAP).
- [ ] Thiết lập alerting (stale, deviation, relayer offline).
- [ ] Run chaos test: mock feed returns wrong value, ensure circuit breaker.