---
title: "Surveillance & Privacy"
description: "Giám sát nhà nước, quyền riêng tư, cân bằng an ninh–tự do."
tags:
  - digital
  - privacy
  - surveillance
updated: 2026-03-17
---

# 👁️ Surveillance & Privacy

## Trục chính
- **Giám sát nhà nước**: thu thập dữ liệu vì an ninh/quản lý; yêu cầu lưu trữ nội địa, cung cấp dữ liệu theo luật.
- **Quyền riêng tư**: quyền được bảo vệ dữ liệu cá nhân, giới hạn mục đích thu thập, đồng ý/thu hồi, quyền truy cập/xóa/sửa.
- **Cân bằng an ninh–tự do**: rủi ro lạm dụng, chilling effect; nhu cầu điều tra tội phạm, khủng bố, bảo vệ hạ tầng trọng yếu.
- **Công nghệ**: nhận diện khuôn mặt, giám sát mạng, phân tích lưu lượng, cảm biến IoT; nguy cơ phân biệt đối xử/false positive.
- **Chuẩn & luật quốc tế**: GDPR (EU), các luật bảo vệ dữ liệu đang nổi ở châu Á; công ước/khuyến nghị về quyền con người số.

## Hàm ý chính sách (gợi ý)
- Khung pháp lý rõ ràng về mục đích, phạm vi, thời hạn lưu trữ, cơ chế giám sát (oversight) và kiểm tra tư pháp.
- Cơ chế minh bạch/giải trình cho việc yêu cầu dữ liệu; audit độc lập (khi có thể) để tránh lạm dụng.
- Phân tầng dữ liệu: cá nhân nhạy cảm, định danh, dữ liệu thiết bị/IoT; nguyên tắc tối thiểu hóa thu thập.
- Kênh khiếu nại/khắc phục cho cá nhân; quy định xử lý vi phạm và bồi thường.

## Checklist cho doanh nghiệp/cá nhân
- Rà soát luật địa phương về bảo vệ dữ liệu & an ninh mạng; xác định nghĩa vụ lưu trữ/khai báo.
- Thiết lập quy trình phản hồi yêu cầu dữ liệu từ cơ quan chức năng: thẩm quyền, phạm vi, log truy cập, minimization.
- Áp dụng “privacy by design”: minimization, pseudonymization/ẩn danh, mã hóa E2E; phân quyền và nhật ký truy cập.
- Đánh giá rủi ro theo use case: nhận diện khuôn mặt, giám sát mạng, dữ liệu vị trí; kiểm tra bias/false positive.
- Đào tạo nhân sự về bảo vệ dữ liệu và kịch bản yêu cầu dữ liệu khẩn cấp.

### Bảng so sánh nhanh luật bảo vệ dữ liệu (PIPL / GDPR / CCPA)

| Tiêu chí | PIPL (Trung Quốc) | GDPR (EU) | CCPA/CPRA (California) |
| --- | --- | --- | --- |
| Phạm vi | Cá nhân tại TQ; áp dụng ngoại lãnh thổ nếu xử lý dữ liệu công dân TQ | Cá nhân tại EU; áp dụng ngoại lãnh thổ nếu nhắm tới/giám sát | Người tiêu dùng CA; áp dụng doanh nghiệp trên ngưỡng doanh thu/dữ liệu |
| Cơ sở xử lý | Đồng ý, hợp đồng, nghĩa vụ pháp lý, lợi ích công, lợi ích hợp pháp hạn chế | 6 cơ sở (đồng ý, hợp đồng, nghĩa vụ pháp lý, lợi ích công, lợi ích hợp pháp, bảo vệ lợi ích sống còn) | “Bán/Chia sẻ” dữ liệu cần opt-out; không có cơ sở lợi ích hợp pháp như GDPR |
| Quyền chủ thể | Truy cập, sửa, xóa, port, hạn chế; yêu cầu chuyển dữ liệu ra nước ngoài phải đánh giá/báo cáo | Truy cập, sửa, xóa, port, hạn chế, phản đối, không bị profiling tự động | Truy cập, xóa, opt-out bán/chia sẻ, giới hạn dữ liệu nhạy cảm (CPRA) |
| Chuyển dữ liệu xuyên biên giới | Đánh giá tác động, phê duyệt/CAC, tiêu chuẩn hợp đồng; yêu cầu nội địa hóa với dữ liệu quan trọng | SCC/BCR/adequacy; đánh giá rủi ro bổ sung | Không bắt buộc SCC; tập trung nghĩa vụ thông báo/opt-out và hợp đồng với bên thứ ba |
| Adequacy / SCC / BCR | Không có adequacy; dùng tiêu chuẩn hợp đồng của CAC; đánh giá tác động, phê duyệt khi dữ liệu quan trọng | Adequacy cho nước/vùng an toàn; nếu không, dùng SCC hoặc BCR + biện pháp bổ sung | Không dùng adequacy/SCC; hợp đồng + nghĩa vụ thông báo/opt-out với bên thứ ba |
| Chế tài | Phạt % doanh thu, đình chỉ dịch vụ, đưa vào danh sách đen | Phạt tới 4% doanh thu toàn cầu | Statutory damages (vi phạm data breach), phạt hành chính qua CPRA |

