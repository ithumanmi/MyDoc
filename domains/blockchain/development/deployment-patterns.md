---
title: "Deployment Patterns"
description: "Upgradeable contracts, proxy patterns, diamond architecture."
tags:
  - deployment
  - upgradeable
  - smart-contracts
updated: 2026-03-11
---

# 🚀 Deployment Patterns

## 1. Upgradeability Models

- **Transparent Proxy:** OpenZeppelin, admin cannot call implementation.
- **UUPS:** logic in implementation, cheaper, requires `upgradeTo` guard.
- **Beacon Proxy:** multiple proxies share implementation.

## 2. Diamond Pattern (EIP-2535)

- Facets chứa logic, diamond storage.
- Upgrade granular per facet.
- Complexity cao → cần tooling (loupe).

## 3. Deployment Workflow

1. Deploy implementation.
2. Deploy proxy with initializer.
3. Verify contract on explorer.
4. Configure timelock/multisig for upgrades.

## 4. Safety Checklist

- [ ] Storage layout pinned (no reordering).
- [ ] Initializer protected (`initializer` modifier).
- [ ] Admin keys stored in multisig (Safe).
- [ ] Upgrade simulation on fork.
- [ ] Rollback plan if upgrade fails.

## 5. Tooling

- OpenZeppelin Upgrades plugin.
- Foundry `forge script` + `broadcast`.
- Defender (OpenZeppelin) automation.

## 🧪 Lab: UUPS Upgrade Drill

**Goal:** triển khai UUPS proxy, upgrade logic và verify trên testnet.

1. Deploy `VaultV1` via UUPS proxy.
2. Write `VaultV2` adding new method.
3. Run upgrade with multisig or timelock mock.
4. Verify storage layout unchanged.

**Deliverables:** deploy scripts + upgrade report + verification links.