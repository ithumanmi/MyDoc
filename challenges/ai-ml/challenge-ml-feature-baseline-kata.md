# Challenge: Feature Engineering + Baseline Model (Kata)

- **Loại:** kata
- **Mảng:** ai-ml
- **Mức:** Beginner
- **Ước lượng thời gian:** 2-4 giờ
- **Prerequisites (tùy chọn):** ML cơ bản, pandas/sklearn.

## Mục tiêu học tập

- Thực hành pipeline cơ bản: split data, feature engineering đơn giản, train baseline, đánh giá.
- Viết code sạch, notebook rõ ràng.

## Đề bài

Cho một dataset tabular (vd: Titanic, Housing, hoặc dataset cố định bạn chọn). Nhiệm vụ:

- Clean/chuẩn hoá dữ liệu ngắn gọn.
- Tạo 3-5 features đơn giản (numeric scaling, categorical encoding, text length… tuỳ dataset).
- Train baseline model (vd: logistic regression/random forest) và so sánh với baseline trống.
- Đánh giá bằng 1-2 metrics chính (vd: accuracy/F1/AUC cho classification; RMSE/MAE cho regression).

## Đầu vào (Input)

- Dataset công khai (link) hoặc file kèm repo.

## Đầu ra (Output)

- Notebook hoặc script + README ngắn mô tả feature, metric, kết quả.

## Tiêu chí chấm (Acceptance)

- **Đúng:** Code chạy, metric được in ra; có train/test split.
- **Tăng nhẹ so với baseline:** Thể hiện cải thiện sau feature engineering.
- **Trình bày:** Giải thích ngắn gọn về feature và metric.

## Gợi ý / Hint

- Dùng train/validation hoặc cross-validation đơn giản.
- Tránh leakage; scale numeric; encode categorical (one-hot/ordinal).

## Reference / Solution (tùy chọn)

- (Tuỳ chọn) Notebook mẫu: `https://github.com/example/feature-baseline-notebook` (thay bằng repo/notebook của bạn nếu có).

