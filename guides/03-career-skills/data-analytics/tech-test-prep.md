# ⏱️ Technical Test Preparation (24h/48h Challenge)

## 1. Kiểu bài thường gặp

| Loại test | Deliverable | Công cụ |
| --- | --- | --- |
| Explorer Notebook | Jupyter/Colab + insight bullet | Python, Pandas |
| Dashboard Build | Power BI/Tableau file + video demo | Power BI, Tableau, Looker Studio |
| SQL Assessment | File `.sql` + kết quả screenshot | DB Fiddle, BigQuery Sandbox |
| Mixed Case | Slide deck + memo + SQL | Slides, Notion, Git |

## 2. Chiến lược quản lý thời gian

| Thời lượng | Gợi ý phân bổ |
| --- | --- |
| **24 giờ** | 2h phân tích đề, 10h xử lý dữ liệu, 6h xây deliverable, 4h viết report, 2h QA |
| **48 giờ** | Ngày 1: 50% data/analysis, Ngày 2: 30% build, 20% review/polish |

> ⏱️ Tip: đặt alarm theo block 90’ Deep Work + 15’ break.

## 3. Checklist trước khi bắt đầu

- [ ] Tài khoản BI/DB đã cài (Power BI, Tableau, dbt cloud demo).
- [ ] Template README/slide sẵn để điền nhanh.
- [ ] Git repo private hoặc folder versioning rõ ràng.
- [ ] Bộ script Python/SQL boilerplate (import, plotting, KPI function).

## 4. Framework thực thi (R.A.C.E)

1. **Read** đề: highlight yêu cầu, KPI, phạm vi dữ liệu.
2. **Architect**: sơ đồ pipeline, quyết định tool (SQL vs Python).
3. **Create**: code + dashboard + trình bày.
4. **Explain**: viết báo cáo, quay Loom demo, ghi assumption & limitation.

## 5. Deliverable template

- **README.md**
    - Mục tiêu
    - Dữ liệu & cleaning steps
    - Insight chính (3 bullet)
    - Recommendation + Next step
    - File/Link đính kèm
- **Slide 5 trang** (mirrored với README)
- **Video demo** ≤5 phút (nếu cho phép)

## 6. Quality Assurance

- Double-check số: sample calculation trong notebook và dashboard khớp.
- Kiểm tra filter/reset trên dashboard.
- Chạy `flake8` hoặc `black` cho script Python.
- Ghi **Known Issues** & đề xuất bước tiếp theo nếu thiếu thời gian.

## 7. Gửi bài & follow-up

- Zip repo/submit link theo hướng dẫn, backup trên Drive.
- Gửi email: tóm tắt deliverable + highlight insight.
- Đề xuất buổi walkthrough 15 phút nếu họ cần.

> 🎯 *After action review:* log lại thời gian, khó khăn, feedback vào [Daily Log](../../../templates/daily-log.md) để lần sau cải thiện.