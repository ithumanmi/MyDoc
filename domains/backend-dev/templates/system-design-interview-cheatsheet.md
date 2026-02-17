# 🧮 System Design Interview Cheatsheet

> [← Back to Backend Roadmap](../README.md)

Những con số "thần thánh" bạn cần nhớ để ước lượng (Estimation) nhanh trong phỏng vấn System Design.

---

## 1. Latency Numbers (Độ trễ) ⏱️
*Con số xấp xỉ năm 2025. Hãy nhớ thứ tự độ lớn (Orders of Magnitude).*

| Operation | Time | Note |
| :--- | :--- | :--- |
| **L1 Cache reference** | 0.5 ns | Siêu nhanh |
| **Mutex lock/unlock** | 100 ns | |
| **Main Memory (RAM) reference** | 100 ns | Nhanh |
| **Compress 1KB with Zippy** | 10,000 ns (10 µs) | |
| **Send 2KB over 1 Gbps network** | 20,000 ns (20 µs) | |
| **Read 1 MB sequentially from Memory** | 250,000 ns (250 µs) | |
| **Round trip within same Data Center** | 500,000 ns (0.5 ms) | Quan trọng |
| **Disk seek (SSD)** | 1,000,000 ns (1 ms) | SSD nhanh hơn HDD nhiều |
| **Disk seek (HDD)** | 10,000,000 ns (10 ms) | Chậm |
| **Read 1 MB sequentially from Network** | 10,000,000 ns (10 ms) | |
| **Read 1 MB sequentially from Disk** | 30,000,000 ns (30 ms) | |
| **Send packet CA -> Netherlands -> CA** | 150,000,000 ns (150 ms) | Ping xuyên lục địa |

👉 **Quy tắc ngón tay cái:**
*   Cache (Redis) ~ **Sub-millisecond** (< 1ms).
*   Database (Disk) ~ **Millisecond** (1-10ms).
*   Network (Cross-region) ~ **Hundreds of milliseconds** (100ms+).

---

## 2. Capacity Estimation Math (Công thức tính nhanh) ➗

### Traffic (Requests per Second - RPS)
*   **DAU (Daily Active Users):** Số user hoạt động hàng ngày.
*   **RPS công thức:** `DAU * Requests_per_User / 86400 (seconds in a day)`
*   **Ví dụ:** 10M DAU, mỗi người 100 req/ngày.
    *   Total Req = 10M * 100 = 1 Tỷ (1 Billion).
    *   RPS = 1,000,000,000 / 86,400 ≈ **11,500 RPS**.

### Storage (Dung lượng)
*   **Bit vs Byte:** 8 Bits = 1 Byte.
*   **Quy đổi:**
    *   1000 B = 1 KB
    *   1000 KB = 1 MB
    *   1000 MB = 1 GB
    *   1000 GB = 1 TB
    *   1000 TB = 1 PB (Petabyte)
*   **Ví dụ:** Lưu trữ 500M tweets mỗi ngày, mỗi tweet 1KB.
    *   Daily = 500M * 1KB = 500GB.
    *   Yearly = 500GB * 365 ≈ **180TB**.
    *   5 Years = 180TB * 5 = **900TB** (Gần 1PB).

---

## 3. Availability Numbers (Độ sẵn sàng) 🛡️

| Availability % | Downtime per Year | Downtime per Day |
| :--- | :--- | :--- |
| **99% (Two nines)** | 3.65 days | 14.4 mins |
| **99.9% (Three nines)** | 8.76 hours | 1.44 mins |
| **99.99% (Four nines)** | 52.6 mins | 8.64 secs |
| **99.999% (Five nines)** | 5.26 mins | 0.86 secs |

👉 **Mục tiêu:** Hầu hết hệ thống lớn (AWS, Google) nhắm tới **99.99%**.

---

## 4. Power of Two (Lũy thừa của 2) 2️⃣
*Hữu ích khi tính toán bộ nhớ và địa chỉ.*

*   2^10 ≈ 1 Thousand (10^3) -> 1 KB
*   2^20 ≈ 1 Million (10^6) -> 1 MB
*   2^30 ≈ 1 Billion (10^9) -> 1 GB
*   2^32 ≈ 4 Billion -> Giới hạn của integer 32-bit (IPv4 addresses).
