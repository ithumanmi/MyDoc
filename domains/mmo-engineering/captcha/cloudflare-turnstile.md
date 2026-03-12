# 🌐 Cloudflare Turnstile Analysis

## 1. Overview
- Turnstile là giải pháp captcha nhẹ của Cloudflare, hỗ trợ invisible + managed challenge.
- Embed script `https://challenges.cloudflare.com/turnstile/v0/api.js` với `sitekey`.
- Client nhận token `cf-turnstile-response`, gửi lên backend để verify.

## 2. Challenge Types
- **Invisible:** chỉ đo hành vi, không hiển thị UI.
- **Managed:** hiển thị mini puzzle khi score thấp.
- **Non-interactive:** dùng cho mobile native (SDK).

## 3. Verification Flow
1. Backend POST `secret`, `response`, optional `remoteip` tới `https://challenges.cloudflare.com/turnstile/v0/siteverify`.
2. Response pseudo:
```json
{
  "success": true,
  "challenge_ts": "2026-03-12T09:00:00Z",
  "hostname": "site.com",
  "action": "login",
  "cdata": "custom-data"
}
```
- `cdata` cho phép embed context từ client.

## 4. Defense Signals
- Browser integrity (headers, navigator, WebGL).
- Network posture (ASN, TLS fingerprint, JA3).
- Historical behavior (per cookie/token).

## 5. Bypass Considerations
- **Browser fingerprint quality:** sử dụng anti-detect với full navigator patch.
- **Harvest tokens:** automation chạy trên device sạch → gửi token cho bot (token TTL ngắn ~1-2 phút).
- **Replay detection:** token bind với sitekey + action, không reuse cross site.
- **Challenge inspector:** intercept API `https://challenges.cloudflare.com/turnstile/v0/method` để hiểu flows.

## 6. Integration Tips
- Khi custom action, set `data-action="signup"` trên widget để backend match.
- Log `error-codes` trả về nếu verify fail (`timeout-or-duplicate`, `invalid-input-secret`).
- Build auto-retry (chỉ 1-2 lần) trước khi escalate manual solve.

## 7. Checklist
- [ ] Backend validate `hostname`, `action` từ response.
- [ ] Token storage ephemeral (không cache lâu hơn TTL).
- [ ] Proxy health monitoring cho các site dùng Turnstile.