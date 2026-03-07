# 🛰️ Coding Challenge #3 – Drone Route Load Balancer

## Bối cảnh
Startup logistics của bạn vận hành **fleet drone** giao hàng tại nhiều thành phố. Mỗi thành phố có tập `delivery segments`, mỗi segment gồm `start_point`, `end_point`, `energy_cost`, `deadline`. Drone có giới hạn năng lượng `max_energy`, và mỗi thành phố có `M` drone hoạt động song song. Yêu cầu: phân bổ segments cho drone sao cho **tối đa hóa số delivery hoàn thành đúng hạn** và **cân bằng tải giữa các drone**.

## Input
- `segments` dạng stream theo thành phố.
- Mỗi segment có thời gian bay `flight_time = distance / speed`, nhưng cost chính là `energy_cost`.
- Drone recharge mất 5 phút sau mỗi nhiệm vụ.

## Yêu cầu
1. Với mỗi thành phố, thiết kế algorithm gán segment cho `M` drone.
2. Không drone nào vượt quá `max_energy` trước khi recharge.
3. Ưu tiên segments có deadline gần và energy thấp.
4. Khi số segment lớn (n > 50k) phải đảm bảo `O(n log n)`.

## Hướng gợi ý

1. **Model as Weighted Interval Scheduling + Load balancing**
   - Tạo interval `start_time`, `finish_time = start + flight_time + recharge`.
   - Weight = `deadline_penalty` hoặc `priority`.
2. **Greedy with Multi-Queue**
   - Sort segments theo `deadline`.
   - Duy trì min-heap per city chứa `(available_time, energy_left, drone_id)`.
   - Khi segment đến: pop drone rảnh nhất (sớm nhất) có `energy_left ≥ energy_cost`.
   - Nếu có nhiều drone thỏa, chọn drone có tổng thời gian bay thấp nhất (cân bằng tải).
3. **Energy management**
   - Khi drone kết thúc nhiệm vụ, cập nhật `energy_left -= energy_cost`. Nếu `energy_left < threshold`, schedule recharge event.
4. **Complexity**
   - Mỗi segment push/pop một lần khỏi heap ⇒ `O(n log M)` (M nhỏ ⇒ gần O(n log n)).

## Bonus câu hỏi
- Làm sao để phân phối workload giữa các thành phố khác nhau? (Hint: dynamic partition / work stealing).
- Nếu drone có thể swap battery tại hub, bạn sẽ thay đổi model thế nào?