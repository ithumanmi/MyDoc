# 🚨 Disaster/Crisis Response Protocol: Kịch Bản 24H Sinh Tử

> [← Back to Advanced Legal](./README.md) | [Home](../../../README.md)

Lý thuyết chỉ có tác dụng vào những ngày nắng đẹp. Khi cơn bão ập tới (bị kiện tụng, tiền bị giam, thanh tra đến gõ cửa), 24 giờ đầu tiên quyết định bạn sẽ an toàn thoát hiểm hay tự tay đào mồ chôn mình vì hoảng loạn.

Đây là giao thức phản ứng nhanh (Emergency Protocol) bạn cần thiết lập.

---

## 1. Khủng Hoảng 1: Nhận Yêu Cầu Gỡ Bỏ Bản Quyền (DMCA Takedown / C&D Letter)

Bạn thức dậy và thấy App của mình bị gỡ khỏi App Store, hoặc Hosting Provider (AWS/DigitalOcean) tạm khóa chốt server vì nhận được đơn kiện DMCA (Digital Millennium Copyright Act), hoặc nhận được thư Cease & Desist (Yêu Cầu Chấm Dứt Hành Vi) từ lầu xanh của luật sư đối thủ.

### 🔴 LỖI CHẾT NGƯỜI (Đừng làm):
*   Sợ hãi và reply/nhắn tin xin lỗi ngay lập tức (Lời xin lỗi có thể được dùng làm bằng chứng Tự Nhận Tội trước tòa).
*   Tức giận và lên mạng xã hội bóc phốt, văng tục với đối thủ (Tạo thêm án "Bôi nhọ danh dự").
*   Tự ý xóa sạch evidence (bằng chứng/database) để phi tang.

### 🟢 GIAO THỨC PHẢN ỨNG 24H:
1.  **Dừng máu chảy:** Nếu hệ thống SaaS bị khóa, dựng tạm một trang "Under Maintenance" (Bảo trì) không đổ lỗi cho ai đưa lên.
2.  **Lock down (Phong tỏa bằng chứng):** Backup toàn bộ Source code version đó, lưu trữ Log email, tin nhắn, hợp đồng thuê dev vào một thư mục Zip mã hóa. Không chỉnh sửa bất cứ thứ gì trong source cũ. 
3.  **Thẩm định Mối đe dọa:** Đọc kỹ bức thư. Họ kiện vì Logo giống? Tính năng giống? Hay lấy trộm code? Rất nhiều thư C&D là do các "Patent Trolls" (Công ty săn bản quyền) vòi vĩnh tiền, không có cơ sở thực tế.
4.  **Counter-Notice (Kháng cáo DMCA):** Nếu bạn bị kiện láo, bạn có quyền gửi "Counter-Notice" cho Apple/Google. Theo luật Mỹ, nếu bên kiện không nộp đơn lên Tòa Án Liên Bang trong 10-14 ngày, App/Host của bạn BẮT BUỘC phải được mở lại.
5.  **Thuê hỏa lực:** Đây là lúc chi 5 triệu VND đặt lịch 1 giờ với Luật sư chuyên Sở hữu trí tuệ (IP Lawyer) để họ soạn thư trả lời bằng "Ngôn ngữ luật", vả lại tính pháp lý của The Cease & Desist Letter kia.

---

## 2. Khủng Hoảng 2: Client Nước Ngoài Bùng Tiền / Vi Phạm Hợp Đồng

Bạn đã code xong hệ thống, bàn giao source. Client (US/EU) ghosting (biến mất), không trả 15.000 USD còn lại. Tranh chấp xuyên biên giới.

### 🔴 LỖI CHẾT NGƯỜI:
*   Đăng source code độc quyền của họ lên mâm Open Source (Github public) như một sự trả đũa. Bạn bị kiện ngược vì phá hoại bí mật kinh doanh.
*   Hack lại vào server của họ để gài mã độc hoặc xóa file. Phạm tội hình sự "Tội phạm mạng" có thể bị Interpol truy nã!

