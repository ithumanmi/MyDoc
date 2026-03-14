# Challenge: Sliding Window / Two Pointers — 3 Bài Cơ Bản

- **Loại:** kata
- **Mảng:** dsa
- **Mức:** Beginner
- **Ước lượng thời gian:** 1-3 giờ
- **Prerequisites (tùy chọn):** [`domains/dsa/README.md`](../../domains/dsa/README.md)

## Mục tiêu học tập
- Thuần thục kỹ thuật sliding window / two pointers.
- Viết giải O(n) và phân tích thời gian/không gian.

## Đề bài
Giải 3 bài sau (chấp nhận đặt tên tuỳ ý):
1) **Subarray Sum = K (non-negative)**: Đếm số subarray có tổng = K (giả sử nums >= 0 để dùng two pointers).
2) **Longest Substring Without Repeating Characters**: Tìm độ dài lớn nhất của substring không lặp ký tự.
3) **Max Sum Subarray of Size K**: Cho K, tìm tổng lớn nhất của subarray độ dài K.

## Đầu vào (Input)
- Mảng `nums` và/hoặc chuỗi `s`, tham số `k` (nếu cần).

## Đầu ra (Output)
- Kết quả cho từng bài (số đếm, độ dài, hoặc tổng tối đa).

## Tiêu chí chấm (Acceptance)
- **Đúng:** Qua test mẫu và test ẩn.
- **Hiệu năng:** O(n) cho mỗi bài; dùng sliding window/two pointers.
- **Code quality:** Rõ ràng, có giải thích ngắn (tại sao di chuyển con trỏ vậy).

## Gợi ý / Hint
- Dùng hashmap/set cho bài substring; đếm lặp và di chuyển left/right.
- Với tổng non-negative, two pointers giữ invariant tổng <= K.

## Reference solution (tùy chọn)
- (Tuỳ chọn) Đính kèm code + test nếu public.