## 🧪 Classic ML Practice Pack

> [← Back to AI/ML Roadmap](../README.md)

Tập bài tập giúp bạn áp dụng Supervised, Unsupervised, Semi-supervised, Feature Engineering và Ensemble vào dataset thực tế.

---

## 1. Regression Challenge (House Prices)

**Goal:** Dự đoán giá nhà.

1. Thu thập dataset (Kaggle House Prices hoặc data địa phương).
2. Làm sạch missing values, tạo feature (interaction giữa diện tích và chất lượng).
3. So sánh Linear Regression, Random Forest, Gradient Boosting.
4. Báo cáo: RMSE, MAE, feature importance.

**Stretch:** Áp dụng stacking (linear + tree) và regularization (Ridge/Lasso).

---

## 2. Classification Challenge (Customer Churn)

**Goal:** Dự đoán khách hàng rời đi.

1. Feature engineering cho thời gian sử dụng, số lần gọi support.
2. Huấn luyện Logistic Regression, XGBoost.
3. Đánh giá Precision/Recall, ROC-AUC, chi phí giữ khách.
4. Áp dụng pseudo-label cho khách chưa rõ outcome (semi-supervised mini experiment).

**Stretch:** Thiết kế active learning loop—chọn 50 khách hàng để chuyên gia review.

---

## 3. Unsupervised Lab (Customer Segmentation)

**Goal:** Tạo phân khúc khách hàng.

1. Chuẩn hóa dữ liệu chi tiêu, hành vi.
2. Thử K-Means, Hierarchical, DBSCAN.
3. Visualize PCA/t-SNE để hiểu cụm.
4. Gán ý nghĩa business cho từng cụm.

**Stretch:** Dùng clustering output làm feature cho mô hình churn.

---

## 4. Anomaly Detection (Fraud or Sensor Data)

**Goal:** Phát hiện giao dịch bất thường.

1. Dùng Isolation Forest, One-Class SVM.
2. Kết hợp domain rule-based features (ví dụ: giao dịch đêm khuya, location mismatch).
3. Đánh giá bằng Precision@K, Recall trong tập bất thường.

**Stretch:** Ensemble anomaly với boosting classifier được train từ một ít mẫu labeled fraud.

---

## 5. Feature Store Mini Project

**Goal:** Xây pipeline tái sử dụng feature.

1. Dùng pandas hoặc dbt để tạo bảng feature (daily aggregations, lag).
2. Lưu metadata (mô tả, chủ sở hữu, refresh schedule).
3. Tích hợp với scikit-learn pipeline.

**Stretch:** Thiết lập drift monitoring cho top feature.

---

## 6. Evaluation & Reporting Template

*   Tạo notebook/report chuẩn gồm:
    *   Vấn đề và dữ liệu.
    *   Feature engineering và lý do.
    *   So sánh model + metric.
    *   Kết luận + bước tiếp theo.

> 🎯 Tip: Dù chỉ làm bài tập, hãy cố gắng deploy nhỏ (Streamlit, FastAPI) hoặc chia sẻ notebook + README. Portfolio thực chiến > chỉ đọc lý thuyết.
