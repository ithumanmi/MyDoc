---
title: "Solana Development"
description: "Anchor, Rust, program architecture và account model."
tags:
  - solana
  - rust
  - anchor
updated: 2026-03-11
---

# ☀️ Solana Development

## 1. Architecture

- **Programs:** smart contract Rust compiled to BPF.
- **Accounts:** state storage (rent-exempt), serialized via Borsh.
- **Instruction:** input payload for program call.

## 2. Anchor Framework

- Macros for account validation (`#[account]`).
- IDL auto-generated for frontend.
- Testing with `anchor test` (local validator).

## 3. Program Design

- Separate state accounts (Config, UserPosition).
- Use PDA (Program Derived Address) for deterministic accounts.
- Validate signer + seeds in instruction.

## 4. Tooling

- Solana CLI, Anchor CLI, Solana Playground.
- Local validator + faucet.
- Explorer: SolanaFM.

## 5. Performance Tips

- Optimize account size (Borsh padding).
- Minimize CPI calls.
- Use compute budget instruction.

## 6. Checklist

- [ ] Define account schema + PDA strategy.
- [ ] Write Anchor tests for all instructions.
- [ ] Handle rent exemption & close accounts.
- [ ] Simulate with local validator before deploy.

## 🧪 Lab: Anchor Escrow

**Goal:** build a simple escrow program using Anchor.

1. Create program with `initialize`, `deposit`, `release`.
2. Use PDA for escrow account.
3. Write Anchor tests with local validator.
4. Integrate frontend call via generated IDL.

**Deliverables:** program code + test logs + demo transaction hash.