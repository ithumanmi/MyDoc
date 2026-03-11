---
title: "Polygon Architecture"
description: "Sidechain PoS, zkEVM, AggLayer vision."
tags:
  - polygon
  - architecture
updated: 2026-03-11
---

# 🔺 Polygon Architecture

## 1. Polygon PoS Chain

- Commit-chain/POS sidechain anchored vào Ethereum.
- Heimdall (Tendermint) + Bor (EVM) dual-layer.

## 2. zkEVM & zkSync-like stacks

- Polygon zkEVM (Type 3) tương thích EVM bytecode.
- Plonky2 proving system, recursion.

## 3. AggLayer Vision

- Unified liquidity + shared proving across L2s.
- Aggregates proofs từ zkEVM, CDK-based L2.

## 4. CDK (Chain Development Kit)

- Cho phép launch zk-powered chains với Polygon tech.

## 5. Checklist

- [ ] Định nghĩa trust assumptions (PoS validators, zk proofs).
- [ ] Data availability strategy (Ethereum DA vs AltDA).
- [ ] Bridge monitoring (PoS bridge vs zk bridge).