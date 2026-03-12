## 🧭 Unsupervised Learning: Học Không Giám sát

> [← Back to AI/ML Roadmap](../README.md)

Không còn label để dựa vào, mô hình phải tự tìm cấu trúc ẩn trong dữ liệu. Đây là bước quan trọng để khám phá dữ liệu mới, giảm chiều, gợi ý phân cụm khách hàng, phát hiện bất thường...

---

## 1. Clustering (Phân cụm)

Tách dữ liệu thành các nhóm tương đồng.

### 1.1 K-Means Clustering
*   Chọn `k` tâm cụm, gán từng điểm vào cụm gần nhất rồi cập nhật tâm.
*   **Ưu điểm:** Nhanh, dễ dùng.
*   **Nhược điểm:** Cần biết trước `k`, nhạy cảm với điểm outlier.
*   **Kỹ thuật hỗ trợ:**
    *   **Elbow / Silhouette:** chọn `k` tối ưu.
    *   **MiniBatch K-Means:** cho dữ liệu lớn/streaming.

### 1.2 Hierarchical Clustering
*   Xây dựng cây phân cụm (dendrogram): Agglomerative hoặc Divisive.
*   Không cần chọn `k` ngay; dùng dendrogram để quyết định.
*   Hữu ích khi muốn hiểu quan hệ giữa cụm (taxonomy sản phẩm, user segments).

### 1.3 DBSCAN / HDBSCAN
*   Dựa trên mật độ điểm dữ liệu.
*   **Ưu điểm:** Phát hiện cụm có hình dạng bất kỳ, tìm nổi bật outlier tốt.
*   **Nhược điểm:** Cần cấu hình bán kính (epsilon) và số điểm tối thiểu.
*   **Ứng dụng:** fraud detection, clustering GPS trajectory.

---

## 2. Dimensionality Reduction (Giảm chiều)

Nén dữ liệu nhiều chiều thành ít chiều để trực quan, giảm nhiễu, tăng tốc model downstream.

### 2.1 Principal Component Analysis (PCA)
*   Tìm các trục mới (principal components) sao cho giữ được phương sai lớn nhất.
*   Thích hợp cho dữ liệu tuyến tính, dễ giải thích.
*   **Whitening:** scale các component để decorrelate.

### 2.2 t-SNE / UMAP
*   Giữ quan hệ cục bộ giữa các điểm.
*   Phù hợp trực quan hóa dữ liệu cao chiều (embeddings, ảnh...)
*   **t-SNE:** Chi tiết cao nhưng chậm, khó bảo toàn cấu trúc lớn.
*   **UMAP:** Nhanh hơn, bảo toàn tốt hơn cấu trúc toàn cục, có thể dùng cho downstream clustering.

### 2.3 Autoencoders & Variational Autoencoders
*   Dùng mạng neural compress rồi reconstruct dữ liệu đầu vào.
*   VAE thêm phân phối xác suất → hữu ích cho generative modeling, anomaly detection.
*   Thường kết hợp với CNN/RNN cho ảnh, audio, time-series.

> 🎯 Tip: Chạy PCA → nén xuống 50 chiều → dùng UMAP visual → áp dụng clustering để có pipeline khám phá dữ liệu mượt mà.

> 🧪 Notebook: [K-Means + UMAP Lab](./notebooks/kmeans-umap-lab.ipynb)

---

## 3. Association Rule Learning (Luật kết hợp)

Tìm các mẫu “hay đi cùng nhau” trong data (Market Basket Analysis).

### **Apriori / FP-Growth**
*   Ví dụ: Khách mua bia thường mua snack.
*   Sử dụng các thước đo **Support**, **Confidence**, **Lift** để đánh giá.

---

## 4. Anomaly Detection (Phát hiện bất thường)

Áp dụng trong bảo mật, tài chính, IoT...

*   **Isolation Forest:** Các điểm lạ dễ bị “cắt” khỏi cây hơn điểm bình thường.
*   **One-Class SVM:** Học biên bao quanh dữ liệu “bình thường”.
*   **Statistical Methods:** Z-score, IQR.

---

## 5. Quy trình thực chiến

1. **Chuẩn hóa dữ liệu:** Scale các features để tránh cụm bị lệch.
2. **Chọn metric phù hợp:** Silhouette Score, Davies-Bouldin...
3. **Kết hợp Domain Knowledge:** Gán ý nghĩa cho cụm; không có nhãn nên con người phải vào cuộc.
4. **Dùng Semi-supervised nếu có nhãn nhỏ:** Label spreading, active learning.

---

## 6. Ứng dụng tiêu biểu

*   Phân cụm khách hàng cho marketing (Customer Segmentation)
*   Gợi ý sản phẩm (Recommendation) dựa trên item similarity.
*   Phát hiện giao dịch gian lận, sensor anomaly.
*   Chuẩn hóa dữ liệu trước khi đưa vào Supervised Learning.

> 📌 Tip: Luôn visualize kết quả phân cụm/giảm chiều để tránh diễn giải sai. Kết hợp với supervised labels nếu có để đánh giá thêm.
