---
title: "Core Banking Modernization Playbook"
description: "Chiến lược chuyển đổi core banking: động lực, kiến trúc mục tiêu, migration và công nghệ."
last_updated: 2026-03-04
---

# 🧠 Core Banking Modernization Playbook

> Core banking là trái tim của ngân hàng. Việc hiện đại hóa quyết định khả năng ra mắt sản phẩm nhanh, mở API cho đối tác và tuân thủ quy định mới. Bài này giúp dev/BA hiểu bức tranh tổng thể khi tham gia các chương trình chuyển đổi core.

---

## 1. Vì sao phải hiện đại hóa?

| Driver | Dấu hiệu | Tác động đến tech |
| --- | --- | --- |
| **Time-to-market** | Ra mắt sản phẩm mới mất 6-12 tháng vì code COBOL, batch | Cần modular architecture, product factory |
| **Cost & Ops burden** | Mỗi năm tốn hàng triệu $ để vận hành mainframe, khó tuyển người | Ưu tiên move to cloud/hybrid, automation ops |
| **Regulatory pressure** | Basel III, IFRS9, eKYC yêu cầu dữ liệu real-time | Tăng nhu cầu streaming data, API event |
| **Open finance & ecosystem** | Đối tác yêu cầu API realtime, webhook | Cần API gateway, consent management |
| **Resilience & scalability** | Batch overnight, downtime 4-6h | Hướng tới active-active, zero-downtime release |

> Chia rõ business driver (product, regulatory, cost) giúp team tech ưu tiên đúng hình thức hiện đại hóa.

---

## 2. Các lựa chọn chiến lược

| Approach | Mô tả | Ưu điểm | Rủi ro |
| --- | --- | --- | --- |
| **Rip & Replace** | Thay core cũ bằng core mới trong 1 lần big bang | Đơn giản hóa landscape, tận dụng core modern | Rủi ro cao, downtime dài, phụ thuộc vendor |
| **Progressive Renovation** | Xây core mới theo mô-đun, chuyển từng sản phẩm | Giảm rủi ro, song song vận hành | Complexity tích hợp, cần governance mạnh |
| **Augment ring-fenced** | Giữ core cũ, xây layer mới cho sản phẩm số | Time-to-market nhanh, ít đụng core cũ | Dễ tạo “spaghetti” nếu không kiểm soát dữ liệu |
| **Composable/Packaged business capabilities** | Xây core dựa trên dịch vụ theo domain | Linh hoạt, dễ scale | Yêu cầu năng lực thiết kế domain, DevOps cao |

> Nhiều ngân hàng chọn “two-speed architecture”: core cũ phục vụ sản phẩm legacy, core mới hỗ trợ digital lending/payments.

---

## 3. Target Architecture Blueprint

```
Channel (Mobile, Web, Branch, Partner API)
        ↓
Experience Layer (API Gateway, BFF, Consent)
        ↓
Domain Services (Customer, Accounts, Lending, Payments)
        ↓
Core Ledger & Product Factory (COTS hoặc build)
        ↓
Data Layer (Operational Data Store, Event Streaming, DWH)
        ↘ Compliance & Reporting (Basel, IFRS)
```

### Thành phần chính
1. **Product Factory:** cấu hình sản phẩm ngân hàng bằng metadata (pricing, fee, limit) thay vì hard-code.
2. **Account & Ledger services:** tách account servicing và GL để dễ audit, hỗ trợ multi-currency.
3. **Event streaming layer:** mọi giao dịch phát ra event (Kafka/Pulsar) phục vụ realtime analytics, fraud, notification.
4. **API & Security:** OAuth2/OpenID, consent, rate limit, idempotency key, audit trail.
5. **DevOps Platform:** CI/CD, IaC cho core (containerized hoặc VM), chaos testing.

---

## 4. Chiến lược Migration

