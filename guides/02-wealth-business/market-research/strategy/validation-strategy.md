# 5. Validation Strategy

> [← Back to Market Research](./README.md)

## 📄 Landing Page Blueprint (Công thức Trang đích)

Mục tiêu của Landing Page không phải để đẹp, mà là để **Chuyển đổi (Convert)** khách tham quan thành người quan tâm (Leads/Wishlists).

### Cấu trúc tiêu chuẩn (High-Converting Structure):

1.  **Hero Section (Màn hình đầu tiên):**
    *   **Headline (Tiêu đề):** Lời hứa lớn nhất của sản phẩm. (VD: "Build your dream factory in space").
    *   **Sub-headline:** Giải thích rõ hơn trong 1 câu. (VD: "Manage resources, automate production, and survive alien attacks").
    *   **Call to Action (CTA):** Nút bấm nổi bật nhất. (VD: "Join Waitlist" hoặc "Wishlist on Steam").
    *   **Visual:** Screenshot hoặc GIF gameplay đẹp nhất (hoặc App Mockup).

2.  **Social Proof (Bằng chứng xã hội):**
    *   Logo các báo đã đưa tin (nếu có).
    *   Số người đã đăng ký/chơi thử. (VD: "Join 5,000+ players").

3.  **Features / Benefits (Tính năng & Lợi ích):**
    *   Đừng liệt kê tính năng kỹ thuật. Hãy nói về lợi ích.
    *   *Bad:* "Hệ thống inventory 50 slot".
    *   *Good:* "Thu thập và chế tạo hàng trăm món đồ mà không lo hết chỗ chứa".
    *   Dùng icon minh họa + text ngắn gọn.

4.  **About the Dev / Team:**
    *   Kể câu chuyện của bạn. Tại sao bạn làm sản phẩm này? (Người dùng thích ủng hộ con người thật hơn là công ty vô hồn).

5.  **Final CTA:** Lặp lại nút bấm một lần nữa ở cuối trang.

---

## 🎮 Steam Page Validation Guide

Bạn chưa cần game xong mới tạo trang Steam. Hãy tạo sớm để **"Hứng" Wishlist**.

### Checklist trước khi Publish trang "Coming Soon":
1.  **Capsule Image (Ảnh bìa):** Cực kỳ quan trọng. Thuê họa sĩ xịn ($300-$500). Đừng tự vẽ nếu không chuyên.
2.  **Trailer (Gameplay Trailer):**
    *   Giây 0-5: Phải show gameplay ngay lập tức. Không logo, không intro đen thui.
    *   Giây 5-30: Show các cơ chế thú vị nhất.
    *   Nhạc nền phải khớp với hành động.
3.  **Screenshots:** Chọn 5 ảnh đẹp nhất, đa dạng môi trường/tính huống. Tránh ảnh menu/setting.
4.  **Tags:** Gắn đúng 5 tags đầu tiên (chúng định hình genre của game). (VD: Roguelike, Deckbuilder, Strategy, Card Game, Pixel Art).

---

## 🚪 Fake Door Test Tutorial (Hướng dẫn Kỹ thuật)

Đây là cách kiểm chứng ý tưởng tính năng (Feature) mà không tốn công code backend.

### Bước 1: Thiết kế UI
*   Thêm nút bấm cho tính năng mới (VD: Nút "Multiplayer Mode" trong game Single-player).
*   Làm cho nó trông thật và bấm được (Clickable).

### Bước 2: Tracking
*   Gắn sự kiện (Event tracking) vào nút đó. (Dùng Google Analytics, Firebase, Unity Analytics).
*   Đếm số lượt bấm (Clicks) trên tổng số người dùng thấy nút (Impressions).

### Bước 3: Thông báo (The "Oops" Message)
*   Khi user bấm vào, hiện popup:
    *   *"Tính năng Multiplayer đang được phát triển! Bạn có muốn là người đầu tiên chơi thử khi nó ra mắt không?"*
    *   Kèm ô nhập Email hoặc nút "Yes, notify me".

### Bước 4: Phân tích
*   Nếu **Click Rate > 20%**: Nhu cầu rất cao -> Nên ưu tiên làm ngay.
*   Nếu **Click Rate < 5%**: Ít người quan tâm -> Bỏ qua hoặc làm sau.

### Fake door vs Landing vs Smoke/Concierge (effort vs signal)
| Phương án | Effort | Signal strength | Khi dùng |
| --- | --- | --- | --- |
| **Fake door** (nút/CTA trong sản phẩm) | Thấp | Trung bình (intent click) | Test tính năng mới với user hiện tại |
| **Landing page** (waitlist/lead) | Thấp-vừa | Trung bình (email/lead) | Test định vị/USP, thu lead rẻ | 
| **Smoke test** (quảng cáo + flow mua/đặt lịch, manual fulfill) | Vừa | Cao (willingness to pay / book) | Trước khi build sản phẩm, đo sẵn sàng trả |
| **Concierge test** (người thật làm dịch vụ) | Cao | Rất cao (retention/pay) | Bắt đầu dịch vụ thủ công để học quy trình/đau thực |

**Smoke test**: chạy ads/traffic vào flow thanh toán/đặt lịch (có thể thu tiền hoặc đặt cọc nhỏ); nếu chưa build, hoàn tiền và xin phỏng vấn. Đo CTR→signup→checkout/booking.

**Concierge test**: bạn (hoặc team) làm thủ công như sản phẩm/dịch vụ hứa hẹn. Dùng khi cần chứng minh outcome và hiểu chi tiết quy trình trước khi tự động hóa. Đo: willingness to pay thực, thời gian/chi phí serve, churn sau 1-2 tuần.

---

## 🧪 MVP vs SLC

### 3. MVP vs SLC
*   **MVP (Minimum Viable Product):** Sản phẩm tối thiểu có thể dùng được. Thường bị hiểu nhầm là làm ra sản phẩm lỗi/thiếu.
*   **SLC (Simple, Lovable, Complete):**
    *   **Simple:** Đơn giản, ít tính năng.
    *   **Lovable:** Giao diện đẹp, trải nghiệm mượt mà.
    *   **Complete:** Hoàn thiện trọn vẹn một luồng trải nghiệm (không phải bản nháp).
    *   *Lời khuyên:* Hãy hướng tới SLC thay vì MVP cẩu thả.

## Steam Playtest (cho Game Dev)
*   Steam cho phép mở tính năng Playtest.
*   Mời cộng đồng vào chơi thử bản Alpha/Beta.
*   Thu thập feedback trực tiếp và wishlist từ sớm.
