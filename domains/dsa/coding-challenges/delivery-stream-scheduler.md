# 🚚 Coding Challenge #1 – Real-time Delivery Stream Scheduler

> **Context:** Bạn đang xây dựng hệ thống real-time cho công ty giao hàng. Luồng request liên tục chảy vào, mỗi request chứa `request_id`, `pickup_time`, `delivery_deadline`, `distance`, `priority_level (1-5)`.

## 🎯 Yêu cầu

- Chỉ có **3 delivery agents**, mỗi agent xử lý **1 delivery tại một thời điểm**.
- Thời gian thực hiện = `distance × 2` phút.
- Mục tiêu: *assign* delivery cho agents sao cho
  - Số delivery trễ deadline là ít nhất
  - Ưu tiên request priority cao hơn
  - Vận hành hiệu quả với 100k+ requests (O(n log n) mong muốn)
- Phải tính tới **time overlap** và tránh brute-force.

## 🔍 Tư duy giải thuật

### 1. Mô hình bài toán

Đây là sự kết hợp của **interval scheduling**, **priority weighting** và **online greedy**:

- Interval = `[pickup_time, pickup_time + duration]` với `duration = distance × 2`.
- Deadline constraint: `pickup_time + duration ≤ delivery_deadline`.
- Priority: càng thấp (1) → càng cao? đề bài: priority_level (1–5), ta giả sử **5 = cao nhất**.

### 2. Chiến lược Greedy + Heaps

1. **Sort request theo pickup_time** (hoặc arrival order trong stream). Khi stream real-time, ta insert theo thời gian đến.
2. Duy trì 2 cấu trúc:
   - `available_agents`: min-heap theo thời điểm agent rảnh (`available_at`).
   - `candidate_tasks`: max-heap theo priority + slack (deadline - duration).
3. Khi đến một request mới:
   - Nếu agent rảnh ngay (`available_at ≤ pickup_time`) ⇒ assign trực tiếp.
   - Nếu chưa có agent rảnh, ta có thể chờ agent sớm nhất. Nhưng để giảm trễ:
     - Push request vào `candidate_tasks` với key: `(priority, deadline, distance)`.
     - Khi có agent rảnh (pop từ `available_agents`), chọn request tốt nhất từ `candidate_tasks`: ưu tiên priority cao, tie-break bằng `deadline` sớm, tie tiếp bằng `shorter duration`.
4. Nếu yêu cầu không thể hoàn tất đúng hạn (dù assign ngay agent rảnh) ⇒ đánh dấu trễ.

### 3. Xử lý overlap & deadline

- Trước khi assign, check `start_time = max(pickup_time, agent_available_at)`.
- `finish_time = start_time + duration`.
- Nếu `finish_time > delivery_deadline` ⇒ request trễ ⇒ có thể skip hoặc ghi vào backlog.

### 4. Pseudocode (O(n log n))

```python
requests = sort_by_pickup_time(stream)
available_agents = MinHeap()  # (available_at, agent_id)
candidate_tasks = MaxHeap()   # (-priority, delivery_deadline, duration, request)

# init 3 agents rảnh lúc 0
for agent_id in range(3):
    available_agents.push((0, agent_id))

late_count = 0

for req in requests:
    # release agents rảnh trước pickup_time
    while available_agents.peek().available_at <= req.pickup_time and not candidate_tasks.empty():
        assign_best_request()

    candidate_tasks.push(build_key(req))

    # nếu có agent rảnh đúng thời điểm này, assign ngay
    if available_agents.peek().available_at <= req.pickup_time:
        assign_best_request()

def assign_best_request():
    agent = available_agents.pop()
    req = candidate_tasks.pop()
    start = max(req.pickup_time, agent.available_at)
    finish = start + req.duration
    if finish > req.delivery_deadline:
        late_count += 1
    agent.available_at = finish
    available_agents.push(agent)
```

> **Note:** Khi stream real-time, ta không sort upfront mà xử lý theo arrival time. Pseudocode trên giả định có thể chunk theo windows.

### 5. Vì sao không brute-force?

- Với 100k requests, mọi cách thử all combinations 3 agents (branching theo thời gian) sẽ bùng nổ (`O(k^n)`).
- Greedy + heap giúp chọn request tốt nhất trong `O(log n)` mỗi lần assign.

## ⚙️ Simulation Real-time

- Xử lý từng request theo thời gian đến (pickup_time) hoặc timestamp stream.
- Khi request đến, insert vào `candidate_tasks`.
- Event loop:
  1. Pop agent rảnh sớm nhất.
  2. Pop request tốt nhất (priority cao + deadline sớm).
  3. Nếu request finish trong deadline ⇒ assign; ngược lại ghi late.
  4. Nếu `candidate_tasks` trống ⇒ agent rảnh chờ.

Để tránh blocking, có thể chia thời gian thành **event queue**:

- `events = PriorityQueue` chứa `(time, type, payload)`
- `type=REQUEST_ARRIVAL` hoặc `AGENT_FREE`.
- Khi agent hoàn thành, push event `AGENT_FREE` để trigger assign.

## 🧠 Bonus – Time Complexity

- Mỗi request insert heap: `O(log n)`.
- Mỗi assignment pop/push heap: `O(log n)`.
- Tổng thể: **`O(n log n)`** (với `n` = số request).
- Memory: `O(n)` (worst-case backlog).

Nếu cần strict real-time, có thể dùng **calendar queue** hoặc **indexed priority queue** để giảm hằng số.

---

> **Further reading:**
> - Interval Scheduling with Deadlines (CLRS)
> - Task Scheduling on Parallel Machines
> - Real-time priority scheduling (Earliest Deadline First, Highest Priority First)
