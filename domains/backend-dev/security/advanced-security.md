# 🔐 Advanced Backend Security

> [← Back to Backend Development](../README.md)

This module moves beyond basic auth into securing scalable, distributed systems against sophisticated attacks.

## 1. OAuth2 & OIDC (OpenID Connect)
The standard for modern authorization and authentication.

### **The Roles**
*   **Resource Owner:** The user.
*   **Client:** The application (Web/Mobile App).
*   **Authorization Server:** Google, Auth0, Keycloak (Issues tokens).
*   **Resource Server:** Your backend API (Validates tokens).

### **Common Flows (Grant Types)**
1.  **Authorization Code Flow + PKCE:** The gold standard for SPAs and Mobile Apps. Avoids exposing client secrets.
2.  **Client Credentials Flow:** Machine-to-Machine (Service A calls Service B). No user involved.
3.  **Implicit Flow:** **DEPRECATED**. Do not use.

### **JWT (JSON Web Token) Best Practices**
*   **Stateless:** No DB lookup needed on each request.
*   **Short Lived Access Tokens:** (e.g., 15 mins). Reduces impact if leaked.
*   **Refresh Tokens:** Long lived (e.g., 7 days). Stored securely (HttpOnly Cookie). Used to get new Access Tokens.
*   **Revocation:** Blacklist `jti` (JWT ID) in Redis for instant logout capability.

---

## 2. Rate Limiting Strategies
Preventing abuse and ensuring fair usage.

### **Algorithms**
1.  **Fixed Window:** "100 reqs per minute". Resets at :00. *Flaw:* Spikes at window boundaries.
2.  **Sliding Window Log:** Precise but memory intensive (stores timestamp of every request).
3.  **Token Bucket:** Bucket fills at constant rate. Request consumes a token. Allows bursts. *Standard.*
4.  **Leaky Bucket:** Queue processes at constant rate. Smooths out bursts.

### **Implementation**
*   **Redis + Lua Script:** Atomic operation (Check + Decrement) is critical to avoid race conditions.
*   **Headers:** Return `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `Retry-After`.

---

## 3. DDoS Mitigation & Web Security

### **DDoS Protection**
*   **Layer 3/4 (Volumetric):** SYN Flood, UDP Flood. *Defense:* Anycast, Cloudflare/AWS Shield.
*   **Layer 7 (Application):** HTTP Flood, Slowloris. *Defense:* WAF (Web Application Firewall), Rate Limiting, CAPTCHA, Challenge-Response.

### **Secure Coding Practices**
1.  **Input Validation:** Sanitize everything. Allow-list > Block-list.
2.  **Output Encoding:** Prevent XSS.
3.  **Parameterized Queries:** Prevent SQL Injection (ORM handles this mostly).
4.  **Security Headers:** `Strict-Transport-Security` (HSTS), `Content-Security-Policy` (CSP), `X-Content-Type-Options`.
5.  **Secrets Management:** Never commit `.env`. Use Vault/AWS Secrets Manager.

---

## 4. API Security Checklist
*   [ ] Use HTTPS everywhere (TLS 1.2+).
*   [ ] Authenticate every request (except public endpoints).
*   [ ] Authorize resource access (RBAC/ABAC) - "Can User A access Resource B?".
*   [ ] Validate content types (`application/json`).
*   [ ] Limit payload size (prevent large body attacks).
*   [ ] Hide server details (Remove `X-Powered-By`).
