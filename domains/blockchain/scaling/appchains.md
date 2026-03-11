---
title: "Appchains"
description: "Application-specific chains, sovereignty vs shared security."
tags:
  - appchain
  - sovereignty
  - scaling
updated: 2026-03-11
---

# 🧩 Appchains

## 1. Definition

- Application-specific blockchain tailored cho 1 use case.
- Control gas token, fee market, governance, upgrades.

## 2. Deployment Models

- **Cosmos SDK chains:** sovereign, IBC interop.
- **Polkadot parachains:** shared security via relay chain.
- **App-rollups:** Arbitrum Orbit, zkSync Hyperchains, Starknet appchains.

## 3. Sovereignty vs Shared Security

- Sovereign chains tự bảo mật → cần validator set.
- Shared security (Polkadot, EigenLayer AVS) giảm overhead.

## 4. Use Cases

- DEX chains (dYdX v4 Cosmos).
- Game chains (Ronin, Immutable zkEVM).
- Enterprise consortia.

## 5. Checklist

- [ ] Decide sovereignty level (own validator vs shared).
- [ ] Token economics (gas, staking, incentives).
- [ ] Interop (IBC, bridges, messaging).
- [ ] Upgrade + governance process.

## 🧪 Lab: Cosmos Appchain Dry Run

**Goal:** dựng appchain mẫu bằng Cosmos SDK.

1. Scaffold chain via Ignite CLI (module cho use case cụ thể).
2. Configure tokenomics (staking denom, inflation, fees).
3. Enable IBC + connect đến testnet relay.
4. Run governance proposal (param change) để test upgrade flow.

**Deliverables:** chain repo, network bootstrapping guide, gov proposal record.