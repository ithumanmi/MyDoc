---
title: "Polygon Development Stack"
description: "PoS chain tooling, zkEVM CDK, DevX notes."
tags:
  - polygon
  - development
updated: 2026-03-11
---

# 🧑‍💻 Polygon Development

## 1. Tooling

- Polygon PoS: Hardhat/Foundry + PoS RPC, PolygonScan.
- zkEVM: Polygon CLI, prover services, Hermez SDK.
- Chain Development Kit (CDK) cho custom zk rollups.

## 2. Deployment Patterns

- Use `fx-portal` bridge contracts cho PoS.
- zkEVM sử dụng batching/proofs, sequencer API.

## 3. App-specific Chains

- Immutable zkEVM, Astar zkEVM, Gnosis Pay chain.
- Shared liquidity qua AggLayer.

## 4. Checklist

- [ ] Gas token (MATIC/ETH) & fee market differences.
- [ ] Bridge contract upgrade process.
- [ ] Monitor sequencer uptime + prover queue.