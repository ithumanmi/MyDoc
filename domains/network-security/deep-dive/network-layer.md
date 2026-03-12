# 🌐 Network Layer Deep Dive: IP, ICMP, Routing

> [← Back to Network Security](../README.md)

Lớp Mạng (Layer 3) định nghĩa cách gói tin đi từ máy này sang máy khác qua nhiều hop. Hiểu sâu IP, ICMP và routing protocols giúp bạn debug sự cố, thiết kế kiến trúc và phòng thủ trước tấn công layer 3.

---

## 1. IP Addressing & MTU

### **IPv4 Essentials**
- Địa chỉ 32 bit, viết dạng dotted decimal (192.168.1.10).
- Subnet mask chia mạng con (VD: /24 -> 255.255.255.0, 256 host).
- CIDR cho phép chia linh hoạt (/29 -> 6 host usable).

### **CIDR Quick Reference**
| CIDR | Hosts usable | Typical use |
| --- | --- | --- |
| /30 | 2 | Link point-to-point |
| /24 | 254 | LAN / VLAN |
| /20 | 4094 | Large subnet / cloud VPC |

### **Subnetting Practice Workflow**
1. **Xác định yêu cầu host & mạng con:** Ví dụ cần 20 subnet, mỗi subnet ≥ 50 host.
2. **Chọn prefix phù hợp:** /26 cung cấp 62 host usable → đủ 50 host.
3. **Tạo bảng subnet:**

| Subnet # | Network | Broadcast | Host range |
| --- | --- | --- | --- |
| 0 | 192.168.10.0/26 | 192.168.10.63 | .1 – .62 |
| 1 | 192.168.10.64/26 | 192.168.10.127 | .65 – .126 |
| 2 | 192.168.10.128/26 | 192.168.10.191 | .129 – .190 |

4. **Xác thực bằng script/calculator:**
```bash
python - <<'PY'
import ipaddress
net = ipaddress.ip_network('192.168.10.0/24')
for i, subnet in enumerate(net.subnets(new_prefix=26)):
    print(i, subnet, 'hosts', subnet.num_addresses-2)
PY
```

### **MTU & Fragmentation**
- MTU mặc định Ethernet: 1500 bytes.
- Nếu packet > MTU và flag DF=0 -> Router sẽ fragment (chia nhỏ) -> tăng overhead, dễ bị drop.
- Với DF=1 và packet quá lớn -> Router gửi ICMP Fragmentation Needed.
- Best practice: Dùng Path MTU Discovery (PMTUD) để tránh fragment.

---

## 2. ARP, ND & Neighbor Tables
- IPv4 dùng **ARP** để map IP ↔ MAC.
- IPv6 dùng **Neighbor Discovery (ND)** dựa trên ICMPv6.
- ARP cache poisoning có thể dẫn tới MITM; dùng Dynamic ARP Inspection (DAI) / static ARP để bảo vệ.

---

## 3. ICMP (Internet Control Message Protocol)

### **Công dụng chính**
- **Type 8/0 (Echo Request/Reply):** Ping kiểm tra reachability.
- **Type 3 (Destination Unreachable):** Host/Port unreachable, fragmentation needed.
- **Type 11 (Time Exceeded):** TTL hết hạn – dùng cho traceroute.

### **Hardening**
- Rate-limit ICMP để chống ping flood nhưng không nên block hoàn toàn (ảnh hưởng PMTUD).
- Triển khai ACL cho phép ICMP cần thiết (type 3, 11) để chẩn đoán mạng.

### **Hands-on**
```bash
# Ping với kích thước lớn & DF
ping -f -l 1472 8.8.8.8   # Windows
ping -M do -s 1472 8.8.8.8  # Linux

# Traceroute with ICMP
tracert 1.1.1.1
sudo traceroute -I 1.1.1.1
```

---

## 4. Routing Table & Protocols Overview
- **Routing Table** chứa prefix → next hop.
- **Static routing**: cấu hình thủ công.
- **Dynamic routing**: dùng protocol để cập nhật tự động.

### **Classification**
- **IGP (Interior Gateway Protocol):** OSPF, IS-IS, EIGRP – dùng trong 1 AS.
- **EGP (Exterior Gateway Protocol):** BGP – trao đổi giữa các AS.

---

## 5. OSPF Deep Dive

### **Concepts**
- Chia network thành **area** (area 0 backbone) để giảm LSDB size.
- Router trao đổi **Link State Advertisements (LSA)**, build LSDB, chạy Dijkstra (SPF) để tạo routing table.

