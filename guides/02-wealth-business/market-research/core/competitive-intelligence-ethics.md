## Competitive Intelligence & Ethics

### Ranh giới nên/không nên
- **OK:** Public data (website, pricing page, public API with allowed usage), review store, ads library, public traffic estimates, job posts, investor deck public, docs không yêu cầu login.
- **Không OK:** Dữ liệu dưới NDA, nội bộ/riêng tư, database leak, social engineering, lừa user/support, mạo danh để xin access.
- **Scraping:** Tôn trọng robots.txt, rate limit; không bypass paywall/DRM. Nếu ToS cấm scraping, không làm.
- **Fake account:** Tránh tạo tài khoản giả/ẩn danh để vượt ToS; ưu tiên dùng trial hợp lệ hoặc bản freemium.
- **Reverse engineering:** Kiểm tra EULA/ToS; nếu cấm RE, không disassemble/decompile; thay vào đó quan sát hành vi bề mặt (UX flow, pricing trigger).

### Best practices
- **Minh bạch nguồn:** Ghi rõ nguồn và ngày thu thập; tránh chỉnh sửa dữ liệu gốc.
- **An toàn pháp lý:** Với thị trường có luật bảo vệ dữ liệu (GDPR/CCPA), không lưu PII nếu không cần; xin consent khi phỏng vấn.
- **Hạn chế tải nặng:** Dùng official API nếu có; đặt rate limit; không DDoS.
- **Đạo đức nghiên cứu:** Không social engineering, không mạo danh, không khai thác lỗ hổng.

### Checklist nhanh
- [ ] Nguồn là public, không NDA
- [ ] ToS/robots.txt được tôn trọng
- [ ] Không dùng tài khoản giả để vượt chặn
- [ ] Ghi nguồn & timestamp
- [ ] Không thu thập PII không cần thiết

> Liên quan: [Competitor Analysis Framework](./competitor-analysis-framework.md)