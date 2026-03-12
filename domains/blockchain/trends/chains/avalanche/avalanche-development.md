---
title: "Avalanche Development Stack"
description: "Avalanche CLI, Subnet-EVM, HyperSDK, testing."
tags:
  - avalanche
  - development
updated: 2026-03-11
---

# 🛠️ Avalanche Development

## 1. Tooling

- **Avalanche CLI:** tạo + deploy Subnet, validator tooling.
- **Subnet-EVM:** modded EVM (gas config, precompiles, fee markets).
- **HyperSDK:** framework Rust/Go để build custom L1 trên Avalanche consensus.

## 2. Testing & Deployment

- Local Subnet spawns (CLI) cho devnet.
- Fuji testnet cho C-Chain/Subnet testing.
- Monitoring: Avalanche Explorer, Avascan, validator dashboards.

## 3. Patterns

- Elastic Subnet cho compliance: whitelist validators, KYC.
- Gaming chains (Shrapnel, GunZ) optimize block times.

## 4. Checklist

- [ ] Gas token config (AVAX vs custom token) trong Subnet-EVM.
- [ ] Cross-chain bridging (LayerZero, Wormhole) integration test.
- [ ] Node requirement (hardware, uptime) cho validator partners.