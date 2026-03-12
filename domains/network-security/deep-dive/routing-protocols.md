# 🛰️ Routing Protocols Deep Dive: OSPF, BGP & Security

> [← Back to Network Security](../README.md) | [Network Layer Fundamentals](./network-layer.md)

Routing protocols quyết định đường đi của packet qua nhiều mạng. File này đào sâu cách vận hành OSPF/BGP, cách mô phỏng lab bằng GNS3/Packet Tracer và chiến lược phòng chống tấn công kiểu BGP hijacking.

---

## 1. Static vs Dynamic Routing

| Type | Ưu điểm | Nhược điểm | Dùng khi |
| --- | --- | --- | --- |
| Static route | Đơn giản, kiểm soát tuyệt đối | Không tự thích ứng khi link down | Lab nhỏ, mạng edge cố định |
| OSPF/IS-IS (Link-state) | Hội tụ nhanh, scale tốt | Phép tính SPF nặng với mạng lớn | Enterprise campus/SD-WAN |
| EIGRP/RIP (Distance vector) | Config nhẹ | Hội tụ chậm, scale kém | Legacy, môi trường nhỏ |
| BGP (Path vector) | Policy-based, hỗ trợ Internet scale | Config phức tạp, hội tụ chậm | ISP, multi-cloud, partner peering |

> 📌 **Checklist trước khi bật dynamic routing:** xác định area/AS, plan IP/subnet, enable authentication, giới hạn interface cần quảng bá.

---

## 2. OSPF Multi-Area Walkthrough

### 2.1 Topology đề xuất
- Area 0 (backbone): R1, R2
- Area 10 (branch): R2, R3
- Area 20 (data center): R1, R4

```
      Area 10           Area 0            Area 20
LAN -- R3 --- (10.0.23.0/30) --- R2 --- (10.0.12.0/30) --- R1 --- (10.0.14.0/30) --- R4 -- DC
```

### 2.2 Cấu hình mẫu (Cisco-like)
```bash
router ospf 1
 router-id 1.1.1.1
 network 10.0.12.0 0.0.0.3 area 0
 network 10.0.14.0 0.0.0.3 area 20
 passive-interface Gig0/1   # interface không cần quảng bá

! Area 10 ABR trên R2
area 10 stub no-summary
area 20 nssa default-information-originate
```

### 2.3 Thực hành trong GNS3 / Packet Tracer
1. Import 4 router IOSv hoặc sử dụng FRRouting container.
2. Cấu hình IP + OSPF theo bảng.
3. `show ip ospf neighbor`, `show ip route ospf` để xác nhận.
4. Thử shutdown link Area 10 để quan sát hội tụ (`debug ip ospf events`).

### 2.4 Hardening
- Bật `ip ospf authentication message-digest` + keychain.
- Passive interface ở switch access.
- Sử dụng `max-metric router-lsa` trong quá trình bảo trì để tránh router tạm thời được chọn đường chính.

---

## 3. BGP: Policy & Internet-facing Design

### 3.1 Terminology nhanh
- **AS (Autonomous System):** tập hợp router cùng chính sách.
- **ASN private/public:** 64512-65534 dùng lab, 1-64511 public.
- **Path attributes:** `AS_PATH`, `NEXT_HOP`, `LOCAL_PREF`, `MED`, `COMMUNITY`.

### 3.2 eBGP vs iBGP
| | eBGP | iBGP |
| --- | --- | --- |
| TTL mặc định | 1 | 255 |
| Nhận route | Từ AS khác | Nội bộ AS |
| Requirement | TTL security/GTSM | Full-mesh hoặc Route Reflector |

### 3.3 Sample Config (FRRouting)
```bash
router bgp 65010
 neighbor 203.0.113.1 remote-as 65020
 neighbor 203.0.113.1 password BGPSECRET
 neighbor 203.0.113.1 ebgp-multihop 2
 network 198.51.100.0/24

ip prefix-list EXPORT permit 198.51.100.0/24
route-map EXPORT permit 10
 match ip address prefix-list EXPORT
set community 65010:100
neighbor 203.0.113.1 route-map EXPORT out
```

