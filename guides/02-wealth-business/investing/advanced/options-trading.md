# 📜 Options Trading (The Safe Way)

> [← Back to Investing](../../../README.md)

Options (Hợp đồng quyền chọn) thường bị coi là cờ bạc. Nhưng nếu dùng đúng cách, nó là công cụ tạo dòng tiền (Income) tuyệt vời.

> **Lưu ý:** Chỉ áp dụng cho thị trường Mỹ (US Stocks). Việt Nam chưa có Options cho cổ phiếu đơn lẻ (chỉ có Chứng quyền/HĐTL rất khác).

---

## 1. Covered Calls (Cho thuê cổ phiếu)

Bạn đang sở hữu 100 cổ phiếu Apple (AAPL). Thay vì để không, hãy "cho thuê" nó.

*   **Cách làm:** Bán 1 hợp đồng Call Option (Sell Call) ở mức giá cao hơn giá hiện tại (Strike Price).
*   **Kịch bản 1 (Giá < Strike):** Bạn giữ nguyên cổ phiếu + Nhận tiền phí (Premium). -> *Tạo thu nhập thụ động.*
*   **Kịch bản 2 (Giá > Strike):** Bạn buộc phải bán cổ phiếu ở giá Strike + Nhận tiền phí. -> *Chốt lời ở giá mong muốn.*
*   *Rủi ro:* Bị mất phần lãi nếu cổ phiếu tăng quá mạnh (Moonshot).

---

## 2. Cash-Secured Puts (Được trả tiền để mua rẻ)

Bạn muốn mua cổ phiếu Tesla (TSLA) nhưng giá $200 đắt quá. Bạn muốn mua ở giá $180.

*   **Cách thường:** Đặt lệnh Limit $180 và chờ (Không được gì nếu giá không khớp).
*   **Cách Options:** Bán 1 hợp đồng Put Option (Sell Put) giá $180.
*   **Kịch bản 1 (Giá > $180):** Bạn không mua được cổ phiếu, nhưng **được giữ tiền phí (Premium)**. -> *Nhận tiền vì đã chờ đợi.*
*   **Kịch bản 2 (Giá < $180):** Bạn buộc phải mua cổ phiếu giá $180 (đúng ý bạn) - Tiền phí đã nhận. -> *Mua được giá rẻ hơn cả $180.*

---

## 3. The Wheel Strategy (Chiến lược Bánh xe)

Kết hợp cả hai để tạo dòng tiền liên tục:

1.  **Sell Put** để mua cổ phiếu giá rẻ.
2.  Nếu bị khớp lệnh (đã sở hữu cổ phiếu) -> Chuyển sang **Sell Covered Call**.
3.  Nếu bị bán mất cổ phiếu (do giá tăng) -> Quay lại bước 1 **Sell Put**.
-> *Lặp lại vòng tròn này để "bào" tiền từ thị trường (Premium harvest).*
