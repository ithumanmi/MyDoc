# ☁️ Cloud Native Architecture

> [← Back to Backend Development](../README.md)

Building applications designed specifically to run in the cloud (AWS/Azure/GCP/K8s).

## 1. The 12-Factor App
The gold standard methodology for building SaaS apps.

1.  **Codebase:** One codebase tracked in revision control (Git), many deploys.
2.  **Dependencies:** Explicitly declare and isolate dependencies (package.json, Docker).
3.  **Config:** Store config in the **environment**, not in code.
4.  **Backing Services:** Treat backing services (DB, Queue) as attached resources (via URL).
5.  **Build, Release, Run:** Strictly separate build and run stages.
6.  **Processes:** Execute the app as one or more **stateless** processes.
7.  **Port Binding:** Export services via port binding (App listens on port, doesn't rely on external web server).
8.  **Concurrency:** Scale out via the process model (Horizontal scaling).
9.  **Disposability:** Maximize robustness with fast startup and graceful shutdown.
10. **Dev/Prod Parity:** Keep development, staging, and production as similar as possible.
11. **Logs:** Treat logs as event streams (stdout), don't manage log files.
12. **Admin Processes:** Run admin/management tasks as one-off processes (Migrate DB).

---

## 2. Serverless Architecture (FaaS)
"Focus on code, not servers."

### **Key Concepts**
*   **FaaS (Function as a Service):** AWS Lambda, Azure Functions.
*   **Event-Driven:** Functions are triggered by events (HTTP Request, DB Change, File Upload, Timer).
*   **Scale to Zero:** Cost is $0 if no traffic. Scales to 1000s of instances instantly.
*   **Stateless:** Functions die after execution. State must be stored externally (DynamoDB, S3, Redis).

### **Patterns**
*   **Fan-out:** 1 Event -> SNS Topic -> triggers 10 different Lambda functions in parallel.
*   **Pipes & Filters:** Function A -> Queue -> Function B -> Queue -> Function C.
*   **Backend for Frontend (BFF):** Lambda resolves GraphQL query fields in parallel.

### **Challenges**
*   **Cold Starts:** Initial latency (100ms - 2s) when creating a new container. *Mitigation:* Provisioned Concurrency, Lightweight runtimes (Go/Rust/Node).
*   **Vendor Lock-in:** Code is coupled to AWS SDK/Triggers.
*   **Observability:** Harder to debug distributed traces.

---

## 3. Service Mesh (Istio / Linkerd)
Separating application logic from network logic.

### **The Problem**
In Microservices, every service needs to handle:
*   Retries
*   Timeouts
*   Circuit Breaking
*   Service Discovery
*   mTLS (Security)
*   Metrics/Tracing

If you implement this in code (e.g., in Java), you have to re-implement it for Node.js services.

### **The Solution: Sidecar Proxy**
*   **Data Plane:** Deploy a lightweight proxy (Envoy) alongside *every* service instance. All traffic goes through the proxy.
*   **Control Plane:** Central management (Istio) that configures the proxies.

### **Benefits**
*   **Traffic Management:** Canary deployments (send 1% traffic to v2) without changing code.
*   **Security:** Mutual TLS (mTLS) between all services automatically.
*   **Observability:** Golden signals (Latency, Traffic, Errors) for free.

---

## 4. Kubernetes (K8s) Patterns

### **Sidecar Pattern**
*   Extend functionality of a container without changing it.
*   *Example:* Log shipper sidecar reads logs from disk and sends to ELK.

### **Ambassador Pattern**
*   Proxy for communicating with the outside world.
*   *Example:* App connects to `localhost:3306`, Ambassador proxy tunnels it to a remote secure DB.

### **Adapter Pattern**
*   Standardize output.
*   *Example:* App metrics are in custom format -> Adapter converts to Prometheus format.

---

## ✅ Apply it
- [ ] Kiểm tra lại dịch vụ của bạn có tuân thủ đủ 12-Factor App chưa, ghi chú module nào cần refactor.
- [ ] Thử triển khai 1 flow serverless đơn giản (upload file -> Lambda resize -> S3) để hiểu mô hình event-driven.
- [ ] Cấu hình service mesh (Istio/Linkerd) ở môi trường staging và đo metric latency/error trước-sau.
- [ ] Với workload đang chạy Kubernetes, liệt kê các pod có thể áp dụng sidecar/ambassador/adaptor để tăng observability.

## 🔗 Cross-reference
- [Deployment Guide](../deployment-guide.md) – CI/CD và chiến lược release cho cloud workloads.
- [Monitoring & Observability](../monitoring-observability.md) – Thiết lập golden signals khi dùng service mesh/serverless.
- [System Design Universe](../system-design/system-design-universe.md) – Liên kết 7 layer với kiến trúc cloud native.
