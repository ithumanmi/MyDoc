## 🧭 Unsupervised Learning: Học Không Giám sát

> [← Back to Classic ML Hub](./README.md) | [← AI/ML Roadmap](../README.md)

Khi không có nhãn, mô hình phải tự tìm cấu trúc ẩn trong dữ liệu. Đây là nền tảng cho customer segmentation, anomaly detection, recommendation, giảm chiều để chuẩn bị cho supervised.

---

## 0. TL;DR & Playbook

1. **Xác định mục tiêu:** clustering, giảm chiều, phát hiện bất thường hay tạo luật kết hợp?
2. **Data Prep:** chuẩn hóa, xử lý thiếu, loại bỏ outlier thô (nếu không cần phát hiện outlier).
3. **Chọn metric vô giám sát:** Silhouette, Davies-Bouldin, Reconstruction Error, Domain feedback.
4. **Visualize mọi bước:** PCA/t-SNE/UMAP để hiểu cấu trúc; review cùng domain để đặt tên cụm.
5. **Đóng gói pipeline:** lưu scaler + mô hình + logic gán label cụm để dùng downstream.

> 📌 Checklist nhanh: scaling? số chiều quá cao? có dùng random seed để reproducible? đã map cụm sang insight kinh doanh?

---

## 1. Clustering (Phân cụm)

Tách dữ liệu thành các nhóm tương đồng.

### 1.1 K-Means / MiniBatch K-Means
*   Chọn `k` tâm cụm, gán từng điểm vào cụm gần nhất rồi cập nhật tâm cho đến khi hội tụ.
*   **Ưu:** nhanh, dễ triển khai, hỗ trợ streaming với MiniBatch.
*   **Nhược:** nhạy cảm với điểm outlier, cần biết trước `k`.
*   **Workflow:** scale feature → chạy nhiều giá trị `k` → Elbow/Silhouette + đánh giá domain → cố định `k` → gán label cụm.

### 1.2 Hierarchical Clustering
*   Xây dựng cây phân cụm (dendrogram): Agglomerative hoặc Divisive.
*   Không cần chọn `k` ngay; dùng dendrogram để quyết định.
*   Hữu ích khi muốn hiểu quan hệ giữa cụm (taxonomy sản phẩm, user segments).

### 1.3 DBSCAN / HDBSCAN
*   Dựa trên mật độ điểm dữ liệu, nên phát hiện được cụm có hình dạng bất kỳ.
*   **Ưu:** tự động loại outlier, không cần `k`.
*   **Nhược:** phải chọn `eps`/`min_samples`, nhạy với scale feature.
*   **Ứng dụng:** fraud detection, GPS trajectory, sensor anomaly.

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
*   **Param tips:**
    * t-SNE: `perplexity` 30-50 cho dataset vừa, tăng nếu data dày.
    * UMAP: `n_neighbors` kiểm soát local/global, `min_dist` kiểm soát độ chặt cụm.

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

| Phương pháp | Khi dùng | Lưu ý |
|-------------|----------|-------|
| **Isolation Forest** | Tabular, dữ liệu nhiều chiều, mix numeric/categorical | Scale không bắt buộc, tune `contamination` để cân bằng FP/FN. |
| **One-Class SVM** | Dataset nhỏ/medium, boundary rõ | Cần scaling, nhạy với outlier nặng. |
| **Autoencoder / VAE** | Dữ liệu phi tuyến, ảnh, chuỗi thời gian | Threshold dựa trên reconstruction error; cần validation dữ liệu sạch. |
| **Statistical (Z-score/IQR)** | Bài toán đơn giản, dữ liệu Gaussian | Không bắt kịp pattern phi tuyến. |

---

## 5. Quy trình thực chiến

1. **Chuẩn hóa dữ liệu:** Scale các features để tránh cụm bị lệch.
2. **Chọn metric phù hợp:** Silhouette Score, Davies-Bouldin...
3. **Kết hợp Domain Knowledge:** Gán ý nghĩa cho cụm; không có nhãn nên con người phải vào cuộc.
4. **Dùng Semi-supervised nếu có nhãn nhỏ:** Label spreading, active learning.

> 🧑‍💼 Deliverable nên có: bảng mô tả cụm + insight, rule đặt tên cụm, script tái tạo pipeline, dashboard visualize (ví dụ Plotly/Bokeh).

---

## 6. Ứng dụng tiêu biểu

*   Phân cụm khách hàng cho marketing (Customer Segmentation)
*   Gợi ý sản phẩm (Recommendation) dựa trên item similarity.
*   Phát hiện giao dịch gian lận, sensor anomaly.
*   Chuẩn hóa dữ liệu trước khi đưa vào Supervised Learning.

> 🔁 Next Steps: sau Unsupervised, xem [Semi-supervised](./semi-supervised-learning.md) để kết hợp nhãn ít + nhãn giả, hoặc build pipeline ensemble với [Ensemble Methods](./ensemble-methods.md).

> 📌 Tip: Luôn visualize kết quả phân cụm/giảm chiều để tránh diễn giải sai. Kết hợp với supervised labels nếu có để đánh giá thêm.
