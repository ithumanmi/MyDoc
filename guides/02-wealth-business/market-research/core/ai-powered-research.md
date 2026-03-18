# ⚡ AI-Powered Market Intelligence: Automate Your Research

> [← Back to Core Methods](./README.md) | [Home](../../../README.md)

Cách nghiên cứu thị trường cũ: Mở 20 tab Google, đọc tay 500 bài báo, đọc mắt 1.000 cái reviews G2, copy-paste mỏi tay ra Notion.
Cách nghiên cứu năm 2026: Trải phẳng Data cho AI tự đọc và nhả Insights. Bạn chỉ là người ra lệnh (Prompting).

Đây là cẩm nang để một người Research đạt năng suất của một đạo quân 10 người.

---

## 1. Review Mining (Đào Vàng Từ Tiếng Chửi Của Khách Khàng)

Đối thủ của bạn có 5.000 lượt rating trên App Store, Google Play hoặc G2. Khách hàng đang chửi họ cái gì? Khách hàng khen họ cái gì? Chỗ khách hàng chửi chính là Feature (Tính năng) số 1 bạn cần build cho App của mình.

### Giao thức tự động hóa (Automated Protocol):

**Bước 1: Cào dữ liệu (Scraping)**
*   Dùng **[Apify](https://apify.com)**. Đây là thiên đường của các "Actors" (Tools cào liệu đã code sẵn).
*   Tìm công cụ: `Google Play Reviews Scraper` hoặc `G2 Reviews Scraper`.
*   Nhập URL App của đối thủ vào. Đặt lệnh cào: "Chỉ lấy Review 1 sao, 2 sao và 3 sao trong 6 tháng gần nhất".
*   Xuất (Export) kết quả ra file `.CSV` (Bảng tính). Bạn sẽ có khoảng 2.000 dòng text toàn là sự phẫn nộ của User.

**Bước 2: Phân tích bằng LLM (ChatGPT Advanced Data Analysis / Claude UI)**
*   Upload luôn file `.CSV` đó lên chatbox của ChatGPT-4o hoặc Claude 3.5 Sonnet.
*   **Prompt Thần Thánh:**
    > "Đây là 2000 reviews thấp sao của App [Tên đối thủ]. Đóng vai một Chuyên gia Phân Tích Hành Vi Khách Hàng (User Researcher). Hãy đọc file này và trích xuất cho tôi:
    > 1. Top 5 Bug (lỗi kỹ thuật) khiến user bực mình nhất, dán nhãn tần suất (%).
    > 2. Top 3 Feature (Tính năng) mà user gào thét đòi hỏi nhưng App này không có.
    > 3. Mô tả Chân dung (Persona) của những người để lại review tức giận nhất này (Họ dùng app vào mục đích gì mà bị lỗi?).
    > Trình bày dưới dạng Table Markdown dễ hiểu."

**Kết quả:** Bạn có bản vẽ Product Roadmap của đối thủ trị giá hàng chục ngàn đô la chỉ với giá API 0.5$.

---

## 2. Market Reports Trong 5 Phút Với Perplexity Pro

Google Search truyền thống đang chết dần bởi SEO Spam. Bạn gõ "Thị trường phần mềm nha khoa 2026", Google sẽ trả về 10 bài viết rác từ các trang bán Khóa Học.

### Thay vì Google, hãy xài Perplexity Pro:
Perplexity không phải là Chatbot, nó là **Answer Engine (Động cơ trả lời)**. Nó tìm kiếm real-time 20 website chất lượng nhất, tổng hợp lại và CÓ TRÍCH DẪN (Citation).

*   **Prompt Bóc Tách Ngành:**
    > "Tôi đang định build một SaaS B2B cho thị trường [Phần mềm Quản lý Phòng Khám Nha Khoa] tại Mỹ. Hãy tổng hợp cho tôi:
    > 1. Market Size (TAM, SAM, SOM) của ngạch này hiện tại.
    > 2. Kể tên 3 gã khổng lồ (Incumbents) đang thống trị.
    > 3. Phân tích 3 xu hướng công nghệ mới (Ví dụ: Tích hợp AI chuẩn đoán X-Quang) đang diễn ra.
    > Bắt buộc phải gắn kèm source link của các trang báo cáo uy tín (McKinsey, Gartner, Forbes) cho từng luận điểm."

Bạn vừa làm xong công việc của một Business Analyst (BA) mất 3 ngày cày báo cáo.

---

## 3. Quét Tệp Khách Hàng (Lead Generation) Tự Động Bằng Apollo + AI

Đừng Research thị trường rồi để đó. Bạn phải "Test nước" (Validation) bằng cách gửi email cho người thật hỏi mua.

1.  **Chốt ICP (Lý lịch khách hàng):** "HR Manager tại các công ty IT < 50 người, ở UK".
2.  Dùng **[Apollo.io](https://apollo.io)**. Set Filter đúng Y chang cái chân dung đó. Quét ra 2,000 người.
3.  Tải 2,000 người đó về file CSV.
4.  Quăng file CSV đó vào AI. Kêu AI tạo ra Dòng Tiêu Đề (Subject Line) cá nhân hóa cho từng người một dựa trên Company Name và Bio của họ.
5.  Load lại vào [Instantly.ai](https://instantly.ai) -> Bấm Gửi Tự Động.

> **Cảnh Giới Tối Thượng:** Sự khác biệt của một Hacker và một Học giả là, Học giả có biểu đồ PDF cực đẹp, còn Hacker có 5 cuộc gọi Zoom Demo (Hẹn qua Cold Email) với Khách hàng thực sự đút tiền vào thẻ tín dụng. AI giúp bạn đốt cháy giai đoạn tạo ra cái Biểu Đồ PDF đó đi.