| Bước | Mô tả | Lưu ý |
| --- | --- | --- |
| **Inventory & Domain mapping** | Liệt kê sản phẩm, quy trình, interface | Dựa vào Banking Capability Map (Customer, Deposit, Lending...) |
| **Data cleansing & modeling** | Chuẩn hóa số dư, trạng thái hợp đồng | Cần reconciliation tool, golden source |
| **Parallel run** | Vận hành core mới & cũ song song | So sánh báo cáo, transaction log |
| **Migration packages** | Di chuyển theo cohort (VD: tài khoản thanh toán, sau đó thẻ...) | Update channel/app theo batch |
| **Cutover & stabilization** | Chuyển traffic, monitoring chặt | Playbook rollback, war room |

**Patterns hữu ích:**
- **Strangler Fig**: wrap core cũ bằng API, chuyển từng domain sang core mới.
- **Data replication + CDC**: đồng bộ thay vì batch (GoldenGate, Debezium, Kafka Connect).
- **Feature toggles**: chuyển dần user sang core mới.

---

## 5. Công nghệ & Vendor landscape

- **Core COTS**: Temenos T24 Transact, Thought Machine Vault, Mambu, Finacle, TCS BaNCS.
- **Cloud-native stack**: Kubernetes, service mesh, event streaming (Kafka, Pulsar), database (CockroachDB, YugabyteDB, Oracle). 
- **Security & Compliance**: HashiCorp Vault (key management), Thales HSM, OpenTelemetry cho observability.
- **Testing tool**: service virtualization (Parasoft, Wiremock), performance lab (JMeter, k6).

> Chọn vendor theo tiêu chí: hỗ trợ regulatory VN, lộ trình product, khả năng mở rộng API, mô hình triển khai (on-prem, cloud, hybrid).

---

## 6. Operating Model & Team

- **Platform team** quản lý core services, DevSecOps, SRE.
- **Domain squad** (Deposit/Lending/Payments) chịu trách nhiệm product backlog + integration.
- **Data & Reporting team** xây pipeline regulatory (NHNN, Basel).
- **Governance**: Architecture board, Change Advisory Board (CAB) cho cutover.
- **Skill uplift**: đào tạo COBOL dev chuyển sang Java/Kotlin, Go; BA học domain event, product factory config.

---

## 7. KPI & Success Metrics

| Nhóm | KPI | Target gợi ý |
| --- | --- | --- |
| **Delivery** | Thời gian ra mắt sản phẩm mới | < 4 tuần để launch feature digital |
| **Reliability** | Core availability | ≥ 99.99% với active-active |
| **Performance** | TPS tối đa | 5-10k TPS cho payment realtime |
| **Cost** | OPEX vận hành core | Giảm 20-30% sau 2 năm |
| **Compliance** | Số lỗi audit | 0 finding nghiêm trọng |

---

## 8. Case study tóm tắt

- **Thought Machine + Mambu tại ngân hàng số SEA**: bắt đầu từ sản phẩm mới (digital lending) → sau 18 tháng chuyển dần tài khoản thanh toán.
- **BBVA**: áp dụng mô hình domain-driven, xây platform API, sau đó tách dịch vụ payments từ core cũ. Sử dụng event sourcing + streaming cho data.
- **NAB (Úc)**: triển khai progressive renovation, 400+ API public, di chuyển theo wave, dev/BA tham gia “product factory squad”.

---

## 9. Checklist cho dự án core banking

- [ ] Định nghĩa business driver + target KPI rõ ràng.
- [ ] Thiết lập architecture principle (cloud-first, API-first, event-driven...).
- [ ] Map domain → quyết định rollout sequence.
- [ ] Chuẩn hóa dữ liệu & thiết kế pipeline migration.
- [ ] Thiết kế framework test: functional, performance, failover.
- [ ] Kế hoạch vận hành song song & cutover.
- [ ] Chương trình change management: đào tạo người dùng nội bộ, update SOP.

---

## 10. Tài liệu đề xuất

- Bain, McKinsey core banking modernization report.
- Temenos/Thought Machine whitepaper.
- Open Banking API specs (UK OBIE, Singapore SGFinDex).
- Sách “Core Banking Systems: Platforms, Innovation, Integration”.
- Podcast: 11:FS FinTech Insider (chủ đề core transformation).

> Bước tiếp theo: tạo playbook chi tiết cho từng domain (Deposit, Lending, Payments) và template đánh giá vendor.