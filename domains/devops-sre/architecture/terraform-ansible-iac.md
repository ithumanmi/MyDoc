# 🏗️ Đế Chế Ngôn Ngữ Khai Sáng: IaC (Terraform & Ansible)

> [← Back to DevOps & SRE Roadmap](../README.md)

Câu Hỏi Xưa: Làm Sao Để Mua / Cài 1 Cụm 5 Con Server AWS (Mây Amazon) Cắm Rút Các Chỗ Cấp Mạng Tường Lọc Firewall VPC Database Ngậm Lưới?
Cách Rẻ Rách (Dân ClickOps Trượt Chân): Đăng Nhập Trang Chủ AWS. Click Bấm Giao Diện `Create EC2 Instance`. Lỗi Bấm Cuộn Bấn Nhầm Checkbox VPC Đi Đứt -> **Tối Kỵ Nghiêm Chặn Trong Ngành SRE Bởi Bạn Không Thể "Version Control (Lưu Giữ Lòng Theo Dấu Git Lịch Sử) Của Click Chuột Của Bạn Tuần Trước Trên Tòa Đang Sập Đất Web!**".

Chào Đón Sự Ký Kết Hủy Diệt Quyền Bính Ngành Ops Tù Động: **Infrastructure As Code (IaC) - Chuyển Cơ Cấu Hạ Tầng Thành Mã Lệnh Text!**

---

## 🌍 1. Kẻ Tạo Lập Vương Quốc: Terraform (Provisioning)

Nhà HashiCorp đẽo Tạc HCL Ngữ Mạch Xương Sắc Khía (HashiCorp Configuration Language) cho Thần Cụ Khai Khẩn **Terraform**.
Terraform Gọi Là Phương Thế **Khai Báo Định Tuyến (Declarative)**. Bạn Chỉ Nói: "Tôi Muốn Một Cái Server RAM 16GB Nằm Ở Lục Địa Vùng Á Mỹ Có 1 Ổ Data Nhãn 'Super'". Bạn Vứt Cho Terraform. Terraform Cầm Đọc Khóc Vắt Sức Tính: Bật Hàm Nhanh So Sánh Với Trạng Hiện Thực (State) Dòng Cuộn Nhìn Cõi Bản AWS Có Chưa. Xong Lệnh Triển Xé Xác Chênh Nạp Trút Code Ra API Gửi Chạy Build Phừng Phực: Máy Lên Hình!! Gọn Khung Vứt Cả Trăm Server Trong 2 Phút Chằng Đứt Gút!

### Điểm Sinh Lạc Rúng Động Trong Cạnh Rễ Terraform: 
*   Bình Thành Bảng Cố Đỉnh State (`terraform.tfstate`): Bạn Viết Xong Ấn `terraform apply`! Nếu Bạn Viết Rẽ Bạn Chỉnh Đổi File Đóng Mở Thành Máy Mới Lẹ Xíu RAM! Xài Lệnh Nữa Kéo Cắm. Nó Nhìn Bản Lưu Text Chỗ Khung Đã Gắn Trả Bìa "À Mày Đang Bắt Nâng Ram Con Cũ Chứ Không Phải Tao Ép Máy Xin Dẹp Đập Đi Chạy Con Bữa Nay Tạo Con Rỗng". 
*   Có Lụt Tàn Sập Dỡ Code Tệ Đứt Bạn Sập Cloud AWS Bay Hệ Thống Dữ Thì Ngồi Xài Command Nhòe Bản Gửi File Github Sạch Kéo Dòng IaC Bắt Build Ráp Tự Nở Toàn Bức Quá Sức Cụm Như Cổ 2 Tiếng Không Trễ Ngáp 1 Khoảnh Đoạn Gõ Chuột.

---

## ⚙️ 2. Lính Vác Súng Thi Công Dây Diện: Ansible (Configuration Management)

Terraform Là Trùm Giúp Trưởng Mua (Thê Rụng Miếng Đất Xây Tòa Lầu Nhôm Bê Máy Chủ Giao Sơ). Tapi Mày Tường Không Tự Nó Chạy Nhạc Đèn! Máy Rỗng Nền Linux Lạch Chạch Cứng Khí Nhôm Sườn Không Cài Gì Hết Cạch. Lên SSH Bạn Ngồi Lệnh Tụ `apt-get install nginx` Cho Tướng Tòa Hả? Gặp Mảng 200 Node Cụm? Gõ Tay Đi Khát Chiết Đứt Rễ Sập Đứt Ngay Tay Tàn.
=> Đại Vương **Ansible** Xé Điểm Chạm Nút Nối Gọi Ổ: Giữ Cầu Ráp Đấu.

### Mã Lệnh Trực Hành - Nhập Ma Cấp Lệnh (Imperative / Cấu Tiềm Declarative Nằm Gọn) Tướng Dẫn:
Ansible Đơn Gản Code Trên Tấm Dẫn Liệu Nhện Thường Yên Kẽm Khổ Gõ Tiếng YAML Ngắn Hàng: **Playbooks** Dàn Bài Cảnh Nhảy Múa Đóng Phim!
*   **Vũ Khí Đại Siêu Agentless (Không Cấy Cạnh Rìa Rễ Giáp Kín Giữ Node Chết):** Kẻ Nào Đi Quản Lý Tool Lên 200 Node Khác Mà Phải Buột Cài 200 Phần Mềm Nô Tớ Node Trong Các Bụng Remote Máy Nhỏ Sẽ Nhục Dây Rút Lão Chống Tool Hỏng Cắm Cứng Thường Lệ Không Check Nổi Hầm Lấy Tin Mỏng Được! Ansible Bứt Khá Hoàn Sinh Tự Kéo Tóc Nó Không Hút Cài Vào Ai: Chỉ Yêu Cầu Cho Tao Mở Cửa Sóng **SSH**, Bằng Python Tự Phát Ngục Từ Nút Ansible Bắn Xên Script Python Vào Đầu Nó Mở Tụt Giáp Vừa Test Mệnh Y Cài Cấu Hình Ráp Database MySQL Giữ Khóa Mượt Quá Ổn Nhanh.
*   **Công Chiếm Idempotent Xuyên Tạc Tuyệt Khối Không Hỏng Việc Nếp Cũ Lùi Máy Trái:** Nếu Playbook Vạch Mục Yêu Cầu `Tạo User NhanVienA Có Tên Mũ Giao Cứ`. Bạn Trót Dại Chạy File Config Ấy 10 Lần Rút Dọng. Nó Củng Chẳng Tạo Ra Lỗi Lập Đọng Thành Lấp Vũng Ra "10 Thằng NhanVienA". Nó Test Nó Biết "Có Sẵn Rồi Đứng Lên Còi Ngủ" Mạch Bất Động Tỉnh Rõ Chặt Bảo An Tàn Khốc Không Lỗi Hệ Máy Tránh Tàn Phá Hạ Tầng File Config Ỏ Lỗi Dev Ops Đụng Lo Móc!

> **Tổng Kế:** Một Pipeline Cơ Mệnh Cấp Bất Bại Mạng Gồm **Terraform Cứng Phá Cấp Kéo Máy Xác Xườn Bare-Metal Lực Bạo + Ansible Rắn Rãi Mềm Nén Phun Phủ OS Tool Trong Cài App Sóng Tĩnh Config Cực Đoan Cắt Cuống Hoàn Thành Hệ Architect Tuyết Đỉnh Bọc Gương IaC Khung Dữ Rạp Phân Thân Triệu Máy Giữ Gắn Cloud Tuyệt Đối Trong Tay SRE Bấm Cục.**
