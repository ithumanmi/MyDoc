---
title: Unsupervised Learning Cheatsheet
description: Core methods, when to use, pitfalls, and quick-start recipes.
---

# 🧭 Unsupervised Learning

## Khi nào dùng
- Không có nhãn, cần khám phá cấu trúc/nhóm ẩn.
- Giảm chiều dữ liệu để trực quan hóa, nén, tiền xử lý.
- Phát hiện bất thường khi thiếu dữ liệu xấu có nhãn.

## Phổ thuật toán chính
- **Clustering:** K-Means, Hierarchical (Ward/Complete/Single), DBSCAN/HDBSCAN, Gaussian Mixture Models (GMM), Spectral Clustering.
- **Dimensionality Reduction:** PCA, t-SNE (trực quan), UMAP, Autoencoder (denoising/variational).
- **Anomaly Detection:** Isolation Forest, One-Class SVM, Elliptic Envelope, Autoencoder reconstruction error.
- **Association Rules:** Apriori, FP-Growth cho market-basket analysis.

## Lựa chọn nhanh
- **Dữ liệu lớn, cần tốc độ:** K-Means (mini-batch), PCA.
- **Dữ liệu phi tuyến, hình dạng cụm phức tạp:** DBSCAN/HDBSCAN, Spectral, UMAP.
- **Nhiều nhiễu/outlier:** DBSCAN/HDBSCAN, Isolation Forest.
- **Trực quan hóa 2D/3D:** UMAP (nhanh, giữ cấu trúc cục bộ), t-SNE (giữ cấu trúc cục bộ tốt nhưng chậm).

## Quy trình chuẩn
1) Chuẩn hóa/scale dữ liệu (StandardScaler/RobustScaler).  
2) Giảm chiều sơ bộ (PCA/UMAP) nếu feature nhiều hoặc nhiễu.  
3) Chọn thuật toán cluster/anomaly phù hợp.  
4) Đánh giá bằng metric không nhãn: Silhouette, Calinski-Harabasz, Davies-Bouldin, hoặc đánh giá định tính (visual).  
5) Kiểm tra ổn định cụm (random seeds, bootstrap) và ý nghĩa business.

## Công thức nhanh (code sketch, Python/Sklearn)
- **K-Means + Silhouette:**
```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

kmeans = KMeans(n_clusters=K, n_init='auto', random_state=42)
labels = kmeans.fit_predict(X_scaled)
score = silhouette_score(X_scaled, labels)
```
- **DBSCAN (epsilon tuning):**
```python
from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.5, min_samples=10).fit(X_scaled)
labels = db.labels_  # -1 là noise
```
- **UMAP để giảm chiều trước khi cluster:**
```python
import umap
import numpy as np
X_2d = umap.UMAP(n_neighbors=15, min_dist=0.1, metric='cosine', random_state=42).fit_transform(X)
```
- **Isolation Forest cho anomaly:**
```python
from sklearn.ensemble import IsolationForest
iso = IsolationForest(contamination=0.02, random_state=42)
pred = iso.fit_predict(X_scaled)  # -1 là anomaly
```

## Pitfalls & lưu ý
- K-Means giả định cụm lồi và tương đương về kích thước → kém với cụm phi tuyến hoặc density khác nhau.
- t-SNE không bảo toàn cấu trúc toàn cục; không dùng trực tiếp để cluster.
- DBSCAN nhạy cảm tham số `eps` và `min_samples`; chuẩn hóa thang đo trước.
- Anomaly detection cần hiệu chỉnh tỷ lệ contamination; luôn kiểm thử trên tập có nhãn mẫu nếu có.

## Đánh giá và trực quan
- Dùng **Silhouette** để tìm K; kết hợp **Elbow** chỉ mang tính gợi ý.
- Trực quan 2D/3D sau giảm chiều; kiểm tra tính nhất quán cụm với nhiều seed.
- Với anomaly: Precision@k, PR curve nếu có nhãn hạn chế; nếu không, cần SME review.

## Liên quan
- [Supervised Learning](./supervised-learning.md)
- [Semi-supervised Learning](./semi-supervised-learning.md)
- [Feature Engineering](./feature-engineering.md)