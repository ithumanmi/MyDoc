# 🕷️ Cào Dữ Liệu Tự Động: Tước Đoạt Nguồn Sống B2B

> [← Back to Apps & SaaS](./README.md) | [Home](../../../README.md)

Trong thị trường B2G (Business-to-Business) hoặc làm SaaS nhắm tới đối tượng công ty, Khách hàng tiềm năng (Leads) của bạn - bao gồm Email, Số điện thoại, Chức vụ chức danh - không nằm trong cái hố bí mật nào cả. **Chúng phơi mình trên LinkedIn, trên hệ thống Capterra, và trên G2.**

Tội ác lớn nhất của Researcher là ngâm mình cả ngày để copy-paste bằng tay. Đây là hệ quy trình tự động hóa (Data Scraping) giúp bạn cào 10.000 tệp khách hàng chỉ bằng 1 cái click chuột, và phân tích rã rời đối thủ.

---

## 1. LinkedIn Sales Navigator + X-Ray: Săn Chức Danh

Sếp bảo: *"Tôi cần thông tin của 500 ông Giám Đốc Nhân Sự (HR Manager) ở các ngành Sản xuất tại Châu Âu để bán SaaS Chấm Công của mình"*.

### ⚒️ Phantombuster (Con Quỷ Bóng Đêm)
1.  **Chuẩn bị mồi:** Lật ví, mua một tài khoản **LinkedIn Sales Navigator** (Khoảng 1-2 triệu VND/tháng). Đây là Radar xịn nhất thế giới.
2.  **Khoanh vùng:** Bật Filter trên Sales Nav: `Chức danh: HR Manager` + `Ngành: Manufacturing` + `Khu vực: EU` + `Size cty: 50-200`. Search. Nó trả ra 10.000 results.
3.  **Triệu hồi Ác Quỷ Phantombuster / Apify:**
    *   Sử dụng Phantom có tên `LinkedIn Search Export`. Cắp cái Link Result ở bước 2 vào tool.
    *   Bấm Run. (Lưu ý: Chỉnh delay an toàn để LinkedIn không khóa mỏ tài khoản của bạn. Vd: Cào 150 người mỗi ngày).
4.  **Trích xuất máu (Email & Số Điện Thoại):** Tool sẽ móc toàn bộ Tên, Link Profile, Công ty vào 1 file Excel. Tiếp tục cắp file Excel đó qua tool `LinkedIn Profile Scraper` kết hợp gắn module `Kaspr` hoặc `Apollo.io` Enrichment. Lúc này, API sẽ luồn vào các lỗ hổng của Internet, móc bằng được **Email đi làm thật sự (work email)** của những Giám Đốc nhân sự đó dán vào file của bạn. Dữ liệu thành phẩm.

---

## 2. Lách Captcha & Lũng Đoạn Bảng Xếp Hạng G2/Capterra

Nếu bạn build 1 phần mềm cạnh tranh trực tiếp (Ví dụ: Định làm phần mềm Chatbot CSKH y như Intercom nhưng rẻ hơn). Bạn cần Cào Data trên G2.com hoặc Capterra.

G2 được mã khóa như pháo đài. Nếu bạn tự viết Python (BeautifulSoup) gỡ, nó bắn reCAPTCHA khóa IP bạn sau đúng 5 phát quét.

### 🟢 Giao Thức Lách Luật (Apify Cloud):
1.  **Vứt server cùi của bạn đi:** Nhảy lên **[Apify](https://apify.com)**. Đây là cỗ máy Cloud Scraping đỉnh cao nhất Châu Âu với dàn Proxies Chống-Bot cực mạnh. Rất khó chặn.
2.  **Tìm Actor xịn:** Search trong Store của Apify từ khóa: `Capterra Scraper` hoặc `G2 Review Scraper`. Các Pháp Sư Ấn Độ đã code sẵn bộ giải Captcha cho nó rồi.
3.  **Tác vụ 1: Cạo Tên Cty Bỏ Rơi:** Bạn dùng Tool Apify quét qua trang đối thủ Intercom. Trích Review 1 và 2 sao đổ lại. Dữ liệu quý nhất nằm ở dòng "Công ty của người review". Đấy! Cái Công Ty X vừa chửi Intercom "Quá Đắt". Bạn mang Tên Công Ty X đó quay lại bước 1 ở trên (Target trên LinkedIn), tìm ra ông CTO, và gửi cho ông 1 cái Email Offer App Của bạn rẻ bằng 1/10. Tỷ Suất Trúng Hợp Đồng Đảm Bảo Lớn Hơn Đi Rải Mail Mù!

---

## 3. BuiltWith & Dữ Liệu Tech-Stack Lộ Thiên

Bạn build 1 App (Plugin) bán lẻ riêng cho các Shop dùng nền tảng Shopify.
Khách hàng của bạn không ở LinkedIn. Khách hàng của bạn là TẤT CẢ NHỮNG CÁI ĐUÔI DOMAIN đang cắm hệ sinh thái Shopify.

### 🔍 Quét Radar Diện Rộng (Ngành Tàu Thủy):
1.  Truy cập **[BuiltWith.com](https://builtwith.com)** hoặc Wappalyzer. (Tool này tự chui qua Source Code của 5 tỷ website trên mạng hàng tuần để coi nó dùng cái Lõi phần mềm gì).
2.  Mua 1 tháng Pro ($395 - Siêu chát nếu không hack), tạo Filter: *"Lọc cho tôi toàn bộ các Website Có Cài Shopify + Có Cài Plugin Đánh Giá AliReviews + Đặt trụ sở tại Mỹ"*.
3.  **Ra Kết Quả:** BuiltWith trả lại cho bạn 1 file `.CSV` gồm 5.000 tên miền Website y chang chân dung đó, kèm Thông Tin Công Ty Quản Lý và Danh Bạ Email Khách Hàng. Việc còn lại của bạn là bật Tool Auto-Email lên bắn chiến dịch Chào Hàng. Đơn rớt như mưa!

> **Tâm Pháp:** "Researcher bình thường thấy số liệu trên Web Browser (Màn hình). Researcher Hacker thấy Source Link của Màn Hình Nằm Sau Cloud Server. Dùng Tools (Apify/Phantom) làm Cây Xà Beo bẩy cửa, lấy thứ mình cần lúc rạng sáng."
