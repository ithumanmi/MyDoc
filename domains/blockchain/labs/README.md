# 🧪 Phòng Thí Nghiệm Algo Trading & MEV On-chain Khủng (Labs)

> [← Back to Blockchain Index](../README.md)

Nơi Đóng Khung Môi Trường Máy Móc Đánh Lệnh Thực Chiến. Những Script Code Cứa Máu Trực Tiếp Trên Nhu Cầu Tiềm Tài Hệ Mạng Block/Sàn CEX.

---

## 🕷️ Lab 1: MEV Sniper Đón Nghe Mempool Node Gắp Pendings Rực Rỡ Bắt Giao Dịch
Định hình Thiết kế Code Node.js Móc Kết Mạng Ổ RPC Vặn Bắt Tiếng Khóc Của Nhóm Giao Dịch Rẻ Đợi Rót Chết Trước Cửa Vách: 

1. Đăng Ký Tạo Node Sống Sốc Socket `Alchemy/Infura` WSS Đỉnh Lưới.
2. Viết App Sứ NodeJs Code Đan Mạch Theo Đuôi Khang Mạng Mempool Tự Tạo Đất Đón.

```javascript
/* Lọc Dò MemPool Truyền Khuyến Cáo Thẳng Lưới Router Máy WSS Alchemy Giao Sóng Sạch */
const ethers = require('ethers');

// Ket Noi Khung Mạng Xuyen Khong Ngu Ngay WSS 
const TrụcMạngNodeGiaWSSPROVIDER = new ethers.providers.WebSocketProvider('wss://eth-mainnet.alchemyapi.io/v2/LoiKhóaAPIXoaMat');
const ToaDoSanDEXRouterUniswap = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'; // Router Rung Rợn Gốc Bắt Chân 

async function ThảThínhSoiMempool() {
    console.log("Ban Đang Nằm Dưới Rừng Tối... Nghe Róp Ráp Từng Hơi Thở Pendings...");

	// Rình Đoán Sự Kiện "Pendings" - Giao Dịch Gấp Khung Rất Yếu Bay Thảo Loanh Quanh Dang Rắn Block Khung Chua Cầm Ké 
    TrụcMạngNodeGiaWSSPROVIDER.on("pending", async (txDấuDặnRáchVétBáoGiaoDịch) => { 
        try {
            const HienRaThonGiaoVach = await TrụcMạngNodeGiaWSSPROVIDER.getTransaction(txDấuDặnRáchVétBáoGiaoDịch); 
             if (HienRaThonGiaoVach && HienRaThonGiaoVach.to === ToaDoSanDEXRouterUniswap) { 
                 // Phát Hiện Cá Mập Mới Dăng Len Lệnh Vao Ung Uniswap!!! Bớ Bát Phá Xong Check Hàm Đầu (Swap, AddLiq)!
                   console.log(`Phat Hien Cá Map Vang Vay Lenh Trục: ${txDấuDặnRáchVétBáoGiaoDịch}`);
                 // .. Giải Mã Sợi Dây Input data Đọc Chốt Coin Đuổi, Thả FlashBot Đổi Bribe Đút Khúc Front-RUN Gấp Phanh Nặng Lượm !!!
             }
        } catch(VòngBiẾuKémMangCăng) {} // Rớt Khung Node Qua Vi Bấm Cứu 
    });
}
ThảThínhSoiMempool();
```
> Kéo Lệnh Này Trong Git Bash Hoặc Window CMD. Ngồi Nhìn Ma Trận Giao Dịch Xẹt Giấy Thần Tốc Réo Xâu Qua Mắt Bạn Nhanh Hơn Mắt Mạng Lắc Bóng Của User Normal! Đầu Vào Chiến Lưới MEV! Mỏ Vàng!

---

## ⚡ Lab 2: Mượn Tiền Cứu Thế Flash Loan Không Thế Chấp Rút 1 Triệu Đô Quyền Sol Trắng (AAVE)

Bạn Không Cần 1 Đồng Vốn Nào Dắt Túi Sinh Nghiệp? Chơi Hack Game Hủy Tiêu Cấp Vũ Trụ Của Solidity Giới DeFi Cung AAVE Rộng Thượng Điền: 
Tự Khúc Vay - Trade Cướp - Trả Nợ Xù Lợi Vang Ác Càng Tốc Độ 1 Khung Giao Dịch Block. Nhanh, Không Ai Kịp Đòi Vỡ Hầm:

```solidity
pragma solidity ^0.8.0;

import "@aave/core-v3/contracts/flashloan/base/FlashLoanSimpleReceiverBase.sol"; // Bùa Nâng Chống Bắn Sẵn Cơ AAVE Code Mở Lấp Gọi File
// ....

contract FlashLoanRachToiGionBot is FlashLoanSimpleReceiverBase {
     constructor(IPoolAddressesProvider NguonChoVayTrumBankGoc)
        FlashLoanSimpleReceiverBase(NguonChoVayTrumBankGoc) {} 

	// Ham Bat Dau Dở Tro Di Vay : Ném Lệnh Cho Tôi Xin Mua Muoc VAY USDC Đi Mày AAVE!
    function YeuCauMượnTiềnKhongDoiNhanhAAVE(address diaChiLoaiCoin(USDC), uint256 SoTienKhoanThung_1TrieuDoLa_Can_Luom) external {
        POOL.flashLoanSimple(
            address(this),
            diaChiLoaiCoin(USDC),
            SoTienKhoanThung_1TrieuDoLa_Can_Luom,
            "",
            0 // Mo Rộng Kiem Soat
        );
    } 

	// Ham Sinh Mệnh Rót (Callback) - Khi AAVE Thả Bọc 1 Triệu Đô Xong Vao Nách Bạn: 
    function executeOperation(address assetUSDC, uint256 amountNhanDC1Trieu, uint256 PhiLaiDoiHoiToThaoKhoc, address KhóaNguonBiTịchNgục, bytes calldata KhangPhạmVô)
        external override returns (bool) {
        
		// !!!!!!!!!!!!!!!!!!!!!!! KHÚC CHIẾN MƯU SỐNG !!!! 
		// Trong Tay Hiện Có 1 Triệu Đô Mới Rút Giây. Code Call Chặn Qua Uniswap -> Bắn Xố Mua Rẻ Lấy Coin A -> Bay Router Vượt Xới Nước Mang Sang DexSushiSwap  Xả Coin B Giá Căng Mở.
        // Hưởng Gom Thùng Dư Được Chén Đoạt $2000 Đô Lũy Thôi. (Arbitrage Hoàn Dư)
		// !!!!!!!!!!!!!!!!!!!!!!! 

         uint256 KhoanCanTraCatNganDeDapLoiMangSong = amountNhanDC1Trieu + PhiLaiDoiHoiToThaoKhoc; // Tien Rút + 0.09% Phí Bạt

		// Chấp Nhận Khóa Van Vọt Rút Tiền Quay Nách Trả Bọc (Nợ Biến Mất Cung Gốc Đời Xóa Đứt). Ban Cầm Khứ Hồi Tiền Lãi Bỏ Sạch Ví Hoàn Thiện Game Flash Xỉa Tốc!. 
        IERC20(assetUSDC).approve(address(POOL), KhoanCanTraCatNganDeDapLoiMangSong);
        return true; 
    }
}
```

---

## 📈 Lab 3: Lưới Tình Máy Phanh Réo Hồn Bot (CEX Grid Bot Python Chống Lừa Đổi) 

Lệnh Script Khung CCXT Python Đóng Rập. 

```python
import ccxt 
import time

sannbinance_BotChoiThe = ccxt.binance({
    'apiKey': 'Rải API Cắm Cổng Key Rỗng Đừng Chụp',
    'secret': 'Xé Lộ Key Rụng Khép Thùng Đáy Bí',
    'enableRateLimit': True, 
})

Lưới_Rao_Khung_Can_Moc_Vot = [92000, 93000, 94000, 95000, 96000, 97000] # Luoi Thu Bẫy Tinh Bot Gặp Trục Treo Lưới!
Trọng_Cung_Tiền_MoiLệnhBiMat_DoLa = 20 # Bốc Mỗi Tay 20$ Tép Lót Đặt 

def BanCuaLuoiRongQuyNhanChốngThao():
    # Lay Rõ Giá Mạng BitCoin Real 
    PháGiaBitcoinDangRoiChờThiDĐoanVừa = sannbinance_BotChoiThe.fetch_ticker('BTC/USDT')['last']

    # Thả Điểm Trả Rình Khung Lập Giao Kéo Ném Giá Xéo Cho Xa Để Máy Đói Nhanh 
    for moc_rào_lưới in Lưới_Rao_Khung_Can_Moc_Vot:
        if moc_rào_lưới < PháGiaBitcoinDangRoiChờThiDĐoanVừa: # Dưới Vực Rớt? Xắp Ráp Lệnh BUY Cứ Mức
             sannbinance_BotChoiThe.create_limit_buy_order('BTC/USDT', Trọng_Cung_Tiền_MoiLệnhBiMat_DoLa / moc_rào_lưới, moc_rào_lưới)
        elif moc_rào_lưới > PháGiaBitcoinDangRoiChờThiDĐoanVừa: # Tren Đỉnh Bật ? Rào Lệnh SELL Tháo Hoàn! 
             sannbinance_BotChoiThe.create_limit_sell_order('BTC/USDT', Trọng_Cung_Tiền_MoiLệnhBiMat_DoLa / moc_rào_lưới, moc_rào_lưới)
            
while True: # Vòn Lặp Tái Sinh Chống Rễ Mạng VPS Chạy Điên ! 
      BanCuaLuoiRongQuyNhanChốngThao()
      time.sleep(3600)  # Thả Nghỉ Tranh Rate limit 3600S / Tieengs Chay Giũa Vong Bot Cuoc Song Chien Lưới Tiền Giao Ảo Máy Trả Cong Vực Cạn Phai!! Kiem Tien Chieu !
```
Bơm Xát Ngập Bot Trading Bẫy Nằm Rải 2 Bên Tháp Giá Đội Cực Biến Code Tố Python CCXT Không Run Lệ Trắng! Bắt Thuật Lưới! Rắn Nhóm Sinh Thành Labs Xếp Đạo Crypto Khủng Lực!
