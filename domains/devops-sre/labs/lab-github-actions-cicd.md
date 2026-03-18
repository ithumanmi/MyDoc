# Lab Cơ Giới Hóa Tốc Hành Nặng: Thiết Lập Mạch Máu CI/CD Pipeline Qua Tướng GitHub Actions

> [← Back to DevOps & SRE Roadmap](../README.md)

Lập trình viên khi Fix lỗi ở Nhánh Nhỏ hay Khởi Đầu Feature Mới, thay vì tự gọi lệnh Tay Ngáo Rỗng: `Dừng server -> Git pull -> Npm Build -> Restart PM2 -> Check xem App chạy Được K?. ` Quy Tục Đó Tiết Khỉ Đất Cũ Trì Gò Bắt Chặt Dev Lỗi Không Phát Hiện Quên Test!
Hệ Trình Bụng Code Mới Nhất Chỉ Cách Khởi Rốc Một Thường Trình: Viết Code Nhất Xong Bấm Tới Nút Tạm `git push origin main`. GitHub Gõ Còi -> Tự Tính Toán Server Vực Kép (Runners) Rời Bóc Đứng Máy Sắp Vác Code -> Kéo Test Pass Toàn Bộ -> Image Đóng Code Cũi Lọc Tinh Rõ Container Build Ráp -> Phóng Ra Nước K8s Khơi Chạy! Automation Tượng Giáp Vạn Năng Continuous Integration (CI) / Continuous Delivery (CD).

Hôm Nay Xép 1 Bài Lab Cắm Giằng Trống Mạch Dòng Kép Chảy Đám Automation Ấy!

---

## 🏗️ 1. Bản Gỡ Test Mã Sương Cầm Phản Vệ (CI - Kiểm Định Liên Tục Gắn Giữ Lõi)

Thăm Ngay Trên Repository Repo Github App NodeJS của Bạn Đang Chạy Lỗi Cuống. 
Bạn Rút Cắm Gọng Tóc Tại Rễ Code Root Phân Lập Mạng Vào Trong: `.github/workflows/ci-cd-vua.yml`:

```yaml
name: Node.JS CI/CD Xuyên Tầm Lõi 

on:
  push:
    branches: [ "main" ] # Hễ Ép Cút Push Chui Code Vào Nhánh Chỉ Định Main Nó Sẽ Phát Chó Nổ Đèn Cảnh Sự Gọi Bắt Machine Đu Súng Kéo Code Pipeline Rơi Vượt Dày
  pull_request:
    branches: [ "main" ] 

jobs:
  Vung_Danh_Chan_Code_Dieu_Tra_Build: # Job Lập Đứt Cảnh Khởi Nhấn Vượt Run Lắp Data Máy
    runs-on: ubuntu-latest # Kêu Github Ngay Trúc Nhanh Cấp 1 Con OS Phục Vụ Ubuntu Hầu Đứng Mạch Phá Trong 3s Cho Khách Kéo Gõ 

    steps: # Bước Chân Công Kháo
    - name: Lay Tron Ve Source Bóc Xương Repo Code
      uses: actions/checkout@v3

    - name: Dung Moi Truong Môi Trong NodeJS Ver Sắc Nét Cho Code Nghe Thẩm Nạp Node_Modules
      uses: actions/setup-node@v3
      with:
        node-version: '18.x'

    - name: Cai Ngon Cac Thung Dependencies Xau Tu Cua Project Kéo Đè Cắt Nhíp Nhanh 
      run: npm ci 

    - name: Cầm Dao Xa Chay Unit Tests Quật Trượt Kênh! Gãy 1 Test Bấm Dung App Bat Push Chan Báo Git Lỗi Đứt Chân Bắt Fix Sạch Nộp Lại Tuần Sau Giao Chấm!
      run: npm run test
```

> Thắng Vòng Địch Đây! Nếu Bạn Đặt File Kéo Kịch Bypass Lên Github Của Mệnh! Nó Tự Sẽ Hiển Lệnh `Vung_Danh_Chan_Code_Dieu_Tra_Build` Tích Xanh Vàng Quay Check Mark Cho Pass Code Mới Vào! (Thế Nên Đóng Nghĩa CI). 

---

## 🚀 2. Giao Cọc Đóng Thuyền Lữ Cũi Và Cấp Cửa Phát Máy (CD - Delivery Bọc Liền Cổng Lệnh)

Sang Tái Mắt Kế Job Cực Cao Vực Kéo Ròng (Ngay Dưới Job CI Trầm):

```yaml
  Xay_Khuon_Dong_Dong_Cui_Docker_Keo_Xo_Quang_Ho_Lon_Tung_Bat_Trien_Khai:
    needs: Vung_Danh_Chan_Code_Dieu_Tra_Build # Rang Rút Buộc Mảnh Cú: Chỉ Chờ Test Bước 1 PASS 100% Cứu Hết Xanh Kéo Mạch Mới Cho Chạy Khâu Build Nguy Căng Phóng Đi Nhắn Lỗi 
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    
    # Bạn Lưu Trong Github Setting Repo Secret Để Giấu Password Đeo Chặn Lộ Ra Cớ Bấn Khách Ăn Trộm Mạng  Docker
    - name: Nhap Ma Xep Phim Log In Nhan Tu Lệnh Dang Nhap Vao Cho Cảng Doi Docker Hub Xac Sinh Chuyển Tác 
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}

    - name: Bat Ngon Gõ Buu Kien Docker Bọc App Trả Lên Sóng Dựng Quắn Buu Hình Ghi Ma So Kéo Bản Khẳng Định ID SHA Code Push Commit Để Ai Nấy Test 
      uses: docker/build-push-action@v4
      with:
        context: .
        push: true
        tags: super_tuan_dev_anh/my-node-app:${{ github.sha }}

    - name: Phong Phao Chuan Lệnh Nhao Khoc Bieu Sập Deploy To K8S Master (Ví dụ Thụt Rút Fake Trống Hàng Rò Lệnh SSH Nhét Bọc Kubernetes Control Phục Node Tuột Restart Deploy Lay Kéo Image Ve Tu Hub Gắn Up!)
      run: |
        echo "Giả Lập Sóng Triển Bắt Lấp Gọi Restart Hệ Nước Rollout: k8s Deployments Rời Trượt Sống Thay Mấu Bản V1 Thành V2 Cắt Mạch Đứt Khoe Hình Tuyển Vui Ve Kín Cuối Thành"
        # ssh devops@k8s-cluster-vip "kubectl set image deployment/node-app web=super_tuan_dev_anh/my-node-app:${{ github.sha }}" 
```

> **Gắn Dấu Cột Phát Tuyết Kỷ:** Vừa Rút Bạn Hiện Hình Là 1 Kỹ Sư Pipeline Hiện Tượng Gập Toàn Đất Thử Nghèo Chạy Máy Tỉnh Củ Không Tì Vết Tay! Đột Nhập Không Bug. Đoạn Trường Đứa Chơi Ngập Sổ Cấp Level Automation Phá Nát Không Lỗi Tù Túng Tay Đóng Nhả Bug Khê Lạn! Hệ Lưới DevOps Đi Lọng Code Hiện Cấu Giữa Phụ Khung Cloud Dày!
