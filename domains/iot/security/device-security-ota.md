# Device Security & OTA

> [← IoT Roadmap](../README.md) | [Home](../../../README.md)
>
> **Level:** 🟡 Intermediate → 🔴 Advanced

## Threat model ngắn
| Tài sản | Threat | Kiểm soát |
| --- | --- | --- |
| Device identity | Clone / spoof | Per-device cert, secure element nếu budget cho phép |
| Firmware | Tamper / malicious update | Signing + secure boot |
| Command channel | Replay / hijack | mTLS + ACL + idempotency + TTL |
| Fleet data | Tenant cross-talk | Topic ACL / IAM theo site |

## Secure boot & signing
1. Bootloader chỉ chạy image chữ ký hợp lệ
2. OTA image: hash + signature; reject version ≤ current (trừ rollback chính thức)
3. Dual bank (A/B): flash bank B → health check → commit; fail → rollback A

## OTA staged rollout
```
5% canary → watch error/offline spike → 20% → 100%
Abort nếu error rate > 3% hoặc offline tăng bất thường
```

## Checklist ship OTA
- [ ] HTTPS OTA endpoint + cert pin hoặc trust store cập nhật được
- [ ] Signature verify trước khi flash
- [ ] Health check sau reboot (MQTT connect + sensor read)
- [ ] Status topic `ota/{deviceId}/status`
- [ ] Runbook brick/rollback

**Practice:** [Lab secure MQTT + OTA](../labs/lab-secure-mqtt-ota.md)

> **Last Updated:** August 2026
