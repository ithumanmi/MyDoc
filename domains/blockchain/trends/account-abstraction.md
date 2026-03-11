---
title: "Account Abstraction"
description: "ERC-4337, smart wallets, paymasters, bundlers."
tags:
  - account-abstraction
  - erc4337
  - wallets
updated: 2026-03-11
---

# 🔑 Account Abstraction (ERC-4337)

## 1. Smart Accounts

- UserOperations (UserOp) thay cho tx truyền thống.
- Modular validation logic (MPC, biometrics, social recovery).
- Wallet SDKs: Safe, Stackup, ZeroDev, Pimlico.

## 2. Bundlers & Paymasters

- Bundler tập hợp UserOp → gửi vào `EntryPoint`.
- Paymaster tài trợ gas (sponsor tx, accept ERC20).

## 3. Use Cases

- Gasless onboarding, subscription payments.
- Session keys cho game/app.
- Multi-chain smart wallets.

## 4. Checklist

- [ ] Xác định wallet template (Safe 4337, Kernel, Biconomy).
- [ ] Paymaster policy (KYB, spend limits).
- [ ] Monitoring bundler uptime + mempool health.
- [ ] UX: fallback khi paymaster out of funds.

## 🧪 Lab: Launch an ERC-4337 Paymaster

**Goal:** chạy paymaster tài trợ gas cho onboarding flow.

**Prerequisites:**
- Tooling: Stackup/Pimlico bundler SDK, Safe 4337 module, Node.js.
- Network: Ethereum testnet (Sepolia) hoặc Base Goerli.
- Skills: Solidity, server scripting, monitoring setup.

### Steps
1. Deploy smart account template (Safe 4337 module hoặc Kernel) + register entry point.
2. Spin up bundler + paymaster service, configure stake/deposit.
3. Thiết lập rule: chỉ sponsor tx NFT claim, giới hạn budget mỗi user, logging userOp hash.
4. Implement monitoring alert khi paymaster balance xuống dưới threshold + auto top-up script.

**Metrics to Track:** số UserOp thành công, chi phí gas/tài trợ, uptime bundler, thời gian xử lý userOp.

**Deliverables:** paymaster config repo, monitoring dashboard, demo video onboarding gasless.

## 🧾 Case Study: Visa + Safe Account Abstraction Pilot

- **Context:** Visa (2023) thử nghiệm recurring payments trên Ethereum với Safe smart account + account abstraction.
- **Key Metrics:** pilot với hàng chục ví nội bộ, interval payment vài phút, gas sponsorship fully covered.
- **Architecture Snapshot:** Visa off-chain service → paymaster → Safe smart account với session keys.
- **Key Insights:**
  - Use case subscription → cần session keys + spending limits.
  - UX flows require fallback to EOAs khi AA unsupported.
  - Paymaster funding via custodial accounts tạo compliance overhead.
- **Risks & Mitigations:** regulatory KYC cho paymaster operators; bundler downtime → fallback to EOA.
- **Takeaway:** Để scale mainstream, cần Payment-as-a-Service + compliance-ready paymaster infrastructure.