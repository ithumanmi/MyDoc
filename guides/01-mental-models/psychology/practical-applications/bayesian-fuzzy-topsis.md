# 🧮 Bayesian Fuzzy TOPSIS cho quyết định đa tiêu chí

## Tóm tắt nhanh
- TOPSIS: chọn phương án gần **giải pháp lý tưởng** và xa **giải pháp tệ nhất**.
- Fuzzy: dùng số mờ (L, M, U) thay cho điểm cứng khi đánh giá mơ hồ.
- Bayesian: cập nhật niềm tin/trọng số khi có dữ liệu mới (pilot/POC) thay vì chấm một lần cố định.
- Quy trình: Khung & thang mờ → Chuẩn hóa & trọng số → Xác định phương án lý tưởng/tệ nhất → Tính khoảng cách → Xếp hạng → Cập nhật Bayesian khi có quan sát mới.

---

## 1) Khi nào dùng?
- Có nhiều tiêu chí và đánh giá mơ hồ (định tính), nhưng muốn **xếp hạng ổn định** thay vì chỉ cộng điểm.
- Có dữ liệu mới dần (pilot, POC, A/B test) và muốn **cập nhật niềm tin** về trọng số/điểm thay vì chấm cố định.

## 2) Ôn nhanh TOPSIS (cứng)
1) Chuẩn hóa ma trận quyết định.
2) Nhân trọng số cho từng tiêu chí.
3) Xác định **Ideal Best** (tốt nhất từng tiêu chí) và **Ideal Worst** (tệ nhất từng tiêu chí).
4) Tính khoảng cách mỗi phương án tới Best và Worst.
5) Điểm xếp hạng = d(Worst) / (d(Best) + d(Worst)); càng gần 1 càng tốt.

## 3) Fuzzy TOPSIS
- Dùng số mờ tam giác (L,M,U) cho từng đánh giá; khoảng cách dùng độ đo giữa các số mờ.
- Ideal Best/Worst cũng là số mờ: lấy max/min theo từng tiêu chí.
- Giải mờ (defuzzify) điểm xếp hạng để so sánh cuối.

## 4) Bayesian Fuzzy TOPSIS (ý tưởng thực dụng)
- **Cập nhật trọng số**: coi trọng số tiêu chí là phân phối (ví dụ Dirichlet). Khi có dữ liệu mới (kết quả pilot), cập nhật posterior → trọng số thay đổi nhẹ.
- **Cập nhật điểm mờ**: với mỗi tiêu chí/phương án, coi tham số (L,M,U) đến từ quan sát; có thêm dữ liệu thì thu hẹp biên mờ (giảm độ rộng).
- Lặp lại TOPSIS sau mỗi lần cập nhật để xem thứ hạng ổn định hơn hay đảo.

## 5) Quy trình gọn
1) **Frame & thang mờ**: tiêu chí 4–7, thang VL/L/M/H/VH → số mờ tam giác.
2) **Đánh giá mờ + trọng số priors**: thu nhận đánh giá; trọng số khởi tạo (Dirichlet α ~ 1 hoặc ưu tiên tiêu chí quan trọng hơn).
3) **Fuzzy TOPSIS cơ bản**: chuẩn hóa mờ, tìm Ideal Best/Worst mờ, tính khoảng cách, xếp hạng.
4) **Cập nhật Bayesian** (khi có dữ liệu mới):
   - Cập nhật trọng số (posterior) theo kết quả thực tế/ưu tiên mới.
   - Cập nhật (L,M,U) dựa trên quan sát (thu hẹp độ rộng nếu chắc chắn hơn).
   - Chạy lại bước 3 để xem thứ hạng biến động.
5) **Nhạy cảm & rào cứng**: thử thay đổi priors ±10–20%; áp dụng must-have để loại phương án vi phạm.

### Công thức/giả mã giản lược
```python
# Giả định đã có fuzzy_matrix[option][criterion] = (L,M,U)
# weights là vector (có thể từ posterior Dirichlet)

def defuzz(tri):
    L,M,U = tri
    return (L+M+U)/3

def fuzzy_distance(a, b):
    # khoảng cách Euclid trên điểm defuzzify (đơn giản hóa)
    return abs(defuzz(a) - defuzz(b))

def fuzzy_topsis(matrix, weights):
    criteria = list(weights.keys())
    options = list(matrix.keys())
    # Ideal best/worst theo từng tiêu chí
    ideal_best = {}
    ideal_worst = {}
    for c in criteria:
        vals = [defuzz(matrix[o][c]) for o in options]
        ideal_best[c] = max(vals)
        ideal_worst[c] = min(vals)
    scores = {}
    for o in options:
        d_best = 0
        d_worst = 0
        for c in criteria:
            v = defuzz(matrix[o][c])
            d_best  += (v - ideal_best[c])**2 * weights[c]
            d_worst += (v - ideal_worst[c])**2 * weights[c]
        d_best = d_best**0.5
        d_worst = d_worst**0.5
        scores[o] = d_worst / (d_best + d_worst)
    return scores

# Bayesian cập nhật trọng số (phác thảo):
# weights ~ Dirichlet(alpha); khi ưu tiên tiêu chí c tăng, alpha[c] += k; rồi lấy kỳ vọng w = alpha / sum(alpha)
```

## 6) Ví dụ ngắn (khung)
- Tiêu chí: Cost (C), Reliability (R), Team Fit (T). Thang VL/L/M/H/VH → số mờ tam giác.
- Trọng số prior (Dirichlet α): C=3, R=4, T=3 → kỳ vọng w≈[0.3,0.4,0.3].
- Đánh giá mờ: A: C=H, R=M, T=H; B: C=M, R=VH, T=M; C: C=VH, R=L, T=VH.
- Chạy fuzzy TOPSIS → xếp hạng. Sau pilot, thấy R của C chỉ đạt “M” (thu hẹp từ L/VH), và ưu tiên R tăng (α_R +=1) → chạy lại; nếu C tụt hạng, chọn A+B.

## 7) Mẹo thực dụng
- Giữ thang nhãn gọn (5 mức) và thống nhất; lưu giải thích khi chọn nhãn.
- Dùng priors trọng số phản ánh chiến lược (ví dụ an toàn cao → α_R lớn hơn).
- Mỗi lần có dữ liệu mới: cập nhật priors nhẹ, tránh dao động lớn (α tăng nhỏ).
- So sánh thứ hạng trước/sau cập nhật để xem phương án nào ổn định.
- Kết hợp rào cứng (must-have) để loại phương án vi phạm, dù điểm fuzzy cao.

## 8) Sai lầm thường gặp
- Dùng thang mờ không thống nhất → không thể tổng hợp.
- Không cập nhật priors khi bối cảnh đổi → mô hình không phản ánh thực tế.
- Chỉ nhìn điểm cuối, không xem khoảng cách Best/Worst → bỏ qua độ ổn định.

## 9) Liên kết gợi ý
- **Fuzzy MCDM (điều kiện mờ chung):** [./fuzzy-mcdm.md](./fuzzy-mcdm.md)
- **MCDM (điểm cứng):** [./multi-criteria-decision-making.md](./multi-criteria-decision-making.md)
- **Decision Razors:** [../decision-making-razors.md](../decision-making-razors.md)