### 3.4 Policy Scenarios
- **Multi-homing:** Sử dụng `LOCAL_PREF` để ưu tiên link chính, `MED` để gợi ý đường vào.
- **Blackhole DDoS:** Quảng bá `/32` với community blackhole tới upstream.
- **Regional exit:** Dùng community để chọn POP phù hợp.

---

## 4. BGP Hijacking Attacks & Mitigations

### 4.1 Attack Methods
1. **Prefix Hijack:** Đăng quảng bá prefix không thuộc AS của mình.
2. **Subprefix Hijack:** Quảng bá prefix nhỏ hơn (/24) → ưu tiên hơn.
3. **Route Leak:** Vô tình/ cố ý quảng bá route học được từ upstream xuống downstream không phép.

### 4.2 Detection Signals
- Sudden AS_PATH change trong route monitor (BGPStream, RIPE RIS).
- Netflow spike từ khu vực địa lý bất thường.
- Drop trong synthetic traceroute (ThousandEyes, Smokeping multi-region).

### 4.3 Mitigations
| Technique | Mô tả |
| --- | --- |
| **RPKI (Route Origin Validation)** | Sử dụng ROA để ISP drop announcement sai. |
| **Prefix filtering** | Chỉ cho phép khách hàng quảng bá prefix đã đăng ký. |
| **Max-prefix limits** | Ngăn router crash do full table leak. |
| **BGP Monitoring** | Sử dụng BGPmon, ARTEMIS hoặc tự build pipeline từ BMP feed. |

### 4.4 Lab: BGP Hijack Simulation
1. Lab 2 AS trên GNS3 (AS65010 legit, AS65030 attacker).
2. Legit quảng bá `10.10.0.0/16`, attacker quảng bá `10.10.10.0/24`.
3. Capture route table và Netflow trên collector (Elasticsearch/Splunk) → quan sát chuyển hướng traffic.
4. Áp dụng prefix filter/RPKI (trên FRR: `rpki` daemon) để block.

---

## 5. Lab Guide: Routing Playground (GNS3/Packet Tracer)

| Step | Hành động |
| --- | --- |
| 1 | Dựng topology 3 router GNS3, switch và 2 host test latency. |
| 2 | Chia subnet theo hướng dẫn [Subnetting Workflow](./network-layer.md#subnetting-practice-workflow). |
| 3 | Cấu hình OSPF multi-area + default route ra Internet giả lập. |
| 4 | Thêm peering eBGP giữa 2 AS, dùng loopback interface làm update-source. |
| 5 | Bật capture Wireshark trên link eBGP để phân tích message OPEN/UPDATE/KEEPALIVE. |
| 6 | Tạo sự cố: shutdown interface, đổi LOCAL_PREF, hoặc chạy script hijack và ghi lại kết quả. |

> 🔁 **Automation gợi ý:** sử dụng Ansible hoặc Python Netmiko để push config hàng loạt, sau đó parse output (`show ip bgp`) bằng TextFSM.

---

## 6. Monitoring & Telemetry

- **sFlow/Netflow export:** gửi về [SIEM Elastic Lab](../labs/siem-log-analysis.md) để phát hiện pattern BGP leak.
- **BGP Monitoring Protocol (BMP):** thu thập update realtime, có thể đẩy vào Kafka rồi SIEM.
- **SNMP/Streaming Telemetry:** track interface flaps (impact routing reconvergence).
- **Dashboards gợi ý:**
  - Timeline số lượng prefix nhận theo peer.
  - Alert khi `AS_PATH` chứa ASN không mong muốn.
  - Heatmap latency theo đường đi (thử với Smokeping, PerfSONAR).

---

## 7. Checklist ôn tập

- [ ] So sánh các loại routing protocol và chọn đúng use case.
- [ ] Tự cấu hình OSPF multi-area có authentication.
- [ ] Thiết lập eBGP + iBGP (loopback, update-source, next-hop-self).
- [ ] Thực hiện lab BGP hijack và viết playbook ứng phó.
- [ ] Tích hợp log Netflow/BGP vào SIEM với rule phát hiện.

> Last Updated: March 2026