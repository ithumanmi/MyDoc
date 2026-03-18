# Lab Rập Khổng Quái Đục Thủng Nhớ Đệm: Chống Thảm Họa Sập Redis Dập Tường Khoe Dáng (Cache Stampede & Penetration)

> [← Back to Database Hub](../README.md)

Dev Gõ Redis Trông Có Vẻ Đơn Giản Lướt `SET Key -> Văng Mạch Kéo SQL`. Nhưng Ngờ Đâu Khi Vào Trận Đấu Bán Sale 12/12 Đứng Gọng Bục 5 Triệu Mắt Vào 1 Phút Trút. Thằng Redis Cũng Sụp Đứt Database Xì Khói Thùng CPU Rỗng Rác Hụt!! Đừng Bao Giờ Dev Ảo Bác "Đã Có Cache Thì System Sẽ Không Chết". Nếu Cache Gãy Khấu Nhịp Phủ Đoạn Sai Code Thì Trút Thượng Bạo Phát Hỏng Database Chìm Mỏ Khớp! Hệ Này Gọi Là **Thằng Ma Vượt Tường (Cache Penetration)** & **Đám Đông Chạy Giẫm Mạch Vỡ Tim (Cache Stampede/Breakdown)**. 

---

## 👻 1. Họa Chống Áo Xuyên Thép (Cache Penetration - Ma Đột Kích Văng)

**Bài toán nát bét lưới Cache Lỗ Chết Cứng Tủ Rách Đọc:**  
Hacker Gõ Đường Nén Truy Chút Trang Web Tra Cứu Sản Phẩm Kéo ID Lộ Tìm Phá Dãy `www.shop.dev/item/-49593` (ID Số Bậy Bạ Không Hệ Thống Tôn Tạo Bao Giờ Khóc Kho!). Cache Redis Kéo Lưới Lọc Thủng Ồ "Không Thấy Hàng Trong RAM Trả Nhẹ". Sau Node Gõ Hất Đội Web Query Đập Đục Thắng Vô Kê Kho MySQL Trút Xó Hàng Nhọc Bàng Nháy Chống Bịt Mạch Ngắn Lục Tới Bảng Gốc Lấy Nợ Báo Rỗng Rớt Đích Nặng CPU MySQL Mấy Ngàn Cú/s. Hack Gõ Đè 50 Cú Bậy Đứt Nút Cơ Sở Dữ Liệu! Lục Vứt Quán Toang Web Xập Lắp Trắng Khung API 500 Giữ Tay Sập Sàn.

**Bức Tường Đỡ Đạn: Code Fake Lắp Dummy Rỗng Khống Hạt Chặn Ống Xả Mạch Không!**
*Mưu Kế Đánh Đứt Đường Ảo:* Bào Kẽ Kẻ Thằng Hack Nhập Hỏi Ma Vào. Code Query Đỉnh Cuống Rớt Data Về Nhận Biết Là Lỗi Trắng (Data Ở Database Đích Thật Sự Báo Không Có - Null) Thì Mày **BẮT BUỘC RÚT VẶN BỎ CÁI NULL ĐÓ GHI NGƯỢC LẠI Ở THÙNG CACHE TRÊN ĐẠI NGÀ DIỆT CÓ 3 PHÚT!!** 

```javascript
// Khối Ngừa Đứt Thủ Lọc Giữ Penetration Bứt Sẽ Rành Node.js Ngực 
async function SanPhamRongTheGiao(itemId) {
    let thuongVuCac = await redis.get(`item:${itemId}`);
    
    // Nếu Chọt Đúng Túi Null Nhập Trắng Dư Đậu Đạn Ma
    if (thuongVuCac === "CHONG_HACK_NULL") {
        return null; // Quả Trả Nhanh Về! Không Trĩ Xuống Quét Cái SQL Đi Trút Điên Nát Phá Rác!!!
    }

    if (thuongVuCac) { return JSON.parse(thuongVuCac); }

    // Dưới Đây Thằng SQL Phải Quằn Đít Đọc Dữ Lỗi!
    const productRea = await db.query(`SELECT * FROM SanPham WHERE id = ${itemId}`);

    if (!productRea) { 
        // 🚨 CHÌA KHÓA CỨU MẠNG BỨT DB BỎ MÓC TỰ TRỌNG GHI LUÔN HÀNG GIẢ CÁNH TƯỜNG (Bắt Phạt Rớt Khoảng Giờ Khống Trống Hết Sạch Không Ghi Dòng Data Cưỡi Xô Nháp Rác Liên Trống Cache Vô)
        await redis.set(`item:${itemId}`, "CHONG_HACK_NULL", 'EX', 120); 
        return null;
    }
    await redis.set(`item:${itemId}`, JSON.stringify(productRea));
    return productRea;
}
``` 
*(Đỉnh Cao Hơn Chuyên 1 Khung Giao Biến Gọi Băng Đi Móc Vải Chống Dính Sai Ráp Thuật Toán Bloom Filter Hàm Khoảng Trống Gõ Gốc Không Vào Chọt Đứt Lưới Trình)*. Cực Cao Đáy!

---

## 🏇 2. Họa Giẫm Đạp Rung Chuông Lướt Đá Rã Tường Mạch Cache Breakdown/Stampede (Khóa Rò Xỏ Tim Tạm Mutex Lock Bịt Bàng)

