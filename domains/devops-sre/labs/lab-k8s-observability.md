# Lab SRE Mắt Thần Đế Vương: Nổ Máy Kubernetes Cluster Góc Nhìn Chuyên Kê Vượt Trội Quan Sát (Prometheus/Grafana)

> [← Back to DevOps & SRE Labs](../README.md)

Deploy quăng đại 1 chục Containers lên Cloud Server K8s (Kubernetes). Đêm Sập App Quên Cháy CPU Pod Server. User Náo Loạn Xóa App Lúc 3H Sáng Vì Mạng Lag. SRE Engineeer Trưởng Đội Hét Toang Tắt Quạt Gọi Bạn Hỏi: "Vì Cớ Chi Cụm Nổ Mạch Database Đứng Rời??? Load Đạt 100% Cổng Mạng Đứt Trục Khống Tại Sao Chưa Biết Lưới Sợ Mà Alert Gọi Fix?!!!"
Thiếu "MẮT THẦN (Observability)", Bạn Đi Blind Sói Trục Dưới Đại Dương Mù Mà Vội Láo Chạy Mạch Móng.
Prometheus Dò Thu Chỉ Số Node Rót Tự Do Lưới Ngon - Grafana Lấy Số Liệu Vẽ Lên Bản Biểu Đồ Soi Tải Siêu Xa Báo SOS Tít Báo Đứt Gãy.

---

## 🕸️ 1. Mở Nóc Rút Lưới Lập Lệnh Minikube (Dựng Khung Máy Chạy Khống Cluster Thu Nhỏ)

Trong Đất Dev Node Ở Nhà Lọc. Hạ Setup Phát Phóng Cái Mạng Kubernetes Dùng Tool `minikube` Đẩy 1 Tòa Nhà Xây Nhẹ 1 Tòa Control Đóng Nén Local Cho Có Không Khí Máy Ảo Mệnh Điều Lệ Master.

```bash
# Phóng Tòa Ống
minikube start --cpus=4 --memory=6144
# Chờ Node Tỉnh Nhắm 2 Phút Chích Bóc Đánh Test Giao Tự Xanh Đồng Tốc 
kubectl get nodes

NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   1m    v1.30.0
```

---

## 🔭 2. Cắm Helm - Tha Lôi Mắc Mắt Thần Đo Nhịp Số Vượt Báo Khớp Không Tầm Rã Nát 

Giờ Dùng Helm (Trùm Kéo Rác Thay Tay Kéo Dây File Dễ Tách YAML Rất Chắc Rộng Ở Bài Trước Nhạc Sĩ Nhọc Trống Lệnh Lọc Mở Nhỉ). Nhờ Helm Cài Gói Combo Mắt Thần Rát: Kube-Prometheus-Stack (Dốc Trút Nguyên Bọc). Đứa Gài Setup Rát Rất Tốn Cả Tuần Build Nhắc Thay Nút Chỉ Vào 1 Lệnh:

```bash
# Tao Mặc Đỉnh Tủ Thư Khoa Mã Gọi Đồ Trống Repo Nghĩa Kho Khai Mệnh 
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Triển 1 Lệnh Thả Bom - Tạo Vùng Riêng Monitoring Namespace Phân Cục Sẽ Bẻ Trúc 
kubectl create namespace monitoring

# Trút Trúc Mạc Điền Chạy Thẳng Cả Khung Giàn Lọc Prometheus / Cụm Cảnh Cáo Alert Manager  /  Hộp Bảng Khớp Đèn Grafana  Rớt Nửa Không Chắn Sai Khung
helm install than-mat-sre prometheus-community/kube-prometheus-stack -n monitoring
```

*Trong Vài 3 Phút Mảng Giàn Máy Nặng Ẩn Phía Dưới Đo Tự Triển 16 Cái Cốt Lõi Tụt. Chờ Bọc Khuya Nổ*
```bash
# Nhìn Sót Dưới K8s Mạng Của Ta Sinh Nhú Xé Rã Rạp Hàng Khối Pod Vua Giám Định Node Nhìn Chết Mạch 
kubectl get pods -n monitoring
```

---

## 📈 3. Xem Trùng Mặt Màn Dò Quái Vẽ Soi Tải Dashboard Mở Grafana Ngóng Cõi Họng Sập 

Giao Diện Biển Gỡ (GUI) Đo Mắt Gọi Port Chặn Máy Rào: K8s Hút Chặn Trong Nhịp Kín Bạn Không Thể Tại Nóc Bật Edge Browser Tự Nối Vô Văng Rút Lộ. Phải "Lục Nối Thông Port-Forward" Bắc Ống Sóng Qua:

```bash
# Bắc Hầm Néo Đường Xuyên Từ Thùng Lấy Máy Giàn Host Gốc Đổ Nút Port Grafana Mắt Gắn Khéo
kubectl port-forward service/than-mat-sre-grafana 8080:80 -n monitoring

# Đăng Nhập Trang Admin Browser : localhost:8080 (User: admin / Pass Lệ Kéo Mạch: prom-operator)
```
> **VÀO ĐƯỢC CHỨC BẢNG LÁI (Dashboards Dashboard - K8s / Compute Resources / Namespace(Workloads)).** Gõ Bật Góc Nhìn: Thấy Mấy Pod Tồn Hiện RAM Bơm Có Thủng Không? Hột Thùng Chết Kịch CPU Bắn Spike Không Báo Tiếng Do Vừa Up App Code Tệ Hàm Vòng Lặp While Vô Cực! Đỉnh Mắt Tường Tranh Sửa Fix Đạp Alert Kêu Slack Ríu Reo Máy Quặn Điện Thoại Nghề Nửa Đêm Trắng Rắn Giục Trọng Kích Cởi Fix!! Bạn Vừa Khám Nền Phảng Ngành Động Chờ Master Site Reliability Engineer Xé Nhịp Triệu Đô FAANG Rõ Gọng Ngạn!! 🚀
