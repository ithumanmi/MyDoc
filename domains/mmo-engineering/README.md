---
title: "MMO Engineering Playbook"
description: "Automation, proxy, anti-detect, risk & ethics guidance for scale campaigns."
tags:
  - mmo
  - automation
updated: 2026-03-12
---

# ⚙️ MMO Engineering Playbook

> Tập trung vào kỹ thuật để scale MMO (Make Money Online) campaigns: automation, proxy farm, anti-detect, Sybil ops.

## 1. Scope & Prerequisites

- **Audience:** MMO operators, growth hackers, security engineers muốn hiểu hệ thống farm quy mô lớn.
- **Prereq:** Linux basics, networking knowledge, scripting (Python/JS), hiểu ToS nền tảng.
- **Warning:** Nhiều kỹ thuật có thể vi phạm điều khoản dịch vụ hoặc pháp luật tại một số quốc gia. Sử dụng có trách nhiệm.

## 2. Roadmap

1. **Anti-detect & Fingerprinting** – hiểu fingerprint, profile isolation.
2. **Proxy Infrastructure** – residential, 4G farm, rotation strategies.
3. **Automation Stack** – browser, mobile, GUI automation, OTP handling.
4. **Tool Development** – Python foundations, API/GUI automation, pack/release tools.
5. **Crypto Sybil Ops** – funding hygiene, randomization, wallet management.

## 3. Modules

| Module | File |
| --- | --- |
| Browser Fingerprinting | [browser-fingerprinting.md](./browser-fingerprinting.md) |
| Proxy Infrastructure | [proxy-infrastructure.md](./proxy-infrastructure.md) |
| Automation Tools | [automation-tools.md](./automation-tools.md) |
| Crypto Sybil Strategies | [crypto-sybil.md](./crypto-sybil.md) |
| Tool Development | [tool-dev/README](./tool-dev/python-foundation.md) *(expand)* |

## 4. Risk & Ethics Checklist

- [ ] Kiểm tra luật địa phương (anti-spam, cybercrime). Tránh sử dụng vào hoạt động phi pháp.
- [ ] Đọc kỹ ToS của platform (Facebook, Google, TikTok). Vi phạm có thể dẫn tới kiện tụng.
- [ ] Tách môi trường thí nghiệm với tài khoản cá nhân (OpSec tối thiểu).
- [ ] Không share dữ liệu người dùng thật, tuân thủ privacy (GDPR, PDPA).
- [ ] Xây dựng incident plan: nếu farm bị compromise, cách revoke access và báo cáo.

## 5. Next Steps

- Hoàn thiện module Tool Dev (đã bổ sung anti-detect integration, lab scripts, deployment tips).
- Mở rộng lab scripts (ví dụ reset 4G IP, quản lý ví, profile health check) và thêm dashboard tham chiếu.
- Mở rộng case study (phone farm, ad account warm-up) với số liệu.