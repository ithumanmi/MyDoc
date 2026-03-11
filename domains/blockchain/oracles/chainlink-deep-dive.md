---
title: "Chainlink Deep Dive"
description: "DON architecture, VRF, Automation (Keepers), CCIP và triển khai thực tế."
tags:
  - chainlink
  - oracle
  - automation
updated: 2026-03-11
---

# 🔍 Chainlink Deep Dive

## 1. Decentralized Oracle Network (DON)

- **Architecture:**
  - Node operators stake LINK, fetch data từ API.
  - Aggregation contract tính median.
  - Heartbeat và deviation threshold quyết định update.
- **Key Parameters:**
  - `roundId`, `answer`, `updatedAt`.
  - Heartbeat (interval update) vs `threshold` (%) trigger update.
- **Operator Selection:** Reputation, SLA via Chainlink Market.

## 2. Data Feeds Integration

```solidity
AggregatorV3Interface priceFeed = AggregatorV3Interface(0x...);
(uint80 roundID, int price,, uint timeStamp,) = priceFeed.latestRoundData();
require(timeStamp > block.timestamp - heartbeat, "stale");
```

- **Best Practices:**
  - Check decimals via `priceFeed.decimals()`.
  - Validate round completeness (`answer > 0`).
  - Fallback mechanism (secondary feed/manual).

## 3. Chainlink VRF (Randomness)

- **Flow:** Request randomness → VRF Coordinator → callback `fulfillRandomWords`.
- **Key Concepts:**
  - Subscription model (fund LINK).
  - KeyHash, gas lane.
- **Use Cases:** NFT mint fairness, gaming loot.

## 4. Automation (Keepers)

- **Purpose:** Automate cron job on-chain (rebalance, distribution).
- **Architecture:** Registrar contract đăng ký task → keepers checkUpkeep → performUpkeep.
- **Checklist:**
  - Idempotent perform function.
  - Fund LINK balance.
  - Emit events for monitoring.

## 5. Chainlink CCIP

- **Cross-Chain Interop:** Send data/message/token giữa chains.
- **Components:** Router contract, off-chain DON, risk isolation.
- **Use Case:** Bridging stablecoin, trigger cross-chain action.
- **Security:** Rate limit, programmable allowlist, risk management module.

## 6. Operations & Monitoring

- Use Chainlink OCR feeds status page.
- Set up alert when `updatedAt` > heartbeat.
- Monitor LINK balance for VRF/Automation.
- Subscribe Chainlink announcement, incident channel.

## 7. Checklist

- [ ] Kiểm tra feed address & decimals theo chain.
- [ ] Implement stale/heartbeat guard và fallback.
- [ ] Thiết kế gas limit phù hợp cho VRF/Automation.
- [ ] Theo dõi LINK balance và set alert.
- [ ] Đăng ký CCIP route với allowlist và rate limit.