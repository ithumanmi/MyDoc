# 📗 Lab: Wireshark Packet Analysis & TCP Anomaly Detection

> Mục tiêu: bắt gói tin bằng Wireshark/tshark, phân tích handshake TCP, phát hiện bất thường như retransmission, port scan, Slowloris.

---

## 1. Setup bắt gói tin

| Công cụ | Ghi chú |
| --- | --- |
| Wireshark GUI | Quan sát trực quan |
| tshark | CLI capture + export CSV |
| tcpdump | Bắt gói tin từ server headless |

### Capture mẫu
```bash
sudo tcpdump -i eth0 -w capture.pcap
scp capture.pcap user@pc:/tmp
```

Hoặc `tshark -i eth0 -Y "tcp" -T fields -e frame.time -e ip.src -e tcp.flags > tcp.csv`.

---

## 2. Phân tích TCP 3-way handshake

1. Filter `tcp.flags.syn == 1 and tcp.flags.ack == 0` để thấy SYN.
2. Theo dõi `SYN, SYN/ACK, ACK` – dùng `Follow TCP Stream`.
3. Kiểm tra `RTT`, `Window size`, `MSS`.

### Checklist
- ACK không trả lời? → nghi DoS SYN flood.
- `tcp.analysis.retransmission` cao → network issue hoặc packet loss.

---

## 3. Bài tập phát hiện port scan

### 3.1 SYN Scan
```bash
nmap -sS <target>
```

Wireshark filter: `tcp.flags.syn == 1 && tcp.flags.ack == 0`
- Sử dụng `Statistics > Conversations` để xem số lượng port.
- Dùng `IO Graph` hiển thị SYN per second.

### 3.2 Xmas/FIN Scan
Filter: `tcp.flags.fin == 1 && tcp.flags.psh == 1 && tcp.flags.urg == 1`.

---

## 4. HTTP/Slowloris Detection

1. Dùng tool `slowhttptest` hoặc `slowloris.py` nhắm vào server lab.
2. Wireshark filter `tcp.len == 0 && http.request.method == "POST"` (giữ kết nối mở).
3. Quan sát `TCP Window Full` hoặc connection nhiều nhưng data nhỏ.

---

## 5. Export + Report
- Xuất `File > Export Objects > HTTP` để trích xuất file.
- Dùng `tshark -r capture.pcap -q -z io,stat,1` để lấy thống kê.

### Báo cáo đề xuất
| Phần | Nội dung |
| --- | --- |
| Summary | Mô tả mục tiêu capture |
| Timeline | Bảng thời gian SYN flood / port scan |
| Evidence | Screenshot filter, IO graph |
| Mitigation | Đề xuất firewall/IDS rule |

> ✅ Hoàn thành khi bạn xác định được ít nhất 2 bất thường (port scan + slowloris) và ghi lại bằng screenshot/IO graph.