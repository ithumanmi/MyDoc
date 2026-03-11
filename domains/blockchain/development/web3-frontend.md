---
title: "Web3 Frontend"
description: "Ethers.js/viem, wagmi, wallet connection, UX patterns."
tags:
  - web3
  - frontend
  - wagmi
updated: 2026-03-11
---

# 🌐 Web3 Frontend

## 1. Core Stack

- **RPC:** Alchemy/Infura/QuickNode + fallback.
- **Lib:** viem (modern), ethers.js v6.
- **Hooks:** wagmi + RainbowKit/ConnectKit.
- **State:** TanStack Query, Zustand.

## 2. Wallet Connection Flow

1. Detect injected wallets.
2. Prompt connect + network guard.
3. Persist session (localStorage).
4. Handle disconnect/chain change.

## 3. Transaction UX

- Pre-flight simulation (`eth_call`).
- Gas estimation + fee breakdown.
- Status: pending → confirmed → failed.
- Graceful handling of `userRejected`.

## 4. Security Patterns

- Verify chainId, contract address.
- Use typed data (EIP-712) for signatures.
- Avoid blind signing; show message summary.
- Use RPC fallback to avoid censorship.

## 5. Tooling

- SIWE authentication.
- Indexing: The Graph/Substreams.
- Analytics: Dune, Flipside.

## 6. Checklist

- [ ] Wallet connection UX tested on mobile + desktop.
- [ ] Error handling cho RPC downtime.
- [ ] Simulation + slippage guard UI.
- [ ] Verified contract addresses by network.

## 🧪 Lab: Wallet Connection + Swap Flow

**Goal:** build a minimal DApp that connects wallet, reads balance, executes swap on testnet.

1. Setup Next.js + wagmi + RainbowKit.
2. Show address + balance + network guard.
3. Integrate a simple swap (Uniswap v2 testnet fork) with `viem`.
4. Add transaction lifecycle UI (pending, success, error).

**Deliverables:** live demo + README (setup steps + screenshots).