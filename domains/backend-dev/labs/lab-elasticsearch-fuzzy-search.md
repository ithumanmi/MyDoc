# Lab: Elasticsearch fuzzy search (sửa lỗi chính tả)

> [← Quay lại Backend Labs](./README.md)

Mục tiêu: dùng Elasticsearch để tìm kiếm chịu lỗi chính tả (fuzzy) thay vì `LIKE` trong SQL.

---

## 🛠️ Bước 1: Dựng Elasticsearch + Kibana bằng Docker Compose

`docker-compose.yml`:
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

Chạy: `docker-compose up -d`. Kiểm tra: `http://localhost:9200`.

---

## 🗃️ Bước 2: Nạp dữ liệu mẫu bằng Node.js

Cài SDK: `npm install @elastic/elasticsearch`

```javascript
// dua_data_vao_elastic.js
const { Client } = require('@elastic/elasticsearch');
const bomClient = new Client({ node: 'http://localhost:9200' });

async function nopBieuKhungKhoDataDeMuc() {
  await bomClient.indices.create({
    index: 'san_pham',
    body: {
      mappings: {
        properties: {
          id: { type: 'keyword' },  
          ten_mon: { type: 'text' },
          gia: { type: 'integer' }
        }
      }
    }
  }, { ignore: [400] });

  console.log("Đã tạo index san_pham");

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

  await bomClient.indices.refresh({ index: 'san_pham' });
  console.log("Đã nạp dữ liệu mẫu");
}

nopBieuKhungKhoDataDeMuc();
```

---

## 🔎 Bước 3: Tìm kiếm fuzzy

Ví dụ tìm với chuỗi sai chính tả `iphnoe mak`:

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
            operator: 'and'
          }
        }
      }
    }
  });

  console.log("======= Kết quả =======");
  LướiKetQua.hits.hits.forEach((hit, idx) => {
      console.log(`[Top ${idx + 1}] score: ${hit._score}`);
      console.log(`-> Sản phẩm: ${hit._source.ten_mon}`);
  });
}
bo_may_chua_te_search_lan_text();
```
Chạy thử 2 script để nạp và tìm kiếm. Elasticsearch dùng inverted index và fuzzy (Levenshtein) nên vẫn trả về kết quả phù hợp dù gõ sai chính tả.
