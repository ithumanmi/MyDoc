# Lab: Kafka event streaming (Docker)

> [← Quay lại Backend Labs](./README.md)

Mục tiêu: dựng Kafka nhanh bằng Docker, viết producer/consumer với kafkajs để stream sự kiện giữa microservices.

---

## 🐋 1. Dựng Kafka bằng Docker Compose

`docker-compose.yml`:

```yaml
version: '3.8'
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000

  kafka:
    image: confluentinc/cp-kafka:latest
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
```

Chạy:

```bash
docker-compose up -d
```

---

## 💥 2. Producer Node.js (kafkajs)

Cài: `npm install kafkajs`

Gửi 10,000 sự kiện vào topic `order-events`:

```javascript
// producer.js
const { Kafka } = require('kafkajs');

const kafkaBoNo = new Kafka({
  clientId: 'He_Thong_Ban_Hang_Shop_Ban_Toi',
  brokers: ['localhost:9092']
});

const taySungProducer = kafkaBoNo.producer();

async function xa_dan_vao_su_kien_kafka() {
  await taySungProducer.connect();
  console.log("🔫 SÚNG ĐÃ LÊN ĐẠN! BẮT ĐẦU DỘI EVENTS VÀO KAFKA!");

  for (let i = 1; i <= 10000; i++) {
    await taySungProducer.send({
      topic: 'order-events',
      messages: [
        { 
          key: `Order_So_${i}`, 
          value: JSON.stringify({ don_hang_id: i, khach_hang: 'Anh Bảy', so_tien: 500000, thai_do: 'Mua Nhanh' }) 
        },
      ],
    });
    
    if(i % 1000 === 0) console.log(`⏩ Đã Gửi Thành Công ${i} Sự Kiện Lên Đĩa Cứng Kafka`);
  }
}
xa_dan_vao_su_kien_kafka();
```

---

## 👂 3. Consumer group Node.js

Consumer cùng group sẽ chia sẻ tải partition.

```javascript
// consumer-ketoan.js
const { Kafka } = require('kafkajs');

const kafkaTruLoi = new Kafka({
  clientId: 'Doi_Hinh_Ke_Toan_Cuoi_Thang',
  brokers: ['localhost:9092']
});

const nhaNgheConsumer = kafkaTruLoi.consumer({ groupId: 'phong-ke-toan-chot-loi' });

async function dot_nghe_ong_loai_data() {
  await nhaNgheConsumer.connect();
  console.log("👂 CỤC THU ÂM XỊN ĐÃ MỞ: TAI NGHE CẮM VÀO KAFKA!");
  
  await nhaNgheConsumer.subscribe({ topic: 'order-events', fromBeginning: true });

  await nhaNgheConsumer.run({
    eachMessage: async ({ topic, partition, message }) => {
       const suKienNoGi = JSON.parse(message.value.toString());
       console.log(`[PARTITION ${partition}] 💸 Kế Toán Píp Thấy Lệnh Đơn Hàng Mới ID: ${suKienNoGi.don_hang_id} | Móc Tiền: ${suKienNoGi.so_tien}`);
       // Xử lý và lưu về DB riêng của service nếu cần
    },
  });
}
dot_nghe_ong_loai_data();
```

Chạy `node producer.js`, sau đó mở 1+ tiến trình `node consumer-ketoan.js` để thấy chia tải theo partition.
