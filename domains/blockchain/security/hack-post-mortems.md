---
title: "Hack Post-Mortems"
description: "Phân tích các vụ hack lớn và lessons learned."
tags:
  - security
  - postmortem
  - incidents
updated: 2026-03-11
---

# 💥 Hack Post-Mortems

## 1. Case Studies

### **The DAO (2016)**
- Root cause: reentrancy.
- Lesson: checks-effects-interactions + reentrancy guard.

### **Poly Network (2021)**
- Root cause: permission check lỗi trong cross-chain messaging.
- Lesson: validate cross-chain proofs & governance.

### **Wormhole (2022)**
- Root cause: missing signature verification in guardian set.
- Lesson: redundant checks + formal verification.

### **Ronin Bridge (2022)**
- Root cause: compromised validator keys.
- Lesson: multi-sig decentralization, HSM, key rotation.

### **Curve Pool (2023)**
- Root cause: Vyper compiler bug.
- Lesson: compiler audit, use battle-tested versions.

## 2. Common Failure Modes

- Key compromise (signing server, deployer).
- Oracle manipulation.
- Logic bug in upgrade or proxy.
- Bridge proof validation flaws.

## 3. Incident Response Checklist

- [ ] Pause protocol / emergency circuit breaker.
- [ ] Snapshot state and communicate.
- [ ] Triage affected contracts & users.
- [ ] Prepare patch or rollback upgrade.

## 4. Deliverable

- Post-mortem template: root cause, impact, timeline, fix.

## 🧪 Lab: Incident Simulation

**Goal:** chạy tabletop exercise mô phỏng vụ hack.

1. Chọn case study (VD: bridge exploit) và mô phỏng timeline.
2. Viết incident report draft: detection, response, containment.
3. Đề xuất patch + long-term mitigation.
4. Retrospective: cập nhật playbook.

**Deliverables:** incident log + improved checklist + lessons learned.