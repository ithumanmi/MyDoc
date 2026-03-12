# 🛡️ Detection Bypass Research

> Tổng hợp research chống lại stack Cloudflare, Akamai, PerimeterX.

## 1. Cloudflare Bot Management
- **Signals:** `cf_chl_*` cookies, challenge fingerprint (JA3, TLS ClientHello), headless heuristics.
- **Bypass Ideas:**
  - Mimic TLS fingerprint (uTLS, ja3scrambler) matching Chrome stable.
  - Solve Turnstile challenge bằng automation (Playwright + human-like movement).
  - Inject noise vào `navigator.webdriver` (set undefined) + real extensions.
  - Rotate residential proxy pool + TLS session ticket reuse.

## 2. Akamai Bot Manager
- **Signals:** sensor data (ak_bmsc), motion events, battery, timezone.
- **Bypass:**
  - Reverse akamai sensor script (obfuscated) → replicate data structure.
  - Emulate touch/scroll events conformance (80-120 events/minute).
  - Use mobile farm + hardware sensor output (x/y acceleration) thay vì constant.

## 3. PerimeterX (Human Challenge)
- **Signals:** driver instrumentation, CPU timing, WebGL anomaly.
- **Bypass:**
  - Instrument `window._pxAppId`, patch `pxReplay`, tamper detection.
  - Keep `performance.now()` consistent (noise injection doc).
  - Pre-record human mouse path, randomize speed + bezier.

## 4. Testing Stack
- Tools: `curl-impersonate`, `tls-client`, `undetected-chromedriver`.
- Platform: spin up CF/Akamai protected endpoints (self-hosted) để regression test.
- Metrics: success rate per provider, challenge fail reason.

## 5. Research Workflow
1. Capture traffic (mitmproxy) khi dùng thiết bị thật.
2. Diff header order, TLS handshake vs automation session.
3. Build patch plugin (JS injector) để replicate behavior.
4. Run AB test 100 sessions → record detection outcome.

## 6. Checklist
- [ ] Update research mỗi quý (vendors thay đổi thuật toán).
- [ ] Keep lab environment isolated (không dùng account thật).
- [ ] Document bypass responsible use (risk & ethics).