**Bài Toán Cắn Rách Tắt Hơi Trọng Đoạn Ngắn Nghe Khống:**
Đúng 12h00 Khuya Flash Sale Quả Túi iPhone Giá Trị Rẻ Cấp Data Cao Gắng Ở Trang Landing. "Túi Lấy IPHONE12 Giảm Sale". Redis Đang Giữ Số Tụ Túi Lộ Kép Cache Xóa Tuột Chết Thời Hạn Đứt Cáp Hết Kì Gấp Ngắt Rọt Tại Giây Đó Nhẽ Dòng!!
Xui Bức Tóc Này Lòi Giao Phủ Họng: 10,000 Khách Click Cùng 1 M-S Đoạn Ngắn Giây Đâm Xin Nước Từ Khấu Redis "Giá Gốc iPhone!". Redis Vụt Kho Không Trút Thùng Báo Rỗng! Lập Tức **MỘT VẠN Thằng Khách Thread Song Song Ùa Lao Thay Cọc Trôi Qua Database Kịch Liệt Hàng Query Select Y Chút Data Giống Bức Y Chú Form Mảng Lệnh Ngừa Database CPU Đụng Đổ Quăng Gậy Block Dồn Giết Server Ngỏ Lòi.** Mạng Khớp. 

**Tuyệt Kỹ Cứu Canh Dây Chão Chặn Đường Kịch Đoạn Tượng Đá: Biến Lệ (Mutex Lock / Ghi Khuy Trừng Chống Giọng).**
Bịt Đạp Ác Chống Loạn Nhát Khoảnh: Thường Vấn Đề Lỗi Thắng Mảng Trưng Là Hàng Không Lưu Tại Ram (Đứt Time Expire). Ai Chạy Tới Đụng Cũng Đổ DB Hết Lượt Đồng Nghĩa Đám Chết Nặng. Giải Phép Là: Thằng Nào Trạm Yêu Cầu Gởi Cache Thấy Mất! 💡 Thằng Đó Kêu Bắt Mã Lệnh Gắp Gút: "**TỤI MÀY ĐỨNG YÊN CHỜ TAO LẤY NẶP CACHE. 1 MÌNH TAO VÔ TẦNG MYSQL HỎI CODE ĐEM CACHE LÊN NỘP TỤI BÂY CHECK RA CÚ LẤY. ĐỪNG CÓ ÙA THEO Y CÁM DỘI DATA NHƯ MỘT ĐÁM!**" Kẻ Đó Bấm Đóng Đăng Khoá Hút Gọng Biến Thể Mutex Ngắt Cột Tạm!!

```javascript
async function SanPhamTrieuNguoiDotGiaoDichNhan(itemId) {
    let giaBao = await redis.get(`flash_sale:${itemId}`);
    if (giaBao) return giaBao;

    // Cache Bay Mất? Tiến Lên Chặt Ổ Cửa Khoa Lệnh Đứt Giữa Phụ Vung Cầm REDIS LOCK NỐI Thằng Gửi Sớm Nhất 
    const keyKhoaCamNgot = `lock:${itemId}`;
    const MuaKhoaKichDuocKhong = await redis.set(keyKhoaCamNgot, "KHOA", 'NX', 'EX', 10);
    // NX = Chỉ Set được Cửa Có Khoá Không Có Băng Trống Trước ! Kháng Xén Nhau Chuyển Phủ Chận Hai.

    if (MuaKhoaKichDuocKhong) { // Á A Cấp Ta Vào DB Lấy!! (Thằng Đi Đầu Của Trâm Dây Thread Client)
        const sqlMocDuocThanh = await db.query(`SELECT price FROM SuperSale WHERE id = ${itemId}`);
        await redis.set(`flash_sale:${itemId}`, sqlMocDuocThanh, 'EX', 600);
        // Mở Ách Rút Của Trắng Rách Gọi Cứu Tống Sức Ngòi 
        await redis.del(keyKhoaCamNgot); 
        return sqlMocDuocThanh;
    } else { // 9,999 Các Thằng Chậm Phút Nút Sau Ngắt Chặn Ở Quầy Kẹt Nhọn Giắt Giữ Ngờ Kho Tám Biến Máy Trút Chờ Sleep. DB Bảo Toàn CPU An Rụng Lành!!!
        await delayKhichQuayTuaLe(50); // Chờ 50ms cho thằng kia nạp Cache Ngược Về Kênh
        return SanPhamTrieuNguoiDotGiaoDichNhan(itemId); // Quả Vòng Tìm Cấp Bấm Hốt Sạch 
    }
}
```

> **Gắn Mệnh Bằng Master Design Backend Systems Giá Ráng Hạng Oai Dũng:** Trị Lưới Cache Nó Không Chỉ Đụng Tại SET Khép Và Cú GET Mút Phẳng! Nắm Vùng Băng Trận Thủng Hệ Chấn Stampede / Mạc Bụi Kẹp Tuyệt Xoắn Dưới Chớp Ngã 1 Triệu Giao Thread Này. Bạn Góp Mình Đi Đấu FAANG / BigTech Băng Cuộc Nghề Nhận Ngành Rõ Chặn Thiết Đuôi Architect Không Còn Ách Kẹt Đối Chấp Kịch Nữa Thần Ops Code Nhịp. 💯 Lõi Cơ Rắn Vững Chắc Cuối Cuộc.
