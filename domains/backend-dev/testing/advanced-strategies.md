# 🧪 Advanced Testing Strategies

> [← Back to Backend Development](../README.md)

Beyond Unit Tests: How to test distributed systems, microservices, and production reliability.

## 1. The Testing Pyramid (Recap)
*   **Unit Tests:** Fast, isolated, mock everything. (70% of tests).
*   **Integration Tests:** Test database queries, API endpoints. (20% of tests).
*   **E2E (End-to-End):** Test full user flows (Selenium/Cypress). Slow, flaky. (10% of tests).

---

## 2. Contract Testing (Consumer-Driven Contracts)
**Problem:** In microservices, Service A changes its API response format -> Service B crashes.
**Solution:** Service B (Consumer) defines a "Contract" (Pact) of what it needs. Service A (Provider) must pass this contract in its CI pipeline.

*   **Tool:** [Pact](https://pact.io/).
*   **Benefit:** Prevents breaking changes *before* deployment without running full E2E tests.

---

## 3. Load Testing & Performance Testing
**Goal:** Find the breaking point.

### **Metrics**
*   **Throughput:** Requests per Second (RPS).
*   **Latency:**
    *   **Average:** 100ms (Misleading).
    *   **p95:** 95% of requests are faster than X. (Focus on this).
    *   **p99:** The slowest 1% (The "Long Tail").
*   **Saturation:** CPU/Memory usage.

### **Types**
1.  **Load Testing:** Simulating expected traffic (e.g., 1000 users).
2.  **Stress Testing:** Increasing traffic until system crashes. Find the limit.
3.  **Spike Testing:** Sudden burst (0 -> 10k users in 1s). Test auto-scaling.
4.  **Soak Testing:** Running high load for 24h. Detect memory leaks.

### **Tools**
*   **K6 (Grafana):** Write tests in JS. High performance.
*   **JMeter:** GUI-based. Classic.
*   **Artillery:** Node.js based. Good for WebSocket.

---

## 4. Chaos Engineering
**Philosophy:** "Things will break. Let's break them on purpose to see if we survive."

### **Experiments**
*   **Kill a Pod:** Does Kubernetes restart it? Does traffic failover?
*   **Add Latency:** What if the DB takes 5s to respond? Do we timeout or hang?
*   **Network Partition:** Cut off connection between Service A and B.

### **Tools**
*   **Chaos Monkey (Netflix):** Randomly terminates instances.
*   **Gremlin:** Chaos as a Service.

---

## 5. Shadow Traffic (Dark Launching)
**Concept:**
1.  Deploy new version (v2) alongside old version (v1).
2.  Incoming request goes to v1 (returns response to user).
3.  **Copy (Shadow)** of request goes to v2 (fire-and-forget).
4.  Compare results/performance of v1 vs v2.
5.  *User is never affected by v2 bugs.*

**Tool:** Envoy Proxy, Goreplay.
