# 👁️ Computer Vision: Thị giác Máy tính (Level 4)

> [← Back to AI/ML Roadmap](../README.md)

Làm sao máy tính "nhìn" thấy con mèo trong bức ảnh? Nó không nhìn thấy lông, mắt, tai. Nó chỉ nhìn thấy ma trận pixel.
Convolutional Neural Network (CNN) là chìa khóa.

---

## 1. CNN (Convolutional Neural Network)

Thay vì kết nối tất cả pixel với nhau (Fully Connected), CNN dùng một bộ lọc (Filter/Kernel) trượt qua ảnh để tìm đặc trưng (Feature).

### **A. Convolution Layer (Lớp tích chập)**
*   **Filter:** Ma trận nhỏ (3x3, 5x5) chứa trọng số.
*   **Sliding Window:** Filter trượt qua ảnh gốc -> Nhân chập -> Ra Feature Map mới.
*   **Ý nghĩa:** Lớp đầu tìm cạnh (Edge), lớp sau tìm hình dạng (Shape), lớp cuối tìm vật thể (Object).

### **B. Pooling Layer (Lớp gộp)**
*   **Max Pooling:** Lấy giá trị lớn nhất trong vùng 2x2.
*   **Mục đích:** Giảm kích thước ảnh (Downsampling) -> Giảm số lượng tham số -> Tăng tốc tính toán & Tránh Overfitting.
*   **Bất biến dịch chuyển (Translation Invariance):** Con mèo nằm ở góc trái hay góc phải thì vẫn là con mèo.

---

## 2. Architectures (Các kiến trúc nổi tiếng)

Đừng tự thiết kế mạng CNN từ đầu. Hãy dùng lại (Transfer Learning) các kiến trúc đã được chứng minh.

### **A. VGG (Visual Geometry Group)**
*   Dùng toàn bộ filter 3x3. Rất sâu (16/19 lớp).
*   Đơn giản, dễ hiểu nhưng rất nặng (nhiều tham số).

### **B. ResNet (Residual Network)**
*   Giải quyết vấn đề Vanishing Gradient khi mạng quá sâu (152 lớp).
*   **Skip Connection:** Cộng trực tiếp input vào output của một block (đường tắt) -> Giúp gradient chảy ngược dễ dàng hơn.

### **C. MobileNet**
*   Tối ưu cho thiết bị di động (Mobile/Edge).
*   **Depthwise Separable Convolution:** Giảm số lượng phép tính đi 9 lần mà độ chính xác giảm không đáng kể.

---

## 3. Object Detection (Nhận diện vật thể)

Không chỉ biết "ảnh này là con mèo" (Classification), mà còn biết "con mèo nằm ở đâu" (Localization).

### **A. YOLO (You Only Look Once)**
*   Nhanh nhất thế giới (Real-time).
*   Chia ảnh thành lưới (Grid). Mỗi ô dự đoán bounding box và class cùng lúc.
*   Phiên bản mới nhất: YOLOv8 (Ultralytics).

### **B. Faster R-CNN**
*   Chính xác hơn YOLO nhưng chậm hơn.
*   Dùng Region Proposal Network (RPN) để đề xuất vùng có vật thể trước, sau đó mới phân loại.
