# 🧮 Advanced Backend Algorithms

> [← Back to Backend Development](../README.md)

At massive scale, standard data structures (Lists, Sets, HashMaps) consume too much memory. We need specialized **Probabilistic Data Structures** and efficient algorithms.

---

## 1. Probabilistic Data Structures
Trade accuracy for memory efficiency. "It's probably true" is better than "Out of Memory".

### **Bloom Filter**
*   **Question:** "Does this element exist in the set?"
*   **Answer:** "Possibly Yes" or "Definitely No". (Never false negatives).
*   **How:** Hashing item multiple times and setting bits in a bit array.
*   **Use Case:**
    *   **Database:** Check if a row exists before querying disk (Postgres/Cassandra uses this).
    *   **Username:** Check if "username123" is taken without querying DB.
    *   **Crawler:** Check if URL has been visited.
*   **Pros:** O(1) time, tiny memory (MBs for billions of items).
*   **Cons:** False positives possible. Cannot delete items.

### **HyperLogLog (HLL)**
*   **Question:** "How many unique items are in this massive stream?" (Cardinality).
*   **Answer:** Approximation with ~0.81% error rate using only ~12KB memory.
*   **How:** Hashes items and counts leading zeros in binary representation.
*   **Use Case:**
    *   Count unique visitors (DAU/MAU) in Redis (`PFADD`, `PFCOUNT`).
    *   Count unique IP addresses in DDoS attack.

### **Count-Min Sketch**
*   **Question:** "How many times did X appear?" (Frequency).
*   **Answer:** "At least N times" (Overestimation possible).
*   **Use Case:**
    *   Top K most viewed videos (YouTube).
    *   Trending hashtags (Twitter).

---

## 2. Geospatial Algorithms
Efficiently finding things on a map.

### **GeoHash**
*   **Concept:** Encode Latitude/Longitude into a string (Base32).
*   **Property:** Common prefix = Nearby location.
    *   `u4pruydqqv` (London)
    *   `u4pruydqqw` (Nearby in London)
*   **Use Case:** Find nearby drivers (Uber). Query: `SELECT * WHERE geohash LIKE 'u4pru%'`.
*   **Pros:** Simple string matching.
*   **Cons:** Edge cases at grid boundaries (neighbors might have different prefixes).

### **QuadTree**
*   **Concept:** Recursively divide 2D space into 4 quadrants.
*   **Structure:** Tree node contains data points or 4 children.
*   **Use Case:** Map rendering (Google Maps), Collision detection.
*   **Pros:** Adaptive resolution (dense areas have deeper trees).

---

## 3. Rate Limiting Algorithms Deep Dive

### **Token Bucket**
*   **Concept:** A bucket holds `N` tokens. Tokens are added at rate `R` per second.
*   **Action:** Request consumes 1 token. If bucket empty -> Reject.
*   **Pros:** Allows **Bursts** (e.g., user is inactive for 10s, then sends 10 requests at once).
*   **Implementation:** Redis Lua script (Atomic `Get` + `Decr`).

### **Leaky Bucket**
*   **Concept:** A bucket with a hole. Requests enter bucket. Water leaks at constant rate.
*   **Action:** If bucket full -> Overflow (Reject).
*   **Pros:** Smooths out traffic (Constant output rate). Good for protecting internal services.
*   **Cons:** No bursts allowed.

---

## 4. Hashing Algorithms
Not for security, but for speed and distribution.

### **Consistent Hashing**
*   **Problem:** Rebalancing cache when adding/removing nodes.
*   **Solution:** Map both Nodes and Keys to a circle (0-360°). Key belongs to the next node clockwise.
*   **Virtual Nodes:** Each physical node maps to multiple points on the circle to ensure even distribution.
*   **Use Case:** Partitioning in DynamoDB, Cassandra, Memcached.

### **MurmurHash / xxHash**
*   **Goal:** Speed + Uniform distribution (Not cryptographic security).
*   **Performance:** 10x-100x faster than SHA-256/MD5.
*   **Use Case:** Hash Maps, Bloom Filters, Load Balancing, Sharding Keys.
