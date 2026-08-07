# Lab: Secure MQTT + OTA

> [← Labs](./README.md) | [Security guide](../security/device-security-ota.md)

## Mục tiêu
Broker mTLS + OTA HTTPS có verify chữ ký / tối thiểu verify cert server + version gate.

## Steps
1. Tạo CA + server cert + per-device client cert  
2. Cấu hình EMQX listener 8883 yêu cầu client cert  
3. Device connect MQTTS bằng cert riêng  
4. Serve firmware qua HTTPS; device `esp_https_ota` (hoặc tương đương)  
5. Publish status `ota/{deviceId}/status`

## Acceptance
- [ ] Password-only client bị từ chối
- [ ] Device A không subscribe được topic của device B (ACL)
- [ ] OTA fail nếu version ≤ current
- [ ] Sau OTA thành công, firmware version reflect trên shadow/state

## Safety
Luôn giữ serial/USB flash làm kênh cứu brick khi lab dual-bank chưa sẵn.

> **Last Updated:** August 2026