### SOP (mẫu) xử lý yêu cầu dữ liệu khẩn cấp từ cơ quan chức năng
1) **Tiếp nhận & xác minh thẩm quyền**: ghi nhận văn bản/yêu cầu; xác minh cơ quan, căn cứ pháp lý, phạm vi dữ liệu, thời hạn.
2) **Đánh giá pháp lý & bảo mật**: kiểm tra phù hợp luật địa phương/FTA/ngành; phân loại dữ liệu (nhạy cảm hay không), mức độ chia sẻ tối thiểu cần thiết.
3) **Phê duyệt nội bộ**: legal/compliance + security; nếu khẩn cấp, áp dụng quy trình rút gọn nhưng vẫn có hai cấp phê duyệt khi có thể.
4) **Chuẩn bị dữ liệu**: trích xuất tối thiểu, mã hóa, log đầy đủ (ai, lúc nào, dữ liệu gì); loại bỏ dữ liệu ngoài phạm vi.
5) **Bàn giao an toàn**: kênh bảo mật, xác nhận người nhận, chữ ký/biên bản; nếu pháp luật cho phép, yêu cầu lệnh bằng văn bản.
6) **Hậu kiểm**: lưu hồ sơ, đánh giá tác động, cập nhật đăng ký/DSR nếu liên quan; rà soát quy trình để cải thiện.

> Gợi ý: tùy quốc gia, có thể cần cơ chế từ chối nếu yêu cầu vượt thẩm quyền hoặc không phù hợp luật; luôn lưu log và hạn chế dữ liệu ở mức tối thiểu.

### Mẫu biểu log bàn giao dữ liệu (tham khảo)

| Trường | Nội dung mẫu |
| --- | --- |
| Mã yêu cầu | REQ-2026-001 |
| Cơ quan yêu cầu | Cơ quan A (đính kèm văn bản số …) |
| Căn cứ pháp lý | Điều … Luật … / Lệnh tòa … |
| Phạm vi dữ liệu | Tối thiểu cần thiết: [miêu tả trường, khoảng thời gian] |
| Phân loại dữ liệu | Nhạy cảm / PII / Phi PII |
| Mức độ nhạy cảm | Cao / Trung bình / Thấp (ghi rõ tiêu chí) |
| Owner dữ liệu | Bộ phận/đơn vị chịu trách nhiệm dữ liệu |
| Phê duyệt nội bộ | Legal: [tên/giờ]; Security: [tên/giờ] |
| Hình thức bàn giao | Kênh mã hóa, mật khẩu gửi kênh tách biệt / bàn giao trực tiếp |
| Người nhận | Họ tên/chức vụ, xác minh ID |
| Thời gian bàn giao | YYYY-MM-DD hh:mm (múi giờ) |
| RTO/RPO dữ liệu | RTO: … ; RPO: … (nếu liên quan tới bản sao/khôi phục) |
| Người thực hiện | Tên + bộ phận |
| Hash/Checksum (nếu file) | SHA-256: … |
| Retention đến ngày | YYYY-MM-DD (hạn xóa bản sao/bản bàn giao) |
| Kênh backup thứ cấp | (Nếu có) vị trí/vùng, mã hóa, quyền truy cập |
| DSR liên quan | ID yêu cầu dữ liệu cá nhân (nếu có), trạng thái xử lý |
| Ghi chú | Hạn lưu log, điều kiện sử dụng, lưu ý pháp lý bổ sung |

## Bảng cân nhắc risk/benefit (mẫu)

| Use case | Lợi ích an ninh/công | Rủi ro quyền riêng tư | Biện pháp giảm thiểu |
| --- | --- | --- | --- |
| Nhận diện khuôn mặt tại nơi công cộng | Tìm kiếm nghi phạm, an ninh sự kiện | Sai lệch/bias, theo dõi diện rộng, lạm dụng | Hạn chế phạm vi, thời gian lưu, audit độc lập, ngưỡng tin cậy |
| Giám sát mạng/metadata | Phát hiện tấn công, tội phạm mạng | Thu thập vượt mức, thiếu minh bạch | Minimization, log truy cập, phê duyệt đa cấp |
| Dữ liệu vị trí (telecom) | Ứng phó khẩn cấp, dịch bệnh | Theo dõi di chuyển cá nhân, tái định danh | Ẩn danh hóa, giới hạn mục đích, thời hạn xóa |
| IoT đô thị (camera, cảm biến) | Quản lý giao thông, hạ tầng | Lộ lọt dữ liệu, sử dụng lại sai mục đích | Segment mạng, mã hóa, chính sách truy cập |
| (Tự điền) | (Lợi ích) | (Rủi ro) | (Biện pháp) |

## Bài tập
- Viết 300 chữ: bạn sẽ thiết kế oversight như thế nào cho một hệ thống nhận diện khuôn mặt trong đô thị?
- Lập SOP ngắn cho doanh nghiệp khi nhận yêu cầu cung cấp dữ liệu: xác minh thẩm quyền, phạm vi, log, trả lời.