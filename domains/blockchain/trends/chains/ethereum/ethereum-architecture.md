---
title: "Ethereum Architecture"
description: "Execution + consensus layers, rollups, danksharding roadmap."
tags:
  - ethereum
  - architecture
updated: 2026-03-11
---

# 🟣 Ethereum Architecture

## 1. Execution vs Consensus Layer

- Post-Merge: Execution Clients (Geth, Nethermind) + Consensus Clients (Prysm, Lighthouse).
- Engine API kết nối hai layer, block proposals đi qua Builder/Relay.

## 2. Rollup-centric Roadmap

- L1 tối ưu bảo mật + data availability.
- L2 rollups (Optimistic & ZK) xử lý execution, đăng dữ liệu lên L1.

## 3. Proto-Danksharding & EIP-4844

- Data blobs cho rollups, giảm phí L2.
- Tiến tới full danksharding với data availability sampling.

## 4. MEV & PBS (Proposer-Builder Separation)

- MEV-Boost, relays, builder marketplace.
- Enshrine PBS trong tương lai để giảm reliance vào relays.

## 5. Checklist

- [ ] Theo dõi client diversity để giảm risk.
- [ ] L2 data costs khi lên roadmap proto-danksharding.
- [ ] MEV policy (builder whitelist, mev-relay).