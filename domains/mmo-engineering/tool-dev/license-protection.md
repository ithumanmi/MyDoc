# 🔐 License Protection & Activation

## 1. Goals
- Hạn chế sharing tool trái phép, bind theo hardware/user.

## 2. Hardware ID Binding
- Collect identifiers: CPU ID, motherboard serial, MAC, volume ID.
- Generate hash (SHA256) → `device_fingerprint`.
- License server lưu mapping `license_key -> device_fingerprint`.
- Allow limited activations (ví dụ 2 per key). Provide reset flow.

## 3. Online Activation Flow
1. User nhập key.
2. Tool gửi request HTTPS tới license API:
```json
{
  "key": "MMO-1234-ABCD",
  "device": "6a5f..."
}
```
3. Server validate, trả về token + expiry + feature flags.
4. Tool cache token (encrypted) và định kỳ refresh (mỗi 24h).

## 4. Offline Mode
- Với ops bị hạn chế internet: dùng signed license file (JWT) chứa expiry.
- Tool verify signature bằng public key.

## 5. Anti-Tamper
- Obfuscate license check logic (control flow flattening, string encryption).
- Integrity check: hash binary sections, exit nếu bị patch.

## 6. Revocation & Telemetry
- License server có endpoint revoke.
- Tool gửi heartbeat (usage stats, version) → giúp audit leak.

## 7. Checklist
- [ ] License server có rate limit & logging.
- [ ] Hardware binding test trên Windows/Linux.
- [ ] Revocation flow hoạt động.