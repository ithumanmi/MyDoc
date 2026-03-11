---
title: "Bitcoin Technical Overview"
description: "UTXO, Script, Taproot, Miniscript tooling."
tags:
  - bitcoin
  - technical
updated: 2026-03-11
---

# ₿ Bitcoin Technical Overview

## 1. UTXO Model

- Coins represented as unspent transaction outputs.
- Stateless contract model vs account-based chains.

## 2. Script & Miniscript

- Stack-based Script (non Turing-complete) -> P2PKH, P2SH, P2WSH.
- Miniscript: structured descriptor for wallets (BDK).

## 3. Taproot & Tapscript

- MAST + Schnorr signatures → flexible spending paths.
- Taproot assets enabling future tokenization.

## 4. Tooling

- PSBT workflow, Hardware wallets, Bitcoin Dev Kit (BDK), Rust Bitcoin.
- Mutiny wallet + Lightning integration.

## 5. Checklist

- [ ] Handle fee estimation + RBF logic.
- [ ] Monitor mempool policy (dust, child-pays-for-parent).
- [ ] Taproot key path vs script path privacy tradeoffs.