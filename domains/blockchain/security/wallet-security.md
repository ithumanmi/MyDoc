---
title: "Wallet Security"
description: "Hardware wallets, seed phrases, social recovery, best practices."
tags:
  - wallet-security
  - custody
  - opsec
updated: 2026-03-11
---

# 🔐 Wallet Security

## 1. Custody Models

- **Self-custody:** bạn tự giữ private key.
- **Multi-sig:** Safe/Gnosis cho team/treasury.
- **MPC:** Fireblocks, Safeheron – không có private key đơn lẻ.

## 2. Hardware Wallets

- Ledger, Trezor, Keystone.
- Always verify address on device.
- Use a dedicated device for high-value wallets.

## 3. Seed Phrase & Backup

- Never store in cloud/notes.
- Use metal backup for fire/water protection.
- Split backup into 2 locations (safe + trusted vault).

## 4. Social Recovery

- **EIP-4337 + account abstraction:** guardians recovery.
- **Gnosis Safe + guardian:** rotate owner keys.
- **2-of-3** for personal use.

## 5. Threats & Mitigation

- Phishing: verify domain, use wallet alerts.
- Malware: isolated device + browser profile.
- SIM swap: disable SMS 2FA, use hardware key.

## 6. Checklist

- [ ] Hardware wallet initialized offline.
- [ ] Seed phrase backup stored safely.
- [ ] Test recovery flow monthly.
- [ ] Multi-sig for treasury.

## 🧪 Lab: Wallet Resilience Drill

**Goal:** thiết lập và test recovery cho ví multi-layer.

1. Setup hardware wallet + create Safe multisig (2-of-3).
2. Document seed phrase backup (metal) + location map.
3. Run recovery test: import seed trên device khác.
4. Practice social recovery (guardian approves new key).

**Deliverables:** runbook (steps, photos redacted), recovery test log.