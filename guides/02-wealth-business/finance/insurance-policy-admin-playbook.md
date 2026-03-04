---
title: "Insurance Policy Administration Playbook"
description: "Quy trình, hệ thống và dữ liệu cho vận hành hợp đồng bảo hiểm (Life & P&C)."
last_updated: 2026-03-04
---

# 🛡️ Insurance Policy Administration Playbook

> Policy Administration System (PAS) là lõi của doanh nghiệp bảo hiểm: định nghĩa sản phẩm, quản lý hợp đồng, dòng tiền phí và quyền lợi. Playbook này giúp dev/BA hiểu kiến trúc, dữ liệu và checklist khi triển khai PAS hiện đại.

---

## 1. Phạm vi & phân loại sản phẩm

| Segment | Ví dụ sản phẩm | Đặc trưng |
| --- | --- | --- |
| **Life Insurance** | Term life, Whole life, Unit-linked | hợp đồng dài hạn, premium định kỳ, riders |
| **Health/Group** | Health plan, Employee benefits | cần quản lý enrollment, capitation |
| **P&C (General)** | Motor, Home, Travel | kỳ hạn 1 năm, claim nhanh |
| **Bancassurance/Embedded** | Micro-insurance, loan protection | tích hợp với ngân hàng/merchant |

> PAS phải hỗ trợ cấu hình sản phẩm linh hoạt: coverage, benefit, phí, rider, underwriting rule.

---

## 2. Policy Lifecycle

1. **Product configuration**: định nghĩa coverage, premium table, underwriting rule, commission.
2. **Illustration & Quote**: tính phí dựa trên tuổi, giới tính, risk factor; xuất proposal.
3. **Application & Underwriting**: thu hồ sơ, eKYC, medical exam (life), rule engine đánh giá.
4. **Issuance & Policy setup**: cấp số hợp đồng, phát hành policy document, kích hoạt billing.
5. **Policy Servicing**: thay đổi thông tin, add rider, upgrade sum assured, holiday premium.
6. **Billing & Collection**: premium schedule, auto-debit, grace period, lapse.
7. **Claims & Payout**: tiếp nhận yêu cầu, kiểm tra điều kiện, tính toán quyền lợi, thanh toán.
8. **Renewal / Termination**: nhắc tái tục, xử lý surrender/maturity.

Mỗi giai đoạn liên quan các hệ thống: PAS, Underwriting, Billing, Claims, CRM.

---

## 3. Kiến trúc hệ thống

| Module | Vai trò |
| --- | --- |
| **Product & Rating Engine** | Metadata sản phẩm, bảng phí, rule |
| **Underwriting Engine** | Rule-based + ML, decision tree |
| **Policy Admin Core** | Lưu state hợp đồng, nhật ký thay đổi |
| **Billing & Payment** | Premium invoicing, collection, reconciliation |
| **Claims Management** | FNOL intake, assessment, approval |
| **Document & Communication** | Hợp đồng, endorsement, notifications |
| **Data Warehouse & Actuarial** | Reserving, IFRS17, risk analytics |

**Integration**: API cho bancassurance, batch với core banking, event streaming cho CRM/analytics.

---

## 4. Dữ liệu & cấu trúc

Entity chính: Product, Policy, Insured Person, Coverage, PremiumSchedule, Rider, Claim, Commission.

| Data field | Ý nghĩa | Lưu ý |
| --- | --- | --- |
| `policy_status` | Inforce, Lapsed, Pending | ảnh hưởng billing & claim |
| `sum_assured` | Số tiền bảo hiểm | thay đổi kéo theo phí |
| `premium_mode` | Annual/Quarterly/Monthly | tác động billing |
| `beneficiary` | Người thụ hưởng | cần encrypt, audit |
| `claim_status` | FNOL, Investigation, Approved | SLA theo loại sản phẩm |

> Data lineage quan trọng cho IFRS17/ICS. Phải hỗ trợ versioning (endorsement history).

---

## 5. Quy định & chuẩn mực

- **IFRS17**: đo lường liability theo nhóm hợp đồng, cần khoản mục CSM.
- **RBC (Risk-based capital)**: báo cáo vốn theo NHNN/Bộ Tài chính.
- **Data privacy**: bảo vệ thông tin sức khỏe, PII.
- **Anti-fraud**: kết nối cơ sở dữ liệu Bộ Tài chính, black list.

---

## 6. KPI & Metrics

| KPI | Giải thích | Target gợi ý |
| --- | --- | --- |
| Time-to-launch product | thời gian cấu hình sản phẩm mới | < 4 tuần |
| Policy issuance TAT | từ application đến inforce | < 3 ngày retail |
| First-year lapse rate | khách hàng hủy trong năm đầu | < 10% |
| Claims turnaround | thời gian từ FNOL đến payout | < 5 ngày health, < 15 ngày life |
| Straight-through processing rate | tỉ lệ hồ sơ auto approve | > 60% retail |

Monitoring: premium overdue, outstanding claims reserve, data reconciliation IFRS17.

---

## 7. Checklist triển khai

- [ ] Xây product catalog + rule engine support versioning.
- [ ] Thiết lập workflow underwriting (auto + manual review).
- [ ] Tích hợp billing với cổng thanh toán, core banking.
- [ ] Xây module policy servicing (endorsement, rider management).
- [ ] Thiết kế claims pipeline: FNOL intake, rule, fraud check.
- [ ] Chuẩn bị data mart cho actuarial (IFRS17, RBC).
- [ ] Cơ chế audit trail, document management, e-signature.

---

## 8. Use case minh họa

1. **Bancassurance**: core banking gửi event khoản vay mới → PAS phát hành loan protection policy tự động, billing gắn với repayment schedule.
2. **Unit-linked product**: integration với investment platform, daily NAV update, policyholder portal cho phép switch fund.
3. **Health group policy**: API enrollment (HR), card issuance, claim adjudication real-time với hospital network.

---

## 9. Công nghệ & vendor

- PAS vendors: Guidewire PolicyCenter (P&C), Duck Creek, Sapiens, Life Asia, FIS, in-house microservices.
- Rule/Rating: Drools, Earnix, in-house.
- Document/E-sign: Docusign, Adobe Sign, in-house template engine.
- Data/Actuarial: SAS IFRS17, Moody’s, in-house data lake.

Ưu tiên kiến trúc composable: tách product config, policy servicing, billing thành dịch vụ độc lập để dễ mở API.

---

## 10. Tài liệu tham khảo

- Bộ Tài chính VN: quy định bảo hiểm (Nghị định 46/2023/NĐ-CP).
- IFRS17 implementation guide.
- Guidewire, Duck Creek whitepaper.
- AON, McKinsey Insurance modernization report.