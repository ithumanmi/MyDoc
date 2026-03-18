# 🕵️ Reverse Engineering Ad Creatives: Thuật "Nhìn Lén" Bài Thi Đối Thủ

> [← Back to Strategy & Advanced](./README.md) | [Home](../../../README.md)

Trong thị trường B2C (Game Mobile, App thương mại, E-commerce, Dropship), Code giỏi chỉ quyết định 20% thành công. 80% còn lại nằm ở việc: Mẫu Ads Video nào đang ra đơn (Conversion)?

"Winning Creative" (Mẫu ads chiến thắng) là sinh mệnh. Thay vì đốt 10.000 USD để test A/B xem video nào hiệu quả, tại sao không đi cướp "Bản thiết kế" từ đối thủ đã đốt 1 triệu USD để test? 

---

## 1. Meta Ads Library (Thư Viện Quảng Cáo Facebook) - Kho Báu Lộ Thiên

Meta ép buộc mọi trang Fanpage phải công khai các quảng cáo đang chạy. Đó là thanh gươm của bạn.

### Cách moi móc dữ liệu (Spying Protocol):
1.  Vào [Meta Ads Library](https://www.facebook.com/ads/library/).
2.  Chọn **Quốc gia: All** (Tất cả). Chọn **Ad Category: All Ads**.
3.  Tìm kiếm tên Fanpage (VD: *Duolingo, Headspace, hoặc tên Game đối thủ*).

### 🔍 Dấu hiệu của một "Winning Creative" (Cờ Đỏ Báo Hỷ):
Làm sao biết video đó đang là cỗ máy in tiền của đối thủ? Trả lời 2 yếu tố:
*   **Tuổi Thọ (Longevity):** Facebook có ghi rõ *"Bắt đầu chạy từ ngày (Started running on)"*. Nếu một Ads bắt đầu chạy từ 6 tháng trước, và ĐẾN NAY VẪN ĐANG CHẠY (Active) -> Nó chắc chắn là hàng siêu phẩm lợi nhuận. Không một doanh nhân ngu ngốc nào đốt tiền duy trì 1 cái video lỗ chỏng gọng suốt 6 tháng trời.
*   **Bản Sao (Duplication):** Nếu bạn lướt thấy cùng **1 nội dung Video y chang**, nhưng được nhân bản thành **30-50 chiến dịch đang chạy ngầm khác nhau**. Điều đó có nghĩa là họ đang Scale Up (Vít ngân sách) mẫu Ads đó hết cỡ.

### Hành Động Phản Kích:
Tải ngay Video đó về máy (dùng các Extension tải video Chrome). Đưa nó vào kho **Swipe File** (Tàng kinh các) của Công ty.

---

## 2. TikTok Creative Center: Nơi Xu Hướng Nảy Mầm

Khác với Meta, quảng cáo TikTok có vòng đời rất ngắn (Ad Fatigue cao). Một video chạy ngon 2 tuần là chết vì user xem ngán.

1.  Vào [TikTok Creative Center -> Top Ads Dashboard](https://ads.tiktok.com/business/creativecenter/).
2.  (Mẹo Nhỏ: Bạn phải đăng nhập thì mới xem đầy đủ Data). Ngôn ngữ Filter: Chọn **Ngành (Industry)** của bạn, và Chọn Mức Độ Tương Tác: **Top 20% CTR** (Tỷ lệ Nhấp chuột).

### 🔍 Bóc Tách Yếu Tố Viral (The Hook Reverse Engineering):
TikTok cung cấp cho bạn biểu đồ thời gian thực: Gây chú ý ở giây nào, Tỷ lệ Drop-off (Khung hình người ta bỏ vuốt đi) ở giây thứ mấy.
Hãy chẻ nhỏ Video đối thủ ra làm 3 phần:
1.  **3 Giây Đầu Tiên (The Hook):** User chú ý vì cái gì? (*Vd: Hình ảnh quái dị, âm thanh la hét, Câu text đập vào mắt: "Tôi đã mất 10 năm mới biết mẹo giảm cân này"*).
2.  **Thân Bài (The Body/Problem-Solution):** Cách họ "Bán" app của mình. Show màn hình UI? Có người đóng Kịch giả (UGC)? 
3.  **Kêu gọi hành động (Call To Action - CTA):** Chỉ vào nút Download mũi tên màu đỏ chói.

> **Chiến lược Clone thần thánh:** Hãy "Xào" lại nội dung: Lấy cái Hook chiến thắng của đối thủ A, ghép với thân bài thuyết phục của đối thủ B, thêm màn chốt sale của bạn. Không bao giờ copy y nguyên (Sẽ bị ban tk quảng cáo do vi phạm IP). Bạn mượn Cấu Trúc (Structure), không mượn Hình Khối (Assets).

---

## 3. Các Spy Tools Trả Phí Mạng Trọng Mật (Cấp Độ Hacker)

Nếu bạn kiếm tiền đủ dày, đây là lúc mua chuộc gián điệp cấp cao (Tools có Phí).

1.  **BigSpy / AdSpy:** (Tốn $50-$150/tháng). Nó không phụ thuộc vào chính sách mở của Facebook. Nó thả hệ thống hàng chục triệu acc clone đi Farm quảng cáo, cào data các lượt Like, Share, Cmt Thật. Nó lọc cho bạn biết: Tệp khách hàng (Targeting) mà đối thủ đang nhắm tới là độ tuổi nào, ở đâu!
2.  **AppMagic (Dành riêng cho Dev Mobile App/Game):** Khi soi đối thủ, bạn có thể click vào mục *"Creatives" (Tuyệt Kỹ Của Tool Này)*. Nó tải hết toàn bộ Ads Video từ Mạng Admob, Unity Ads, Applovin, IronSource của đối thủ về cho bạn mổ xẻ. 

> **Khẩu Quyết Sinh Tồn B2C:** "Nếu bạn chưa có 50 Video Ads của đối thủ nằm trong máy chiếu để mổ xẻ mỗi tối T7, bạn chưa có tư cách bấm nút Bỏ Tiền (Publish Campaign) chạy Quảng cáo. User không cài App của bạn vì tính năng nó đỉnh. User cài app bạn vì cái Video đó đánh vào phần Vô Thức/Động Dục/Sợ Hãi của 3 giây mắt nhìn."
