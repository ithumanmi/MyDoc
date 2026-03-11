---
title: "Move Development"
description: "Aptos/Sui Move, object-centric model, resource safety."
tags:
  - move
  - aptos
  - sui
updated: 2026-03-11
---

# 🧬 Move Development (Aptos/Sui)

## 1. Core Model

- **Resource types:** asset cannot be copied/dropped.
- **Modules:** publish once, expose entry functions.
- **Object-centric:** Sui uses objects (owned/shared).

## 2. Aptos vs Sui

| Aspect | Aptos | Sui |
| --- | --- | --- |
| State model | Account-based | Object-based |
| Parallelism | Block-STM | Object parallel execution |
| Tooling | Aptos CLI, Move Prover | Sui CLI, Sui Move |

## 3. Architecture Patterns

- Split module: `core`, `vault`, `router`.
- Use capability pattern for admin actions.
- Store events for indexer queries.

## 4. Tooling

- Move Prover for formal verification.
- Explorer: Aptos Explorer, Sui Explorer.
- Indexing: Aptos Indexer, Sui Indexer.

## 5. Checklist

- [ ] Define resource invariants.
- [ ] Access control via capabilities.
- [ ] Test with Move Prover + unit tests.
- [ ] Optimize object size & ownership.

## 🧪 Lab: Move Payment Vault

**Goal:** build a simple vault module with deposit/withdraw and capability control.

1. Define `Vault` resource with balance.
2. Implement `deposit`, `withdraw` entry functions.
3. Add admin capability for emergency pause.
4. Run Move Prover for invariants.

**Deliverables:** module code + prover report + test results.