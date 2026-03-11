---
title: "Wallet Security"
description: "Hardware wallet, multisig, social recovery, threat model checklist."
tags:
  - security
  - wallet
  - gnosis-safe
updated: 2026-03-11
---

# 🔐 Wallet Security Playbook

> **Goal:** Bảo vệ private key cá nhân và tổ chức khỏi phishing, malware, compromise.
> **Deliverables:** Security architecture (hardware, multisig, social recovery), operational checklist.
> **Success Criteria:** Không mất khóa, audit access log, recovery plan rõ ràng.

## 1. Wallet Types

| Type | Use-case | Pros | Cons |
| --- | --- | --- | --- |
| Software wallet (Metamask, Rabby) | Retail, testing | Dễ dùng | Dễ bị malware/phishing |
| Hardware wallet (Ledger, Trezor, Keystone) | Cold storage, signing | Private key off device | Cost, UX |
| Multisig (Gnosis Safe) | DAO treasury, team fund | Shared control, policy | Need coordination |
| Smart contract wallet (Argent, Safe{wallet}) | Social recovery, batching | Custom logic, AA-ready | Gas, upgrade risk |

## 2. Hardware Wallet Best Practices

- Mua từ official store, kiểm tra seal.
- Sử dụng passphrase 25th word, PIN > 6 digits.
- Air-gapped signing (Keystone, QR) nếu cần.
- Firmware update định kỳ.

## 3. Multisig Architecture

- **Gnosis Safe:** threshold (e.g., 2/3, 3/5).
- **Module:** Owner manager, spending limit, delay.
- **Ops:**
  - Define signer role (treasury, tech, legal).
  - Rotation process.
  - Emergency signer backup.

## 4. Social Recovery / Smart Wallet

- Guardians (friends/device) có thể approve recovery.
- EIP-4337 account abstraction: bundler + paymaster.
- Tools: Argent, Safe, Soul Wallet.

## 5. Threats & Mitigation

| Threat | Mitigation |
| --- | --- |
| Phishing (fake site, signing) | Use wallet allowlist, hardware confirmation, ENS content hash verification |
| Malware/keylogger | Dedicated device, hardware wallet, disable browser extensions |
| SIM swap | Avoid SMS 2FA, use authenticator, remove phone numbers from exchange |
| Insider | Multisig threshold, policy, audit log |
| Seed loss | Metal backup, split via Shamir Secret Sharing |

## 6. Recovery Plan

1. Document seed storage location (metal, safe).
2. Practice recovery on spare wallet.
3. Multisig – define who triggers recovery, quorum.
4. Social recovery – specify guardians, update contact.

## 7. Checklist

- [ ] Chọn wallet type phù hợp (hardware, multisig, AA wallet).
- [ ] Thiết lập seed backup (metal, Shamir) và kiểm tra phục hồi.
- [ ] Áp dụng policy ký giao dịch (2FA, address book, hardware confirmation).
- [ ] Định kỳ review signer list, rotate compromised device.
- [ ] Thiết lập incident response (phishing report, revoke approvals, revoke session).