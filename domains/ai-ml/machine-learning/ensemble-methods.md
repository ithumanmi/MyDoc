## 🌲 Ensemble Methods: Sức mạnh “đội hình” trong Classic ML

> [← Back to Classic ML Hub](./README.md) | [← AI/ML Roadmap](../README.md)

Thay vì dựa vào một model đơn, ta kết hợp nhiều model lại để giảm phương sai, giảm bias hoặc tăng tính ổn định. Ensemble là bí kíp vô địch Kaggle, production scoring, và cả feature selection.

---

## 0. TL;DR & Mindset

- Bắt đầu bằng **model đa dạng**: Linear → Tree → Boosting → kNN/SVM.
- **Không phải lúc nào ensemble cũng cần**: baseline yếu → cải thiện feature trước.
- **Tune từng base model ổn định** rồi mới ensemble.
- Chú ý **độ lệch dữ liệu**: bagging giảm variance, boosting giảm bias, stacking khai thác pattern residual.
- Luôn giữ **validation sạch** để đo generalization (nested CV hoặc holdout).

> 🧪 Checklist: có log out-of-fold predictions? đã kiểm tra data leakage khi stacking? track seed để reproducible?

---

## 1. Bagging (Bootstrap Aggregating)

Huấn luyện nhiều model độc lập trên các mẫu dữ liệu bootstrap (lấy mẫu có lặp) rồi lấy trung bình/đa số.

### 1.1 Random Forest

| Thành phần | Chi tiết |
| --- | --- |
| Sampling | Lấy mẫu bootstrap cho từng cây + random subset features tại mỗi split |
| Voting | Classification: majority vote. Regression: trung bình |
| Hyperparameters | `n_estimators`, `max_depth`, `max_features`, `min_samples_leaf` |

**Out-of-Bag (OOB) Error:** khoảng 36.8% dữ liệu không được chọn vào bootstrap → dùng làm validation miễn phí. Bật `oob_score=True` trong sklearn để giám sát overfit.

### 1.2 Extra Trees (Extremely Randomized Trees)

* Split point chọn hoàn toàn ngẫu nhiên trong khoảng giá trị → variance thấp hơn.
* Hữu ích khi dataset lớn, cần tốc độ huấn luyện nhanh.

> ⚙️ Workflow: chuẩn hóa pipeline → train RF với `n_estimators=500` + monitor OOB → dùng SHAP/Permutation để chọn feature → fine-tune boosting model.

---

## 2. Boosting (Sequential Learning)

Huấn luyện model tuần tự. Mỗi model mới học từ lỗi của model trước.

### 2.1 AdaBoost

* Cặp trọng số mẫu tăng lên nếu bị dự đoán sai.
* Base learner: tree depth=1 (decision stump) → giảm variance mạnh.
* Nhạy cảm với noise → cần làm sạch dữ liệu trước.

### 2.2 Gradient Boosting Machines (GBM)

* Mỗi stage fit vào residual của stage trước theo gradient của loss.
* Có thể chọn loss khác nhau: squared error, logistic, quantile.

### 2.3 XGBoost (Extreme Gradient Boosting)

* **Regularization:** L1/L2 trực tiếp trên leaf weights → tránh overfit.
* **System tricks:** Sparse-aware, cache optimization.
* **Useful params:** `eta`, `max_depth`, `subsample`, `colsample_bytree`, `gamma`.

### 2.4 LightGBM

* **Histogram-based:** gom giá trị thành bins → huấn luyện nhanh, memory nhỏ.
* **Leaf-wise growth + depth limit:** tăng accuracy nhưng cần `min_data_in_leaf` để tránh overfit.
* Hỗ trợ categorical qua `categorical_feature` + xử lý missing tự động.

### 2.5 CatBoost

* Native categorical encoding bằng ordered statistics → tránh target leakage.
* Có built-in text embedding, GPU acceleration.
* Ít cần tuning phức tạp, thích hợp baseline nhanh.

> 🚀 Tip: Dùng early stopping với validation set (`early_stopping_rounds=100`) để tự động dừng boosting trước khi overfit.

