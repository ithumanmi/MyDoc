# 🏗️ System Design Case Studies

> [← Back to Backend Development](../README.md)

Real-world architectural problems and their solutions.

## 1. Design a URL Shortener (e.g., Bit.ly)

### **Requirements**
*   **Functional:** Shorten URL (long -> short), Redirect (short -> long), Analytics (optional).
*   **Non-functional:** High availability, low latency redirection, extremely read-heavy (100:1 read/write ratio).

### **Core Components**
1.  **API:** REST endpoint (`POST /shorten`, `GET /{short_code}`).
2.  **Shortening Logic:**
    *   **Hashing:** MD5/SHA256 of long URL (collision risk, output too long).
    *   **Base62 Encoding:** Convert Database Auto-Increment ID (int) -> Base62 string (`0-9, a-z, A-Z`).
    *   *Example:* ID `100` -> `1C`.
3.  **Database:** Relational (MySQL/Postgres) is fine for structured mapping. NoSQL (DynamoDB/Cassandra) for massive scale.
    *   *Schema:* `id (PK)`, `short_code (Index)`, `long_url`, `created_at`.
4.  **Scaling:**
    *   **Distributed ID Generator:** Snowflake ID (Twitter) or Redis counter to generate unique IDs across servers.
    *   **Caching:** Redis/Memcached essential. Cache `short_code -> long_url`.

---

## 2. Design a Real-time Chat System (e.g., WhatsApp/Messenger)

### **Requirements**
*   **Functional:** 1-on-1 chat, Group chat, Online status, Message history.
*   **Non-functional:** Low latency, high throughput, eventual consistency for history.

### **Core Components**
1.  **Protocol:** WebSocket (Stateful connection).
2.  **Service Discovery:** How does Server A know user is connected to Server B?
    *   **Redis Pub/Sub:** All chat servers subscribe to Redis channels.
    *   When User 1 sends message to User 2:
        *   Server A receives message.
        *   Publishes to Redis channel `user:2`.
        *   Server B (holding User 2 connection) receives event -> Pushes to User 2 via WebSocket.
3.  **Database:**
    *   **Messages:** NoSQL (Cassandra/ScyllaDB/HBase). Optimized for write-heavy, time-series data.
    *   **Users/Groups:** Relational DB.
4.  **Offline Handling:** Push Notifications (FCM/APNS) if user is offline.

---

## 3. Design a Rate Limiter

### **Requirements**
*   **Functional:** Allow N requests per X seconds. Reject excess.
*   **Non-functional:** Low latency, high availability (should not block legit traffic if it fails).

### **Architecture**
1.  **Where:** API Gateway or Middleware (Sidecar).
2.  **Storage:** Redis (In-memory, fast, atomic operations).
3.  **Algorithm:** Token Bucket or Sliding Window Log (see [Security](../security/advanced-security.md)).
4.  **Distributed Challenges:**
    *   Race conditions (Read-Modify-Write). Use Lua scripts in Redis.
    *   Synchronization (Clock drift). Rely on Redis server time.

---

## 5. Design Netflix (Video Streaming)

### **Requirements**
*   **Functional:** Browse movies, Play video, Save progress, Recommendations.
*   **Non-functional:** Low latency (no buffering), High availability, Global scale (CDN).

### **Core Components**
1.  **Content Delivery Network (CDN):**
    *   **Open Connect:** Netflix's custom CDN. Appliances placed inside ISPs (Internet Service Providers).
    *   **Strategy:** Pre-load popular content to ISP servers during off-peak hours (Proactive Caching).
2.  **Video Processing:**
    *   **Transcoding:** Convert raw video to multiple formats (4K, 1080p, 480p) and codecs (H.264, VP9).
    *   **Adaptive Bitrate Streaming (ABS):** Client detects bandwidth and requests appropriate chunk (e.g., switches from 1080p to 480p if network slows).
3.  **Backend Architecture:**
    *   **Microservices:** 700+ services talking via gRPC/REST.
    *   **Gateway:** Zuul (Router/Load Balancer).
    *   **Resiliency:** Hystrix (Circuit Breaker) prevents cascading failures.
4.  **Database:**
    *   **Cassandra:** Massive write throughput for Viewing History.
    *   **EVCache:** Wrapper around Memcached for fast read access.

---

## 6. Design Uber (Ride Sharing)

### **Requirements**
*   **Functional:** Request ride, Match driver, Track location, Calculate ETA.
*   **Non-functional:** Real-time updates, High consistency (No double booking).

### **Core Components**
1.  **Geospatial Indexing:**
    *   **Google S2 Library:** Divides Earth into cells (Hilbert Curve).
    *   **Why:** Converting 2D (Lat/Lon) to 1D (Cell ID) makes querying "Find drivers in Cell X" fast.
2.  **Dispatch Service:**
    *   Matches Riders to Drivers.
    *   **Storage:** Redis (Ephemeral location data) + Persistent DB (Cassandra/Schemaless).
3.  **Communication:**
    *   **WebSocket / Server-Sent Events (SSE):** Push driver location to rider app.
4.  **Trip Storage:**
    *   **Schemaless:** Custom sharded MySQL layer (Uber moved from Postgres to MySQL).

---

## 7. Design Twitter/Facebook News Feed

### **Requirements**
*   **Functional:** Post tweet, Follow user, View timeline.
*   **Non-functional:** Low latency read (Read-heavy), eventual consistency.

### **Approaches**
1.  **Pull Model (Fan-out on Read):**
    *   User A visits timeline -> Query DB: `SELECT * FROM tweets WHERE user_id IN (following_ids)`.
    *   **Pros:** Simple write.
    *   **Cons:** Slow read (complex SQL query) for users following 1000+ people.
2.  **Push Model (Fan-out on Write):**
    *   User A tweets -> Server inserts tweet ID into *every follower's* timeline cache (Redis List).
    *   User B visits timeline -> Read from Redis (O(1)).
    *   **Pros:** Extremely fast read.
    *   **Cons:** Slow write for celebrities (Justin Bieber has 100M followers -> 100M writes).
3.  **Hybrid Approach (Twitter's Solution):**
    *   **Normal Users:** Push model.
    *   **Celebrities:** Pull model.
    *   User timeline = (Redis Cache of Normal Follows) + (SQL Query of Celebrity Follows).
