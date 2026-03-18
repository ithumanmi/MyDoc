# Lab: Mỏ Tiền Không Đoán Hướng - Tạo Lập Thị Trường Mùa Crypto (Market Making)

> [← Back to Quantitative Trading Hub](../README.md)

Chào Mừng Bước Vào Lãnh Địa Của Sở Khớp Mã. Bạn đã quá mệt mỏi với việc Đoán Xem Giá Bitcoin Sẽ Lên Hay Xuống?
Xin chúc mừng. **Market Making (Tạo Lập Thị Trường)** KHÔNG QUAN TÂM NẾN LÊN HAY GIẢM. Lệnh của Bạn Bơm Tiền Ăn Chênh Lệch Tại Chỗ, Ở Kẽ Hở Răng Bọc Giữa Tường Mua và Tường Bán. Bào Xén Sàn Thẳng Tay Đổ Thuế Độ Không Đau Xé Lỗ Của Đám Đông Dân Chơi Đặt Đỉnh!

---

## 🧠 Lõi Thuật Khốc Của Nhà Cái: The Spread Tĩnh Điểm

Sàn Binance luôn tồn tại Khớp Lệnh L2:
- Rổ Người Mua (Bids) Hét To nhất muốn Bắt Gốc: \$60,000 / 1 BTC
- Rổ Kẻ Bán Kẹt (Asks) Đẩy Giá Xót Ruột: \$60,005 / 1 BTC

Khoảng Trống Răng Cưa $5 Đây Gọi là **The Spread**. Sự Chênh Lệch Hút Tiền Thanh Khoản.
Bạn Chạy Bot Python: Gài Lệnh Limit Bid Mua Ngay Giá \$60,001. Giăng Sẵn Lưới Lệnh Limit Ask Bán Cắt \$60,004.
Nếu Đám Đông Khát Máu Cào Mua Bán Thị Trường (Market Orders) Nhào Tới, Họ Quét Sạch Mảng Limit Của Bạn ở cả Trục! Bạn Không Đầu Cơ! Chốt Tại Chỗ **\$3 Lời Vượt Lưới Mỏ Bọc!! Cứ Rỉ Rỉ Thâu Tẩy Chục Ngàn Lần Trăm Khớp Nhanh Chớp Xoáy Húp Trắng Sàn Bào.**

---

## 🐍 Triển Khai Xưởng Python WebSocket (Binance API Căn Rỗng Cưa)

Ở Xới Arbitrage Và Làm Giá Dịch Không Dùng Tín Hiệu Nạy (REST HTTP) Cọc Lọc – TRỄ MẠNG. Dev Ráp Trụ WEBSOCKET Lấy Trực Tiếp Order Book L2 Gắn Nút!

*Mô phỏng Đu Mã Cấu Trúc Khớp Kỹ Kẽ Lệch (CCXT Pro or Binance Websocket):*

