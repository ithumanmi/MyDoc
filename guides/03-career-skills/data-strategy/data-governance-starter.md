# 🛡️ Data Governance Starter Kit

> Thiết lập nền tảng quản trị dữ liệu nhẹ nhàng nhưng hiệu quả cho SMB/scale-up.

## 1. Trụ cột chính (3P)

| Pillar | Nội dung |
| --- | --- |
| **People** | Data Owner, Data Steward, Data Council |
| **Process** | Catalog, Quality checks, Incident response |
| **Platform** | Metadata store, Access control, Monitoring |

## 2. Vai trò & trách nhiệm

| Role | Trách nhiệm chính |
| --- | --- |
| **Data Owner** | Quyết định ai được dùng dữ liệu, approve thay đổi |
| **Data Steward** | Đảm bảo chất lượng, cập nhật catalog, training |
| **Data Custodian (IT)** | Quản lý hạ tầng, backup, bảo mật |
| **Data Governance Council** | Họp hàng tháng, xử lý dispute, phê duyệt policy |

## 3. Quy trình catalog tối giản

1. Chọn công cụ (Notion/Airtable hoặc giải pháp như Collibra, Atlan).
2. Template metadata: Tên bảng, mô tả, Owner, Freshness, SLA, Data Sensitivity.
3. Thiết lập workflow review: mỗi quý kiểm tra và cập nhật.

## 4. Data Quality Checklist (DAACE)

- **D**uplicates? (Trùng lặp, cần dedup)
- **A**ccuracy? (So khớp nguồn gốc/ground truth)
- **A**vailability? (Freshness, downtime)
- **C**ompleteness? (Tỷ lệ null)
- **E**xceptions? (Log lại lỗi & cảnh báo)

## 5. Access & Compliance

- Phân tầng dữ liệu (Public / Internal / Restricted / Highly Restricted).
- RBAC hoặc ABAC cho BI tools và warehouse.
- Chính sách retention & backup: định nghĩa thời gian lưu trữ.
- Đào tạo bảo mật (phishing, xử lý PII) mỗi 6 tháng.

## 6. Incident Playbook

1. Detect: alert từ monitoring hoặc người dùng.
2. Triage: xác định phạm vi, mức độ ảnh hưởng.
3. Fix: rolling back, patch data, communicate.
4. Post-mortem: ghi lại nguyên nhân gốc, action item.

> 📌 *Tip:* bắt đầu nhỏ với 5–10 bảng critical, sau đó mở rộng; đừng đợi đủ ngân sách lớn mới triển khai governance.