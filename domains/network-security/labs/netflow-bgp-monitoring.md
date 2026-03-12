# 🌐 Lab: NetFlow & BGP Monitoring for Route Anomalies

> Mục tiêu: thu thập NetFlow + BGP update từ lab GNS3/EVE-NG, đẩy về Elastic/Splunk để phát hiện route leak, BGP hijack và traffic spike bất thường.

---

## 1. Kiến trúc lab

| Thành phần | Vai trò |
| --- | --- |
| **GNS3 topology (AS65010, AS65020)** | Sinh traffic + BGP update |
| **Flow exporter (nprobe/pmacct/Cisco IOS)** | Xuất NetFlow v5/v9 |
| **BMP collector (OpenBMP/Facebook BMP)** | Thu thập BGP update realtime |
| **Elastic Stack / Splunk / InfluxDB** | Lưu trữ + dashboard |

### Topology đề xuất
```
AS65010 (R1) --- eBGP --- (R2) AS65020
   |                       |
Host A                 Host B
```

---

## 2. Thu thập NetFlow

### 2.1 Cisco IOSv / FRRouting exporter
```bash
interface Gig0/0
 ip flow ingress
 ip flow egress

ip flow-export version 9
ip flow-export destination 192.168.100.10 2055   # collector
ip flow-cache timeout active 1
ip flow-cache timeout inactive 15
```

### 2.2 Collector bằng nProbe → Logstash/Elasticsearch
```bash
sudo apt install -y nprobe
sudo nprobe --collector-port 2055 --zmq tcp://127.0.0.1:5556

sudo logstash -f netflow-pipeline.conf
```

`netflow-pipeline.conf`
```conf
input {
  zeromq {
    mode => "client"
    endpoint => "tcp://127.0.0.1:5556"
    topology => "pushpull"
  }
}
filter {
  mutate { add_field => { "[@metadata][index]" => "netflow-%{+YYYY.MM.dd}" } }
}
output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
    index => "%{[@metadata][index]}"
  }
}
```

---

## 3. Thu thập BGP Update (BMP)

### 3.1 FRRouting config
```bash
router bgp 65010
 bmp server 1 address 192.168.100.11 port 5000
 bmp server 1 monitoring policy in
 bmp server 1 statistics interval 30
```

### 3.2 Collector OpenBMP
```bash
docker run -d --name openbmp -p 5000:5000/tcp openbmp/openbmp:latest
docker logs -f openbmp
```

OpenBMP có thể stream vào Kafka/Logstash để đưa vào Elastic.

---

## 4. Dashboard & Detection

### 4.1 Kibana Lens
- **Lens 1:** `sum(netflow.bytes)` theo `source.as` → phát hiện traffic tăng đột biến từ AS lạ.
- **Lens 2:** `count(bmp.update)` filter `as_path` chứa ASN bất thường.

### 4.2 Alert rule mẫu (Elastic)
```kql
netflow.destination.as: 65010 AND netflow.bytes > 5000000
```
Combine cùng event `bmp.as_path: "*65030*"` để nghi ngờ hijack.

### 4.3 Splunk SPL
```spl
index=netflow dest_as=65010
| timechart sum(bytes) by src_as

index=bmp_updates as_path="*65030*"
| stats latest(prefix) by peer_asn
```

Alert khi sum(bytes) tăng > 2x baseline trong 5 phút + xuất hiện ASN mới.

---

## 5. Lab Exercises

1. **Baseline:** chạy iPerf giữa Host A ↔ B, ghi nhận NetFlow.
2. **Traffic spike:** chạy `iperf -u` giả lập DDoS, xem dashboard Bytes/second.
3. **Hijack:** R2 quảng bá subprefix /24 → quan sát BGP update + traffic route lại.
4. **Mitigation:** bật prefix-filter hoặc RPKI (FRR `rpki`) → xác nhận alert giảm.

---

## 6. Reporting & Next Steps
- Xuất dashboard PNG + mô tả incident timeline.
- Viết playbook: khi ASN lạ xuất hiện → contact upstream + áp dụng roa filter.
- Kết nối NetFlow/BMP vào SOAR để tự động mở ticket nếu route leak kéo dài > 5 phút.

> ✅ Lab hoàn thành khi bạn tạo được alert kết hợp NetFlow spike + BGP path anomaly.