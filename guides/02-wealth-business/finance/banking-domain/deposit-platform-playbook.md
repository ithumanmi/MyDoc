---
title: "Deposit Platform Playbook"
description: "Thiết kế và vận hành nền tảng tiền gửi (CASA, TD, savings) cho dev/BA."
last_updated: 2026-03-04
---

# 🏦 Deposit Platform Playbook

> Deposits (CASA, tiết kiệm, kỳ hạn) là nguồn vốn rẻ nhất của ngân hàng. Dev/BA cần hiểu cấu trúc sản phẩm, quy trình và hệ thống để triển khai nhanh các gói tài khoản, chương trình lãi suất và liên thông với kênh số.

---

## 1. Sản phẩm & cấu trúc

| Nhóm sản phẩm | Đặc điểm | Tham số cần cấu hình |
| --- | --- | --- |
| **CASA (Current & Savings Account)** | Không kỳ hạn, hỗ trợ thanh toán | loại tài khoản, phí duy trì, lãi suất bậc thang, hạn mức giao dịch |
| **Time Deposit (TD)** | Có kỳ hạn (1-36 tháng), lãi cố định | kỳ hạn, lãi suất theo kỳ, phương thức tái tục, tất toán trước hạn |
| **Combo packages** | Bundled với thẻ, e-banking | điều kiện duy trì số dư, cashback, fee waiver |
| **FX/Multicurrency** | Giữ ngoại tệ | loại tiền, tỷ giá, phí chuyển đổi |

> Thiết kế Product Factory phải cho phép BA cấu hình: interest rule, fee rule, tier, campaign.

---

## 2. Quy trình nghiệp vụ chính

1. **Account Opening**: KYC (eKYC hoặc branch), chọn sản phẩm, ký điều khoản, tạo số tài khoản. Integrate với KYC engine, AML.
2. **Funding & Sweeps**: Nạp tiền via cash, chuyển khoản, payroll. Có thể set auto-sweep giữa CASA ↔ TD.
3. **Interest Accrual & Posting**: Hệ thống tính lãi hàng ngày (EOD batch) hoặc real-time, post vào account hoặc GL.
4. **Fee Management**: thu phí duy trì, phí giao dịch, waiver theo điều kiện.
5. **Statements & Notifications**: e-statement, push/email, regulatory notice (NHNN).
6. **Closure & Dormant**: xử lý tài khoản không hoạt động, báo cáo NHNN.

---

## 3. Hệ thống & tích hợp

- **Deposit Module/Core**: quản lý account master, balance, interest.
- **GL/Accounting**: mapping chart of accounts, tự động bút toán.
- **Payment Switch**: Napas, SWIFT cho giao dịch ra/vào.
- **Channels**: mobile/web, branch teller, API partner.
- **Campaign Engine**: apply lãi suất/fee đặc biệt.
- **Reporting**: NHNN báo cáo 01/BC-TTT, AML monitoring.

**Integration pattern**: API cho real-time (balance inquiry, hold funds), batch/file cho interest posting, regulatory reporting.

---

## 4. Dữ liệu & mô hình

Entity chính: Customer, Account, Product, Balance, Transaction, Fee, InterestSchedule.

| Trường quan trọng | Mục đích | Lưu ý |
| --- | --- | --- |
| `account_status` | Active/Dormant/Closed | trigger workflow xử lý |
| `interest_method` | simple, daily balance, average daily balance | ảnh hưởng engine tính lãi |
| `hold_amount` | Số dư bị hold (VD: pending card txn) | cần real-time update |
| `sweep_rule` | Cấu hình auto transfer | support multi-tier |

> Dữ liệu phải tuân PCI/PII: mask số tài khoản, encrypt data at rest.

---

## 5. KPI & Monitoring

| KPI | Ý nghĩa | Target gợi ý |
| --- | --- | --- |
| CASA/Total deposit ratio | Mức vốn rẻ | > 50% đối với ngân hàng retail |
| Time-to-launch sản phẩm mới | Tốc độ product factory | < 2 tuần |
| Interest accuracy | Sai lệch tính lãi | < 0.01% tổng lãi |
| API latency cho balance inquiry | Trải nghiệm digital | < 200ms |

Alert: theo dõi mismatch GL vs. account ledger, volume dormant.

---

## 6. Checklist triển khai

- [ ] Thiết kế product catalog + metadata.
- [ ] Xác định công thức tính lãi, test với data sample.
- [ ] Tích hợp KYC/AML trước khi mở tài khoản.
- [ ] Xây interface balance inquiry, statement API.
- [ ] Thiết lập batch EOD: interest, fee, reconciliation.
- [ ] Chuẩn hóa báo cáo NHNN, AML scenario.
- [ ] Đảm bảo DR & backup cho ledger.

---

## 7. Use case mẫu

1. **Ra mắt gói tài khoản lãi suất bậc thang**: BA cấu hình tier trong product factory, dev cập nhật API interest preview. Test scenario: thay đổi tier, retroactive.
2. **Auto-sweep sang kỳ hạn khi số dư > X**: workflow event-driven (Kafka) kích hoạt job chuyển tiền, update TD account.
3. **Digital onboarding 100% online**: tích hợp eKYC, e-sign, instant account issuance, push notification.

---

## 8. Tài liệu tham khảo

- Temenos Deposits module, Thought Machine Vault docs.
- NHNN thông tư về tiền gửi (VD: 48/2018/TT-NHNN).
- ISO 20022 camt.* messages cho statement.
- Case study DBS digibank (deposit factory).