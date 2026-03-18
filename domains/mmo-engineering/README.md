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
3. **Advanced Stealth ✨** – Vượt hố đen TLS (JA3/JA4) fingerprint và che giấu lỗ rò CDP.
4. **Automation Stack** – browser, mobile, GUI automation, OTP handling.
5. **AI-Driven Farming ✨** – Sử dụng LLM tích hợp RAG chống nhận diện spam kịch bản cứng, debate tự động, tăng Trust Account thật giả bất khuất.
6. **Tool Development** – Python foundations, API/GUI automation, pack/release tools.
5. **Crypto Sybil Ops** – funding hygiene, randomization, wallet management.

## 3. Modules

| Module | File |
| --- | --- |
| Browser Fingerprinting | [browser-fingerprinting.md](./browser-fingerprinting.md) |
| Advanced Mạng Stealth | [anti-detect/tls-and-cdp-stealth.md](./anti-detect/tls-and-cdp-stealth.md) *(TLS Fingerprinting, Custom Chromium)* ✨ |
| Proxy Infrastructure | [proxy-infrastructure.md](./proxy-infrastructure.md) |
| Automation Tools | [automation-tools.md](./automation-tools.md) |
| AI-Driven Farming | [automation-tools/ai-driven-farming.md](./automation-tools/ai-driven-farming.md) *(Bots hóa thân LLM RAG debate mượt mà)* ✨|
| Crypto Sybil Strategies | [crypto-sybil.md](./crypto-sybil.md) |
| Tool Development | [tool-dev/README](./tool-dev/python-foundation.md) *(packaging, licensing, CI)* |
| Captcha & Challenge Solving | [captcha/INDEX](./captcha/README.md) *(reCAPTCHA, hCaptcha, Turnstile, OCR, audio)* |
| Network Layer (4G/Providers) | [network/INDEX](./network/4g-farm-hardware-guide.md) |
| Platform Playbooks | [platforms/INDEX](./platforms/README.md) *(Facebook/TikTok/Google)* |
| Behavioral Biometrics Spoofing| [platforms/behavioral-biometrics.md](./platforms/behavioral-biometrics.md) *(Qua mặt phân tích lực gõ phím, vuốt màn hình)* ✨|
| Operations & Monitoring | [operations/README](./operations/farm-dashboard.md) *(new)* |
| Operational Monitoring | [operations-monitoring.md](./operations-monitoring.md) |
| Case Studies | [case-studies.md](./case-studies.md) *(Phone farm, warm-up, bot ops, airdrop)* |
| **MMO Thao Trường Labs** | **[labs/README.md](./labs/README.md)** *(Diy 4G Proxy, Gỡ Cloudflare, Cày Reddit AI Vằng Tốc Thực Chiến Lõi)* ✨ |

## 4. Economics & ROI Modeling

- **Cost Stack:**
  - `CapEx`: phone farm hardware, PC controller, SIM modem.
  - `OpEx`: proxy 4G/residential fee, SIM top-up, tool license, nhân sự vận hành.
  - `Failure Cost`: account bị ban, checkpoint (chi phí thay thế).
- **KPIs chính:**
  - `CPA_farm` (Cost per Account) = (CapEx amortized / số account hoạt động) + OpEx chia theo chu kỳ.
  - `Revenue_per_account` = GMV * take rate hoặc hoa hồng trung bình.
  - `ROI` = `(Revenue_per_account - CPA_farm) / CPA_farm`.
- **Break-even Analysis:**

| Item | Sample value |
| --- | --- |
| CapEx phone rack | $3,500 (khấu hao 12 tháng) |
| OpEx/tháng | $1,200 (proxy 600 + SIM 400 + điện/nv 200) |
| Active accounts | 300 |
| CPA_farm | $3,500/12/300 + $1,200/300 ≈ **$5.6/account/tháng** |
| Revenue/account | $8.0 |
| ROI | (8 - 5.6) / 5.6 ≈ **43%** |

- **Scenario planner:**
  - Track churn rate: nếu `ban_rate > 15%/tháng` → CPA tăng mạnh, cần nâng health.
  - Sensitivity: mô phỏng khi proxy giá tăng 20% hoặc trust score giảm khiến revenue/account giảm.
- **Tools:** Google Sheets, AirTable, hoặc script Python đọc log ROI (kết nối [operations-monitoring.md](./operations-monitoring.md) để lấy metrics run-time).
- **Decision Gate:** chỉ scale farm mới khi ROI > target (ví dụ 30%) và break-even < 45 ngày.

## 5. Risk & Ethics Checklist

- [ ] Kiểm tra luật địa phương (anti-spam, cybercrime). Tránh sử dụng vào hoạt động phi pháp.
- [ ] Đọc kỹ ToS của platform (Facebook, Google, TikTok). Vi phạm có thể dẫn tới kiện tụng.
- [ ] Tách môi trường thí nghiệm với tài khoản cá nhân (OpSec tối thiểu).
- [ ] Không share dữ liệu người dùng thật, tuân thủ privacy (GDPR, PDPA).
- [ ] Xây dựng incident plan: nếu farm bị compromise, cách revoke access và báo cáo.

## 6. Next Steps

- Hoàn thiện module Tool Dev (đã bổ sung anti-detect integration, lab scripts, deployment tips).
- Mở rộng lab scripts (ví dụ reset 4G IP, quản lý ví, profile health check) và thêm dashboard tham chiếu.
- Mở rộng case study (phone farm, ad account warm-up) với số liệu. → xem [case-studies.md](./case-studies.md).
- Chuẩn hóa CI/CD cho tool nội bộ → xem mục dưới.

---

## 7. CI/CD cho MMO Tools

- **Repo Structure:**
  - `src/automation/`: script Puppeteer/Playwright.
  - `src/ops/`: ADB, proxy manager, monitoring agent.
  - `tests/`: unit test + smoke test (fake platform sandbox).
- **CI Pipeline (GitHub Actions/GitLab CI):**
  1. Lint & unit test (pytest, jest) cho mỗi PR.
  2. Build artifact (PyInstaller/Node pkg) + sign checksum.
  3. Static analysis (Semgrep, dependency audit) để tránh malware nội bộ.
- **CD Flow:**
  - Release branch tag `tool-vX.Y`. Pipeline upload artifact lên S3/MinIO + cập nhật changelog.
  - Automation để push config mới tới ops server qua Ansible.
  - Rollout wave: 10% farm → 50% → 100% nếu không thấy alert bất thường (theo [operations-monitoring.md](./operations-monitoring.md)).
- **Feature Flags:** mô tả YAML/JSON (enable_email_verify, disable_auto_post) để ops bật/tắt mà không rebuild.
- **Secret Handling:** dùng Vault hoặc sops để mã hóa API key, OTP seed; CI giải mã bằng OIDC token, không hardcode.
- **Release Checklist:**
  - [ ] Test pass & artifact signed.
  - [ ] Docs/changelog cập nhật.
  - [ ] Rollback plan (giữ bản N-1 trên repo).
  - [ ] Ops team xác nhận nhận tool qua Telegram/Slack bot.