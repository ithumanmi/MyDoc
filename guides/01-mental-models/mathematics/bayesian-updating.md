# 📈 Bayesian Updating thực dụng

## Tóm tắt nhanh
- Công thức Bayes dạng odds: **Posterior Odds = Prior Odds × Likelihood Ratio (LR)**.
- Dùng **LR** để cập nhật nhanh niềm tin khi có bằng chứng tuần tự (test y tế, tín hiệu kinh doanh, A/B test).
- Quy trình: đặt prior (base rate) → xác định LR cho từng bằng chứng → nhân dồn → chuyển về xác suất.

---

## 1) Bayes dạng xác suất vs dạng odds
**Dạng xác suất (quen thuộc):**
\( P(A\mid B) = \dfrac{P(B\mid A)P(A)}{P(B)} \)

**Dạng odds (cập nhật nhanh):**
\( \text{Posterior Odds} = \text{Prior Odds} \times \text{Likelihood Ratio} \)

- **Odds** của A: \( \dfrac{P(A)}{1-P(A)} \).
- **Likelihood Ratio (LR):** \( \dfrac{P(B\mid A)}{P(B\mid \neg A)} \). LR > 1 tăng niềm tin; LR < 1 giảm niềm tin.
- Sau khi nhân, chuyển lại thành xác suất: \( P = \dfrac{\text{Odds}}{1+\text{Odds}} \).

## 2) Khi nào nên dùng Bayesian Updating?
- Nhận tín hiệu tuần tự: test y tế nhiều lần, nhiều chỉ báo kinh doanh, nhiều sự kiện bảo mật.
- Khi base rate (tỷ lệ cơ bản) quan trọng và thay đổi kết luận mạnh (ví dụ bệnh hiếm, gian lận hiếm).
- Khi cần “cộng dồn niềm tin” mà không phải tính lại toàn bộ phân phối mỗi lần.

## 3) Ví dụ nhanh: test y tế lặp
- Base rate bệnh: 0.1% → Prior odds = 0.001 / 0.999 ≈ 0.001001.
- Test 1: Độ nhạy 99% (TPR), Độ đặc hiệu 99% → LR+ = 0.99 / 0.01 = 99.
  - Posterior odds = 0.001001 × 99 ≈ 0.0991 → P ≈ 0.090 (9%).
- Test 2 (độc lập, cùng chất lượng) lại dương tính:
  - Prior odds mới = 0.0991. Posterior odds = 0.0991 × 99 ≈ 9.81 → P ≈ 0.907 (90.7%).
- **Bài học:** Test lặp có thể làm xác suất nhảy vọt khi LR lớn; nhưng với bệnh hiếm, một test dương tính chưa đủ cao.

### Biến thể: test chất lượng vừa phải
- Độ nhạy 90%, Độ đặc hiệu 90% → LR+ = 0.9 / 0.1 = 9.
- Base rate 0.1%: Posterior sau 1 test ≈ 0.9%; sau 2 test ≈ 7.6% (thấp hơn nhiều so với test 99/99).
- **Bài học:** Test kém chính xác làm xác suất tăng chậm; cần nhiều bằng chứng hoặc test tốt hơn.

## 4) Ví dụ A/B test đơn giản (chuyển đổi)
- Prior: Variant B “có cải thiện” so với A chỉ 30% (odds = 0.3/0.7 ≈ 0.4286).
- Quan sát 1: dữ liệu cho LR = 2 (tín hiệu vừa phải). Posterior odds = 0.4286 × 2 = 0.857 → P ≈ 46%.
- Quan sát 2: thêm dữ liệu mới, LR = 3. Posterior odds = 0.857 × 3 = 2.571 → P ≈ 72%.
- **Bài học:** Kết hợp dữ liệu tuần tự; mỗi đợt tăng/giảm niềm tin mượt mà thay vì “đạt p<0.05 mới tin”.

### Biến thể: sản phẩm mới & tín hiệu hỗn hợp
- Prior “sản phẩm sẽ thành công” = 20% (odds = 0.2/0.8 = 0.25).
- Bằng chứng 1 (survey sớm, bias cao): LR = 1.5 → odds = 0.375 → P ≈ 27.3%.
- Bằng chứng 2 (cohort retention D7 tốt): LR = 3 → odds = 1.125 → P ≈ 52.9%.
- Bằng chứng 3 (CAC tăng mạnh, tín hiệu xấu): LR = 0.5 → odds = 0.5625 → P ≈ 36%.
- **Bài học:** Chuỗi bằng chứng trái chiều được cộng dồn có kiểm soát; tín hiệu xấu kéo niềm tin xuống thay vì bỏ qua.

### Biến thể: phát hiện gian lận (fraud)
- Prior “giao dịch là gian lận” = 0.2% (odds ≈ 0.002004).
- Tín hiệu 1: IP bất thường (LR = 8) → odds ≈ 0.016 → P ≈ 1.6%.
- Tín hiệu 2: Thiết bị lạ + velocity cao (LR = 6) → odds ≈ 0.096 → P ≈ 8.8%.
- Tín hiệu 3: Thẻ từng chargeback (LR = 10) → odds ≈ 0.96 → P ≈ 49%. Rào cứng kích hoạt: chặn/tạm giữ.
- **Bài học:** Với base rate rất thấp, cần nhiều tín hiệu mạnh mới vượt ngưỡng hành động; hãy định nghĩa ngưỡng (review thủ công, chặn tự động).

## 5) Checklist áp dụng nhanh
1) Ghi rõ **Prior** (base rate). Nếu không biết, thử phạm vi (ví dụ 0.1%–5%).
2) Xác định **LR** cho từng bằng chứng (từ độ nhạy/đặc hiệu, hoặc từ power/likelihood của thí nghiệm).
3) Nhân dồn odds với LR theo thứ tự bằng chứng.
4) Chuyển về xác suất để diễn giải; so với ngưỡng hành động (trigger/stop).
5) Nếu bằng chứng không độc lập, hạ LR xuống (bảo thủ); đặt **ngưỡng hành động** rõ: review thủ công, chặn, hay tiếp tục quan sát.

## 6) Sai lầm thường gặp
- Quên base rate → phóng đại rủi ro hiếm (bệnh hiếm, gian lận hiếm).
- Nhân LR của các bằng chứng phụ thuộc như thể độc lập → thổi phồng kết quả.
- Dừng sớm sau một tín hiệu yếu; hoặc không cập nhật khi có dữ liệu mới.

## 7) Công cụ tính nhanh (pseudo-code)
```python
def odds(p):
    return p/(1-p)

def prob(o):
    return o/(1+o)

def update(prior_p, lrs):
    o = odds(prior_p)
    for lr in lrs:
        o *= lr
    return prob(o)

# Ví dụ: prior 0.001, hai bằng chứng LR=99,99
print(update(0.001, [99,99]))  # ~0.907
```

## 8) Liên kết gợi ý
- **Probability thực dụng:** [./probability-real-life.md](./probability-real-life.md)
- **Statistics traps:** [./statistics-mental-models.md](./statistics-mental-models.md)
- **Decision under uncertainty:** [../psychology/practical-applications/multi-criteria-decision-making.md](../psychology/practical-applications/multi-criteria-decision-making.md)