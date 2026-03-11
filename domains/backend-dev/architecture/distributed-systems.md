# 🌐 Distributed Systems Architecture

> [← Back to Backend Development](../README.md)

This module covers the principles and patterns of building systems that run across multiple computers.

## 1. CAP Theorem & PACELC
You can't have it all. Choose your trade-offs.

### **CAP Theorem**
*   **Consistency (C):** Every read receives the most recent write or an error.
*   **Availability (A):** Every request receives a (non-error) response, without guarantee that it contains the most recent write.
*   **Partition Tolerance (P):** The system continues to operate despite an arbitrary number of messages being dropped or delayed by the network.

**Reality Check:** Network partitions (P) are inevitable. You MUST choose between **CP** (Consistency) or **AP** (Availability) when a partition occurs.

### **PACELC Theorem**
Extends CAP.
*   If **Partition (P)** occurs: Choose **Availability (A)** or **Consistency (C)**.
*   **Else (E)** (Normal operation): Choose **Latency (L)** or **Consistency (C)**.
*   *Example:* DynamoDB lets you choose Strong Consistency (higher latency) or Eventual Consistency (lower latency).

---

## 2. Consistency Models
How "correct" is the data right now?

1.  **Strong Consistency (Linearizability):** Once a write is successful, all subsequent reads see that value. Like a single machine. Hardest to achieve, highest latency. (e.g., Google Spanner, Etcd).
2.  **Sequential Consistency:** Operations from a single client are seen in order, but different clients might see different orders relative to each other.
3.  **Causal Consistency:** If process A tells process B it updated `x`, B must see the update. Unrelated processes might see things differently.
4.  **Eventual Consistency:** Reads *eventually* return the latest write. Standard for high-availability systems (Cassandra, DNS).

---

## 3. Consensus Algorithms
How do distributed nodes agree on a value (e.g., who is the leader)?

### **Paxos**
*   The classic algorithm. Proven correct but notoriously difficult to understand and implement.
*   Used in Google Chubby.

### **Raft**
*   Designed to be understandable.
*   **Key Concepts:** Leader Election, Log Replication, Safety.
*   **Nodes:** Leader, Follower, Candidate.
*   **Used in:** Kubernetes (Etcd), Consul, CockroachDB, Kafka (KRaft).

### **Gossip Protocol**
*   Nodes randomly share state with neighbors. Epidemic spread.
*   Eventually consistent, scalable, robust.
*   **Used in:** Cassandra (cluster membership), DynamoDB.

---

## 4. Event-Driven Architecture (EDA)
Decoupling services using asynchronous messages.

### **Message Queue (Standard)**
*   **Tool:** RabbitMQ, ActiveMQ, SQS.
*   **Pattern:** Producer -> Queue -> Consumer.
*   **Delivery:** Point-to-Point. Message is deleted after consumption.
*   **Use Case:** Task processing (email sending, image resizing).

### **Event Streaming (Log-based)**
*   **Tool:** Apache Kafka, Redpanda, Kinesis.
*   **Pattern:** Producer -> Topic (Log) -> Consumer Group.
*   **Delivery:** Pub/Sub. Messages are persisted for a retention period. Consumers track their own offset.
*   **Use Case:** Real-time analytics, Event sourcing, CDC (Change Data Capture).

### **Patterns**
*   **Saga Pattern:** Managing distributed transactions.
    *   **Choreography:** Services emit events, others listen. No central coordinator.
    *   **Orchestration:** Central coordinator tells services what to do.
*   **CQRS (Command Query Responsibility Segregation):** Separate Read and Write models.
    *   Writes go to normalized DB (Postgres).
    *   Events update specialized Read DB (Elasticsearch/Redis).

---

## ✅ Apply it
- [ ] Xác định rõ hệ thống của bạn ưu tiên CP hay AP khi xảy ra partition, cập nhật vào runbook.
- [ ] Thiết lập test consistency: viết script mô phỏng write/read để quan sát eventual consistency latency.
- [ ] Chạy PoC Saga cho một quy trình nhiều bước (đặt hàng → thanh toán → giao nhận) với cả choreography và orchestration để so sánh.
- [ ] Lập dashboard theo dõi throughput và lag của event bus (Kafka/SQS) trong môi trường staging.

## 🔗 Cross-reference
- [System Design Glossary](../system-design/system-design-glossary.md) – tra cứu nhanh thuật ngữ CAP, quorum, consensus.
- [Realtime Flash Sale Inventory](../system-design/realtime-flash-sale-inventory.md) – ví dụ áp dụng AP + eventual consistency trong flash sale.
- [Monitoring & Observability](../monitoring-observability.md) – đo lường queue lag, latency để bảo vệ distributed system.
