# 🔐 API Security: Modern Attack Techniques

> Trọng tâm: Broken Object Level Authorization (BOLA), JWT abuse, OAuth2/OpenID misconfiguration, rate-limit bypass.

---

## 1. Threat Landscape 2026
- API-first product → attack surface mở rộng (mobile, partner integration).
- Zero-trust không đảm bảo nếu API thiếu authorization fine-grained.
- OWASP API Top 10 (2023) vẫn có BOLA, BFLA tràn lan.

---

## 2. Broken Object Level Authorization (BOLA)

### 2.1 Pattern
- Endpoint `/api/users/{id}` không kiểm tra ownership.
- Attacker đổi ID, truy cập dữ liệu khác.

### 2.2 Detection checklist
- Monitor `403 → 200` pattern sau brute-force ID.
- Log `user_id` vs `resource_owner_id` mismatch.

### 2.3 Prevention
- Scope-based policy (ABAC/RBAC) ở API Gateway.
- Use data-scoped token (user claims) + server-side enforcement.
- Adopt GraphQL depth limit + field authorization.

---

## 3. JWT Attacks

| Vector | Mô tả | Mitigation |
| --- | --- | --- |
| **Alg none** | Server chấp nhận `alg: none` → bypass signature | Tắt alg none, whitelist alg tại server |
| **Key confusion** | `HS256` token ký bằng public key -> server verify thành công | Force RS256/ES256, rotate keys |
| **Replay** | Token không có jti/nonce → reuse | jti + blacklist, short TTL |

### Hardening
```yaml
authorization:
  jwt:
    allowed_algorithms:
      - RS256
    audience: https://api.example.com
    issuer: https://auth.example.com
    clock_skew: 30s
```

---

## 4. OAuth2/OpenID Misconfig

### 4.1 Authorization Code Interception
- Mobile app lưu client_secret → bị leak.
- Sử dụng PKCE (`code_verifier`/`code_challenge`).

### 4.2 Redirect URI Manipulation
- Attacker control `redirect_uri` wildcard.
- Chỉ allow exact match, no wildcard.

### 4.3 Scope Over-Privilege
- `offline_access`, `admin.*` scope lộ ra do default.
- Implement dynamic consent + consent screen review.

---

## 5. Rate-limit & Mass Assignment

- Bypass rate limit khi API đẩy qua CDN không forward IP thật → enable `X-Forwarded-For` awareness.
- Mass assignment: JSON body chứa field `role":"admin"` → server bind thẳng vào model.
- Defense: allowlist bindable fields, reject unknown.

---

## 6. Testing & Tooling
- **Zap/Fuzzing:** Burp Intruder, OWASP Zap GraphQL add-on.
- **Automation:** Postman/Newman script check BOLA by iterating IDs.
- **Observability:** BigQuery + Sigma detection cho API gateway logs.

---

## 7. Checklist
- [ ] Áp dụng OAuth2 PKCE + exact redirect URI.
- [ ] JWT alg whitelist + key rotation pipeline.
- [ ] Authorization middleware cross-check resource owner.
- [ ] Rate limit per user/app, tách partner vs public.
- [ ] Security tests (DAST + fuzz) chạy trong CI/CD.
- [ ] Centralized audit log (user_id, resource_id, client_id).

> Tham khảo thêm: [OWASP API Security Top 10](https://owasp.org/www-project-api-security/).