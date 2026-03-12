---
title: "Base Development Stack"
description: "OP Stack dev tooling, Coinbase APIs, deployment notes."
tags:
  - base
  - development
updated: 2026-03-11
---

# 🧑‍💻 Base Development

## 1. Tooling

- Standard Optimism/OP Stack tooling: Hardhat/Foundry + `forge script`, `op-node` for local dev.
- Base-specific RPC endpoints (Alchemy, Infura, Coinbase Cloud) với low latency.
- Coinbase Onchain Kit, wallet SDKs (Smart Wallet, MPC).

## 2. Deployment & DevOps

- Bridges: `StandardBridge` contracts; use Base Portal for deposit.
- Monitoring: Dune dashboards, BaseScan, Optimism Superchain telemetry.

## 3. Integrations

- Coinbase Commerce, Onramp, Smart Wallet.
- Farcaster, Friend.tech style social apps (Frames) leveraging Base primitives.

## 4. Checklist

- [ ] Gas estimation differences (EIP-1559 style vs Optimism custom fee).
- [ ] Sequencer refunds + finality assumptions (L1 vs L2).
- [ ] Compliance review nếu tích hợp với Coinbase accounts.