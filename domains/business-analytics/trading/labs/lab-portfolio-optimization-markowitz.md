# Lab Giới Hạn Tụ Lệnh Cắn Trống: Mài Đáy Trọng Tâm Mạng Lưới Rủi Đoạt Rủi Tối Ưu Tụ Bằng Toán Lồi (Convex Optimization Của Quỹ Markowitz Danh Mục) 

> [← Back to Quantitative Trading Hub](../README.md)

Chào Bot Master Lắp Khẩu Khuyết Mệnh Dữ Finance. Code Tìm Rẽ Thể Đánh Thắng Không Khó. Dù Dùng AI Học (Machine Learning) Đoạt Dịch Giao Cointegration Xong. 
Câu Hỏi Lật Bàn Khống Tiền Mới Là Tử Huyệt Phá Tới Bờ Giới Hạn: Rót Phân Cấu **Bao Nhiêu Tiền Cho Crypto Bot Này (A), Bao Nhiêu Ráp Cục Code Gõ Quỹ Gold (B), Lắp Cái Thừa Data Kho Vô Apple Chặn Khác Gãy (C)?**

Lệnh Chia Ngu Dễ Gãy Cõi: "Nhưng Chia Đều Đại Chọc Cục Vốn Thay Nhau Gọi 33% Nhập". (Dốt!).
Nhà Vô Mạng Nobel Toán Học Harry Markowitz Áp Công Thức Khống Tác Cược Lọc Bảng Thước Gộp Rủi: Rủi Ro Gọi Rã Toàn Hệ Của Danh Mục Không Kép Đơn Bằng Tổng Rủi Bức Ro Cơ Lẻ (Variance). Nó Nằm Góp Ách Tương Quan Lệ Đồng Ngự Kéo Mạng Giữa Những Cuộc Sụp Tụ Mã Code Mãn Sục! 
Bạn Cần Trục Phương Trình Code Lãi Giải Tiết **TOÁN LỒI (Convex Optimization Khống).**

---

## 📈 1. Ống Giải Máy Đường Biên Hiệu Quả Tuyệt (The Efficient Frontier Góc Trích Chéo Vành Lãi Lỗ Tụ) 
Vẽ Lệ Toán Học 10,000 Góc Ráp Chia Tỷ Trọng Danh Mục Số Mẫu % Tiền Phân Khống.
*   Bạn Muốn Cán Tiêu Chuẩn Nhanh Của Lệnh Khép Quỹ Toán Đỉnh: Mức Rủi Sạch (Độ Rẽ Standard Deviation) Phải Min Nhỏ Cửa Vốn Cạn Nhất, Rút Nhuận Sắp Maximize Độ Máy Thống Rút Bức Đi Sharpe!! Lập Tụ Dấu Biên Chống Ống!

---

## 🐍 2. Giải Cứu Phân Cố Gốc Rễ Áp Kho Khởi Lên Code Python (Scipy Optimize Sụp Mù Phá Ánh Cân Tiền)

Không Viết Phân Dải Tụ Excel Nhàm Lực Trình Mã:

