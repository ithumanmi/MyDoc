## 🏆 Kaggle Competition Guide

> [← Back to Labs](./README.md)

Chiến lược tham gia Kaggle từ chọn cuộc thi đến submission tối ưu.

---

## 1. Chọn cuộc thi phù hợp

- Mục tiêu: học hay ranking?
- Public vs private dataset?
- Solo hay team?
- Check timeline & prize.

Tip: bắt đầu bằng competition Playground (Tabular Playground, Titanic) để quen workflow.

---

## 2. Setup & Workflow chuẩn

1. Clone starter notebook (EDA baseline) → tạo repo riêng.
2. Tracking (W&B/MLflow) + version data (DVC/Kaggle datasets).
3. Mỗi experiment dùng nhánh Git riêng.
4. Log notebook version + seed để reproducible.

Checklist:

- [ ] Xác minh metric evaluation (AUC, RMSE, LogLoss...)
- [ ] Tạo validation scheme (K-fold, Stratified, TimeSeries split)
- [ ] Viết script `prepare_data.py`, `train.py`, `predict.py`

---

## 3. Exploratory Data Analysis (EDA)

- Missing values, outliers, correlations.
- Feature importance baseline (RandomForest/XGBoost).
- Visualize target distribution.

Output: `EDA.md` hoặc notebook tóm tắt findings.

---

## 4. Baseline Modeling

- B1: simple model (Logistic/LightGBM) kiểm metric.
- B2: tuned model (Optuna) → so sánh CV vs public LB.
- Ensemble/stacking khi có ≥3 mô hình mạnh.

> Luôn so sánh offline metric và LB để phát hiện data leakage.

---

## 5. Teamwork & Collaboration

- Dùng Kaggle Team hoặc Github/Notion chia tasks.
- Blend hoặc stacking meta-model.
- Lưu submission history (+ LB score).

---

## 6. Submission & Ranking

- Submission file đúng format (ID + prediction).
- Lưu script sinh submission để rerun.
- Theo dõi chênh lệch Public vs Private LB → đa dạng hóa validation.

> 📝 Tip: Chạy `kaggle competitions submissions -c <name>` để log lịch sử submissions.

---

## 7. Post-Competition

- Đọc giải pháp top teams (write-up, notebook).
- Refactor code thành template cho dự án kế tiếp.
- Viết blog/summary → thêm vào portfolio.

> 🎯 Bonus: Tạo repo `kaggle-<competition-name>` với `README` mô tả pipeline, score, bài học.
