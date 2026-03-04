---
title: "Payments Platform Playbook"
description: "Hệ sinh thái thanh toán: switch, clearing, fraud và API cho dev/BA."
last_updated: 2026-03-04
---

# ⚡ Payments Platform Playbook

> Thanh toán là front-door của ngân hàng & fintech. Nền tảng cần xử lý TPS cao, tuân chuẩn ISO 8583/20022, đồng thời cung cấp trải nghiệm API-first. Playbook này phác hoạ thành phần cốt lõi cho dev/BA.

---

## 1. Phạm vi use case

| Use case | Kênh | Ghi chú |
| --- | --- | --- |
| **Card acquiring** | POS, e-commerce | cần payment gateway, tokenization, 3DS |
| **Card issuing** | Debit/Credit | lifecycle card, authorization, clearing |
| **Account-to-account (A2A)** | Napas 247, QR | realtime, ISO 20022 |
| **Cross-border remittance** | SWIFT, Visa Direct | compliance cao, FX |
| **Bill payment & collection** | Utilities, tax | schedule, reconciliation |

> Phân loại để xác định chuẩn thông điệp và SLA.

---

## 2. Kiến trúc thành phần

| Layer | Chức năng |
| --- | --- |
| **Channel & API** | REST/gRPC cho partner, SDK checkout, QR API |
| **Gateway** | Routing theo merchant, 3DS, token vault |
| **Switch** | ISO 8583/20022 parser, routing Napas/Visa/Master |
| **Authorization Engine** | Balance check, limit, fraud decision |
| **Settlement & Reconciliation** | Clearing file, GL posting, dispute |
| **Fraud & Risk** | Real-time scoring, velocity rules, case management |

**Supporting services**: Merchant management, pricing/fee engine, reporting portal.

---

## 3. Giao thức & chuẩn dữ liệu

- **ISO 8583** cho card auth: cần quản lý MTI, bitmap, field mapping.
- **ISO 20022** (pacs.008, pacs.002) cho instant payment.
- **QR**: EMVCo, VietQR (NAPAS) data format.
- **3DS 2.0**: risk-based authentication.
- **Tokenization**: PCI DSS, vault service.

Logging phải mask PAN, CVV; tuân thủ PCI DSS.

---

## 4. Quy trình chính

1. **Onboarding merchant**: KYB, risk scoring, thiết lập MID/TID, contract.
2. **Authorization**: request từ POS/app → Gateway → Switch → Issuer; apply fraud rule.
3. **Clearing & Settlement**: nhận file từ scheme (Visa/Master) hoặc Napas, đối soát, tạo GL entry.
4. **Dispute & Chargeback**: workflow theo scheme rules, timeline chặt.
5. **Reporting & Reconciliation**: merchant portal, file payout, mismatch alert.
6. **Fraud Monitoring**: rule engine + ML, alert handler, blocklist.

---

## 5. KPI & SLO

| KPI | Ý nghĩa | Target |
| --- | --- | --- |
| TPS peak | Khả năng xử lý | 3-5k TPS (tùy ngân hàng) |
| Authorization latency | Trải nghiệm thanh toán | < 300ms domestic |
| Success rate | Giao dịch thành công | > 98% |
| Fraud rate (basis point) | Rủi ro | < 10 bps |
| Dispute resolution time | SLA với merchant | < 7 ngày |

Observability: tracing end-to-end (gateway → switch → issuer), monitor queue lag.

---

## 6. Checklist triển khai

- [ ] Thiết kế domain routing (domestic, international, wallet).
- [ ] Implement ISO 8583/20022 adapter + schema validation.
- [ ] Tích hợp authorization engine (balance, limit, risk).
- [ ] Xây batch clearing, reconciliation, GL interface.
- [ ] Thiết lập fraud stack: rule engine + ML, case management.
- [ ] Đảm bảo PCI DSS: token vault, network segmentation, key management.
- [ ] API documentation + sandbox cho merchant/partner.

---

## 7. Use case

1. **QR ecosystem**: hỗ trợ VietQR + merchant dynamic QR, instant settlement, fee sharing.
2. **BNPL merchant integration**: API real-time decision, installment plan, merchant settlement D+1.
3. **Cross-border payout**: mapping ISO 20022 ↔ SWIFT, compliance screening (OFAC, sanctions).

---

## 8. Công nghệ & vendor

- Switch/Gateway: FIS, ACI, BPC, in-house microservice.
- Fraud: Feedzai, Featurespace, in-house ML.
- Tokenization: Thales, Visa Token Service.
- Observability: OpenTelemetry, Kafka monitoring.

> Ưu tiên kiến trúc scale-out (K8s), support blue/green deploy.

---

## 9. Tài liệu tham khảo

- Napas specs, Visa/Master rules, SBV quy định 19/2016/TT-NHNN (thanh toán không dùng tiền mặt).
- EMVCo technical docs, ISO 20022 resources.
- 11:FS payments report, McKinsey Global Payments Map.