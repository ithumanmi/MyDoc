---
title: "Staking Risks & Penalties"
description: "Slashing, correlation, validator failure và pháp lý."
tags:
  - staking
  - risk
  - slashing
updated: 2026-03-11
---

# ⚠️ Staking Risks & Penalties

## 1. Slashing Types

- **Double-sign:** ký 2 block/attestation cho cùng slot.
- **Surround vote (Casper FFG):** attestation bao quanh vote trước đó.
- **Inactivity leak:** khi network offline dài, validator bị giảm balance.

## 2. Risk Categories

| Risk | Description | Mitigation |
| --- | --- | --- |
| Operational | Hardware fail, power loss | UPS, redundant ISP, remote signer |
| Software | Client bug, outdated version | Client diversity, fast patching |
| Key management | Key leak/chairman | Slashing protection DB, multisig control |
| Correlation | Same provider/operator for many validators | DVT, geo distribution |
| Smart contract | LST or restaking contract bug | Audited protocol, insurance |
| Regulatory | Staking seen as security/yield product | Legal review, compliance |

## 3. Monitoring Signals

- Missed attestation > threshold.
- Validator balance dropping (via BeaconChain API).
- Relay disconnect (if MEV-Boost).
- LST peg deviation > 0.5%.

## 4. Incident Response

- Pause operator duties (voluntary exit if needed).
- Use slashing protection DB khi chuyển client.
- Communicate với delegators (if staking pool).
- File insurance claim (if coverage).

## 5. Legal/Tax Consideration

- Jurisdiction may classify staking reward as income (taxable on receipt).
- Custodial staking service có thể yêu cầu license.

## 6. Checklist

- [ ] Redundant infra (power, network, hardware).
- [ ] Client diversity + auto update plan.
- [ ] Slashing protection DB backup.
- [ ] Insurance/coverage hoặc reserve fund.
- [ ] Compliance review (KYC/AML nếu cung cấp dịch vụ staking).