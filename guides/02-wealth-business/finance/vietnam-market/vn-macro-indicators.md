# 📊 Vietnam Macro Indicators Dashboard

## 1. Chỉ số lõi (theo dõi hàng tháng/quý)
| Nhóm | Chỉ số | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| Tăng trưởng | GDP YoY (quý), IIP, Retail sales | GSO | GDP theo quý; IIP cho sản xuất, retail cho tiêu dùng |
| Lạm phát | CPI YoY, Core CPI | GSO | Ảnh hưởng lãi suất điều hành |
| Tiền tệ | Policy rate (OMO/Rediscount), Credit growth, M2 | SBV | Room tín dụng, bơm/hút thanh khoản |
| Cán cân | Trade balance, FDI đăng ký/giải ngân | GSO, MPI | FDI dẫn dắt KCN, logistics |
| Thị trường vốn | VNIndex, P/E, Margin debt | HOSE/HNX/FiinPro | Đánh giá định giá & rủi ro đòn bẩy |
| Trái phiếu | G-bond 5Y/10Y yield, C-bond issuance | HNX/FiinPro | Spread G/C bond, khối lượng phát hành |
| Bất động sản | Giá sơ cấp/2nd tier tại HN/TPHCM, Absorption | CBRE/Savills/BCTC | Phản ánh chu kỳ BĐS |

## 2. Dashboard gợi ý
- **Credit growth vs GDP**: credit impulse.
- **CPI vs Policy rate**: dự báo nới/siết tiền tệ.
- **FDI disbursement**: momentum ngành KCN.
- **Bond maturity wall**: đáo hạn theo quý, theo ngành.
- **ETF & foreign flow**: mua/bán ròng theo tuần.

## 3. Cadence cập nhật
- **Monthly:** CPI, trade, FDI giải ngân, policy rate, VNIndex, bond yield.
- **Quarterly:** GDP, credit growth, EPS cập nhật, phát hành C-bond.

## 4. Tooling
- Google Sheet/Notion với API (FiinPro, SSI, HSX) hoặc manual import CSV.
- Alert khi CPI vượt target, credit growth chậm, yield G-bond tăng nhanh.

---
> Quay lại [Overview](./README.md)