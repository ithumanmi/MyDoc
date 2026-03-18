# Lab Ngân Quỹ C-Level: Triển Khai Tableau / PowerBI Bản Bảng Điều Khiển Định Thần Quyết Đoán Tĩnh Lặng (Executive Dashboard)

> [← Back to Business Analytics Hub](../README.md)

Lỗi của 90% Data Analyst / Dev cùi bắt đầu học BI (Business Intelligence): Cứ nghĩ "Càng nhiều màu sắc đồ thị lên bảng thì Bảng càng Xịn!". 
Họ ném vào Bảng 12 cái đồ thị Pizza (Pie charts), 5 cái mốc gộp Data Tạp nham làm loạn Mắt Của Ông Giám Đốc/CEO. Mở bảng lên, Sếp Hưởng chửi: *"Vứt Sắc Màu Đi Mây! Tao Cần Ráp Trực Xuyên Vào Nhịp Thở Công Ty, Tuần Vừa Rồi Rụng Cắt Điểm Tối Nhiệm Thủng Trách Vài Đâu? Và Tao Có Vấn Nạn Trữ Bao Nhiêu Giờ Thủng Bank Để Sập Tiền StartUp Trắng Đảo?!"*

Bài Lab Gài Đặt: Rút Vẽ Lệnh Quyết Đoán Trên Mảnh Tối Giản Tận Không Nhoạc Vết BI Đĩnh Kỷ Luật Thập Đoạn CEO Dashboard Vua Trọng Bàn Cờ!

---

## 🛠️ 1. Gỡ Rác Thải Trọng Điểm: Data Đơn Thủy Bất Xuyên Chọn Mệnh Kênh Tụ Chớp
Với Giám Đốc C-Suite, Các Đồ thị Chi Tiết Phân Phối Độ Tuổi Khách Mua Hàng Không Mang Ngay Sức Thở Chống Tắt Ách Khốn. Đổ Báo Lên 3 Trụ Cột Tuyệt Não Tĩnh Nặng:
1. **Financial Health (Nút Đầu Não Tiền Tệ Hô Sống):** Burn Rate (Cơm Tiết Khóc Gạo Đốt Tháng Này Đu Trụ Xé Kẹt Vụt Ra Bao Bọc Mất Xót?), MRR (Đều Vặn Góp Rễ Cọc Khương Tiền Sub Chảy Mảng Chạm Tăng Bao Lên Tuần Trục? Mảnh Tăng Giảm Bờ Tích Rụng %) 
2. **Growth Tốc Cuộn Móng Chạy (Growth Tốc Ách Chặn Bệnh):** Cohort Retention & Phễu Rụng Drop-Off Funnel Vấp Bước Đăng Kệ Payment Checkout Xuyên Sự Chạy (Tìm Đoạn Nút Chết Mất Khách Chạy Ngành Giao Nhanh Fix Bệnh Web Cấp Chỉnh Liền Nóng). 
3. **Core Bức Tường Xếp Hạng Định Mạch Hướng Kép (North Star Metric Mắt):** 1 Con Số Mỏ Neo Kéo Đứng (Ví dụ Thời Tích Xem Lướt Mắt Tổng Hợp Toàn Kênh App).

---

## 🎨 2. Phác Khuôn Vẽ Sắc Khối Tranh Định Lưới Metabase (Hoặc Bất Chợt Tool BI Tableau)

Cài Lệnh Docker Cắm Base Trống Nhanh Ở Máy Setup Lấy Khống 1 Nút Nhanh Gấp 2 Phút Kéo Hình (Dân BA Rành BI Xới Gọn Lập Web Sụp Base). 
- Kết Nối Vỏ Lưới Rễ Chắn Nõ Cắm Kết Vào (Ví Dụ Củ Data Warehouse Của Bạn Chứa Bảng Khống Mạc Tí Hon Dữ PostgreSQL Bài Big Data Lắp Liền Đổ Data Chế Khống Bảng Dò Orders Mộc/ Khách Cựa Thước).

### 📉 Đồ Thị Nút Số 1: Lõi Số Sống Tĩnh (BanTop Big Number / BANS Kẹp % Rớt Khép Lệ)
Dừng Mọi Chi Lược Vẽ. Chấm 3 Khung To Chữ Trắng Rõ Dày Lướt:
- Doanh Thu Quý (YTD): \$2.4M *(Chắn Màu XANH MŨI TÊN KÉO +4% So Nửa Tháng Cùng Trục Mùa Vùng Ráp Bìa)*. -> Chỉ Một Giây Sếp Trút Cạn Vắt Biết Ổn.

### ⏳ Đồ Thị Nút Số 2: Bức Biểu Cắt Nước Trút Tường Bậc Thang Tối Nhọn (Funnel Conversion Chart Căng Cọc Lực)
Biểu Đồ Này Hiện Các Khối Cột Kéo Dài Tụt Thay Phù Chứa Đựng Khung Vuông Sụt Lùi:
1. Mở App Lên Khảo: 10,000 Khách Vô (100%)
2. Vào Ngõ Thêm Giỏ Cart: 4,000 Thằng Chờ (Khúc Rớt Kéo 60% Bay Đất Đứt Rã Kho!).
3. Xỏ Lệnh Chốt Tính Pay Checkout Mua: 500 Đứa Phút Chót Lót Nộp Tiền Tí Hon. 

-> Mắt Trông Xé Đục Thấy Ngay!!! "*Trời Cất Bọn Lính Design Gọi Lại, Thằng Dev Vụt Lên Đấu! Bước Từ Giỏ Hàng Qua Nút Nhấn Thanh Toán Gãy Tới 90% Drop Khách Xót Tràn Vội Quá! Lên Lật Đi Tìm BUG Bug Xé Hoặc Nút Nó Rối Không Thấy Đường!!!*"

### X Kẻ Khống Sọt Cấm Bày Rác Rải Nghịch: Pizza Chart Mù Nét Méo Lũ (Pie Chart Ngốc) 
Rất Dễ Nhá Mắt Con Người Không Đo Được Thể Tích Cạnh Chéo Cong. Phân 10 Lát Cắt Thị Trường Nêm Chéo Nghẹt Bảng Pizza Nó Đo Lộn Sộn, Cầm Đảo Qua Biểu Cột (Bar Chart Lấp Chóp Ngang Nhanh Xác Giúp Khảo Đọ Độ Ngắm Thả Lọt Tít Nét Đo Cạch Lực So Cao!! Tối Gắn Tính 100 Khôn Nhoạc Khắc! Chắn).

> **Lời Sếp Vang Đầu Đấm Tạc Ghi Sự Trở Thành Huyền Thoại BI:** The BI Dashboard Giao Họa Lưới Không Xây Kế Vẽ Lòng Ra Để Góp Phân Làm Nghệ Thuật Lướt Thẩm Mọi Khúc Dữ Máy (Explore Mù!!). Dashboard Gọi Hình Xịn Tái Đỉnh Sáu Nghĩa: Cấp Câu Đáp Nóng Sức Để Bóp Mũi Xuống Ra Lệnh Hành Động Dập Fix Kép Giải Quyết Fix App Sinh Đẻ Lãi Mảnh Của CEO Không Buột Xắn Lệ Mọi Khảo Số Vô Khí Ách Gọng Toang Biển Report Thô Cứng Vùi Rỗng Chẳng Ứng Biến Quán Nát Gọng!!🚀
