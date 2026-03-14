---
title: "Finance Domain Playbook cho Developer & BA"
description: "Tư duy hệ thống, quy trình nghiệp vụ, dữ liệu và compliance khi xây sản phẩm tài chính."
last_updated: 2026-03-04
---

# 🏦 Finance Domain Playbook cho Developer & Business Analyst

> Để làm việc hiệu quả với ngân hàng, fintech, bảo hiểm, dev & BA cần hiểu cách dòng tiền vận hành, hệ thống lõi hoạt động và quy định chi phối. Bài này là bản đồ tóm tắt những gì bạn cần nắm để dịch yêu cầu nghiệp vụ sang giải pháp kỹ thuật.

---

## 1. Finance Landscape: Ai làm gì?

| Segment | Vai trò chính | Sản phẩm tiêu biểu | Xu hướng tech |
| --- | --- | --- | --- |
| **Banking (Retail/Corporate)** | Huy động vốn, cho vay, thanh toán | Tài khoản thanh toán, tín dụng, LC, treasury | Core banking hiện đại, API banking, Open Finance |
| **Payments & Fintech** | Kết nối merchant, ví điện tử, switch | Cổng thanh toán, BNPL, QR, remittance | ISO 20022, realtime payment, fraud engine AI |
| **Securities/Brokerage** | Giao dịch cổ phiếu, trái phiếu, phái sinh | Trading app, margin lending | Low-latency system, event-driven OMS |
| **Insurance (Life/P&C)** | Quản lý rủi ro, sản phẩm bảo hiểm | Hợp đồng nhân thọ, sức khỏe, xe | Policy admin platform, automation claims |
| **Asset Management** | Quỹ đầu tư, wealth management | Mutual fund, ETF, private fund | Portfolio analytics, risk dashboards |

> Dev cần xác định mình đang phục vụ segment nào để hiểu rõ stakeholder (Risk, Compliance, Ops, Relationship Manager...)

---

## 2. Bản đồ quy trình nghiệp vụ

### 2.1 Banking – Retail Lending
1. **Onboarding & KYC:** thu thập hồ sơ, định danh (eKYC, OTP). Hệ thống liên quan: KYC engine, AML screening.
2. **Credit Evaluation:** gọi các dịch vụ scoring (CIC/credit bureau, nội bộ). Risk model sử dụng data transaction, thu nhập.
3. **Account/Loan Setup:** tạo hợp đồng, lịch trả nợ. Core banking cập nhật GL (general ledger).
4. **Disbursement & Repayment:** kết nối payment switch, collection engine, nhắc nợ tự động.

### 2.2 Payments – Card & QR
1. Merchant đăng ký (KYB) → thiết lập MID/TID.
2. Giao dịch phát sinh → chuyển qua Payment Gateway → Switch (Napas/Visa/Master).
3. Clearing & Settlement → cuối ngày đối soát file (Recon) giữa các bên.
4. Chargeback/Fraud → engine phát hiện bất thường, workflow xử lý tranh chấp.

### 2.3 Securities – Trade Lifecycle
1. Order placement (FIX API, Web/Mobile) → OMS.
2. Risk checks: margin, position limit.
3. Matching tại Sở (HOSE/HNX) → confirm về broker.
4. Clearing (T+2) → Depository (VSD) cập nhật sở hữu.

### 2.4 Insurance – Policy Lifecycle
Quy trình Quote → Underwriting → Policy Issuance → Claims. Automation cần tích hợp actuarial tables, document workflow, payout engine.

---

## 3. Hệ thống & kiến trúc điển hình

| Layer | Mô tả | Ví dụ hệ thống |
| --- | --- | --- |
| **Core Systems** | Ghi nhận giao dịch, số dư, hợp đồng | Core banking (Temenos, Finacle), Core insurance, Ledger |
| **Channel Layer** | App/Web, branch, call center | Mobile banking, trading app |
| **Integration Layer** | ESB/API Gateway, message broker | Mulesoft, Kong, Kafka |
| **Risk & Compliance** | AML, fraud detection, credit scoring | Fircosoft, Feedzai, SAS | 
| **Data & Analytics** | DWH, regulatory reports, BI | Oracle DWH, PowerBI, Basel reporting |
| **External Services** | Credit bureau, payment switch, govt APIs | CIC, Napas, e-invoice, eKYC provider |

**Patterns quan trọng:**
- Event sourcing để audit giao dịch.
- Saga/Orchestration cho quy trình phức tạp (giải ngân, claims).
- Idempotency & retry cho API thanh toán.
- Dual-write vs. outbox để đảm bảo nhất quán core & downstream.

