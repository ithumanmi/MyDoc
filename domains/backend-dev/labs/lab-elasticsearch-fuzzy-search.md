# Lab Nâng Cáo: Xây Cỗ Máy Tìm Kiếm Của Tiki/Shopee Dùng ElasticSearch (Fuzzy Match Lỗi Chính Tả)

> [← Back to Backend Labs](./README.md)

Khi Bạn SQL Chọn `WHERE name LIKE '%iphone%'`:
1. Quét Cả Table Hàng Triệu Dòng (O(N) Độ Chậm).
2. Gõ Sai "iphnoe" Sẽ Ra Khung Trắng Xóa! 

**ElasticSearch (Thư Viện Phân Tích Lucene Máy Java Mở Khung Search Inverted Lưới Từ Lóa Text Ngữ Cảnh)** Sẽ Cứu Việc Kinh Doanh Bán Hàng Ngàn Đơn Mặc Lỗi Gõ Máy Của Bạn Dùng Thuật Toán Khoảng Cách Băng Đảo (Fuzzy Levenshtein Distance).

---

## 🛠️ Bước 1: Treo Docker Kiệu Đưa ElasticSearch Và View Dashboard (Kibana)

Dựng Khung Máy Java: `docker-compose.yml`:
```yaml
version: '3'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.8.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m" # Xài 512MB RAM Cho Nhẹ Local!
    ports:
      - "9200:9200"
  kibana:
    image: docker.elastic.co/kibana/kibana:8.8.0
    ports:
      - "5601:5601"
```

Chạy Terminal: `docker-compose up -d`. Vào Trình Duyệt Go Tầng Kiểm Tra Máy Search Sống: `http://localhost:9200`.

---

## 🗃️ Bước 2: Nạp Gạo Bơm Hàng Triệu Record Bằng NodeJS (Phân Điểm Bảng `san_pham`)

Cài SDK Tìm Kiếm: `npm install @elastic/elasticsearch`
Bạn Viết NodeJS Mồi Thọc Lỗ Bắn Data Trắng Qua File Bulk Để Khung Elastic Tự Phân Ra Chém Text Lập Lỗ Cắt Index Matrix Nhanh:

```javascript
// dua_data_vao_elastic.js
const { Client } = require('@elastic/elasticsearch');
const bomClient = new Client({ node: 'http://localhost:9200' });

async function nopBieuKhungKhoDataDeMuc() {
  // Khoi tao Dinh Dang Phieu Bieu Thuc Data (Index) Co Ten La 'san_pham'
  await bomClient.indices.create({
    index: 'san_pham',
    body: {
      mappings: {
        properties: {
          id: { type: 'keyword' },  
          ten_mon: { type: 'text' }, // Loại Text Này Thần Kì Elastic Sẽ Máy Chém Analyzer Nát Ra Bã Tokens! 
          gia: { type: 'integer' }
        }
      }
    }
  }, { ignore: [400] });

  console.log("Nối Ống Index Vào Sợi Tích Lũy Thành Bảng Kho Rỗng 'san_pham' 🌪️");

  // Dua Mau 1 Vach Data San Pham Cho Elastic No Chop!
  const KhoSotSanPhams = [
    { id: 'PROD_1', ten_mon: 'Điện Thoại iPhone 16 Pro Max 256GB Gold', gia: 35000 },
    { id: 'PROD_2', ten_mon: 'Sạc Dự Phòng Pisen Chính Hãng', gia: 500 },
    { id: 'PROD_3', ten_mon: 'Bao Da Ốp Lưng SamSung Galaxy Cứng', gia: 200 },
    { id: 'PROD_4', ten_mon: 'Tai Nghe Không Dây Apple AirPods Pro', gia: 6000 }
  ];

  for (let mon of KhoSotSanPhams) {
     await bomClient.index({
       index: 'san_pham',
       document: mon
     });
  }

  // Lệnh Báo Cho Elastic "Sắp Xếp Dọn Index Lại Để Cứu Lưới Query Dịch Search Có Ngay" (Hoàn Tất Nạp)
  await bomClient.indices.refresh({ index: 'san_pham' });
  console.log("Xong Kho Nạp Data Phẳng Vào Nút Lưới Text Analyzer Của Elastic! 🍔");
}

nopBieuKhungKhoDataDeMuc();
```

---

## 🔎 Bước 3: Tìm Kiếm Lỗi Chính Tả Chệch Cỡ (Fuzzy Trả O(1) Match Score Lucene)

Bây Giờ Khách Mù Mắt Gõ: `iphnoe mak` Trên Ô Search. Máy Vẫn Trả Đơn!

```javascript
// tim_loi_chinh_ta.js
const { Client } = require('@elastic/elasticsearch');
const timCuaClient = new Client({ node: 'http://localhost:9200' });

async function bo_may_chua_te_search_lan_text() {
  const ChuKhachGoLoiMuoi = "iphnoe mak"; // VIẾT SAI MẤT NÚT NGUYÊN BẢN CHỮ "IPHONE" ! 

  console.log(`Bắt Đầu Quăng Lưới Tìm Thuật Cáp Fuzzy Với Text: [Khách Gõ: "${ChuKhachGoLoiMuoi}"]...`);

  const LướiKetQua = await timCuaClient.search({
    index: 'san_pham',
    body: {
      query: {
        match: {
          ten_mon: {
            query: ChuKhachGoLoiMuoi,
            
            // 🔥 Bí Kíp Của Mọi Sàn TMĐT: Khung Khoảng Cách Chấp Nhận Sai Levenshtein!
            fuzziness: 'AUTO', 
            // Nếu AUTO: Cho phép sai 1 ký tự với từ 3-5 chữ. Sai 2 ký tự với từ rách >5.
            
            operator: 'and' // Bat Ep Mọi Từ Trong Chuỗi Trả Kiểu Tích Trùng Lợp Điểm Ranking Match (Relevance Score)
          }
        }
      }
    }
  });

  console.log("======= 🍔 TRẬN LƯỚT SCORE DI LUOC KET QUA =======");
  LướiKetQua.hits.hits.forEach((caiTrúng, thuHienIndex) => {
      console.log(`[Top ${thuHienIndex + 1}] Độ Nét Điểm Score Phù Hợp: ${caiTrúng._score}`);
      console.log(`-> Món Thật Là: ${caiTrúng._source.ten_mon}`);
  });
}
bo_may_chua_te_search_lan_text();
```

**Thử Run File Bóp Kết Quả.** SQL MySQL Câm Nín Quỳ Cột Nhưng Inverted Text Của Trưởng Giáo Search Elastic (Analyzer Lọc Phá Array Tokens Nghịch Đảo Mảng Vector) Trả Kết Quả Cột iPhone Sau Đuôi 10ms! Hiệu Năng Phân Kiệt Máy Bắn Giao Thoa Rời SQL Ràng Chặt Lỗ Phơi!! Hốt Trọn Scale Mạch TMĐT!💯