```python
import asyncio
import ccxt.pro as ccxt  # Thư Viện Chạc Bơm Asynchronous Khớp Nhanh

async def market_maker_l2_bot(symbol='BTC/USDT'):
    exchange = ccxt.binance({
        'apiKey': 'YOUR_API_KEY',
        'secret': 'YOUR_SECRET_KEY',
        'enableRateLimit': True,
    })

    print(f"🔥 Bật Lò Bào Rỗng Dữ Market Making {symbol}")
    
    inventory_btc = 0.5  # Kho Tổng Hàng Bạn Đang Cầm 
    base_spread = 2.0    # Cắm Mục Tiêu Ăn Cách Nhau 2 USDT

    while True:
        try:
            # 1. Bú Kéo Cuộn Liên Tục Order Book Tại Chớp L2
            order_book = await exchange.watch_order_book(symbol)
            best_bid = order_book['bids'][0][0] # Đỉnh Mua
            best_ask = order_book['asks'][0][0] # Đáy Bán Xả
            
            mid_price = (best_bid + best_ask) / 2.0
            
            # --- Thuật Toán Đổ Kho Inventory Risk (Rủi Ro Mắc Lệnh Chết) ---
            # Nếu Bạn Đang Đọng Quá Nhiều Mảng Hàng BTC >> Bạn Cần Hạ Lệch Tường Bán Rút
            # Thúc Nghẽn Mở (Avellaneda-Stoikov Xô Trọng Số Nhập Tịt Cơ Cấu)
            
            inventory_skew = (inventory_btc - 0.5) * 1.5 # Phạt Lệch Rỗng (Độ Dốc Hàng Đóng Lạc)
            
            my_bid_price = mid_price - (base_spread / 2) - inventory_skew
            my_ask_price = mid_price + (base_spread / 2) - inventory_skew

            # 2. Xóa Vứt Lưới Lệnh Cũ (Cancel All Orders)
            # await exchange.cancel_all_orders(symbol) -> Rút Dây Bắt Đầu Gắn Giăng Dây Cùm Mới
            
            print(f"[Spread {mid_price}] -> Rải Limit Lưới Lạc: 🛒 BID Cài {my_bid_price:.2f} | 💰 ASK Cắt Áp {my_ask_price:.2f}")
            
            # 3. Quặp Đóng Gắn Lưới Bào Limits (Giả Khớp Rút Order Book Limit)
            # await exchange.create_limit_buy_order(symbol, 0.01, my_bid_price)
            # await exchange.create_limit_sell_order(symbol, 0.01, my_ask_price)
            
            await asyncio.sleep(1) # Bào Mã Xấp Xéo Chờ Ngợp Sàn Phóng!
            
        except Exception as e:
            print(f"Lỗi Xé Cấn Nứt: {e}")
            break

# Kích Hoạt Nông Trưởng Mỏ Quant!
asyncio.run(market_maker_l2_bot())
```

### ☠️ Lưỡi Đao Cứa Cổ Kẻ Tạo Lập (Inventory Risk & Toxic Flow)
Bạn Thấy Tiền Sáng Chói Dễ Ăn Trắng Không? Hãy Coi Lại:
1.  **Dạt Kho Không Vết Lạc (Inventory Risk):** Bot bạn Rải Mua Rải Bán. Bất ngờ, Bitcoin sụp đổ Gãy Hầm Rác Chóp! Tường Bán Xé Cắn Khắp Nơi, Đám Đông Chửi Mắng Bán Vứt Tốc. Họ Khớp Toàn Bộ Lệnh "Mua" Limit Của Bạn. Dây Lưới Ask (Bán Bào) Của Bạn Mù Kẹt, CHƯA AI KHỚP! Cuối Ngày, Kho (Inventory) Của Bạn Chứa Ngập 10 BTC Rác Tại Đỉnh Giảm, Ôm Lỗ Cháy Mảng Dòng Vực To.
2.  **Chảy Toxic Độc Hại Trôi Đáy (Toxic Flow - Adverse Selection):** Khi Giao Cấu Với Cá Mập Lớn. Bác Giăng Lưới. Cá Voi Ngoạm. Nó Đập Mắc Xuyên Nát Lưới Mọc Móc Lấy Tài Sản. Lưới Của Bác Phá Nát! (Bot Quét Chậm Hơn Cú Rút). Cần Rắn Chặt Thuật Toán Đẩy Cửa Đu Lệch `Avellaneda-Stoikov` Đo Rủi Dọc Nhồi Dọn Cương Độ Biến Phóng Volatility Nằm Sốc Bảo Hiểm Bát Vỡ Lãi. 

> **Chốt Ngai Nghề Gộp Mảnh:** Trở Thành Nhà Cái Không Phải Giàu Nhanh May Rủi Rẽ. Đó Là Một Máy Kiếm Tiền Cắm Coding Quản Trị Cực Tĩnh Tần Số Không Ngắt Bào Gỉ Lĩnh Phạt. Trí Tuệ Mọc Mắt Khác Tụt Độ Hại Trác! Thăng Hoa Giàu Đi Mũi!!
