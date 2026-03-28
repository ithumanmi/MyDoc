# 🌫️ Ra quyết định đa tiêu chí trong điều kiện mờ (Fuzzy MCDM)

## Tóm tắt nhanh
- Dùng khi dữ liệu/nhận định không chắc chắn, khó cho điểm chính xác (ví dụ: “khá tốt”, “rủi ro hơi cao”).
- Thay vì điểm cứng, dùng **thang ngôn ngữ** (Very Low/Low/Medium/High/Very High) ánh xạ sang **số mờ tam giác** để tính toán.
- Quy trình: Frame tiêu chí & thang mờ → Thu nhận đánh giá mờ → Tổng hợp & giải mờ (defuzzify) → Xếp hạng → Kiểm tra nhạy cảm.

---

## 1) Khi nào dùng Fuzzy MCDM?
- Nhận định chuyên gia mang tính định tính: độ rủi ro, mức phù hợp văn hóa, “dễ bảo trì”, “khó triển khai”.
- Dữ liệu đầu vào biến động hoặc thiếu: giá dự kiến, SLA ước lượng, effort/độ phức tạp chưa rõ.
- Cần gom ý kiến nhiều người, mỗi người dùng từ ngữ mơ hồ; cần một thang chung để so sánh công bằng.

## 2) Thang ngôn ngữ → số mờ tam giác (ví dụ)
| Nhãn | Số mờ tam giác (L, M, U) | Nghĩa |
|------|--------------------------|-------|
| VL (Very Low) | (0.0, 0.0, 0.25) | Rất thấp |
| L  (Low)      | (0.0, 0.25, 0.5) | Thấp |
| M  (Medium)   | (0.25, 0.5, 0.75)| Trung bình |
| H  (High)     | (0.5, 0.75, 1.0) | Cao |
| VH (Very High)| (0.75, 1.0, 1.0) | Rất cao |

*Có thể tinh chỉnh biên (L, M, U) theo ngữ cảnh; giữ tính nhất quán trong toàn bộ bảng.*

## 3) Quy trình Fuzzy MCDM (rút gọn)
1) **Frame & thang mờ:** tiêu chí 4–7; chọn thang ngôn ngữ và ánh xạ số mờ.
2) **Thu đánh giá mờ:** mỗi phương án, mỗi tiêu chí: chọn nhãn (VD: “High”, “Medium”). Nếu nhiều chuyên gia, lấy trung bình mờ (trung bình L, M, U).
3) **Tổng hợp:** nhân số mờ với trọng số (trọng số cũng có thể là mờ) và cộng lại → được điểm mờ tổng.
4) **Giải mờ (defuzzify):** dùng trung bình trọng số (centroid) = (L + M + U) / 3 để ra điểm crisp.
5) **Xếp hạng & kiểm tra:** xếp hạng theo điểm defuzzified; đổi thang mờ hoặc trọng số ±10–20% để xem thứ hạng có đảo.

### Pseudo-code minh họa (Python)
```python
def defuzzify(tri):
    L, M, U = tri
    return (L + M + U) / 3

def fuzzy_score(option, weights):
    # option: dict {criterion: (L,M,U)}, weights: dict {criterion: w}
    total = 0
    for c, tri in option.items():
        w = weights[c]
        total += defuzzify(tri) * w
    return total
```

## 4) Ví dụ nhanh
**Bài toán:** Chọn vendor A/B/C với tiêu chí: Giá (Cost), Độ tin cậy (Reliability), Phù hợp đội (Team Fit).

- Thang mờ: VL/L/M/H/VH như bảng trên. Trọng số: Cost 0.4, Reliability 0.35, Team Fit 0.25.
- Đánh giá (chọn nhãn, rồi ánh xạ):
  - Vendor A: Cost = H (0.5,0.75,1.0) rẻ; Reliability = M; Team Fit = H
  - Vendor B: Cost = M; Reliability = VH (0.75,1.0,1.0); Team Fit = M
  - Vendor C: Cost = VH; Reliability = L; Team Fit = VH
- Tính điểm (defuzzify × weight, cộng):
  - A ≈ 0.75*0.4 + 0.5*0.35 + 0.75*0.25 = 0.675
  - B ≈ 0.5*0.4 + 0.92*0.35 + 0.5*0.25 ≈ 0.661
  - C ≈ 0.92*0.4 + 0.25*0.35 + 0.92*0.25 ≈ 0.735
- **Xếp hạng:** C > A > B. Nếu rào cứng “Reliability không được Low”, C vi phạm → loại C, chọn A kèm điều khoản giảm rủi ro.

## 5) Mẹo thực dụng
- Định nghĩa rõ nhãn và bảng mờ từ đầu; dùng chung cho mọi người để so sánh công bằng.
- Giữ số tiêu chí và mức nhãn gọn để tránh nhiễu (5 mức VL/L/M/H/VH thường đủ).
- Ghi chú lý do chọn nhãn (tránh cảm tính trôi nổi khi rà soát lại).
- Dùng pilot/POC để cập nhật lại nhãn (ví dụ “Reliability” từ H xuống M) rồi tính lại.

## 6) Sai lầm thường gặp
- Thang mờ không thống nhất giữa người chấm → không cộng/trung bình được.
- Không có rào cứng nên kết quả mờ “cao điểm” nhưng vi phạm điều kiện tối thiểu.
- Không kiểm tra nhạy cảm trọng số/thang mờ → thứ hạng mong manh.

## 7) Tài liệu/khung liên quan
- **MCDM (điểm cứng):** [./multi-criteria-decision-making.md](./multi-criteria-decision-making.md)
- **Decision Razors:** [../decision-making-razors.md](../decision-making-razors.md)
- **Three Levels of Thinking:** [./three-levels-of-thinking.md](./three-levels-of-thinking.md)