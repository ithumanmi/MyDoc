# 🧠 PKM System: Xây Dựng Bộ Não Thứ Hai

> [← Back to Productivity](../README.md) | [CSDL cá nhân (Personal Knowledge Base)](./personal-knowledge-base.md)

## Tại sao bạn cần PKM?
Bộ não con người rất giỏi trong việc **sáng tạo ý tưởng** (Thinking), nhưng lại rất tệ trong việc **lưu trữ thông tin** (Storage).
*   Bạn có bao giờ đọc một cuốn sách hay nhưng 2 tuần sau quên sạch?
*   Bạn có ý tưởng lóe lên lúc đang tắm nhưng sau đó không nhớ nổi?

**Personal Knowledge Management (PKM)** là hệ thống giúp bạn lưu trữ, tổ chức và chuyển hóa thông tin thành kiến thức hữu ích. Mục tiêu là xây dựng một **"Bộ não thứ hai" (Second Brain)** kỹ thuật số.

---

## 1. Phương pháp PARA (Tổ chức thông tin) 🗂️
Được phát triển bởi Tiago Forte, PARA là cách sắp xếp file/note dựa trên **Hành động (Actionability)** thay vì Chủ đề (Topic).

### P - Projects (Dự án)
*   **Định nghĩa:** Những việc đang làm, có mục tiêu cụ thể và **Deadline**.
*   **Ví dụ:** "Viết báo cáo quý 1", "Lên kế hoạch du lịch Nhật Bản", "Học khóa Python cơ bản".
*   *Mức độ ưu tiên:* Cao nhất.

### A - Areas (Lĩnh vực)
*   **Định nghĩa:** Những trách nhiệm dài hạn, **không có Deadline** nhưng cần duy trì tiêu chuẩn.
*   **Ví dụ:** Sức khỏe, Tài chính, Gia đình, Phát triển bản thân.
*   *Mức độ ưu tiên:* Trung bình.

### R - Resources (Tài nguyên)
*   **Định nghĩa:** Những chủ đề bạn **hứng thú**, muốn tìm hiểu thêm hoặc tham khảo sau này.
*   **Ví dụ:** Thiết kế web, Lịch sử nghệ thuật, Công thức nấu ăn, Quotes hay.
*   *Mức độ ưu tiên:* Thấp.

### A - Archives (Lưu trữ)
*   **Định nghĩa:** Những thứ đã hoàn thành (Projects cũ) hoặc không còn quan tâm nữa.
*   **Mục đích:** Giữ cho hệ thống gọn gàng nhưng không mất dữ liệu.

---

## 2. Quy trình CODE (Xử lý thông tin) ⚙️

### C - Capture (Thu thập)
*   Chỉ lưu lại những gì **gây ấn tượng mạnh** (Resonate). Đừng lưu rác.
*   Công cụ: Readwise, Web Clipper, Apple Notes.

### O - Organize (Sắp xếp)
*   Sắp xếp theo **PARA**. Hỏi: "Thông tin này giúp ích cho Dự án nào?" thay vì "Thông tin này thuộc chủ đề nào?".

### D - Distill (Chắt lọc)
*   Tóm tắt ý chính (Progressive Summarization).
*   Biến note dài 10 trang thành 3 gạch đầu dòng cốt lõi (Essence).

### E - Express (Thể hiện)
*   Kiến thức chỉ có giá trị khi được chia sẻ hoặc tạo ra sản phẩm.
*   Dùng kiến thức đã lưu để viết bài, làm video, giải quyết vấn đề.

---

## 3. Zettelkasten (Hộp thẻ ghi chú) 🗃️
Phương pháp của Niklas Luhmann để liên kết các ý tưởng rời rạc.
*   **Fleeting Notes:** Ghi chú nhanh, tạm thời.
*   **Literature Notes:** Ghi chú từ sách/báo (dùng ngôn ngữ của bạn).
*   **Permanent Notes (Atomic Notes):** Mỗi note chỉ chứa **1 ý tưởng duy nhất**, có thể hiểu độc lập.
*   **Linking:** Quan trọng nhất là tạo liên kết (Backlink) giữa các note để tạo ra mạng lưới tri thức.

👉 **[Mẫu thực hành: PARA Dashboard Template](../../../templates/para-dashboard.md)**

---

## 4. Tool Stack Gợi Ý Theo Giai Đoạn 🧰

| Giai đoạn | Mục tiêu chính | Công cụ gợi ý | Ghi chú |
| --- | --- | --- | --- |
| **Capture nhanh** | Ghi chú tức thời, mọi nơi | Apple Notes / Google Keep · Drafts · Notion Mobile | Tập trung tốc độ, đồng bộ đa thiết bị |
| **Highlight & Sync** | Gom highlight sách/web | Readwise · Readwise Reader · Matter | Tự động sync sang Notion/Obsidian |
| **Thinking Workspace** | Viết, link, distill | Notion (PARA/Projects) · Obsidian (Zettelkasten) · Capacities | Chọn 1 công cụ làm “bộ não chính” |
| **Automation** | Bơm dữ liệu giữa app | Zapier · Make · Readwise API | Dùng khi workload > 20 note/tuần |
| **Resources** | Tra cứu thêm tool | [resources/tools.md](../../../resources/tools.md) | Danh sách app cập nhật theo từng nhu cầu |

> **Tip:** Đừng ôm quá nhiều app. Chọn 1 Capture + 1 Workspace chính, còn lại dùng để hỗ trợ. Khi thay công cụ, đảm bảo dữ liệu export được (Markdown/CSV).
