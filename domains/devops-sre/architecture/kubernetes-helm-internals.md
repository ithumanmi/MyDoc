# Đế Chế Docker & Nhà Vua Điều Phối Kubernetes (K8s) Core Internals

> [← Back to DevOps & SRE Roadmap](../README.md)

Trước đây, khi 1 App (NodeJS) muốn cài Đè lên Thằng App Khác (Python) trên cùng 1 Server, Hai Thằng Thư Viện Chửi Lộn Dẫn Sang Đứt Máy.
- **Docker** ra đời (Đóng Cũi Container): Gói Cả Môi Trường Kèm Source Code Chạy Gọn Cô Lập Không Dẫm Mặt Nhau. Đưa File Đi Máy Nào Thì Chạy 100% Y Chang Lỗi Giống Trên Máy Đứa Coder. 
Nhưng nếu bạn có 50 cái Cũi Docker Trống Lốc. Và Server 1 sập bốc cháy? -> Cứu Hộ Ai Cứu? 

Đấy là lúc Bộ Định Chuyển Huyện Thoại Tư Lệnh Biển **Kubernetes (K8s)** Từ Lõi Google Nhảy Ra Thị Trường. K8s Không Phải Nơi Cài App. Nó Là Con Robot Điều Cử Đi Trông Giữ Giám Sát Cũi!

---

## ⚓ 1. Giải Phẫu Cluster (Cụm K8s Giao Đình Hạt Nhân)

Một Cụm K8s Luôn Có 1 Não Chỉ Huy (Control Plane / Master Node) và Bầy Tôi Tớ Cày Cuốc (Worker Nodes).

### A. Bộ Sậu Đầu Não (Control Plane - Master Node)
*   **kube-apiserver:** Đón Mọi Cuộc Gọi Nhập (Dân Tình Viết File Lệnh Yaml Chỉ Nhằm Thằng Này Đút Vào). 
*   **etcd:** Cuốn Sổ Nam Tào (Key-Value Store Rất Gắt Vững). Node Master Có Sập Khởi Lại Đọc Etcd Sẽ Nhớ Mình Đang Ra Lệnh Tới Đâu Ở Xóm Cluster Cấm Khai Phá.
*   **kube-scheduler:** Chuyên Đánh Hơi Thấy Node Tớ Nào Đang Rảnh CPU Dư RAM Để Bố Thằng Server API Server Nhét Kẹp Khéo Léo Thằng `Container Mới` Cho Công Bằng! (Thằng Trọng Tài Phân Bổ RAM).
*   **kube-controller-manager:** Lo Quan Sát Xem. Nếu Quy Định Kêu "Phải Chạy 4 App Lúc Khác Tắt 1", Nó Ngó Xuống Cụm Worker Đang Thấy Đứt 1 App Mất Mạng, Lập Tức Nó Đi Đẻ Nhồi Kéo Móc Lên 1 Thằng Bù Ngay Số Liệu Etcd Nhận Đình! (Vòng Lặp Control Loop).

### B. Bọn Tá Điền Chết Thường Xuyên (Worker Nodes)
*   **Kubelet:** Tiếng Nói Chó Báo Tin Đứng Khung Rìa Thôn Worker Mỗi Cây Lệnh Trồng (Agent). Rình Ràng Nhìn Thấy API Mẹ Trên Kia Ré Báo Thay Thì Lập Tức Ôm Ráp Cũi Dành Container Vào Docker Desktop Node Chạy Lên Mặt Ngay Kịp Khớp Lệnh Kube-Scheduler Chia Phần Tới! 
*   **Kube-proxy:** Thiết Kế Cửa Ngõ Dây Lưới Cho App Nói Cố Được IP Nói Với IP, Ngay Gọn Trong Nhà, Ngoài Xóm Nhau Cắm Port Node.

---

## 🧱 2. Cấu Trúc Bụng Lưới Mã (Pods, Replicas, Services)

Kubernetes Không Quản Lý Trực Tiếp "Container" Trần Truồng. Nó Bọc Bằng Một Túi Bù Khung Tên Là **Pod**.
*   **Pod (Phân Tử Sống Nhỏ Nhất):** 1 Pod Thường Chỉ Chứa 1 Container, Hoặc Chứa Container Phụ (Sidecar - Băng Keo). Pod Có Thể Xẹp Vụt Chết Đi Bất Ngờ Khi Lỗi (IP Pod Thay Đổi Liên Tục Nếu Được Rước Lại Lên Mới).
*   **ReplicaSet / Deployment (Vương Miện Nhân Bản):** Đừng Chỉ Cho 1 Pod Nát Chạy! Tôi Gói Pod Vào Vỏ Deployment Khung. "Mệnh Lệnh: Giữ 3 Pod (Replica=3) Liên Tục Sống Rống Cùng 1 Lõi Image Image:V1 Cho Mạch Chạy Bất Khả Sập". Đây chính là Tính Năng Vàng Chóe Sức Cứu Rỗi: **Self-Healing (Tự Chữa Lành - Chống Đứt Service)**. 
*   **Service (Bưu Cục Quản Dây Đầu Lệnh Tĩnh IP):** Nếu 3 Pod Cực Ách Nó Thay Đổi Xóa Nháp IP Khắp Node Chạy Rụng Đi Mới. Thằng Đầu Kẻ Khách Dưới Client Web Vào Cửa Bắt Sóng Ai? (10.1.X.X?). Sai! Nó Nhốt Biến Vào Tường Chắn `Service`. Khách Kẹt Request Vào Tường Lược Load Balancer IP Tĩnh Của Thằng Service, Tường Kia Tự Biểu Trổ Thảy Thọt Vô Tròn Trình Cho Những Pod Còn Sống Chạy Dưới Ẩn Kia! Thấu Gỡ Bài Đi Lỏng Đứt Kết Nối!

---

## 🎁 3. Tạm Biệt Rác YAML - Kỷ Nguyên Helm Charts

Nếu Triển NodeJS Lên Cụm Bạn Phải Tự Viết: 1 File `deployment.yaml`, 1 Thằng `service.yaml`, Cấu Hình Secrets Quăng Pass... Rãi Dài Hàng Ngàn Dòng Dân Kẹt Trọn Chết Mòn Vã Tay Khổ Mỏi Lỗi Indent. Gửi Code Vác Nhau Chạy Dev-Stag-Prod Gãy Vì Port Khác Mép Nhau Lưới Khủng! Lệnh Thay Biến: Tự Tới Hỏng!
**Helm** Xuất Mạng Giải Ách! Nó Trút Đổ Hóa K8s Như Phần Mềm Của Thằng Debian OS / Windows Setup.

*   Helm Biến Tất Cả Các File YAML kia thành Bản Thể Mẫu Chỗ Thay Biến Khuôn Sắt Rắn (**Templates**). 
*   Mọi Điểm Chốt Khác Nhau Giữa Server Nội Chỉnh Port Tùy Ý Đóng Vào Sổ Khay Tham Số Trống Trơn Thùng `values.yaml` Rìa Mép Cuối Nhạc!
*   **Cài Đặt PostgreSQL Scale Đứt Đuôi Cluster Bây Giờ Chỉ Có 1 Dòng Mệnh Cục Gọn Đuôi Command CLI Rõ Thay Vì Ngồi Soạn 50 Trang Giấy CODE CHỈ DƯỚI GÓC CẢ HỘ Lệnh K8S NGẮN NHẬT Trấn :**  
    `helm install may_chu_data bitnami/postgresql` ! Khủng Khiếp Biến Hình Xuyên Gọng System Ops Mòn Cũ Lạnh!
