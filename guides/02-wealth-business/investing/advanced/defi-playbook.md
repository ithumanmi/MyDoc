## DeFi Playbook (2026)

> Liên kết: Phần này là bản tóm tắt thực thi ngắn, nội dung nền tảng xem thêm [Crypto & DeFi Fundamentals](./crypto-defi.md) và chiến lược tổng thể tại [Digital Assets Strategy](./digital-assets-strategy.md). Khi nào dùng? DeFi = lớp chiến thuật/alpha bổ sung cho danh mục sau khi đã có core (cash/equity/bond) và khung phân bổ từ Digital Assets Strategy.

### 1) Trụ cột chính
- **Lending/Borrowing (Aave/Compound):** Over-collateral, chọn oracle đáng tin (Chainlink), theo dõi health factor; tránh stablecoin rủi ro. Với Aave, kiểm tra freeze/pause và mức LTV từng asset.
- **AMM/DEX (Uniswap/Curve/GMX):** Với stable pool (Curve) chú ý peg & depth; với volatile pool chú ý impermanent loss vs fee APR. GMX/Perp DEX: kiểm tra funding rate, open interest.
- **Derivatives (perpetuals/options):** dYdX/GMX cho perp; Lyra/Dopex cho options. Kiểm soát đòn bẩy; chỉ dùng margin nhỏ; đặt stop/cảnh báo thanh lý.
- **RWA/LST/LRT:** LST/LRT (stETH, wstETH, rsETH, ezETH...) – xem contract, cap, rủi ro re-stake. RWA (treasury, credit): xem audit, SPV, thanh khoản thứ cấp.

### 2) Quy trình tối thiểu
1) **Chain chọn lọc:** ưu tiên ETH/L2 lớn; TVL/liquidity đủ; tránh “APY lạ”.
2) **Ví & OpSec:** ví chính lưu trữ, ví thao tác riêng; revoke định kỳ; hardware nếu giá trị lớn; tránh ký contract lạ.
3) **Check smart contract:** audit, time-in-market, TVL, multisig (≥2/3), bug bounty; kiểm tra oracle (Chainlink?) và pause guardian.
4) **Entry nhỏ → tăng dần:** thử với vốn nhỏ, đo spread/slippage, test withdraw/unstake.
5) **Tracking:** dashboard (DeFiLlama, Dune), sheet dòng tiền, cảnh báo giá/thanh lý; ghi lại APY/fee và % vốn/giao thức.

### 2.1) Khi nào nên dùng DeFi trong portfolio?
- **Từ khung chiến lược:** Nếu core đã có equity/bond/cash và allocation cho digital assets (xem [Digital Assets Strategy](./digital-assets-strategy.md)), DeFi có thể là lớp alpha/thu nhập (lending, LP) hoặc hedge (perp, options) với tỷ trọng giới hạn.
- **Không nên:** dùng đòn bẩy cao khi chưa có emergency fund hoặc khi chưa vượt Level 2 (theo Investor Checklist). Tránh all-in stablecoins/tokens rủi ro để “farm” APY.

### 3) Rủi ro & hạn chế
- Smart contract bug, oracle manipulation, quản trị tập trung (multisig 1/1).
- Liquidity risk: pool mỏng, token mới. Kiểm tra depth & volume.
- Peg risk (stable/bridged asset), LST depeg, slashing risk với LRT.
- Regulatory/ToS: tránh sử dụng dịch vụ cấm địa lý; cân nhắc thuế/tuân thủ.

### 4) Checklist tham khảo
- [ ] Ví thao tác tách biệt, seed offline.
- [ ] Revoke allowance định kỳ (revoke.cash).
- [ ] Kiểm tra audit/multisig/TVL trước khi deposit; kiểm tra oracle & pause.
- [ ] Ghi log APY, risk rating từng giao thức; limit % vốn/giao thức; tránh farm token lạ không thanh khoản.
- [ ] Thiết lập cảnh báo giá/thanh lý.

### 5) Công cụ
- **Data:** DeFiLlama, Dune, TokenTerminal.
- **Security:** revoke.cash, Tenderly/DeBank for allowance view.
- **Automation:** Simple alerts (TradingView), sheet tracker.

### 6) Ví dụ cấu hình vị thế (gợi ý, không phải lời khuyên đầu tư)
- **Lending conservative:** 5% vốn portfolio vào Aave V3 ETH; collateral ETH (LTV 75%, HF mục tiêu >1.6). Vay USDC ≤30% collateral; không re-leverage. Dùng alert khi HF <1.4.
- **LP stable-stable:** 3% vốn vào Curve stables (USDC/DAI/USDT). Kỳ vọng fee APR 3-6%, IL ≈0 nếu peg ổn. Rút nếu peg lệch >0.5% hoặc volume giảm mạnh.
- **Perp hedge nhỏ:** 1% vốn làm margin trên dYdX; đòn bẩy 2-3x short BTC/ETH để hedge danh mục spot. Luôn đặt stop; sizing mục tiêu max loss <0.25% portfolio.
- **Options bảo hiểm:** 0.5% vốn mua put spread 1-3 tháng cho BTC/ETH trên Lyra/Dopex; coi như phí bảo hiểm giảm tail risk.

