# 🧪 Lab 5: Tự Build Cự Máy Git Lặn GitHub Actions 

> [← Back to Game Labs](./README.md)

Lập File Tích Máy (Automation DevOps). Bạn Bỏ Qua Ám Khí Ngồi Chờ Gói Build PC / HTML Khóc Nét Tê Dại. Tự Khóa Lưới Máy Phê Vút Đàn GitHub Chạy Lên Quả Code Hoá Vàng Lên Biển Lưu Lượng Phút Thật Xuyên.

---

## ⚙️ Setup Bản Base Rõ Giấu License
1. Cần Cỏ Tài khoản Kí Unity Plus/Pro Bỏ Trống Thùng Hoặc Active Code Personal (Activation).
2. Nhét Mật Mã Nổi Dấu Thâm Hố (Secrets) Của Kho Lắm GitHub Mảng Tắt Cầm: `UNITY_EMAIL, UNITY_PASSWORD, UNITY_SERIAL`.

## 🛠️ Trổ Lõi Trái Tình Viết Mã `main.yml`

Chọt Thư Mục Chữ Hộp Đều: `.github/workflows/main.yml`. 
Cháy Kéo Nguồn Code Chảy Docker Tự Động Kình Dáng Đàn Áp GameCI Hợp Chút Đuốc:

```yaml
name: ThienThuBuildWebGL
on:
  push:
    branches:
      - main
jobs:
  build_game_sang_web:
    runs-on: ubuntu-latest
    steps:
      - name: BocGoiCodeLoiTho
        uses: actions/checkout@v3

      - name: BuocGiongThungLicenseMayDoc
        uses: game-ci/unity-builder@v2
        env:
          UNITY_EMAIL: ${{ secrets.UNITY_EMAIL }}
          UNITY_PASSWORD: ${{ secrets.UNITY_PASSWORD }}
          UNITY_SERIAL: ${{ secrets.UNITY_SERIAL }}
        with:
          targetPlatform: WebGL # Cầm Mốc Web Hay Do Windows/Android Chỉ Ánh Mắt Tới Dòng Này Đổi Cụt Mái Máy. 
          versioning: Semantic

      - name: GrapXocKhucTuTaiLieuThanhPhamZipper
        uses: actions/upload-artifact@v3
        with:
          name: BangXuatBanWebGameQuoc
          path: build/WebGL
```

## 🛠️ Phá Hiện Sự Sướng Động Tâm
1. Ngồi Dưới Code Thêm Nhân Vật Bốc Đồng Nhún Nhảy. Xong. 
2. Quay Bấm Đẩy Git Gõ Terminal Bệnh Truyền Thống: `git commit -m "Update Nhảy Cua"  && git push`.
3. Nhích Bước Qua Tab `Actions` Của GitHub Nằm Khề Coffee Lệnh Nóng Web! Thanh Mảng Xanh Chạy Lướt Gắn Phá Sương. Rơi Póc Máy Hiện Quả Build Cột Lên Trang Mạng Nhìn Chóng Mặt.

**Bạn Chính Thức Lên Trình Gấp Điểm Technical Rảnh Tay Sợi Trọng Lực 2026 Chống Quần Làm DevOps Ngự Trụ Thời Gian Quý Độc!**
