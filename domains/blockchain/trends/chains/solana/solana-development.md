---
title: "Solana Development Stack"
description: "Anchor, PDAs, CPIs, testing, tooling."
tags:
  - solana
  - development
updated: 2026-03-11
---

# 🛠️ Solana Development

## 1. Anchor Framework

- Macro-based Rust framework cho program.
- IDL + client generation, account constraints, error handling.

## 2. Program Derived Addresses (PDAs)

- Deterministic addresses từ seeds + program ID.
- Không có private key, dùng cho state ownership, authority.

## 3. Cross Program Invocations (CPIs)

- Cho phép gọi program khác -> composability (Token Program, Raydium pools).
- Cần quản lý account metas và compute budget.

## 4. Tooling & Testing

- `solana-test-validator`, Anchor tests, Seahorse (Python DSL), Solana Playground.
- Jito block engine cho MEV-aware tx.

## 5. Checklist

- [ ] Lint program (cargo clippy, `anchor lint`).
- [ ] Security: kiểm tra account constraints, reinit lock.
- [ ] Monitoring compute unit usage, log analyzer.