---

## 4. Dữ liệu & chuẩn thông điệp

| Chuẩn | Dùng ở đâu | Dev cần lưu ý |
| --- | --- | --- |
| **ISO 8583** | Thẻ (ATM/POS) message | MTI, bitmap, field 2 (PAN), field 35 (track2), field 55 (EMV). Phải mask PAN khi log. |
| **ISO 20022** | Thanh toán realtime, cross-border | MX messages (pacs.008, pain.001). XML schema chặt chẽ, versioning. |
| **SWIFT MT/MX** | Liên ngân hàng quốc tế | MT103 (remittance), MT940 (statement). Bảo mật (SWIFTNet). |
| **FIX Protocol** | Chứng khoán | Low latency, tag-based, cần session management. |

**Data models phổ biến:** Customer 360, Account, Transaction, Product hierarchy, Limit/Exposure, GL chart of accounts.

> Checklist: xác định dữ liệu nhạy cảm (PII, PCI-DSS) → áp dụng tokenization, encryption, access control.

---

## 5. Compliance & Risk cho dev/BA

- **KYC/AML:** phải tích hợp screening danh sách đen (OFAC, UN), theo dõi giao dịch đáng ngờ (STR). Logging đầy đủ.
- **PCI DSS / Data privacy:** hạn chế lưu thẻ, dùng vault/token. Đảm bảo cryptography, key rotation.
- **Regulatory Reporting:** NHNN/SSC yêu cầu file định dạng chuẩn, timeline cố định. Build pipeline data + validation.
- **Audit Trail:** mọi thao tác nhạy cảm phải có trail (user, timestamp, before/after). Thường dùng event log hoặc CDC.
- **Business Continuity:** DR site, RPO/RTO. Dev cần thiết kế replication và switch-over plan.

---

## 6. Use case cho Developer

1. **API Banking Sandbox:** thiết kế API account inquiry, payment initiation với rate limit, OAuth2, consent log.
2. **Payment Switch Integration:** xử lý ISO8583, map field, đảm bảo idempotent khi retry.
3. **Fraud Detection Pipeline:** ingest real-time transaction → feature store → model scoring → action (block/allow) trong <300ms.
4. **Loan Origination Workflow:** xây microservice orchestrator gọi KYC, scoring, document service, e-sign.
5. **RegTech Automation:** sản xuất báo cáo Basel III (LCR, CAR) từ data warehouse.

---

## 7. Use case cho Business Analyst

1. **Process Mapping:** vẽ swimlane cho quy trình tín dụng, xác định touchpoint IT.
2. **Requirement Breakdown:** chuyển yêu cầu NHNN (thông tư) thành rule config (VD: giới hạn room tín dụng theo ngành).
3. **Data Requirement Spec:** xác định trường cần lưu trong AML monitoring, mapping nguồn dữ liệu.
4. **UAT Planning:** định nghĩa test case end-to-end (loan từ hồ sơ đến tất toán), mô phỏng dữ liệu thật.
5. **Stakeholder Alignment:** điều phối Risk, Compliance, IT, Product – tạo RACI rõ ràng.

---

## 8. Checklist triển khai dự án Finance

- [ ] Xác định regulatory scope (NHNN, SSC, MOF...).
- [ ] Liệt kê hệ thống cần tích hợp và giao thức (API, file, MQ).
- [ ] Đánh giá dữ liệu nhạy cảm → kế hoạch bảo mật.
- [ ] Thiết lập môi trường test với data giả lập nhưng realist.
- [ ] Định nghĩa SLA/OLA giữa các hệ thống.
- [ ] Chuẩn bị playbook xử lý sự cố (fraud spike, hệ thống thanh toán down).
- [ ] UAT & kiểm thử hiệu năng (TPS, latency) sát với production.

---

## 9. Tài nguyên đề xuất

- **Sách:** “Bank 4.0” (Brett King), “Payments Systems in the U.S.”, “Trading and Exchanges” (Larry Harris).
- **Chuẩn mực:** Basel III docs, PCI DSS v4.0, ISO 20022 docs.
- **Blog/Community:** Finextra, The Financial Brand, MAS Tech Stack, Vietfintech.
- **Dataset/API:** NHNN, World Bank, open banking sandbox (Singapore, UK), VNPay/Napas docs.

> Gợi ý tiếp theo: đào sâu từng mảng (VD: core banking modernization, insurance policy admin) bằng cách tạo file chuyên sâu riêng.