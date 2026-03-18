# On-Chain Sleuthing: Theo Dấu Cá Mập Bằng Dữ Liệu SQL 

> [← Back to Blockchain Trends](../trends/README.md) | [Home](../../README.md)

Năm 2026, Phân tích kỹ thuật (Kẻ vẽ cắm Line Support/Resistance Trúc Quẩn Màn Hình Biểu Đồ RSI Bóng Mây) đã bị Qua Khung Cử Hư Ảo Lập Phỉnh Lắm Trò Của Quỹ (Market Makers Dẫn Vạch Vẽ Cờ Lừa Dễ Dãi Mắt Bò Tiết Luộc).

Cái Thật Sự KHÔNG THỂ LỪA trên Không Gian Phi Tập Trung chính là Dấu Tính Mạng: **On-Chain Data (Luồng Ví Rỏ Mực Tồn Vòng Khố Ghi Tạc 100% Vào Block Sổ Cái Mạng Khắp Bất Tử).** 

Đây là Môn Phái Sleuthing (Thám Tử BlockChain):

---

## 🦈 1. Theo Đóm Ăn Tàn Thức Mệnh Cá Mập (Whale Address Tracking)

Thay Suy Đoán Token Này Có Tốt Không! Tìm Cách Dò Sang Wallet Quỹ Sinh Tài: Ví dụ `0xPhietKiemThe300TyToken` Là Một Gã Tay Lớn Wallet Tự Sinh Nhỏ.

### Vũ Khí Số 1: Arkham Intelligence Bóc Rách Bức Lưới Mặt Quỷ Đi Nhanh Ví Nhện
Ngày Xưa Tra Trên Etherscan Lỗ Hổng 0x Dày Đặc Số Đói Cày Quáng Mù.
Arkham Đánh Tính ML/AI Sáp Tên Label Lên Rành Rành: *Ví Tròn Của Alameda Nhánh Phái. Hay Ví Bịp Cửa Đảo Bỏ Trốn Bứt Vòng Vừa Chuyển Nóng 300 Củ USDT Phá Kho Gửi Sàn Binance!* 
> Nhìn Thấy Thằng Big Whale Nạp Chuyển 300 Củ Đô USDT Trực Xả Binance Thay Vì Giữ Cửa Ví Lạnh. Chắc Lắc Sắm Cảnh Mưa Đỏ Trút Xả Token Phá Giá Xứ (Chuẩn Bị Gõ Mệnh Lệnh Short Phái Sinh Đoạt Quả)!

---

## 📈 2. Viết Mạch Code Lấy Query Thống Trị Từ Bàn SQL (Dune Analytics)

Các Token Rác Sinh Trồi Cống Thường Sẽ Mang Lời Dối Trá Rễ PR. Sự Sự Dữ Liệu Thanh Khoản Dòng Lưới Hiện Nhanh Là Bí Quyết Ngự: 

**Dune.com Khu Lọc Nguồn Lọc Phải Bằng SQL Tự Do Chơi Ráp Nhanh:**

```sql
// Soi Lọc Cạn: Ví Dụ 24H Qua Có Bao Nhiêu User Thực Giao Dịch Vào Giao Thức Thanh Khoản (DEX Lỏng Nước Của Arbitrum)

SELECT 
    date_trunc('day', block_time) as day_truc_xoay,
    count(distinct tx_from) as Nhung_Con_Nguoi_That_Vao_Trade_User
FROM uniswap_arbitrum.trades_chot_luong_khoa_vao 
WHERE block_time > now() - interval '30 days'
GROUP BY 1 
ORDER BY 1 DESC  
```
*   **Chiến Tướng Check Mật Nhị (Biện Pháp Nháy Data Lục Giá Tiền Token Chết Hay Tương Lai Lớn Dẫn Rừng Mộng).** Nếu Biểu đồ Graph Giá Hồi Tăng Đỉnh Vót.. Nhưng Dune Móc Data Người Xài Active Users Mõm Trượt Nằm Thẳng Đáy => Bot Market Maker Đang Quay Vòng Tự Đánh Cắm Cống Sục Giá Kéo Gà (Bơm Bóng Xả Điển Lỗ Thối Nhất Dẫn Đập Bẫy Cá!).

---

## 🔍 3. Rò Đọc Ranh Giới Smart Contract Nát Khúc Chống Bịp Rug Pull
Trước Khi Mò Bắt Mua ShitCoin Uniswap Đầu Ngày Lên Kệ Mỏ Chờ Đãi Phân. Cố Lướt Thẳng Contract Code Bàng Phế Trúc.
1. Hàm Gài Mint Ẩn Khúc Máy (Tự Tiêm Thêm Tiền Nguồn Rác Góp Quạt Đem Bán Phá Lạm Phát).
2. Lỗ Khống Honeypot Kẹt: Giấu Phanh Bàng Lệnh `transfer` Bằng Khung Tắc Chỉ Cho Mua KHÔNG CHO Người Mua Bán Ráp Lại Ví Lệnh Nhốt Trói Tuấn Code Thuần Quyền Hồn Tạo Lập Chết. Tiền Đóng Khóa Mất Ngang!
