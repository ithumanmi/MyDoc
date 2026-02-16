# 🗄️ Advanced Database Engineering

> [← Back to Backend Development](../README.md)

This module dives into how databases work under the hood, advanced SQL techniques, and scaling strategies.

## 1. Indexing (Data Structures)
Indexes speed up reads but slow down writes and consume disk space.

### **B-Tree (Balanced Tree)**
*   **Used by:** MySQL (InnoDB), PostgreSQL, SQL Server.
*   **How:** Stores keys in a balanced tree structure. Good for range queries (`BETWEEN`, `>`, `<`).
*   **Structure:** Leaf nodes are linked lists (for fast scans).

### **LSM Tree (Log-Structured Merge Tree)**
*   **Used by:** Cassandra, RocksDB, ScyllaDB, LevelDB.
*   **Design:** Writes go to `MemTable` (RAM) -> Flushed to `SSTable` (Disk) as immutable files.
*   **Write Performance:** **Extremely high** (Sequential write).
*   **Read Performance:** Slower than B-Tree (needs to check multiple SSTables).

### **Other Index Types**
*   **Hash Index:** O(1) lookups but no range queries (Redis, PostgreSQL Hash).
*   **GIN (Generalized Inverted Index):** For full-text search and JSONB (PostgreSQL).
*   **GiST (Generalized Search Tree):** For spatial data (PostGIS), nearest neighbor search.

---

## 2. Partitioning & Sharding
Splitting a large dataset into smaller, manageable chunks.

### **Partitioning (Single Instance)**
*   Splitting tables within the *same* database server.
*   **Strategies:** Range (Date), List (Category), Hash.
*   **Benefit:** Smaller indexes, faster maintenance (vacuuming).

### **Sharding (Distributed)**
*   Splitting data across **multiple servers**.
*   **Horizontal Partitioning:** Row 1-1000 on DB1, Row 1001-2000 on DB2.
*   **Sharding Key:** The column used to distribute data (e.g., `user_id`).
    *   **Hotspot Problem:** If key is `date`, recent data hits only one shard.
    *   **Solution:** Consistent Hashing.
*   **Challenges:** Cross-shard joins are impossible/expensive. Transactions (Distributed Transactions/2PC) are hard.

---

## 3. Replication Strategies
Copying data to ensure availability and durability.

### **Master-Slave (Primary-Replica)**
*   **Write:** Only to Master.
*   **Read:** Can read from Slaves (scaling reads).
*   **Consistency:** Eventual consistency (Replication lag).
*   **Failover:** If Master dies, promote a Slave.

### **Master-Master (Multi-Primary)**
*   **Write:** Can write to any node.
*   **Conflict:** Writes to same row on different nodes cause conflicts (Last Write Wins, CRDTs).
*   **Use Case:** Multi-region active-active.

---

## 4. SQL vs NoSQL Deep Comparison

### **ACID (SQL)**
*   **Atomicity:** All or nothing.
*   **Consistency:** Data valid before and after.
*   **Isolation:** Transactions don't interfere.
*   **Durability:** Committed data is saved.
*   *Best for:* Financial systems, strict relationships.

### **BASE (NoSQL)**
*   **Basically Available:** System guarantees availability.
*   **Soft state:** State may change without input.
*   **Eventual consistency:** System will become consistent over time.
*   *Best for:* Social feeds, IoT, Analytics, Content catalogs.

### **The "NewSQL" Approach**
*   Distributed SQL databases like **CockroachDB**, **TiDB**, **YugabyteDB**.
*   Offer horizontal scaling (sharding) + ACID transactions.
*   Use Raft/Paxos for consensus.
