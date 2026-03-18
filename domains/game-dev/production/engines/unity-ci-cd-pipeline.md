# CI/CD Pipeline Cho Game Dev: Tự Động Hóa Nhàm Chán

> [← Back to Production & Engines](../README.md) | [Home](../../../README.md)

*Cảnh quen thuộc của Solo Dev lúc 2 giờ sáng:* Nhấn Ctrl+B (Build And Run). Khóa cứng Unity Editor trong 45 phút, ngồi nhìn thanh Loading chạy ngước ngơ máy tính đơ lag. Cuối cùng, 45 phút trôi ra file APK lủng, quên tắt Debug Panel. Mệt mỏi ném vô xó đi ngủ!

Chào mừng bạn đến với khái niệm **DevOps cho Game Dev (Continuous Integration / Continuous Deployment - CI/CD)**. Thức tỉnh năng lực của Server.

---

## ⚙️ 1. CI/CD Là Gì Trong Game Development?

Bạn viết code (Code C#). Máy tính của Cloud sẽ tự giác làm 3 việc Đen Đói sau đây (Trong lúc máy tính bạn Vẫn Đang Thảnh thơi Viết Code Tiếp hoặc Đóng màn hình Đi Chơi):

1.  **CI (Continuous Integration):** Test code tự động. Trải hệ luồng Unit Test, Đảm bảo bản Check-in mới lên Git không đập vỡ tính năng Bắn Súng của Ngày hôm qua. (Chống Regression Bug).
2.  **Continuous Build (Nightly Build):** Kéo Source Code Mới Nhất Trên Nhánh `main`, Kích hoạt dòng lệnh gọi Unity Không Cần Giao Diện (Headless Mode), Build Rớt ra Dạng File `.exe` hoặc `WebGL`. 
3.  **CD (Continuous Deployment):** Tự xách tấm File Build vừa Xong, Vứt thẳng Cổ Tải Lên Máy chủ Nội Bộ Cty Đêm Khuya (Cho Tester sán láng Có Bản Xài), hoặc ném văng Lên Steam qua SteamPipe/ TestFlight Apple chờ Duyệt Chớp Mắt!

---

## 🤖 2. GitHub Actions: Lưỡi Dao Pha Lê Miễn Phí

Năm 2026, Gamebuilder / Jenkins quá rườm rà. **GitHub Actions** (chạy nhờ hạ tầng Ubuntu/Windows Container của Microsoft miễn phí 2000 phút/tháng) là bạn nối khố siêu xịn.

### Cơ Chế Hoạt Động Của GitHub Actions Cho GameBuilder 
File Ma thuật chỉ nằm trong một hẻm thư mục tên: `.github/workflows/main.yml` (Định dạng Yaml).
Kịch bản (Workflow) khi bạn `git push`:
1.  **Checkout Code:** Lấy toàn bộ Project Unity từ Git xuống cái máy tính Đám mây (Runner).
2.  **Setup Tooling (Hành Động GameCI):** Kéo cái Docker Hình Nộm chứa Phiên Bản Unity Chính Xác Nhất của bạn (VD: `ubuntu-unity-2023.2.14f1`).
3.  **Activation:** Nhập mã số License Unity Của Cty/Cá Nhân bạn (Dấu bí mật Repository Secrets) để Unity Nhận ra bạn.
4.  **The Build:** Chạy lệnh nén Nguồn vào Thành Cụm Game Rắn Chắc. Chỏ Đầu Ra Dạng (Windows 64Bit).
5.  **Artifact Upload:** Gói cục Quả Thành Phẩm ZIP Lại. Quăng Lên Vách Git Sừng sững Hoặc Discord Cho Anh Em Ấn Download!

---

## 🚀 3. Mốc Rẻ Nhanh Giải Phóng Thời Gian

"Mất 1 Lần Trầy Trật Thức Đêm Setup CI/CD, Xa Rời Cảnh Chuột Rút Build File Trọn Kiếp". 

Việc Phân nhánh `Develop -> QA -> Prod` Xử lý Hoàn Toàn bằng Nhánh Git Branch. 
*   Bất Cứ Code nào Push Vào Dải nhánh `qa-testing_branch` -> Chĩa thẳng Nòng Build Ra `APK Android` quăng Discord Cho Tester Kẹp máy Tính Bảng. 
*   Push qua Dải nhánh `Release-Steam_branch` -> Phun Thành Phẩm thẳng Lên Dashboard Store.

> 🧪 **Thực hành vỡ lòng:** Thôi đọc lý thuyết. Nhảy vào [Lab: Setup GitHub Actions Build Unity WebGL Tự Động YML Định Dạng](../../labs/lab-unity-github-actions.md) để thấy máy móc làm mướn cho mình sướng cỡ nào!
