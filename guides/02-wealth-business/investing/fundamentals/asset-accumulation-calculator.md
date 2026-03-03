# 📊 Asset Accumulation Calculator Template

> Dùng template này để tính số tiền cần tích lũy cho từng tầng (ngắn hạn, trung hạn, dài hạn) và xác định khoản đóng góp đều đặn (DCA) cần thiết.

---

## 1. Thông tin đầu vào

```
Tên mục tiêu: _________________________
Tầng tài sản:  □ Ngắn hạn  □ Trung hạn  □ Dài hạn

Target Amount (FV): __________ VND
Thời gian (năm): __________
Lãi suất kỳ vọng (r/năm): __________ %
Chu kỳ đóng góp: □ Tháng  □ Quý  □ Năm

Số tiền hiện có (PV): __________ VND
Đóng góp ban đầu: __________ VND

Ghi chú: _______________________________________
```

---

## 2. Công thức tham chiếu

### 2.1. FV của khoản đóng góp định kỳ (Future Value of Annuity)

\[
FV = P \times \frac{(1 + r)^n - 1}{r}
\]

Trong đó:
- **P**: Khoản đóng góp mỗi kỳ.
- **r**: Lãi suất mỗi kỳ (ví dụ: 8%/năm → r = 0,08/12 nếu đóng góp hàng tháng).
- **n**: Tổng số kỳ đóng góp (số năm × số kỳ trong năm).

### 2.2. Tính ngược lại P từ Goal FV

\[
P = FV \times \frac{r}{(1 + r)^n - 1}
\]

### 2.3. Lồng PV (số tiền hiện có)

\[
FV_{Total} = PV \times (1 + r)^n + P \times \frac{(1 + r)^n - 1}{r}
\]

Nếu đã biết được **Goal FV**, bạn có thể tính P bằng cách:

\[
P = \frac{Goal\ FV - PV \times (1 + r)^n}{\frac{(1 + r)^n - 1}{r}}
\]

---

## 3. Bảng tính mẫu (monthly)

| Biến số | Giá trị |
| --- | --- |
| Goal (FV) | 800.000.000 VND |
| PV hiện tại | 100.000.000 VND |
| Thời gian | 5 năm |
| Lãi suất kỳ vọng | 8%/năm |
| Số kỳ (n) | 5 × 12 = 60 |
| r (mỗi tháng) | 0,08 / 12 = 0,0067 |
| Khoản đóng góp cần thiết (P) | `= (800M - 100M*(1+r)^60) / (((1+r)^60 - 1)/r)` |

> 💡 *Gợi ý:* Bạn có thể copy công thức này vào Google Sheets hoặc Excel để tự động tính. Trong Sheets:
`= (Goal - PV*(1+r)^n) / (((1+r)^n - 1)/r)`

---

## 4. Tracker theo thời gian

| Kỳ | Số tiền đóng góp | Lũy kế đóng góp | Lũy kế + lãi | Sai số so với mục tiêu |
| --- | --- | --- | --- | --- |
| Tháng 1 | | | | |
| Tháng 2 | | | | |
| ... | | | | |

### Quick Audit (mỗi quý)
- [ ] Tôi đạt ≥ 90% số tiền đóng góp kế hoạch?
- [ ] ROI thực tế so với kỳ vọng?
- [ ] Cần điều chỉnh r (lãi) hay P (đóng góp) không?

---

## 5. Checklist điều chỉnh

- [ ] Tăng thu nhập hoặc cắt giảm chi tiêu để tăng P nếu sai số > 10%.
- [ ] Chuyển sang sản phẩm lợi suất cao hơn nếu r thực tế quá thấp.
- [ ] Gia hạn thời gian nếu biến cố lớn làm hụt tiến độ.
- [ ] Chốt lời/bảo toàn vốn khi mục tiêu trung hạn đã đạt.

---

## 6. Log quyết định

```
Ngày: __________
Thay đổi: _________________________________
Lý do: ___________________________________
Hành động tiếp theo: ______________________
```

> 🧠 *Template này chỉ là điểm khởi đầu. Bạn có thể nhân bản file cho từng mục tiêu hoặc nhúng vào Notion/Google Sheets để theo dõi động.*
