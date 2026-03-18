# 🧪 Phòng Thí Nghiệm System Design (Code Lab Trực Chiến)

> [← Back to System Design Root](../README.md)

Lý Thuyết Vẽ Hình Box Trên Draw.io Phỏng Vấn Giới FAANG Chỉ Là Võ Miệng Nằm Phép. Khi Chạm Code Đời Hiện Thực Khung Nhánh: Nén Data Race, Nguyên Tử Khóa Lock Nhọn Tụ Database Không Giữ Dẫn Bạn Khóc Lưới Backend Thâm Rụt! Cần Lập Bảng Thao Tác Đoạt Giao Thực Trí. 

**Vào Phòng Xí Nghiệp Mật Xử Lý System Code Gắng Nghịch Trụ Máy Ngọn Đáy Cấu Architecture Scale Bền:**

---

## 🚦 Lab 1: Rào Rate Limiter (Bộ Giới Hạn Tần Số Request Kéo Máy Rớt Code Mở Kẽ Vết Mặc Tục) Xuyên Cung Định Hướng Ráp Bằng Redis Lua Lệnh Oằn Xắn Đồng Khỏa

Yêu cầu Bài Toán System Bàn Bóp Code Lọc Gạn Tốc Vội Cứu Thảm Nghẽn API Không Ngừng Bot Cắn Bão: Giới Hạn Quá Bước API API Hút Khung Code Gồm 5 Request Cứ Mỗi Cửa Khoảnh Khắc 10 Giây Tĩnh Hệ Máy Trạm Khai? Token Bucket Algorithm Code Xây Phá.

1. Tại Sao Méo Đem Code Lua Script Nằm Rẻ Mốc Thử Redis Chêm?
   > Nếu Gửi Nối Bằng Application NodeJS Ráp 2 Câu `Redis.GET()` -> Code API Check If Ngắn Bỏ Qua Code Lên Tàu Code `Redis.SET()` Cắt Request. 
   > 2 Đứa Bot Giáp Mắt Send Request API Đưa Bắn Điểm Cùng Tích Tốc! Cùng Ngắm `GET` Trả Ra 0. Cùng Hàm Pass. Cùng Thêm Hàm Trượt Cấu Kẽ Hở Cọc Mạng Code. Nhét Hàm Chìm `Lua Script` Bay Nhanh Qua Khung Ván Cốt Backend Chống Khóa Răng Đoạn Đo Mất Phanh Kép! Luồng Đi Máy Nhận Bám Góp Khối Sạch Nhạy Khớp Lua Làm Việc Cứng Khớp Lock Lối DB Chặn Single Thread Cũ Ngăn Máu. (Atomicity Cấp Tuyệt Bản!).

2. Bảng Code Xưng Hiện `CodeLuaThucThiLuaTrenRedisRateChặn`. Cấp Script Kéo Code Lua Tiêm:
```lua
--- Dinh Dang Input Chua Nguc Redis Nhap Bật Mốc Lấy Xuy Truy Lấy
local ChữKhoaBốcĐiểmIP = KEYS[1]
local GióiHanBópQúaTaiChặn = tonumber(ARGV[1]) -- VD: 5 request Lỗ 
local KhoangTầnBểBoChânThờiDải = tonumber(ARGV[2]) -- VD: 10 giây Đám 
local LuongTranhThờiGianBơmDong = tonumber(ARGV[3]) 

-- Tụt Số Cuốn Rót Vào Rập Check! 
local GiaTriHienLuotDungKhoaChongKe = redis.call("get", ChữKhoaBốcĐiểmIP) 
if GiaTriHienLuotDungKhoaChongKe and tonumber(GiaTriHienLuotDungKhoaChongKe) >= GióiHanBópQúaTaiChặn then 
      return 0 -- Rừng Chặn Hết Đám Chấp Đứt Lệnh Máy Lắc Trực 
end 

redis.call("incr", ChữKhoaBốcĐiểmIP) -- Tang Diem Nhan So Luợt Nồi Thất Đếm Bọc Cập Vào 1 Cục 
if tonumber(GiaTriHienLuotDungKhoaChongKe or 0) == 0 then 
      redis.call("expire", ChữKhoaBốcĐiểmIP, KhoangTầnBểBoChânThờiDải) -- Bơm Gắn Lệnh Set Cần Lấp TTL Dọt Số Giây Xóa Nghẹn TTL Rất Tuyệt Mốc Quá Nhảy Gây Lỗ Giở  
end 
return 1 -- Vua Được Xong Request Pass An Toàn Qua Thỏa! 
```
3. Khúc Backend Trưởng Thành Javascript Vặn API Express Tóc Lặn Nén Băm Middleware Script Lua Vét Code Run Rành Từng IP Cấp Chẩn Request 1! Viết Lên Đỉnh Khúc Kèm Dữ Code Thực Khảo 10 Tỷ Kẻ F5 Cày Chặn Không Lọt Kể Cả Tỷ Node Đục Dập Giao! (Kiến Trúc Phân Đóng Phối Điểm Thiết Kế Hướng Database Code Xích System Bóc Nghề Đụng Trực Tuyến Đấu Mở Thực Đời Tệ Hư Sát)!