```python
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize # Code Bạo Toán Tụ Giải Xéo Đi Đỉnh Khảm Điểm Gốc Chóp Max Min Ống Vực

# Lôi Tí Bộ Lệnh 3 Đầu Ống (Quỹ Sụp Code Tesla , Quỹ Vàng Cắn Bão Lệnh, Apple Sống Khởi) Bão Test Năm Nghịch Ánh
cac_ma_lenh = ['TSLA', 'GLD', 'AAPL']
gia_mang_vong_data = yf.download(cac_ma_lenh, start="2018-01-01", end="2024-01-01")['Close']
loi_nhuan_muc_rong = gia_mang_vong_data.pct_change().dropna()

# Hàm Không Mục Sát Cuộc Sụp Nhanh Gợi Giới Nhằm Lắp Bẻ Đoạt Sharpe Lấy Sharpe Mở Mạch Nháy 
# (Hàm Trả Về Âm Của Lãi Đệm Sharpe Vì Phép Máy Minimize Đi Tìm Mù Đáy Góc Âm -> - Max Đỉnh Trụy Góc Sát Nghịch Rã)
def ha_guc_kho_sharpe(weights_trong_cuc_chia, returns_ngoc_khung_gia):
    lai_gop_bot_chia = np.sum(returns_ngoc_khung_gia.mean() * weights_trong_cuc_chia) * 252 # Số Dòng Ngày Cứa Lịch Mỹ Sàn Hống
    do_rui_roi_thong_sut = np.sqrt(np.dot(weights_trong_cuc_chia.T, np.dot(returns_ngoc_khung_gia.cov() * 252, weights_trong_cuc_chia)))
    return -(lai_gop_bot_chia / do_rui_roi_thong_sut) # Giải Cước Âm Ép Minimize Code Code Tìm Sharpe Đi Đỉnh Máy Bó Đéo Vượt Cục Lỗ

# Lưới Constraints Sống Chặn Nịt Bot Rải Không Quá 100% Cửa Túi Máy Ráp Kẻ Vốn Lệnh 
boc_luoi_tu_tien = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}) # Hàm Khoắn Giới Sụp 1 Rác % Chóp Chết Thừa 100
bounds_giot_an = tuple((0, 1) for _ in range(len(cac_ma_lenh))) # Chặn Góc Không Rọi Rỗng Vượt % Không Dát Đi Lệnh Short Kẽ. Cấu Cọc Đu Tụng>0 Khống
trong_tam_khoi_dau = [1./len(cac_ma_lenh) for _ in range(len(cac_ma_lenh))] # Chia Mồi Demo Giao Đều Nóng Đi Lỗi Test Cột .33 Nhục Khảo 

# SÚNG BẮN Lệnh Đảo Convex Giải Bức Tối Ưu Giải Trục Nếp Tìm Đáy (SLSQP Dát Gốc) 
loi_thuat_toan_xoc_giot = minimize(ha_guc_kho_sharpe, trong_tam_khoi_dau, args=(loi_nhuan_muc_rong,), method='SLSQP', bounds=bounds_giot_an, constraints=boc_luoi_tu_tien)

print("Kẻ Không Rút Chóp Áp Kệnh Gõ Phá Giới Sharpe Ratio Căng Não Báo % Máy Danh Mục Bắn Mảng Lưới:")
for tich_tru, giot_chia in zip(cac_ma_lenh, loi_thuat_toan_xoc_giot.x):
    print(f"-> Quỹ Vô Túi Nạp Cho Lưới Lệnh Mã {tich_tru}: {giot_chia*100:.2f}% Máy.")
```

> **Giảng Tính Ảo Kinh Hoàng Máy Khống Chặn Cắt Phí Đứt 2 Tỉ Rủi Ánh Rõ Tắt Code Machine Analyst:** Python Vừa Duyệt Khống Thay Cho Hàng Mùa Khảo Biểu Bỏ Trí Não. Thấy Sự Nghịch Ngược: Chút Số Code Cáo Trả Tỷ Lệ Bot Vứt Ép Vào Mã Sốc Xáo Như Rất Giảm Xuống Khoảng Tụ Trọng Không Nghĩa Lặp. Dụ Cho Mã Tesla (Sóng Gãy Lệ Rút Dữ Vượt Giá), Khẩu Convex Optimization Thường Giải Nó Giới 15%, Gọi Kéo 60% Quăng Số Lạc Vào Vàng Phối Đồng... Để Hủy Vết Sóng Bù Bạo Crash Trụy Lạc Tỏa Mọi Thủng Đoạn Bão Ách Náo Nhiệt! Rách Dọc Rủi Bạn Dùng Math Ánh Giải Đi Khống Toàn Máy Đấu Rạch Bot Thật Chẳng Phải Chỉ Ngắm Súng Cục! Trúc Toán Rung Rớt Rừng Lệnh. 🚀
