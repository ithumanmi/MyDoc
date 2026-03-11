---
title: "Platform Engineering"
description: "IDP, golden paths, self-service infra cho đội dev."
tags:
  - backend
  - architecture
  - platform
updated: 2026-03-11
---

# 🛠️ Platform Engineering (2024-2026)

## 1. Internal Developer Platform (IDP)
- **Goal:** chuẩn hoá toolchain, cung cấp self-service environment.
- **Stack:** Backstage, Humanitec, Port, internal portal.
- **Capabilities:** service catalog, template scaffold, runtime provisioning, policy guardrail.

## 2. Golden Paths & Templates
- **Golden path:** quy trình chuẩn cho use case (build API, tạo job, deploy feature flag).
- **Templates:** tạo repo kèm CI/CD, observability, security baseline.
- **Automation:** CLI/portal click → tạo infra via IaC (Terraform, Crossplane).

## 3. Self-service Infrastructure
- **Environment on-demand:** dev tạo sandbox cluster/namespace.
- **Infra as product:** platform team sở hữu SLA, support, roadmap.
- **Guardrails:** policy-as-code (OPA, Kyverno) enforce security.

## 4. Telemetry & Feedback
- **Success metric:** lead time, infra ticket giảm, adoption golden path.
- **Feedback loop:** developer survey, feature usage analytics.

## ✅ Apply it
- [ ] Audit hiện trạng toolchain (CI, CD, observability) → xác định gap cần platform.
- [ ] Thiết kế service catalog + template (Backend API, Worker, Data pipeline).
- [ ] Build POC IDP (Backstage + plugin) với self-service provision namespace.
- [ ] Tích hợp policy guardrail (OPA) trong pipeline IDP.
- [ ] Đo metric DORA trước/sau rollout.

## 🔗 Cross-reference
- [deployment-guide.md](../deployment-guide.md) – pipeline CI/CD nền tảng.
- [devops-sre/devops-lab-pack.md](../devops-sre/devops-lab-pack.md) – lab automation.
- [architecture/modular-monolith.md](./modular-monolith.md) – chuẩn module trước khi templatize.
- [security/zero-trust-architecture.md](./zero-trust-architecture.md) – policy khi self-service infra.