---
title: "Avalanche Architecture"
description: "Snow consensus, Primary Network, Subnets, scaling roadmap."
tags:
  - avalanche
  - architecture
updated: 2026-03-11
---

# 🏔️ Avalanche Architecture

## 1. Snow Consensus Family

- Repeated subsampled voting (Snowball, Snowman) → low latency, probabilistic finality ~1-2s.
- Separate consensus for DAG (X-Chain) vs linear (C-Chain, Subnets).

## 2. Primary Network (X/P/C Chains)

- **X-Chain:** AVAX transfers, DAG consensus.
- **P-Chain:** Validator coordination, Subnet staking.
- **C-Chain:** EVM-compatible smart contracts (Snowman consensus).

## 3. Subnets

- Application-specific chains with custom VMs (EVM, WASM, Rust) + own validators.
- Elastic Subnets hỗ trợ permissioned + KYC requirements (enterprise, gaming).

## 4. Directional Roadmap

- Avalanche Warp Messaging (AWM) cho cross-subnet messaging.
- HyperSDK + custom VMs, Firewood storage improvements.

## 5. Checklist

- [ ] Validator phải stake tối thiểu 2,000 AVAX và tham gia Primary Network trước khi join subnet.
- [ ] Đánh giá trust assumptions của từng subnet (validator overlap, KYC).
- [ ] Theo dõi lộ trình AWM/Firewood ảnh hưởng thông lượng.