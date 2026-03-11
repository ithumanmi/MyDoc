---
title: "Price Feeds Design"
description: "TWAP, manipulation resistance, deviation-based updates và fallback design."
tags:
  - oracle
  - price-feed
  - defi
updated: 2026-03-11
---

# 📈 Price Feeds Design

## 1. Price Source Options

| Source | Pros | Cons |
| --- | --- | --- |
| Centralized exchange API | Deep liquidity | API downtime, trust in exchange |
| Chainlink aggregated feed | Decentralized, audited | Update interval, cost |
| On-chain DEX (Uniswap v3 TWAP) | Permissionless, free | Manipulation via flash loan |
| Hybrid (Chainlink + TWAP) | Resilience | Complexity |

## 2. TWAP & Manipulation Resistance

- **On-chain TWAP:** Use Uniswap v3 `observe()` over window (e.g., 30 min).
- **Flash Loan Attack:** Attackers trade large amount to skew price → need long window or limit max change.
- **Mitigation:**
  - Increase observation window.
  - Use median of multiple pools.
  - Cap price movement per block.

## 3. Update Strategy

- **Deviation-based:** update when `abs(newPrice - lastPrice)/lastPrice > threshold` (e.g., 0.5%).
- **Heartbeat:** force update every X seconds even không deviation.
- **Adaptive:** shorter heartbeat khi volatility cao.
- **Push vs Pull:** push (Pyth) cho high-frequency, pull (Chainlink) cho general.

## 4. Fallback Patterns

- **Dual Feed:** Primary Chainlink, fallback Pyth/Uniswap TWAP.
- **Manual Override:** Governance multisig set price emergency (có timelock).
- **Circuit breaker:** Pause protocol khi feed unavailable.
- **Off-chain Signed Price:** Oracle committee sign price, upload on demand.

## 5. Validation Logic (Solidity)

```solidity
function _validatePrice(int256 price, uint256 updatedAt) internal view {
    require(price > 0, "Invalid");
    require(block.timestamp - updatedAt < HEARTBEAT, "Stale");
    require(_deviationOk(price), "Too volatile");
}
```

- Compare vs DEX TWAP: `require(abs(price - dexPrice) < maxDeviation)`.

## 6. Monitoring Metrics

- **Staleness:** % time feed stale.
- **Deviation Alerts:** Chainlink vs Pyth difference > threshold.
- **Latency:** Time between market move và on-chain update.
- **Cost:** Gas per update, LINK spent.

## 7. Checklist

- [ ] Chọn nguồn dữ liệu chính + phụ (Chainlink/Pyth/DEX).
- [ ] Định nghĩa threshold deviation, heartbeat, observation window.
- [ ] Implement validation + fallback logic trong smart contract.
- [ ] Thiết lập monitoring (Grafana/Alert) cho staleness, deviation, cost.
- [ ] Viết runbook khi feed lỗi (switch fallback, manual override).