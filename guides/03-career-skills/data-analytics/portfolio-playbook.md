# 📁 Data Portfolio Playbook 2026

> Mục tiêu: xây 3–5 dự án có business impact, dễ đọc, dễ đánh giá cho nhà tuyển dụng/khách hàng.

## 1. Chọn dự án chiến lược

| Loại dự án | Use-case | Gợi ý dữ liệu |
| --- | --- | --- |
| Operations Dashboard | Supply chain, inventory | Kaggle Retail, public logistics data |
| Marketing Funnel | Acquisition, retention | Google Analytics sample, open e-commerce sets |
| Finance / Forecasting | Revenue, budgeting | SEC filings, World Bank, data.gov |
| Product Analytics | Cohort, feature adoption | App Store scrape, game telemetry sample |

> ✅ Checklist chọn dự án: (1) Có KPI rõ, (2) có câu chuyện người dùng, (3) thể hiện ít nhất 2 kỹ năng (SQL + Viz, hoặc Viz + Stats).

## 2. Quy trình thực hiện (S.P.A.R.K)

1. **Scope:** Định nghĩa câu hỏi business + KPI.
2. **Prepare:** Thu thập dữ liệu, log cleaning (notebook/README).
3. **Analyze:** SQL/Python; ghi lại assumptions, bias.
4. **Reveal:** Dashboard + narrative 3-act (Context → Insight → Action).
5. **Knowledge Share:** Video demo 3 phút + write-up.

## 3. Cấu trúc repo mẫu

```
project-name/
├─ data/ (raw, processed)
├─ notebooks/
├─ dashboard/ (Tableau twbx hoặc Power BI pbix)
├─ README.md (story, KPI, insight)
└─ assets/thumbnail.png
```

## 4. Template README (rút gọn)

```
# Tên dự án & KPI chính

## 1. Tại sao?
- Pain point
- Stakeholder

## 2. Dữ liệu & quy trình
- Nguồn dữ liệu
- Cleaning steps
- Tools

## 3. Insight chính
- Bullet 1 (số liệu cụ thể)
- Bullet 2

## 4. Hành động đề xuất
- Action + Expected impact

## 5. Tệp đính kèm
- Notebook link
- Dashboard link
```

## 5. Tiêu chuẩn chất lượng

- **Reproducibility:** Có notebook/script + hướng dẫn chạy.
- **Visualization hygiene:** màu sắc nhất quán, chú thích rõ, highlight insight.
- **Business-first narrative:** mở đầu bằng tác động, không chỉ liệt kê số.
- **Accessibility:** có video demo, PDF snapshot.

## 6. Showcase & Social Proof

- Đăng GitHub repo + Tableau Public/Power BI Service.
- Viết LinkedIn/Twitter thread kể lại hành trình làm dự án.
- Xin mentor/đồng nghiệp review để thêm testimonial.
- Đính kèm vào CV (link ngắn gọn), thêm QR khi phỏng vấn onsite.

## 7. Maintenance

- Review mỗi quý: cập nhật tooling mới (dbt, DuckDB).
- Nếu dữ liệu cũ, ghi chú “Last refreshed: mm/yyyy”.
- Track số lượt truy cập, phản hồi để cải thiện.

> 💡 Tip: tạo “Portfolio Ops” board trong Trello/Notion để quản lý backlog dự án, trạng thái review, feedback.