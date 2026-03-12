## 🌓 Semi-Supervised Learning: Kết hợp Label + Unlabeled

> [← Back to AI/ML Roadmap](../README.md)

Trong thực tế, có một ít dữ liệu đã gắn nhãn (label) và rất nhiều dữ liệu chưa nhãn. Semi-supervised Learning (SSL) tận dụng cả hai để đạt kết quả gần bằng supervised mà không tốn công gán nhãn.

---

## 1. Khi nào dùng Semi-supervised?

*   **Label đắt đỏ:** Chẩn đoán y khoa, pháp lý, tài chính…
*   **Có nhiều dữ liệu chưa nhãn:** Log hệ thống, clickstream, ảnh, text.
*   **Muốn pretrain nhanh:** SSL giúp model hiểu cấu trúc data trước khi fine-tune.

---

## 2. Các phương pháp cốt lõi

### **A. Self-Training / Pseudo-Labeling**
1. Train model bằng tập có nhãn nhỏ.
2. Dùng model đó tạo pseudo-label cho dữ liệu chưa gán nhãn.
3. Chọn những mẫu có confidence cao để bổ sung vào tập train.
4. Lặp lại (Iterative).

*   **Ưu:** Dễ triển khai với bất kỳ classifier nào.
*   **Nhược:** Lỗi ban đầu có thể lan rộng nếu không kiểm soát threshold.

### **B. Consistency Regularization**
*   Giả định: model nên cho kết quả giống nhau dù input bị nhiễu nhẹ.
*   Kỹ thuật: Mean Teacher, Π-model, MixMatch, FixMatch.
*   Dùng augmentation (flip ảnh, dropout, noise) rồi ép model giữ prediction ổn định.

### **C. Graph-based / Label Propagation**
*   Xây đồ thị các điểm dữ liệu (Node = sample, Edge = similarity).
*   Lan truyền nhãn từ node đã biết sang node chưa nhãn.
*   Phù hợp bài toán có cấu trúc: social network, recommendation.

### **D. Generative Models**
*   Sử dụng VAE, GAN để học phân bố dữ liệu chưa nhãn.
*   Semi-supervised GAN: discriminator vừa phân biệt real/fake vừa phân loại class.

---

## 3. Best Practices

1. **Quality check pseudo-labels:** Dùng confidence threshold, hoặc chỉ lấy top-K.
2. **Balance data:** Tránh để pseudo-label làm lệch class distribution.
3. **Augmentation chuẩn:** Tùy domain (ảnh, text, tabular) mà chọn augmentation phù hợp.
4. **Active Learning kết hợp:** Hỏi chuyên gia gán nhãn cho những mẫu model còn phân vân.

---

## 4. Workflow gợi ý

1. Chuẩn hóa data + feature engineering cơ bản.
2. Train supervised baseline.
3. Áp dụng SSL (pseudo-label hoặc consistency) với unlabeled set.
4. Fine-tune lại trên tập kết hợp.
5. Đánh giá bằng validation có nhãn; giám sát drift của pseudo-label.

---

## 5. Use Cases

*   Nhận diện văn bản (OCR) / trợ lý nhập liệu.
*   Phát hiện ý định người dùng với ít dữ liệu annotated.
*   Phân loại ảnh công nghiệp, ảnh vệ tinh.
*   Nâng cấp chatbot: label intent limited nhưng log hội thoại rất nhiều.

> 💡 Tip: Khi dataset có cấu trúc không cân bằng, kết hợp SSL với Ensemble (ví dụ: pseudo-label bằng LightGBM, kiểm tra lại bằng SVM) để giảm rủi ro lan truyền nhãn sai.