### **OSPF Packet Types**
1. **Hello:** Phát hiện neighbor, giữalive.
2. **DBD (Database Description):** Tóm tắt LSDB.
3. **LSR (Link State Request):** Yêu cầu chi tiết.
4. **LSU (Link State Update):** Gửi chi tiết LSA.
5. **LSAck:** Xác nhận nhận được LSA.

### **Lab Idea**
```bash
# GNS3/EVE-NG: 3 router OSPF
interface Gig0/0
 ip address 10.0.12.1 255.255.255.0
 router ospf 1
 network 10.0.12.0 0.0.0.255 area 0

# Kiểm tra LSDB
show ip ospf database
```

### **Security Considerations**
- Bật **OSPF authentication** (MD5/SHA) để tránh rogue router.
- Giới hạn adjacency (passive interface) nơi không cần thiết.

---

## 6. BGP Deep Dive

### **Core Ideas**
- BGP là path vector, trao đổi thông tin giữa Autonomous Systems (AS).
- Thuộc tính quan trọng: **AS_PATH, NEXT_HOP, LOCAL_PREF, MED**.
- Chính sách routing dựa trên policy, không chỉ cost.

### **Peering Types**
- **eBGP:** giữa các AS khác nhau (ISP ↔ ISP, ISP ↔ Enterprise).
- **iBGP:** trong cùng AS để quảng bá route học từ eBGP.

### **Sample Config (Cisco-ish)**
```bash
router bgp 65001
 neighbor 203.0.113.1 remote-as 65002
 neighbor 203.0.113.1 password SECRET
 network 203.0.113.0 mask 255.255.255.0

# Policy: ưu tiên transit mục tiêu
route-map PREFER-TRANSIT permit 10
 set local-preference 200
 neighbor 203.0.113.1 route-map PREFER-TRANSIT in
```

### **Security & Stability**
- Dùng **TTL security / GTSM** để chống spoofed TCP session.
- Triển khai **RPKI** để ngăn announcement sai (route hijacking).
- Thiết lập max-prefix để tránh full table crash.

---

## 7. Troubleshooting & Monitoring
- **Tools:** `mtr`, `pathping`, `ip route`, `show bgp summary`, `birdc show route`.
- **Netflow / sFlow:** quan sát traffic abnormal (DDoS, route leak).
- **Honeyroutes:** đặt route fake để phát hiện quét mạng (advanced).

### 🔗 Related Labs & Guides
- **[SIEM & Log Analysis (Elastic Stack)](../labs/siem-log-analysis.md):** Thu thập Netflow/host log để phát hiện bất thường layer 3.
- **[Splunk Threat Hunting Basics](../labs/splunk-threat-hunting.md):** Dò SSH brute-force, registry persistence – liên hệ với log network.
- **[Advanced Detection Use Cases](../labs/advanced-detection-usecases.md#1-lateral-movement-via-remote-service-creation--smb):** Lateral movement + SMB cross-layer monitoring.
- **Hands-on Subnetting Calculator:** Dùng script Python ở phần 1 hoặc công cụ [Subnet Cheat Sheet](https://www.practicalnetworking.net/ip-subnet-calculator) để luyện chia mạng.
- **GNS3 Routing Lab:** Kết hợp `network-layer.md` với [Virtual Lab Setup](../labs/virtual-lab-setup.md) để dựng 3 router OSPF và thử thêm session BGP lab.
- **BGP Security Scenario:** Sử dụng [Advanced Detection Use Cases](../labs/advanced-detection-usecases.md#6-bgp-hijacking-detection---netflow--bgp-monitoring) (nếu có) hoặc tự tạo log Netflow để mô phỏng hijack.

---

## 8. Further Practice
- Build lab OSPF multi-area + redistributes static route.
- Thiết lập eBGP session giả lập bằng FRRouting (FRR) trên lab Linux.
- Dùng Wireshark filter `ospf` hoặc `bgp` để xem packet format.
- Mô phỏng **BGP hijacking**: Dùng 2 AS trên GNS3, cố ý quảng bá prefix sai và quan sát bằng `show ip bgp` + log Netflow, sau đó triển khai filter/RPKI để mitig.
- Bài tập **Path MTU Discovery**: capture packet DF=1 khi ping size lớn để thấy ICMP Fragmentation Needed.

> Last Updated: March 2026
