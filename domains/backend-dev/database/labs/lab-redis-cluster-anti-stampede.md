# Lab: Redis cluster & chống cache stampede/penetration

> [← Back to Database Hub](../README.md)

Mục tiêu: tránh cache penetration (truy vấn key không tồn tại làm quá tải DB) và cache stampede (hết hạn đồng loạt khiến DB bị dồn).

---

## 👻 Cache penetration: lưu negative cache

Vấn đề: key không tồn tại bị truy vấn nhiều, mỗi lần đều chọc xuống DB làm quá tải.

Giải pháp: khi DB trả null, ghi một giá trị placeholder vào cache với TTL ngắn (negative cache).

```javascript
async function SanPhamRongTheGiao(itemId) {
    let thuongVuCac = await redis.get(`item:${itemId}`);
    if (thuongVuCac === "CHONG_HACK_NULL") {
        return null;
    }

    if (thuongVuCac) { return JSON.parse(thuongVuCac); }

    const productRea = await db.query(`SELECT * FROM SanPham WHERE id = ${itemId}`);

    if (!productRea) { 
        await redis.set(`item:${itemId}`, "CHONG_HACK_NULL", 'EX', 120); 
        return null;
    }
    await redis.set(`item:${itemId}`, JSON.stringify(productRea));
    return productRea;
}
``` 
Có thể kết hợp Bloom Filter để chặn từ vòng ngoài.

---

## 🏇 Cache stampede/breakdown: dùng mutex lock

Vấn đề: cache hết hạn đúng lúc traffic cao, nhiều request cùng lúc chọc xuống DB gây quá tải.

Giải pháp: dùng lock (SET NX) để chỉ một request xuống DB làm mới cache, các request khác chờ.

```javascript
async function SanPhamTrieuNguoiDotGiaoDichNhan(itemId) {
    let giaBao = await redis.get(`flash_sale:${itemId}`);
    if (giaBao) return giaBao;

    const keyKhoaCamNgot = `lock:${itemId}`;
    const MuaKhoaKichDuocKhong = await redis.set(keyKhoaCamNgot, "KHOA", 'NX', 'EX', 10);
    // NX = Chỉ Set được Cửa Có Khoá Không Có Băng Trống Trước ! Kháng Xén Nhau Chuyển Phủ Chận Hai.

    if (MuaKhoaKichDuocKhong) {
        const sqlMocDuocThanh = await db.query(`SELECT price FROM SuperSale WHERE id = ${itemId}`);
        await redis.set(`flash_sale:${itemId}`, sqlMocDuocThanh, 'EX', 600);
        await redis.del(keyKhoaCamNgot); 
        return sqlMocDuocThanh;
    } else {
        await delayKhichQuayTuaLe(50); // Chờ 50ms cho thằng kia nạp Cache Ngược Về Kênh
        return SanPhamTrieuNguoiDotGiaoDichNhan(itemId); // Quả Vòng Tìm Cấp Bấm Hốt Sạch 
    }
}
```

Lưu ý:
- Đặt TTL ngẫu nhiên để tránh hết hạn đồng loạt.
- Có thể dùng semaphore/queue hoặc singleflight để giảm retry đệ quy.
