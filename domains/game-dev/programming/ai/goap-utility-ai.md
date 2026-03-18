# Hệ Quản Trị AI Sinh Tồn (GOAP & Utility AI)

> [← Back to AI Programming](../README.md) | [Home](../../../README.md)

Lập trình viên khi mới học AI thường cắm mặt vào **FSM (Máy trạng thái - State Machine)** [đã được hướng dẫn tại Lab 2](../../labs/README.md). FSM rất tuyệt cho Boss Chiến Đấu có 3-4 Form.
Nhưng nếu bạn làm NPC Nông Dân phải Đan rổ, Trồng Cây, Hay Chó Sói phải Đi Rình Chuột Đói Mới Đánh Bắt Buổi Chiều Tà. FSM sẽ mọc ra một Tơ Lòng Thòng 88 Đường Giao Tiếp Rối Loạn Cản Mã Chết Tức Tưởi. 

Đây là lúc dùng AI Hệ Điều Hành Đỉnh Cấp Cho RPG Sinh Tồn!

---

## 🎯 1. GOAP (Goal-Oriented Action Planning) (Thằng Siêu Kế Hoạch Lạnh Lùng)

Cha đẻ của GOAP nằm Ở Quái Nhân Vật Trong Siêu Phẩm Tiền Sử (The F.E.A.R). Bạn Đưa Cho Địch 1 Mục Tiêu, Chúng Nó Tự Mò Đường Làm Thao Tác Chết Dính Từng Chi Tiết Hành Vi.

### Hoạt Động (Nhờ Việc Lấy Biến Nghịch Suy)
Trong FSM, bạn Code: *"Nếu Đói -> Đi bẻ bắp -> Cầm bắp ăn luôn"*.
Trong GOAP, Coder Quăng ra 1 Đống Hành Động (Gái Đi Bar, Khát Nước, Ăn Trộm Súng, Đi Lấy Đạn), Mỗi Thằng Hành Động Khai Báo Điều Kiện Cầm (Preconditions) Trị Giải Được Quả Báo (Effects).
*   Ví Dụ Thẻ Hành Động `Gặp_Địch_Bóp_Cò_Súng`: Điều kiện cần `Có Chứa Súng=True`, Effect Xong `Giết Địch=Đạt Rẽ Trái Đỉnh`.

NPC Có Dã Tâm Goal Kêu: `Mong Giết_Địch_Hoa_Lá(Đạt)`.
Não Nó Sẽ Rì Soát Đi Dò Từ Ngược Lại Đuôi Hệ Mạng Action Tree:
> Goal Nhận [Giết Địch] -> Thử Nhét Hành Động Bóp Cò -> Nhưng Nó Xem Mệnh Điều Kiện Precondition Khuyên `Súng=Chưa Cầm` Rỗng Rỗng! -> Não Cất Công Lặn Ra Tim Cái Hành Động Gì Mang Lại Effect Súng Trên Người Nhất -> Bắt Được Thằng `Lượm_Súng` Hành động Quãng Trước. 

> *Phá Xuyên Mạch Ván Thành Chuỗi String Plan Hoàn Chí: Đi Lượm Súng -> Tìm Địch Bóp Cò Mạng Lướt Ván Hoàn Thiện.* 🤯

Tất cả Chạy Dynamic Dữ dội. Bọn NPC FEAR Siêu Kinh Dị Hầm Trí Chống Player Khó Như Quỷ.

---

## ⚖️ 2. Utility AI (Chấm Điểm Nhu Cầu Góp Gạo Cân Đong The Sims)

Vào những game Chilling Nuôi Nông Trại Chó Gà Mèo (Rimworld), Thằng Nào Trông Có vẻ Tâm Trạng Lang Thang Cũng Tính Toán Như Utility AI Toán Mệnh: (Bảng Góp Điểm Điếm Chết Rớt Khóc Cười Đơn Giản Lập Ráp Gây Nhiễu).

### Biểu Đồ Thước Rõ Nhu Cầu Đơn Tuyến
Mỗi Thằng Nhu Cầu Chạy Ra Điểm Từ (0 - 100).
*   Mức Ngủ Nhu Cầu Điểm = `Curve Toán Lũy Đo Chi Tiền Thời Gian Mắt Chống Buồn Cụt`. (Ra 82 Điểm Đạt Lệnh Giục Lớn Cảnh Ngủ Xụp)
*   Mức Xả Bụng Cần Trút Đạt = 99 Điểm Đòi Tràn Ly Lập Tức.
*   Trồng Khoai Cày Sân Việc = 30 Điểm Ế Độ.

Hệ Thống Rút Bài Toán Chốt: Hành Trình Thằng Sim Bỏ Đi Đái Trước Ở Toilet Xong Chạy Lên Giường Phá Nước Miếng Bọt Rụng Rời Cảnh 80 Mức Độ Buồn. Đứng Quan Sát Mắt Quần Cày Chậm Sướng Nhất Giải Phóng Nhân Đạo Trí Tuệ Khác Thường Gây Mê Cày Lên 6 Triệu Bản Copies Game Giữ Chân Sinh Tồn Thâm Múi!

> 🧪 **Chuyển Phạt Bắt Tay Code:** [Lab: Code The Sims Gã Khùng Có Khát - Ngu - Sợ Chấm Điểm Ưu Tiên AI](../../labs/lab-utility-ai-sims.md) Bằng Script C# Viết Mộc Sạch Cười. Mặc kệ Nav Mesh Quấn Rối Thằng Hề Tâm Linh!
