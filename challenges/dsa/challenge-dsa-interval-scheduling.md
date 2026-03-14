# Challenge: Interval Scheduling with Minimum Rooms

- **Loại:** kata
- **Mảng:** dsa
- **Mức:** Intermediate
- **Ước lượng thời gian:** 1-2 giờ
- **Prerequisites:** [`domains/dsa/README.md`](../../domains/dsa/README.md)

## Mục tiêu học tập
- Áp dụng greedy cho bài toán interval scheduling (meeting rooms).
- Phân tích độ phức tạp thời gian/không gian và chứng minh tính đúng đắn ngắn gọn.

## Đề bài
Cho danh sách các khoảng thời gian meeting `[start, end)` (end > start). Tìm **số phòng tối thiểu** cần có để không trùng lịch.

## Đầu vào (Input)
- `n` dòng chứa `start end` (int), hoặc 1 mảng intervals.

## Đầu ra (Output)
- Một số nguyên: số phòng tối thiểu.

## Tiêu chí chấm (Acceptance)
- **Đúng:** Kết quả chuẩn với test mẫu và test ẩn.
- **Hiệu năng:** O(n log n) với sort + heap (min-heap end times).
- **Code quality:** Rõ ràng, có giải thích ngắn gọn (tại sao greedy đúng).

## Gợi ý / Hint
- Sort intervals theo start, dùng min-heap theo end để tái sử dụng phòng.
- Khi start >= min-end, pop heap và reuse phòng.

## Reference solution (tùy chọn)
- (Tuỳ chọn) Viết lời giải và test trong repo của bạn; link tại đây nếu public.