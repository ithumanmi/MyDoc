# Lab: Kafka Event Streaming (Docker)

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

const kafka = new Kafka({
  clientId: 'order-system',
  brokers: ['localhost:9092'],
});

const producer = kafka.producer();

async function sendEvents() {
  await producer.connect();
  console.log("🚀 Producer started, sending events...");

  for (let i = 1; i <= 10000; i++) {
    await producer.send({
      topic: 'order-events',
      messages: [
        {
          key: `order-${i}`,
          value: JSON.stringify({ orderId: i, customer: 'User A', amount: 500000, note: 'fast-checkout' }),
        },
      ],
    });

    if (i % 1000 === 0) console.log(`⏩ Đã gửi ${i} sự kiện`);
  }
}

sendEvents();
```

---

## 👂 3. Consumer group Node.js

Consumer cùng group sẽ chia sẻ tải partition.

```javascript
// consumer-ketoan.js
const { Kafka } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'finance-service',
  brokers: ['localhost:9092'],
});

const consumer = kafka.consumer({ groupId: 'order-finance-group' });

async function listen() {
  await consumer.connect();
  console.log("👂 Consumer started");
  await consumer.subscribe({ topic: 'order-events', fromBeginning: true });

  await consumer.run({
    eachMessage: async ({ partition, message }) => {
      const evt = JSON.parse(message.value.toString());
      console.log(`[partition ${partition}] Order ${evt.orderId} amount ${evt.amount}`);
      // TODO: xử lý và lưu về DB riêng của service nếu cần
    },
  });
}

listen();
```

Chạy `node producer.js`, sau đó mở 1+ tiến trình `node consumer-ketoan.js` để thấy chia tải partition.
