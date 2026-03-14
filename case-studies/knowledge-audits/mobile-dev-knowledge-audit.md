# 📱 Mobile App Development Knowledge Audit: Thử thách "SuperApp Evolution"

> **Mục đích:** Đo lường năng lực thiết kế, phát triển và tối ưu hóa ứng dụng di động toàn diện, từ kỹ thuật Cross-platform đến trải nghiệm người dùng (UX) và chiến lược kinh doanh.
> **Phiếu trả lời:** [Tải mẫu tại đây](../answer-templates/mobile-answer-template.md)
> 
> **Kịch bản:** Bạn là **Mobile Tech Lead** của "EcoRide" - một ứng dụng đa dịch vụ (SuperApp) bao gồm gọi xe, giao đồ ăn và ví điện tử. Ứng dụng đang phục vụ 500.000 người dùng hàng ngày và chuẩn bị mở rộng ra thị trường Đông Nam Á.

---

## 🛠️ Thử thách 1: Technical Depth & State Management (Chiều sâu kỹ thuật)
*Đo lường năng lực xử lý luồng dữ liệu phức tạp và hiệu năng app.*

**Tình huống:** Người dùng phản nàn rằng khi đang đặt xe, nếu họ chuyển sang xem menu đồ ăn, trạng thái chuyến xe cũ bị mất hoặc app bị giật lag (jank) khi danh sách món ăn có hàng trăm item.

**Câu hỏi:**
1.  Bạn sẽ chọn giải pháp **State Management** nào để quản lý trạng thái phức tạp và chia sẻ dữ liệu giữa các module (gọi xe, giao đồ ăn) mà không làm app trở nên khó bảo trì? (Ví dụ: **BLoC**, **Riverpod** cho Flutter; hay **Redux**, **Zustand** cho React Native?) Tại sao?
2.  Làm thế nào để tối ưu hóa hiệu năng render cho danh sách cực lớn (Infinite List) mà vẫn đảm bảo mượt mà (60/120 FPS)? Giải thích cơ chế **View Recycling** hoặc **Lazy Loading** trong framework bạn chọn.

**Thước đo:**
*   **🟢 Beginner:** Biết dùng `setState` hoặc `useState` cơ bản cho từng màn hình riêng lẻ.
*   **🔴 Expert:** Thiết kế được kiến trúc **Multi-module State**, giải thích được cách tối ưu **Rebuild/Re-render** và xử lý **Memory Leak** khi chuyển đổi giữa các tác vụ nặng.

---

## 🎨 Thử thách 2: UX & Design System (Trải nghiệm & Thiết kế)
*Đo lường tư duy về giao diện và sự đồng nhất trên mọi thiết bị.*

**Tình huống:** EcoRide cần hỗ trợ cả Dark Mode và giao diện tùy chỉnh theo từng quốc gia (Localization). Ngoài ra, app phải chạy tốt trên cả điện thoại giá rẻ và máy tính bảng (Tablet).

**Câu hỏi:**
1.  Bạn sẽ thiết kế **Design System** và hệ thống **Theming** như thế nào để việc thay đổi màu sắc, font chữ toàn app diễn ra trong 1 phút?
2.  Làm thế nào để xử lý **Responsive Layout** cho các thiết bị có tỉ lệ màn hình khác nhau (ví dụ: màn hình gập - Foldables, màn hình có "tai thỏ" - Notch)?

**Thước đo:**
*   **🟢 Beginner:** Fix cứng kích thước (hardcoded values) và tạo các bản copy giao diện cho từng ngôn ngữ.
*   **🔴 Expert:** Sử dụng **Design Tokens**, thành thạo **Flexbox/Layout Builder**, và áp dụng kỹ thuật **Adaptive UI** để thay đổi cấu trúc giao diện tùy theo kích thước màn hình (Screen size breakpoint).

---

## 📡 Thử thách 3: Advanced Features & Offline-first (Tính năng nâng cao)
*Đo lường năng lực xử lý phần cứng và kết nối mạng chập chờn.*

