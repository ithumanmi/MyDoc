---
title: "Lending Platform Playbook"
description: "Blueprint cho khoản vay bán lẻ/doanh nghiệp: quy trình, scoring, servicing và công nghệ."
last_updated: 2026-03-04
---

# 💳 Lending Platform Playbook

> Tín dụng là nguồn doanh thu chính nhưng cũng là rủi ro lớn. Playbook này giúp dev/BA hiểu vòng đời khoản vay, hệ thống cần tích hợp và chỉ số theo dõi khi xây nền tảng lending hiện đại.

---

## 1. Phạm vi sản phẩm

| Segment | Sản phẩm | Phức tạp |
| --- | --- | --- |
| **Retail lending** | Personal loan, credit card, BNPL | yêu cầu onboarding nhanh, scoring tự động |
| **Secured lending** | Mortgage, auto loan | cần quản lý tài sản đảm bảo, giải ngân nhiều đợt |
| **SME/Corporate** | Working capital, trade finance | quy trình phê duyệt nhiều cấp, limit theo công ty |

> Lựa chọn tech stack khác nhau: retail ưu tiên straight-through processing, corporate cần workflow tùy biến.

---

## 2. Loan Lifecycle

1. **Lead & Application**: thu thập thông tin khách hàng, thu nhập, giấy tờ. Channel: mobile/web/branch/partner API.
2. **KYC & Document**: eKYC, OCR đọc hồ sơ, lưu trữ trên DMS.
3. **Credit Scoring**: gọi CIC/credit bureau, nội bộ transaction, dùng machine learning.
4. **Underwriting & Approval**: rule engine (policy), manual review (risk officer) nếu > limit.
5. **Contracting & Disbursement**: e-sign, tạo hợp đồng, giải ngân qua payment switch hoặc escrow.
6. **Servicing**: tính lãi, thu nợ định kỳ, xử lý tất toán sớm, restructuring.
7. **Collections & Recovery**: nhắc nợ (soft), chuyển sang thu hồi (hard), bán nợ.

Workflow thường chia microservice: application, decisioning, account servicing, collections.

---

## 3. Hệ thống & tích hợp

- **LOS (Loan Origination System)**: quản lý onboarding đến approval.
- **LMS/Core Lending**: quản lý hợp đồng, lịch trả, interest accrual.
- **Decisioning/Rule Engine**: Drools, FICO Blaze, in-house ML service.
- **Document Management**: lưu hồ sơ, versioning, audit.
- **Collections Platform**: workflow, dialer, SMS.
- **Data/Analytics**: PD/LGD/ECL, IFRS9.
- **External services**: CIC, eKYC provider, property valuation, vehicle registry.

Integration: event-driven cho status loan, API cho scoring, batch cho báo cáo regulatory.

---

## 4. Dữ liệu & mô hình

Entity chính: Application, Customer, LoanAccount, Collateral, Schedule, Repayment, Delinquency.

| Data point | Mục đích | Lưu ý |
| --- | --- | --- |
| `credit_score` | Quyết định lãi suất, limit | lưu cả source và thời điểm |
| `DSR` (Debt Service Ratio) | Đánh giá khả năng trả nợ | update khi thêm khoản vay |
| `MIS bucket` | Days past due | drive collection strategy |
| `collateral_value` | Tính LTV | cần cập nhật định kỳ |

> Tuân thủ bảo mật hồ sơ: mã hóa giấy tờ, phân quyền truy cập.

---

## 5. Automation & AI

- **Pre-screen ML**: phân loại hồ sơ low risk → auto approve.
- **Income estimation** từ banking transaction.
- **Fraud detection**: phát hiện synthetic identity.
- **Collections prioritization**: xếp thứ tự gọi nhắc nợ dựa trên propensity.

---

## 6. KPI & Risk Metrics

| Nhóm | KPI | Target |
| --- | --- | --- |
| **Growth** | Approval rate | 30-50% (tuỳ segment)
| **Speed** | Time to yes | < 5 phút retail, < 3 ngày SME |
| **Risk** | NPL (Non-performing loan) | < 3% retail, < 2% mortgage |
| **Loss** | Net credit loss | theo budget |
| **Collections** | Cure rate per bucket | ≥ 70% bucket 1 |

---

## 7. Checklist triển khai

- [ ] Xác định policy & risk appetite, chuyển thành rule/scorecard.
- [ ] Thiết kế data contract cho application, scoring, approval.
- [ ] Xây integration với CIC/credit bureau, eKYC.
- [ ] Thiết lập workflow cho underwriting (manual + automated).
- [ ] Cấu hình repayment schedule, fee, penalty.
- [ ] Thiết lập collection strategy + tooling (SMS, call center, field).
- [ ] Chuẩn bị báo cáo regulatory (NHNN: dư nợ, phân loại nợ).

---

## 8. Use case

1. **Buy Now Pay Later**: cần instant scoring, merchant API, risk limit theo user, event-driven repayment.
2. **SME working capital**: require multi-party approval, collateral registry integration, disbursement theo milestone.
3. **Loan restructuring**: BA xác định rule restructure, dev update schedule recalculation + accounting entries.

---

## 9. Tài liệu tham khảo

- CIC, NHNN quy định phân loại nợ (VD: 02/2023/TT-NHNN).
- FICO best practices, Bain lending modernization report.
- Thought Machine Smart Contracts (lending), Mambu lending engine.
- IFRS9, Basel IRB guidelines.