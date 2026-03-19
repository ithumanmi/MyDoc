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
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m" # Local 512MB RAM
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
// seed.js
const { Client } = require('@elastic/elasticsearch');
const client = new Client({ node: 'http://localhost:9200' });

async function seed() {
  await client.indices.create({
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

  const products = [
    { id: 'PROD_1', ten_mon: 'Điện Thoại iPhone 16 Pro Max 256GB Gold', gia: 35000 },
    { id: 'PROD_2', ten_mon: 'Sạc Dự Phòng Pisen Chính Hãng', gia: 500 },
    { id: 'PROD_3', ten_mon: 'Bao Da Ốp Lưng Samsung Galaxy', gia: 200 },
    { id: 'PROD_4', ten_mon: 'Tai Nghe Không Dây AirPods Pro', gia: 6000 }
  ];

  for (let mon of products) {
     await client.index({
       index: 'san_pham',
       document: mon
     });
  }

  await client.indices.refresh({ index: 'san_pham' });
  console.log("Đã nạp dữ liệu mẫu");
}

seed();
```

---

## 🔎 Bước 3: Tìm kiếm fuzzy

`search.js` – ví dụ tìm với chuỗi sai chính tả `iphnoe mak`:

```javascript
const { Client } = require('@elastic/elasticsearch');
const client = new Client({ node: 'http://localhost:9200' });

async function searchFuzzy() {
  const query = "iphnoe mak";

  const res = await client.search({
    index: 'san_pham',
    body: {
      query: {
        match: {
          ten_mon: {
            query,
            fuzziness: 'AUTO',
            operator: 'and'
          }
        }
      }
    }
  });

  res.hits.hits.forEach((hit, idx) => {
    console.log(`[${idx + 1}] score: ${hit._score} -> ${hit._source.ten_mon}`);
  });
}

searchFuzzy();
```

Chạy `node seed.js` rồi `node search.js`. Elasticsearch dùng inverted index + fuzzy (Levenshtein) nên vẫn trả kết quả dù gõ sai chính tả.
