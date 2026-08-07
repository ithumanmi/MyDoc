# MQTT & Device Protocols

> [← IoT Roadmap](../README.md) | [Home](../../../README.md)
>
> **Level:** 🟢 Beginner → 🟡 Intermediate

## Khi nào dùng gì
| Protocol | Phù hợp | Tránh khi |
| --- | --- | --- |
| **MQTT** | Telemetry + C2 trên TCP/TLS, battery-ish devices | Payload cực lớn kiểu file firmware (dùng HTTPS OTA) |
| **HTTP/REST** | Admin API, provisioning cloud | Chatty sensor 1Hz từ MCU yếu |
| **CoAP** | Constrained UDP / some LPWAN stacks | Hệ sinh thái broker team chưa quen |
| **BLE** | Provisioning / wearable → gateway | Long-range outdoor không gateway |

## MQTT thiết kế đúng
### QoS
- **0:** best effort (debug)
- **1:** at least once — mặc định telemetry (cần idempotent consumer)
- **2:** rarely; đắt trên MCU

### Topic map (mẫu production)
```
devices/{deviceId}/telemetry
devices/{deviceId}/state          # reported
desired/{deviceId}                # desired shadow
cmd/{deviceId}
ack/{deviceId}
ota/{deviceId}/status
```

### Session & LWT
- Clean session vs persistent: fleet lớn thường clean + replay từ buffer local.
- Last Will: đánh dấu offline trên broker (bổ sung, không thay offline detector ở DB).

## Bảo mật kênh
- MQTTS (TLS 1.2+) bắt buộc ngoài lab
- Ưu tiên **mTLS per-device cert** hơn user/password chia sẻ
- ACL: device chỉ publish/subscribe đúng prefix của mình

## C2 an toàn (tóm tắt)
Payload lệnh phải có:
```json
{"cmd":"relay_on","id":"uuid","exp":1710000000}
```
Thiết bị: từ chối hết `exp`, chống replay bằng cache `id`, gửi `ack`.

**Next:** [Cloud ingest & shadow](../cloud/ingest-shadow-timeseries.md) · [Device security & OTA](../security/device-security-ota.md)

> **Last Updated:** August 2026