### 7) Bảng so sánh nhanh một số giao thức (2026)
| Loại | Giao thức | Điểm nổi bật | Rủi ro lưu ý |
| --- | --- | --- | --- |
| Lending | **Aave V3** | TVL cao, risk params chi tiết, hỗ trợ L2 | Freeze/pause có thể kích hoạt; theo dõi HF/liq threshold |
| Lending | **Compound V3** | Đơn giản, isolated USDC market | Ít tài sản hơn; phụ thuộc oracle |
| AMM | **Uniswap V3** | LP vị thế tập trung, phí tuỳ pool | IL cao nếu chọn range hẹp sai hướng |
| AMM/Stable | **Curve** | Deep liquidity cho stable/peg | Peg risk, rủi ro gauge/bribe token |
| Perp | **dYdX** | Orderbook, phí thấp, thanh khoản cao | Đòn bẩy; funding; compliance khu vực |
| Perp/GMX-style | **GMX** | Swap + perp, shared pool GLP/GMX | Rủi ro oracle, định giá index, IL cho LP |
| Options | **Lyra/Dopex** | On-chain options | Thanh khoản options mỏng; spread rộng |
| LST/LRT | **stETH/wstETH, rsETH, ezETH** | Yield staking/restaking | Depeg, slashing, rủi ro restake phức tạp |

### 8) Sizing gợi ý theo % NAV (tùy khẩu vị; không phải lời khuyên đầu tư)
- **Profile thận trọng:** Tổng digital assets ≤5-10% NAV; trong đó DeFi hoạt động (lending/LP/perp/options) ≤2-3% NAV; hạn chế đòn bẩy, ưu tiên stable/bluechip.
- **Profile cân bằng:** Digital assets ~10-20% NAV; DeFi hoạt động ≤5-7% NAV; mỗi giao thức ≤1-2% NAV; perp/options chủ yếu để hedge.
- **Profile mạo hiểm:** Digital assets 20-40% NAV; DeFi hoạt động 8-12% NAV; cap mỗi giao thức ≤2-3% NAV; perp tối đa 5% NAV margin với đòn bẩy thấp.

### 9) Checklist OpSec mở rộng (on-chain)
- [ ] **Ví phân tầng:** ví lạnh lưu trữ, ví thao tác nhỏ; không tái sử dụng ví chính để ký hợp đồng lạ.
- [ ] **RPC riêng/không theo dõi:** dùng RPC riêng (Alchemy/Infura custom) hoặc privacy RPC để giảm rò rỉ metadata.
- [ ] **Allowlist/Permission:** ưu tiên giao thức permissionless, contract đã audit; tránh dApp yêu cầu quyền quá mức; kiểm tra domain/phishing.
- [ ] **Chữ ký & quyền:** đọc kỹ permission khi ký; tránh ký `setApprovalForAll` không cần thiết; dùng revoke.cash định kỳ.
- [ ] **2FA & thiết bị:** phần mềm ví với 2FA nơi hỗ trợ; thiết bị sạch, tránh cài extension lạ; khóa màn hình, chống keylogger.
- [ ] **Bridge & stable chọn lọc:** ưu tiên bridge lớn/audit; tránh stablecoin/bridged asset ít thanh khoản; kiểm tra peg.
- [ ] **Alert & logging:** thiết lập cảnh báo giá/HF/thanh lý; lưu log giao dịch và seed/backup ngoại tuyến; kiểm tra lại địa chỉ nhận/gửi.

### 10) Bảng ví dụ phân bổ NAV (minh họa, giả định NAV = 100, không phải lời khuyên đầu tư)
| Profile | Digital assets tổng | DeFi hoạt động | Lending | LP stable | Perp hedge | Options hedge | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Thận trọng | 8 | 2 | 1.0 (Aave V3) | 0.7 (Curve stables) | 0.2 (dYdX 2-3x) | 0.1 (put spread) | HF>1.6; không re-leverage |
| Cân bằng | 15 | 5 | 2.0 | 1.5 | 1.0 | 0.5 | Cap mỗi giao thức ≤1-2%; perp để hedge spot |
| Mạo hiểm | 30 | 10 | 3.0 | 3.0 | 2.5 | 1.5 | Cap mỗi giao thức ≤2-3%; perp đòn bẩy thấp |

### 11) Thiết lập alert chi tiết (gợi ý công cụ TradingView/Telegram/Bot tự host)
- **Lending (Aave):** Alert khi **HF <1.5** (vàng) và **HF <1.4** (đỏ). Theo dõi tin nhắn risk/pause từ Aave (Twitter/Discord). Với tài sản thế chấp biến động cao, đặt ngưỡng cao hơn.
- **Perp funding:** Alert funding rate tuyệt đối >0.01%/8h (0.03%/ngày) để cân nhắc đóng/vị thế đối nghịch; hoặc khi funding flip dương → âm cho long.
- **Peg stable/Curve:** Alert khi giá bất kỳ stable trong pool lệch >0.5% so với 1.0 (0.995/1.005). Kiểm tra thêm depth/volume trước khi rút.
- **Price stop:** Đặt alert giá cho tài sản thế chấp chính (ETH/BTC) tại các mốc cắt lỗ hoặc nơi HF có nguy cơ chạm 1.3.
- **On-chain allowance:** Định kỳ (tuần/tháng) nhắc revoke; có thể script cron kiểm tra allowance lớn và gửi cảnh báo Telegram.