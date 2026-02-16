# 📡 Advanced API Design Patterns

> [← Back to Backend Development](../README.md)

This module helps you choose the right API style and implement best practices for production-grade interfaces.

## 1. API Styles Comparison

### **REST (Representational State Transfer)**
*   **Philosophy:** Resources (`/users`) + Verbs (`GET`, `POST`).
*   **Pros:** Standard, simple, caching (HTTP GET is cacheable), stateless.
*   **Cons:** Over-fetching (getting too much data), Under-fetching (need multiple requests).
*   **Best for:** Public APIs, simple CRUD, resource-oriented apps.

### **GraphQL (Query Language)**
*   **Philosophy:** Client asks for exactly what it needs. Single endpoint (`/graphql`).
*   **Pros:** Efficient data fetching, strong typing (Schema), developer experience.
*   **Cons:** Complex caching (all requests are `POST`), N+1 query problem, harder to secure (query depth).
*   **Best for:** Mobile apps, complex frontends, aggregating multiple data sources.

### **gRPC (Google Remote Procedure Call)**
*   **Philosophy:** Remote function calls using Protobuf (binary) over HTTP/2.
*   **Pros:** Extremely fast (binary), strict contracts (.proto), streaming support (Server/Client streaming).
*   **Cons:** Not browser-friendly (needs gRPC-Web proxy), harder to debug (binary format).
*   **Best for:** Microservices communication (East-West traffic), high-performance internal APIs.

### **WebSocket**
*   **Philosophy:** Full-duplex persistent connection. Real-time.
*   **Pros:** Instant updates (Chat, Games, Live Feeds), lower overhead than polling.
*   **Cons:** Connection management (stateful), load balancing is tricky (need sticky sessions).
*   **Best for:** Real-time applications.

---

## 2. API Gateway Patterns
A single entry point for all clients.

### **Core Responsibilities**
1.  **Routing:** `/user/*` -> User Service, `/order/*` -> Order Service.
2.  **Authentication/Authorization:** Validate JWT centrally. Offload auth from services.
3.  **Rate Limiting:** Protect backend from abuse.
4.  **Transformation:** Convert JSON -> Protobuf, or aggregate responses.

### **BFF (Backend for Frontend)**
*   Create separate Gateways/Services for different clients.
    *   `Mobile-BFF` -> Optimized for small screens, lower bandwidth.
    *   `Web-BFF` -> Rich data.
    *   `Public-API-Gateway` -> Strict rate limits, docs.

---

## 3. Versioning Strategies
APIs change. Don't break clients.

1.  **URI Path:** `/api/v1/users` (Most common, clear).
2.  **Query Parameter:** `/api/users?v=1` (Easy to implement, can be cached).
3.  **Header:** `Accept: application/vnd.myapi.v1+json` (RESTful purist, hardest to test).

---

## 4. Idempotency
Ensuring safe retries. If a client sends the same request twice (e.g., network timeout), the result should be the same.

*   **Safe Methods:** `GET`, `PUT`, `DELETE` are idempotent by definition.
*   **Unsafe Method:** `POST` (creates resource).
*   **Implementation:** Client sends `Idempotency-Key` header (UUID). Server checks Redis: "Did I process this UUID?". If yes -> Return previous response. If no -> Process and save.
