---
title: "Cosmos Architecture"
description: "Tendermint, Cosmos SDK, IBC, interchain security."
tags:
  - cosmos
  - architecture
updated: 2026-03-11
---

# 🌐 Cosmos Architecture

## 1. Tendermint BFT

- Consensus Byzantine Fault Tolerance với instant finality (~6s).
- Separation networking/consensus vs application layer.

## 2. Cosmos SDK

- Module-based framework (bank, staking, gov).
- App-specific chains customize module + params.

## 3. IBC (Inter-Blockchain Communication)

- Light-client verified packets giữa chains.
- Channels + relayers, hỗ trợ ICS-20 token transfer.

## 4. Interchain Security & Shared Sequencing

- ICS v1: consumer chains thuê security từ Cosmos Hub.
- Mesh security, Neutron/Stride adopters.

## 5. Checklist

- [ ] Monitor validator set health, slashing risk.
- [ ] Relayer uptime + fee incentives.
- [ ] Upgrade path (CometBFT, ABCI++).