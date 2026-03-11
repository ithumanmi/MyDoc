---
title: "On-chain Oracles"
description: "Chainlink, API3, Pyth, data sourcing patterns và checklist tích hợp."
tags:
  - oracle
  - data-availability
  - web3
updated: 2026-03-11
---

# 🔗 Oracles & Data Feeds

> **Goal:** Đảm bảo smart contract nhận dữ liệu off-chain tin cậy, chống manipulation, latency thấp.
> **Deliverables:** Data feed selection matrix, reputation/SLAs, fallback strategy, integration checklist.
> **Success Criteria:** 99.9% uptime feed, deviation < threshold, failover < 1 block.

## 1. Oracle Types

| Type | Ví dụ | Ưu điểm | Nhược |
| --- | --- | --- | --- |
| Pull-based | Chainlink Data Feeds | Decentralized network, off-chain computation | Phí cao hơn, latency ~seconds |
| API-first (First-party oracle) | API3 Airnode | Data provider tự publish → trust giảm | Cần provider vận hành |
| High-frequency | Pyth, Chronicle | Push via wormhole / SVM, update ~sub-second | Dependency vào publisher set |
| Custom oracle | Self-hosted + threshold signing | Linh hoạt, dữ liệu riêng | Phải tự bảo mật | 

## 2. Modules

- [Oracle Problem & Attack Vectors](oracle-problem.md)
- [Chainlink Deep Dive](chainlink-deep-dive.md)
- [Price Feeds Design](price-feeds-design.md)
- [Decentralized Oracles Landscape](decentralized-oracles.md)
- [Oracle Integration Lab](labs.md)
- [Oracle Audit Exercises](audit-exercises.md)

## 3. Design Patterns

1. **Pull with Heartbeat:** contract read aggregator, ensure timestamp < X.
2. **Dual Oracle (Chainlink + Pyth):** median or fallback.
3. **Manual Circuit breaker:** admin can freeze when deviation > threshold.
4. **On-chain TWAP:** combine DEX price (Uniswap v3 TWAP) + oracle price.

## 4. Testing & Monitoring

- **Test:** mock aggregator, fuzz timestamp/stale data.
- **Simulation:** use Tenderly to simulate feed update.
- **Monitoring:**
  - Deviation alert (Pyth price vs DEX).
  - Feed stale > heartbeat.
  - Chainlink DON incident RSS.

## 5. Checklist

- [ ] Chọn oracle phù hợp use-case (Chainlink/API3/Pyth/custom).
- [ ] Thiết kế fallback và circuit breaker.
- [ ] Viết test với mock feed, fuzz stale/negative.
- [ ] Thiết lập monitoring + alert (stale, deviation, downtime).
- [ ] Đánh giá chi phí gas/latency & update frequency.