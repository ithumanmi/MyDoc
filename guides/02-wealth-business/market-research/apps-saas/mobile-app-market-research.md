# 📱 Mobile App Market Research (Non-Game Focus)

> [← Back to Market Research](./README.md)

Hướng dẫn nghiên cứu thị trường dành riêng cho các ứng dụng di động (Utilities, Productivity, Social, Health, Education...).

---

## 1. ASO Intelligence (App Store Optimization)

Khác với Game (thường dựa vào viral/ads), App sống nhờ **Search Traffic**.

### Keyword Research
*   **Mục tiêu:** Tìm từ khóa có lượng tìm kiếm (Volume) cao nhưng độ cạnh tranh (Difficulty) thấp.
*   **Công cụ:**
    *   **MobileAction / AppTweak:** (Dùng thử Free trial).
    *   **Sensor Tower:** Xem Top Keywords của đối thủ.
*   **Chiến lược:**
    *   Đừng cố rank từ khóa chung chung như "Fitness" hay "Photo Editor".
    *   Hãy nhắm vào **Long-tail Keywords**: "Home workout for men without equipment", "Vintage film photo editor".

### Category Analysis
*   **Utilities (Tiện ích):** Users tìm kiếm giải pháp cho một vấn đề cụ thể (VD: QR Code Scanner, PDF Converter).
    *   *Key Metric:* Retention Rate (Họ có quay lại dùng lần sau không?)
*   **Social (Mạng xã hội):** Users tìm kết nối.
    *   *Key Metric:* Viral Coefficient (K-factor) - 1 user mời được bao nhiêu user mới?

---

## 2. UI/UX Research (Nghiên cứu Giao diện & Trải nghiệm)

Trong thế giới Mobile App, **UX kém = Uninstall ngay lập tức**.

### Sử dụng Mobbin (hoặc các thư viện UI)
*   **Website:** [mobbin.com](https://mobbin.com/) (Thư viện UI lớn nhất).
*   **Cách nghiên cứu:**
    *   **Onboarding Flow:** Xem cách các app lớn (Duolingo, Headspace) dẫn dắt người dùng mới. Họ hỏi gì? Họ xin quyền (Permission) lúc nào?
    *   **Paywall Screens:** Màn hình chào mời trả tiền được thiết kế ra sao? (Nút tắt ở đâu? Lợi ích được highlight thế nào?)
    *   **Empty States:** Khi chưa có dữ liệu, màn hình trông như thế nào để không bị trống trải?

### Tự trải nghiệm (Dogfooding)
*   Tải 5 app top đầu trong ngách của bạn.
*   Chụp màn hình (Screenshot) lại toàn bộ flow từ lúc mở app đến lúc thực hiện xong chức năng chính.
*   Dán vào Figma/Miro để so sánh.

---

## 3. Review Mining (Đào sâu đánh giá)

Đọc review trên App Store/Google Play là cách nhanh nhất để tìm **Feature Gap**.

### Phương pháp
1.  Lọc review **2-4 sao** (Review 1 sao thường là chửi bới vô lý, 5 sao thường là khen xã giao). Review trung bình chứa nhiều feedback xây dựng nhất.
2.  Tìm các cụm từ: *"I wish it had..."*, *"Why can't I..."*, *"Great app but..."*.
3.  **Ví dụ:**
    *   App Note-taking đối thủ không có tính năng sync iCloud -> Cơ hội của bạn.
    *   App Meditation đối thủ bắt đăng ký mới cho nghe thử -> Cơ hội của bạn: Cho nghe thử miễn phí 1 bài.

---

## 4. Business Model & Monetization

App kiếm tiền khác Game.

### Advanced Monetization Strategy
*   👉 **[Mobile App Monetization Advanced](./mobile-app-monetization-advanced.md):** Chiến lược Hybrid (Ads + IAP + Sub), tối ưu gói Subscription và Offerwall.

### Freemium vs Free Trial
*   **Freemium:** Dùng miễn phí tính năng cơ bản, trả tiền để mở khóa tính năng cao cấp (Premium).
    *   *Phù hợp:* Utilities, Tools.
*   **Subscription (Đăng ký):** Trả phí hàng tháng/năm.
    *   *Phù hợp:* Content apps (Meditation, Education), Productivity.
    *   *Mẹo:* Hầu hết doanh thu đến từ gói **Yearly** (Hàng năm).

### Ad Monetization
*   Chỉ nên dùng cho App đơn giản, users dùng thường xuyên nhưng thời gian ngắn (VD: Calculator, Flashlight - dù giờ ít ai làm mấy cái này).
*   Tránh lạm dụng Interstitial Ads (Quảng cáo che màn hình) gây ức chế.