**Tình huống:** Tài xế EcoRide thường xuyên phải di chuyển vào vùng sóng yếu (hầm chung cư, vùng sâu). Họ cần xem được bản đồ và nhận chuyến ngay cả khi mất mạng tạm thời.

**Câu hỏi:**
1.  Bạn sẽ thiết kế cơ chế **Offline-first** như thế nào? Bạn chọn lưu trữ dữ liệu tại chỗ bằng **SQLite**, **Room**, hay **Hive**? Làm thế nào để đồng bộ hóa dữ liệu (Sync) khi có mạng trở lại mà không gây xung đột?
2.  Làm thế nào để tối ưu hóa việc sử dụng **GPS (Location Services)** và **Background Tasks** để theo dõi tài xế mà không làm cạn kiệt pin điện thoại của họ?

**Thước đo:**
*   **🟢 Beginner:** Chỉ hiện thông báo "Mất kết nối mạng" và yêu cầu người dùng thử lại.
*   **🔴 Expert:** Thiết kế được luồng **Optimistic UI** (cập nhật giao diện trước khi server phản hồi), làm chủ kỹ thuật **Background Fetch** và **Local Caching Strategy**.

---

## 📈 Thử thách 4: Monetization & Growth (Kinh doanh & Phát hành)
*Đo lường năng lực biến app thành cỗ máy kiếm tiền và thu hút user.*

**Tình huống:** CEO muốn tích hợp gói thành viên cao cấp (Subscription) để người dùng được miễn phí ship. Đồng thời, bạn cần tối ưu hóa app để tăng thứ hạng trên Store (ASO).

**Câu hỏi:**
1.  Làm thế nào để tích hợp hệ thống **In-App Purchase (IAP)** trên cả App Store và Play Store một cách an toàn? Bạn sẽ xử lý vấn đề **Server-side Validation** (xác thực hóa đơn) như thế nào?
2.  Những yếu tố nào trong code và metadata ảnh hưởng lớn nhất đến **ASO (App Store Optimization)**? Làm thế nào để giảm **App Size** (dung lượng tải về) để tăng tỉ lệ chuyển đổi cài đặt?

**Thước đo:**
*   **🟢 Beginner:** Chỉ biết gắn thư viện IAP và mong nó chạy đúng.
*   **🔴 Expert:** Hiểu rõ quy trình **Store Guidelines** (để tránh bị reject), biết cách dùng **Dynamic Assets** (On-demand resources) để giảm dung lượng, và sử dụng **Deep Linking** để tối ưu hóa luồng marketing.

---

## 🧠 Thử thách 5: Engineering Excellence & CI/CD (Chất lượng kỹ thuật)
*Đo lường năng lực bảo trì và vận hành hệ thống app quy mô lớn.*

**Tình huống:** Mỗi lần ra phiên bản mới, team Mobile mất 2 ngày để build thủ công và test trên 20 loại máy khác nhau. Thỉnh thoảng app vẫn bị crash ngay sau khi cập nhật.

**Câu hỏi:**
1.  Bạn sẽ thiết lập luồng **CI/CD** như thế nào cho Mobile? (Sử dụng công cụ như **Fastlane**, **GitHub Actions**, hay **Bitrise**).
2.  Làm thế nào để triển khai tính năng mới cho 5% người dùng trước khi tung ra 100% (Canary Release/Feature Flags)? Bạn sử dụng công cụ gì để giám sát lỗi thời gian thực (**Crashlytics**)?

**Thước đo:**
*   **🟢 Beginner:** Build file `.apk/.ipa` trên máy cá nhân và gửi qua Zalo/Telegram để test.
*   **🔴 Expert:** Tự động hóa hoàn toàn từ **Unit Test**, **UI Test** đến **Auto-submit Store**. Thành thạo kỹ thuật **Remote Config** để điều chỉnh tính năng mà không cần user cập nhật app.

---

## 📊 Bảng tự chấm điểm (Scoring Rubric)