### 🟢 GIAO THỨC PHẢN ỨNG 48H:
1.  **Stop Work Order (Dừng thi công):** Dừng toàn bộ hỗ trợ server, revoke (thu hồi) các loại API keys, SSH keys thuộc quyền quản lý của bạn (Những thứ thuộc tài nguyên hợp pháp do bạn cung cấp).
2.  **Gửi The "Demand Letter" (Thư yêu cầu thanh toán cứng rắn):** Gửi một email lịch sự nhưng lạnh lùng, trích dẫn rõ Khoản/Điều vi phạm trong Hợp đồng Dịch Vụ, tạo Deadline thanh toán cuối cùng (thường là 7 ngày).
3.  **Gài chế độ tự hủy pháp lý (Poison Pill):** Nếu bạn trong giới hạn quyền hạn giữ Source chưa bàn giao final (Giai đoạn Staging), hãy treo tiến trình lại. 
4.  **Truy vết Quốc tế (Escalation):** Mất 15.000 USD là số tiền lớn. Bạn không thể kiện dân sự từ VN sang Mỹ vì án phí đắt hơn số tiền. Thay vào đó: Mở hồ sơ tranh chấp trên các nền tảng Escrow nếu có (Upwork/Fiverr). Hoặc tìm kiếm (Hire) một cơ quan Thu hồi nợ quốc tế (International Debt Collection Agency) - Họ sẽ lấy 30% số tiền nếu thu được, chứ bạn không mất đồng nào. Cơ quan này sẽ phá nát tín dụng (Credit Score) của công ty Mỹ kia, khiến họ sợ chết khiếp.

---

## 3. Khủng Hoảng 3: Cục Thuế Gửi Thông Báo Mời Lên Giải Trình

Bưu điện gửi một tờ giấy: "Mời ông/bà lên Chi cục thuế... để giải trình về dòng tiền thu nhập từ nước ngoài (Google/YouTube/Upwork)".

### 🔴 LỖI CHẾT NGƯỜI:
*   Trốn giấy triệu tập. (Hành vi cực tồi tệ, thuế sẽ lập tức khóa mã số thuế hoặc đóng băng TK ngân hàng của bạn).
*   Đến cơ quan thuế và "Tự thú" khóc lóc khai ra tất cả mọi thu nhập nhỏ giọt từ 5 năm trước chưa bị phát hiện để mong xin tha. Họ sẽ phạt bạn đến đồng cuối cùng dựa trên các lời khai hớ hênh.

### 🟢 GIAO THỨC PHẢN ỨNG DẬP LỬA:
1.  **Duy trì bình tĩnh, thái độ hợp tác:** Cán bộ thuế luôn dùng "nguyên tắc suy đoán" lớn hơn thực tế để dọa. Nhưng thái độ của bạn phải luôn là công dân tốt, chỉ thiếu sót do chưa hiểu thủ tục hành chính thay vì "Cố ý trốn thuế".
2.  **Nguyên tắc "Hỏi gì đáp nấy - Không cung cấp thừa":** Đọc kỹ thư thông báo yêu cầu giải trình cho NĂM nào? TÀI KHOẢN nào? NGUỒN nào? Chỉ in sao kê tài khoản chính xác nội dung họ yêu cầu. Không in nguyên sổ cái ngân hàng của tất cả ví điện tử khác dâng lên. Thuế hỏi món nào, lấy file chứng từ (Invoice/Hợp đồng) đối chiếu món đó.
3.  **Truy tìm lá chắn giảm trừ:** Báo ngay với Chuyên gia Thuế (Tax Consultant ở VN - Phí tầm vài triệu) trước ngày hầu tra. Trong luật thuế VN, tùy bản chất dòng tiền (Từ Google Adsense sẽ bị tính dạng Bản quyền 7%; Từ làm công ăn lương sẽ bị tínhy Thuế lũy tiến tới 35%). Consultant sẽ giúp bạn "Khung" (Frame) lại dòng máu đổ về kia thuộc mã Tên loại hình nào ít bị đóng phạt nhất một cách Hợp Pháp. Xin cán bộ hướng dẫn cách lập Hộ kinh doanh cho tương lai.

> **Quy Tắc Vàng:** "Trong mọi khủng hoảng pháp luật – Phản hồi (Respond) lại sự việc sau khi tham vấn kỹ lưỡng, chứ đừng Phản ứng (React) do sợ hãi hay phẫn nộ kích động."
