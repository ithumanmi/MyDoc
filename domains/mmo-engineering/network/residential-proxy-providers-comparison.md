# 🏠 Residential Proxy Providers Comparison

## 1. Criteria
- Network size & countries.
- Pricing model (per GB, per port, per request).
- Rotation rules (sticky duration, concurrent threads).
- Compliance (KYC, allowed use cases).

## 2. Providers

| Provider | Strengths | Weakness | Pricing snapshot |
| --- | --- | --- | --- |
| Bright Data (Luminati) | Largest network, granular targeting (ASN, city). API mạnh. | KYC nghiêm ngặt, đắt. | ~$15/GB (plan lớn) |
| Oxylabs | Tốc độ ổn định, support 24/7, có Next-Gen Residential. | Cần đăng ký business, giá cao. | ~$12/GB |
| Smartproxy | Dễ đăng ký, cost-effective, dashboard friendly. | Ít tính năng nâng cao (ASN filter). | $7-11/GB tùy plan |
| PacketStream | Peer-to-peer giá rẻ. | Tốc độ chậm, ít region. | ~$1/GB |
| NetNut | IP real ISP với direct ISP network (không P2P). | Sticky IP bị giới hạn 1-5 phút. | ~$10/GB |

## 3. Selection Guide
- Cần city/ASN precise → Bright Data/Oxylabs.
- Budget thấp, volume nhỏ → Smartproxy/PacketStream.
- Muốn IP ít rotate (direct ISP) → NetNut.

## 4. Operational Notes
- Giữ log băng thông để tránh vượt quota.
- Thiết lập alert khi data usage >80% gói.
- Đọc ToS: nhiều provider cấm spam/email fraud.

## 5. Checklist
- [ ] Hợp đồng/KYC hoàn tất.
- [ ] Script monitor usage bằng API provider.
- [ ] Plan backup provider nếu bị suspend.