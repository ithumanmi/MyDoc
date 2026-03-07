# 🧪 Coding Challenge #2 – Memory Window Anomaly Detector

## Bối cảnh
SaaS của bạn ingest log từ hàng triệu IoT devices. Mỗi log record có dạng `(timestamp, device_id, memory_usage_mb)`. Bạn cần hệ thống real-time phát hiện **anomaly**: trong bất kỳ cửa sổ thời gian `W` phút, nếu có **>= K** thiết bị vượt ngưỡng `threshold_mb` thì trigger alert ngay.

## Input stream
- Sắp xếp theo timestamp tăng dần (real-time append).
- Multiple readings từ cùng 1 device trong cửa sổ.

## Yêu cầu
- Cửa sổ trượt `W` phút (ví dụ 10 phút).
- Nếu trong cửa sổ hiện tại có ít nhất `K` device **khác nhau** có lần đọc `memory_usage ≥ threshold`, bắn alert.
- Hệ thống phải xử lý 200k events/s.

## Gợi ý giải thuật

1. **Sliding Window + HashMap + Min-Heap**
   - Dùng deque/queue lưu events đang nằm trong cửa sổ.
   - HashMap `device -> count` số lần vượt ngưỡng trong cửa sổ.
   - Khi event mới đến, push vào queue và cập nhật map.
   - Pop khỏi queue những event có `timestamp < current - W` và cập nhật map.
   - Track số device đang vượt ngưỡng (hashmap size). Nếu ≥ `K` → emit alert.
2. **Optimization**: dùng `Counter` + refcount để tránh loop toàn bộ map.
3. **Time Complexity**: mỗi event push/pop O(1) amortized ⇒ tổng O(n).

## Bonus
- Mở rộng: chia theo region (multi-tenant) → dùng `dict<region, sliding window state>`.
- Nếu stream disorder ±ε giây: cần buffer nhỏ và sort theo window.