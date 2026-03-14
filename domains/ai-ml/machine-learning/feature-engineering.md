---
title: Feature Engineering Cheatsheet
description: Kỹ thuật tạo đặc trưng, xử lý dữ liệu và lưu ý tránh leak.
---

# 🧰 Feature Engineering

## Nguyên tắc nền
- **Leakage:** Tách train/val/test trước, fit scaler/encoder trên train, áp dụng lên val/test.
- **Pipeline hóa:** Dùng `ColumnTransformer`, `Pipeline` (sklearn) để tái lập quy trình.
- **Baseline trước:** Dùng mô hình đơn giản để kiểm tra giá trị của feature mới.

## Xử lý dữ liệu số
- **Scaling:** Standard/MinMax/RobustScaler; với phân phối lệch, dùng log/Box-Cox/Yeo-Johnson.
- **Outliers:** Winsorize/clip, hoặc mô hình robust (Huber, Quantile). Đừng xóa nếu outlier mang thông tin.
- **Binning:** Quantile binning hoặc domain-driven binning để bắt phi tuyến.

## Xử lý dữ liệu phân loại
- **Low cardinality:** One-Hot/Ordinal (nếu có thứ tự).  
- **High cardinality:** Target Encoding, CatBoost Encoding, Hashing.  
- **Leak check:** Với Target Encoding, dùng K-fold mean hoặc leave-one-out để tránh rò rỉ.

## Thời gian & chuỗi thời gian
- Trích xuất: năm/tháng/tuần/ngày/giờ; cờ ngày lễ/cuối tuần; khoảng cách thời gian giữa các sự kiện.  
- Rolling/expanding features: mean/std/min/max, EWMA.  
- Lag features: `y_{t-1}, y_{t-7}`…; chú ý không dùng tương lai.

## Văn bản & NLP (nhẹ)
- BoW/TF-IDF cho baseline.  
- N-gram từ 1–2/3; giới hạn vocab theo tần suất.  
- Embeddings: từ mô hình pre-trained (e.g., sentence-transformers) rồi giảm chiều (PCA/UMAP) nếu cần.

## Hình ảnh & tín hiệu (nhẹ)
- Thống kê đơn giản: mean/std/kurtosis, năng lượng theo dải tần (FFT).  
- Sử dụng embedding từ model pre-trained (CNN/ViT) làm feature tabular.

## Tương tác & phi tuyến
- Polynomial features (cẩn thận nổ chiều).  
- Cross features: ratio, difference, count, frequency encoding.  
- GroupBy statistics theo entity (user/product): mean target, counts, recency — nhớ tránh leak bằng K-fold.

## Chọn lọc đặc trưng
- Filter: VarianceThreshold, Correlation, Mutual Information.  
- Wrapper: RFE, Sequential Feature Selection.  
- Embedded: L1 (Lasso), Tree-based importance (permutation importance đáng tin hơn impurity).

## Kiểm thử giá trị feature
- So sánh AUC/RMSE trước và sau khi thêm feature trên cùng split.  
- Dùng permutation importance hoặc SHAP để xem feature có thực sự đóng góp.  
- Giảm feature nếu lợi ích nhỏ và chi phí tính toán lớn.

## Pitfalls
- Target leakage từ tương lai hoặc từ thống kê tính trên toàn tập.  
- Mismatch train/test do encoding/normalization fit sai tập.  
- High cardinality + one-hot → ma trận thưa cực lớn, dễ overfit.

## Liên quan
- [Model Selection](./model-selection.md)
- [Ensemble Methods](./ensemble-methods.md)
- [Supervised Learning](./supervised-learning.md)