| Lĩnh vực | Thang điểm (1-10) | Gợi ý tự vấn |
| :--- | :---: | :--- |
| **Tech & Performance** | ____ / 10 | Bạn có thể xử lý mượt mà app 100 màn hình với data phức tạp không? |
| **UX & Design System** | ____ / 10 | Giao diện của bạn có "chuẩn chỉnh" trên cả iPhone 15 Pro Max và máy Android cỏ không? |
| **Offline & Hardware** | ____ / 10 | App của bạn có hoạt động thông minh khi không có mạng không? |
| **Business & ASO** | ____ / 10 | Bạn có biết cách đưa app lên Top Store và kiếm được tiền từ nó không? |
| **Ops & CI/CD** | ____ / 10 | Bạn quản lý app bằng quy trình tự động hay bằng "sức người"? |

### 🏆 Xếp hạng năng lực Mobile Dev:
*   **0 - 15 điểm:** **Junior App Developer**. Cần học chắc kiến thức nền tảng trong `domains/mobile-dev/`.
*   **16 - 30 điểm:** **Mid-level Developer**. Có khả năng build app hoàn chỉnh nhưng chưa tối ưu về quy trình và hiệu năng.
*   **31 - 45 điểm:** **Mobile Tech Lead**. Khả năng thiết kế kiến trúc SuperApp và dẫn dắt team sản xuất tốt.
*   **46 - 50 điểm:** **Mobile Architect / Product Founder**. Bạn có thể kiến tạo những sản phẩm di động đẳng cấp thế giới.

---

## 🔑 Answer Key: Góc nhìn Chuyên gia (Expert Guidelines)

### Thử thách 1: Tech & Performance
*   **State Management:** Ưu tiên mô hình **Unidirectional Data Flow** (như BLoC hoặc Redux). Tách biệt logic business ra khỏi UI module.
*   **Tối ưu List:** Dùng **ListView.builder** (Flutter) hoặc **FlatList** (React Native) để chỉ render những gì hiện trên màn hình. Tránh các tác vụ nặng (nén ảnh, parse JSON lớn) trên **Main Thread/UI Thread**.

### Thử thách 2: UX & Design System
*   **Responsive:** Dùng tỉ lệ phần trăm hoặc các đơn vị tương đối (logical pixels). Luôn test trên các thiết bị có mật độ điểm ảnh (DPI) khác nhau.
*   **Theming:** Sử dụng **InheritedWidget** (Flutter) hoặc **Context API** (React) để cung cấp Theme cho toàn bộ cây thư mục app.

### Thử thách 3: Offline-first
*   **Sync:** Sử dụng mô hình **Local-first**. Lưu mọi thao tác vào Local DB trước, sau đó dùng một background worker để đồng bộ với server bằng cơ chế **Idempotency Key** để tránh trùng lặp dữ liệu.

### Thử thách 4: Business & ASO
*   **ASO:** Tập trung vào **Keywords**, **Screenshots** sinh động và **Rating/Review**. App size càng nhỏ (dưới 20MB cho app cơ bản) thì tỉ lệ cài đặt càng cao.
*   **IAP Validation:** Luôn thực hiện verify hóa đơn trên Server (Backend) để tránh user hack mua hàng bằng các công cụ can thiệp local.

### Thử thách 5: Ops & CI/CD
*   **Fastlane:** Là công cụ bắt buộc để tự động hóa việc chụp ảnh màn hình, quản lý certificates và submit lên Store.
*   **Feature Flags:** Dùng **Firebase Remote Config** để bật/tắt tính năng theo từng nhóm user (A/B Testing).

---

## 🚀 Tài liệu bổ trợ để "Level Up"
*   **Lộ trình toàn diện:** [Mobile App Roadmap](../../domains/mobile-dev/README.md)
*   **Kỹ năng thiết kế:** [Refactoring UI](https://www.refactoringui.com/)
*   **Vận hành App:** [Fastlane Documentation](https://fastlane.tools/)
*   **Tư duy sản phẩm:** [Indie Hacker Guide](../../guides/03-career-skills/game-dev/game-indie-hacker-guide.md) (Có thể áp dụng cho Mobile App)
