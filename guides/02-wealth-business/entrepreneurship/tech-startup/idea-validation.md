# 💡 Idea Validation: Đừng Xây Dựng Thứ Không Ai Cần

> [← Back to Tech Startup Guide](./README.md)

**Sự thật phũ phàng:** 42% startup thất bại vì "No Market Need".
Bạn có thể có code sạch nhất, architecture xịn nhất (Microservices, K8s), nhưng nếu không ai cần sản phẩm của bạn, tất cả đều vô nghĩa.

Hướng dẫn này giúp bạn kiểm chứng ý tưởng **trước khi** viết dòng code đầu tiên.

---

## 1. Tư Duy Cốt Lõi: Problem First 🎯

Đừng bắt đầu bằng "Tôi có ý tưởng về một App AI...".
Hãy bắt đầu bằng "Tôi thấy mọi người đang gặp vấn đề X rất đau đớn...".

*   **Vấn đề (Pain point):** Phải đủ đau. (Thuốc giảm đau > Vitamin).
*   **Tần suất:** Họ gặp vấn đề này bao lâu một lần? (Hàng ngày > Hàng năm).
*   **Giải pháp hiện tại:** Họ đang giải quyết nó như thế nào? (Excel, Thuê người, Chịu đựng).

> **Quy tắc vàng:** Fall in love with the problem, not the solution.

---

## 2. The Mom Test: Nghệ Thuật Phỏng Vấn 🗣️

Khi bạn hỏi mẹ: "Mẹ ơi, ý tưởng này có hay không?", mẹ bạn sẽ luôn nói "Tuyệt vời con trai!". Đó là lời khen xã giao (False Positive).

**Cách hỏi đúng (theo Rob Fitzpatrick):**
1.  Đừng nói về ý tưởng của bạn. Hãy hỏi về cuộc sống của họ.
2.  Hỏi về quá khứ, không phải tương lai.
    *   ❌ "Bạn có nghĩ sẽ dùng app này không?" (Họ sẽ chém gió).
    *   ✅ "Lần cuối cùng bạn gặp vấn đề này là khi nào? Bạn đã xử lý nó ra sao?" (Sự thật).
3.  Lắng nghe lời phàn nàn, đừng bán hàng.

---

## 3. Smoke Test (Kiểm Thử Khói) 💨

Làm sao để biết họ **thực sự** muốn mua, chứ không chỉ "chém gió"?
-> **Đo lường hành động, không phải lời nói.**

### Bước 1: Landing Page Giả (Fake Door)
*   Dựng 1 trang web đơn giản mô tả giải pháp (dùng Carrd, Framer - tốn 30 phút).
*   Thêm nút "Mua ngay" hoặc "Đăng ký sớm".

### Bước 2: Chạy Ads / Seed Forum
*   Bỏ $50 chạy Google/Facebook Ads nhắm đúng đối tượng.
*   Hoặc post vào các Group chuyên môn.

### Bước 3: Đo Conversion Rate
*   Nếu 100 người vào -> 0 người click "Mua": **Ý tưởng tồi.**
*   Nếu 100 người vào -> 20 người click: **Có tín hiệu tốt (Validation).**
*   Lúc này mới hiện thông báo: *"Xin lỗi, chúng tôi đang xây dựng. Hãy để lại email để nhận ưu đãi 50% khi ra mắt."*

---

## 4. Concierge MVP (MVP Thủ Công) 👨‍💼

Đừng vội code hệ thống AI phức tạp. Hãy làm thủ công trước.

**Ví dụ:** Bạn muốn làm App gợi ý món ăn AI.
*   **Thay vì:** Code AI model, scraping data, mobile app.
*   **Hãy:** Tạo 1 form Google. Khách điền sở thích -> Bạn tự tay Google tìm món ăn -> Gửi email cho họ.
*   **Mục tiêu:** Kiểm chứng xem họ có hài lòng với kết quả gợi ý không. Nếu làm thủ công mà họ còn chê, thì AI cũng vô dụng.

---

## 5. Các Kỹ Thuật Validation Nâng Cao Khác 🚀

Ngoài Smoke Test và Concierge MVP, bạn có thể áp dụng thêm:

### 5.1. Wizard of Oz MVP (Phù Thủy Xứ Oz)
*   **Concept:** Bề ngoài trông giống như một sản phẩm hoàn chỉnh, tự động hóa hoàn toàn, nhưng thực chất bên trong là con người đang vận hành thủ công (fake it until you make it).
*   **Ví dụ:** **Zappos** (bán giày online).
    *   Founder Nick Swinmurn không nhập hàng, không xây kho.
    *   Anh đến cửa hàng giày địa phương chụp ảnh, đăng lên web.
    *   Khi có khách đặt, anh ra cửa hàng mua và gửi đi.
    *   **Validation:** Chứng minh người ta dám mua giày qua mạng mà không cần thử.

### 5.2. Crowdfunding (Gọi Vốn Cộng Đồng)
*   **Concept:** Dùng nền tảng như Kickstarter hoặc Indiegogo để bán trước sản phẩm (Pre-order) khi nó chưa tồn tại.
*   **Cách làm:** Tạo video demo cực xịn, viết trang mô tả hấp dẫn.
*   **Validation:** Đây là bài test tối thượng về **Willingness to Pay**. Nếu mọi người bỏ tiền thật ra mua một thứ chưa có, thị trường chắc chắn tồn tại.
*   **Ví dụ:** **Pebble Watch** đã thu được 10 triệu USD trước khi sản xuất chiếc đồng hồ đầu tiên.

---

## 6. Checklist: Khi Nào Nên Bắt Đầu Code? ✅

Bạn chỉ nên mở IDE lên khi đã có đủ 3 tín hiệu:

1.  [ ] **Vấn đề rõ ràng:** Bạn gọi tên được nỗi đau và khách hàng gật đầu lia lịa.
2.  [ ] **Willingness to Pay:** Đã có ít nhất 5 người đồng ý trả tiền (Pre-order), Crowdfunding thành công, hoặc 100 email đăng ký chờ.
3.  [ ] **Founder-Market Fit:** Bạn hiểu lĩnh vực này sâu sắc hơn người ngoài.

---

## 7. Case Study: Dropbox 📦

Drew Houston (Founder Dropbox) không code sản phẩm ngay.
1.  Anh làm một **Video giả** mô tả cách Dropbox hoạt động (kéo thả file, đồng bộ tức thì).
2.  Post video lên Hacker News.
3.  Kết quả: Danh sách chờ (Waiting list) tăng từ 5,000 -> 75,000 qua một đêm.
4.  Lúc đó anh mới bắt đầu code.

> **Bài học:** Validate trước, Build sau.
