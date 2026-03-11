---
title: "Zero Trust Architecture"
description: "mTLS everywhere, identity proxy, least privilege cho backend."
tags:
  - backend
  - security
  - architecture
updated: 2026-03-11
---

# 🔐 Zero Trust Architecture (2024-2026)

## 1. Principles
- **Never trust, always verify:** mọi request phải được authenticate/authorize, kể cả nội bộ.
- **Assume breach:** segment network, monitor lateral movement.
- **Continuous evaluation:** identity, device posture, context.

## 2. mTLS Everywhere
- **Service-to-service:** Istio/Linkerd Envoy sidecar cấp cert động, rotate thường xuyên.
- **Client-to-edge:** TLS termination ở edge + re-encrypt vào mesh.
- **Certificate management:** SPIRE/SPIFFE cấp danh tính workload.

## 3. Identity-aware Proxy
- **IAP/BeyondCorp:** proxy đứng trước app, kiểm tra identity + device.
- **Tool:** Google IAP, Cloudflare Access, Pomerium.
- **Granular policy:** RBAC/ABAC theo người dùng, nhóm, điều kiện (context-aware access).

## 4. Least Privilege Patterns
- **Microsegmentation:** phân vùng network, chỉ mở port cần thiết.
- **Policy-as-code:** OPA, Cedar để enforce ở API gateway, service mesh, DB.
- **Just-in-time access:** tự động cấp quyền tạm thời qua approval flow.
- **Secrets management:** HashiCorp Vault, AWS Secrets Manager, rotate.

## 5. Observability & Threat Detection
- **Telemetry:** log mọi authz decision, mTLS handshake, denied traffic.
- **SIEM/SOAR integration:** phát hiện hành vi bất thường.
- **Zero trust posture score:** theo dõi coverage.

## ✅ Apply it
- [ ] Bật mTLS trong mesh hoặc API gateway, kiểm tra cert rotation.
- [ ] Đặt identity-aware proxy trước admin/internal tools, enforce SSO + device posture.
- [ ] Viết policy OPA/Cedar cho CRUD API quan trọng.
- [ ] Triển khai secret rotation tự động, audit secret usage.
- [ ] Thiết lập dashboard zero-trust (coverage, denied requests, policy drift).

## 🔗 Cross-reference
- [security/backend-security.md](../security/backend-security.md)
- [devops-sre/kubernetes-patterns.md](../devops-sre/kubernetes-patterns.md) – mTLS, network policy.
- [architecture/platform-engineering.md](./platform-engineering.md) – self-service nhưng vẫn zero trust.
- [monitoring-observability.md](../monitoring-observability.md) – log/metric phục vụ threat detection.