### 2.6 Khi nào chọn Boosting nào?

| Thuật toán | Khi dùng | Lưu ý |
|------------|----------|-------|
| AdaBoost | Dữ liệu sạch, noise thấp, muốn model đơn giản | dễ overfit khi có outlier nặng |
| GradientBoosting (sklearn) | Dataset nhỏ/trung bình, cần custom loss | chậm hơn XGB/LGBM nhưng code dễ debug |
| XGBoost | Tabular kích thước vừa → lớn, cần regularization mạnh | tune `eta`, `max_depth`, `min_child_weight`, `subsample` |
| LightGBM | Dữ liệu rất lớn, high cardinality, nhiều numeric | set `min_data_in_leaf`, `feature_fraction`, `max_depth` để tránh overfit |
| CatBoost | Nhiều categorical, muốn baseline mạnh nhanh | ít cần preprocessing nhưng nên chuẩn hoá missing |

---

## 3. Stacking (Meta-learning)

Theo kiến trúc nhiều tầng:

1. **Level-1 (Base models):** Logistic Regression, Random Forest, LightGBM, Neural Net... Huấn luyện bằng K-fold và lưu **out-of-fold predictions**.
2. **Level-2 (Meta-model):** Train trên dữ liệu mới (predictions) để học cách kết hợp. Thường dùng logistic/linear hoặc model đơn giản để tránh overfit.
3. **Blender:** Có thể là Ridge, XGBoost hoặc NN tùy bài.

Best practices:
* Sử dụng `sklearn.ensemble.StackingClassifier` hoặc thư viện như `mlxtend` để quản lý pipeline.
* Feature cẩn thận: scale prediction probabilities trước khi feed meta-model.
* Giữ lại validation set chưa động tới để đo generalization (nested CV).

> 🧩 Ví dụ pipeline: K-fold (5 folds) → huấn luyện base models (LR, RF, LGBM) → lưu out-of-fold predictions → concat thành feature OOF → train meta-model (Logistic/CatBoost) → inference bằng cách trung bình prediction trên mỗi fold.

---

## 4. Voting / Blending

*   **Hard Voting:** Lấy đa số phiếu từ các classifier.
*   **Soft Voting:** Trung bình xác suất dự đoán.
*   **Blending:** Giống stacking nhưng dùng holdout set nhỏ cho meta-learner (ít sạch hơn stacking).

---

## 5. Thực chiến & Best Practices

1. **Đa dạng model:** Ensemble chỉ mạnh khi các base learners có lỗi khác nhau.
2. **Regularization:** Đặc biệt với boosting để tránh overfit.
3. **Feature Importance:** Dùng SHAP, Permutation Importance để hiểu model.
4. **Pipeline:** Kết hợp với feature engineering, hyperparameter tuning, automation (Optuna/Ray Tune + MLflow).
5. **Monitoring:** log từng base model + ensemble metric; track drift.
6. **Khi nào dùng?** Khi single model đã tối ưu mà vẫn muốn tăng thêm vài % accuracy hoặc cần model ổn định trước khi deploy.
7. **Chi phí:** Boosting chiếm nhiều compute; cân nhắc pruning tree, giảm depth, quantize model khi deploy.

---

## 6. Use Cases

*   Credit scoring, risk modeling (Boosting ~ chuẩn vàng).
*   Fraud detection (Kết hợp anomaly + boosting).
*   Kaggle/competitions: Stacking + blending nhiều model.
*   Feature selection: Random Forest importance để chọn feature cho model khác.
*   Healthcare/Finance: stacking logistic + boosting để giữ explainability (logistic) nhưng vẫn có power (boosting).
*   Recommender/tabular lớn: LightGBM/CatBoost + ranker stacking.

> 💡 Tip: Với dữ liệu lớn, bắt đầu bằng LightGBM/XGBoost với early stopping để có baseline mạnh. Khi cần thêm vài % cuối, thử stacking/blending, hoặc kết hợp với deep model (TabNet, FT-Transformer) để tăng đa dạng.
