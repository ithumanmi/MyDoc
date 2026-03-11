---
title: "Ethereum Development Stack"
description: "Foundry, Hardhat, Solidity patterns, account abstraction tooling."
tags:
  - ethereum
  - development
updated: 2026-03-11
---

# 🧰 Ethereum Development

## 1. Tooling

- **Foundry** (forge/cast/anvil) cho testing, fuzzing.
- **Hardhat** với plugins (Ethers.js, TypeChain, Tenderly).
- **OpenZeppelin** libraries, security tooling (Slither, Echidna).

## 2. Smart Contract Patterns

- Proxy/upgradeable (UUPS, Transparent).
- Access control (RBAC, Ownable, roles).
- Account Abstraction: ERC-4337 bundler SDKs (Stackup, Pimlico).

## 3. Testing & Deployment

- Anvil/Hardhat node, fork mainnet để simulate.
- DevOps: Foundry script, Hardhat deploy, SafeOps multisig.

## 4. Checklist

- [ ] Static analysis + fuzz tests trước deploy.
- [ ] Access control review, Pausable/Guardian.
- [ ] Monitoring (OpenZeppelin Defender, Tenderly alerts).