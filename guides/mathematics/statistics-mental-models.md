# 📊 Thống kê & Những cái bẫy tư duy (Statistics Mental Models)

## 1. Định lý Giới hạn Trung tâm (Central Limit Theorem - CLT)
Định lý kỳ diệu nhất của thống kê.
*   **Nội dung:** Cho dù quần thể gốc có phân phối kỳ dị thế nào (méo mó, hỗn loạn), nếu bạn lấy đủ nhiều mẫu ngẫu nhiên (sample) và tính trung bình của chúng, thì các giá trị trung bình này sẽ tuân theo **Phân phối chuẩn (Normal Distribution)** hình chuông.
*   **Ý nghĩa:** Đây là lý do tại sao chúng ta có thể dùng thống kê để dự đoán các hiện tượng phức tạp. Sự hỗn loạn của cá nhân bị triệt tiêu khi xét trên đám đông.
*   **Ứng dụng:** Thăm dò dư luận, Kiểm soát chất lượng sản phẩm (Six Sigma).

## 2. Khoảng tin cậy (Confidence Interval) & Sai số chuẩn
Đừng bao giờ tin vào một con số đơn lẻ (Point Estimate). Hãy tin vào một khoảng (Range).
*   **Sai:** "Ứng viên A sẽ được 55% phiếu bầu."
*   **Đúng:** "Ứng viên A sẽ được từ 52% đến 58% phiếu bầu, với độ tin cậy 95%."
*   **Công thức (cho tỷ lệ):** $\hat{p} \pm Z \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$
    *   $n$ càng lớn (mẫu càng to) -> Khoảng tin cậy càng hẹp -> Độ chính xác càng cao.
    *   **Bài học:** Khi đọc báo cáo, luôn hỏi: "Cỡ mẫu (n) là bao nhiêu?". Nếu $n=10$, vứt báo cáo đó đi.

## 3. Trị số p (p-value) & Ý nghĩa thống kê
Khái niệm bị hiểu sai nhiều nhất.
*   **Giả thuyết không ($H_0$):** Không có gì đặc biệt xảy ra (Ví dụ: Thuốc không có tác dụng, sự khác biệt chỉ do ngẫu nhiên).
*   **p-value:** Xác suất để thấy dữ liệu như hiện tại (hoặc cực đoan hơn) *nếu* $H_0$ là đúng.
    *   $p < 0.05$ (5%): Khả năng ngẫu nhiên xảy ra chuyện này rất thấp -> Ta bác bỏ $H_0$ -> Kết luận thuốc có tác dụng (**Có ý nghĩa thống kê**).
    *   $p > 0.05$: Có thể do ăn may -> Không đủ bằng chứng kết luận.
*   **Cảnh báo (p-hacking):** Nếu bạn thử 20 giả thuyết khác nhau, xác suất 1 cái có $p < 0.05$ do ngẫu nhiên là rất cao. Đừng "tra tấn dữ liệu cho đến khi nó thú nhận".

## 4. Tương quan (Correlation) vs Nhân quả (Causation)
Hệ số tương quan $r$ chạy từ -1 đến 1.
*   $r = 1$: Tương quan dương hoàn toàn.
*   $r = 0$: Không liên quan.
*   **Bẫy:** Gà gáy ($A$) và Mặt trời mọc ($B$) có tương quan cực cao ($r \approx 1$). Nhưng giết gà không làm mặt trời tắt nắng.
*   **Confounding Variable (Biến gây nhiễu):** Yếu tố $Z$ tác động lên cả $A$ và $B$. (Ví dụ: Ăn kem và Chết đuối cùng tăng do Nhiệt độ nóng).

## 5. Phân phối Chuẩn vs Phân phối Đuôi Dày (Normal vs Fat-tailed)
*   **Mediocristan (Thế giới trung bình):** Chiều cao, Cân nặng. Tuân theo phân phối chuẩn. Sự kiện cực đoan (người cao 3m) là không thể.
*   **Extremistan (Thế giới cực đoan):** Tài sản, Thị trường chứng khoán, Dịch bệnh. Tuân theo **Power Law**.
    *   Quy tắc 80/20 (Pareto).
    *   Sự kiện "Thiên nga đen" (Black Swan): Một sự kiện hiếm gặp (đuôi dày) có thể xóa sổ toàn bộ thành quả.
    *   **Bài học:** Đừng dùng các công thức rủi ro của Phân phối chuẩn (như Value at Risk - VaR) cho thị trường tài chính. Bạn sẽ phá sản.

## 6. Nghịch lý Simpson (Simpson's Paradox)
Xu hướng xuất hiện trong các nhóm dữ liệu nhỏ nhưng lại đảo ngược khi gộp chung các nhóm lại.
*   **Ví dụ:** Tỷ lệ trúng tuyển ĐH Berkeley (1973).
    *   Nam: 44% trúng tuyển. Nữ: 35% trúng tuyển. -> Có vẻ phân biệt đối xử nữ giới?
    *   Khi chia theo từng khoa: Nữ giới có tỷ lệ trúng tuyển **cao hơn** nam giới ở hầu hết các khoa.
    *   **Lý do:** Nữ giới nộp đơn vào các khoa khó (tỷ lệ chọi cao), Nam giới nộp vào các khoa dễ.
*   **Bài học:** Luôn nhìn sâu vào bối cảnh (context) và các biến ẩn. Dữ liệu tổng hợp (Aggregated data) thường che giấu sự thật.

## 7. Hồi quy về trung bình (Regression to the Mean)
Trong các sự kiện có yếu tố may mắn, một kết quả cực đoan (quá tốt/quá xấu) thường sẽ được theo sau bởi một kết quả bình thường hơn.
*   **Thể thao:** Cầu thủ lên bìa tạp chí (sau một mùa giải xuất thần) thường chơi dở vào mùa sau. Không phải do "lời nguyền", mà do họ chỉ đang quay về phong độ thực (Mean) sau một chút may mắn.
*   **Khen thưởng/Trừng phạt:** Bạn mắng nhân viên khi họ làm kém -> Họ làm tốt lên (thực ra là quay về trung bình). Bạn khen khi họ làm tốt -> Họ làm kém đi. -> Dẫn đến ảo tưởng rằng "Trừng phạt hiệu quả hơn Khen ngợi".

---

## 🛠️ Ứng dụng Thực chiến (Life Applications)

### 1. Trung bình (Mean) vs Trung vị (Median)
Khi đọc báo "Lương trung bình của người Việt là X triệu". Hãy cẩn thận.
*   Nếu Bill Gates bước vào quán bar, lương "trung bình" của mọi người trong quán sẽ tăng lên hàng tỷ đô. Nhưng lương thực tế (Median) không đổi.
*   **Bài học:** Với những dữ liệu có phân phối đuôi dày (Lương, Tài sản), hãy nhìn **Median** (Trung vị - con số ở giữa) thay vì Mean.

### 2. Base Rate Neglect (Bỏ qua tỷ lệ cơ bản)
Bạn muốn mở nhà hàng. Bạn thấy ông A mở nhà hàng thành công rực rỡ. Bạn nghĩ mình cũng thế.
*   **Thống kê:** 60% nhà hàng phá sản trong năm đầu. 80% phá sản trong 5 năm. Đây là Tỷ lệ cơ bản (Base Rate).
*   **Tư duy:** Đừng chỉ nhìn vào trường hợp cá biệt (Inside View). Hãy nhìn vào con số thống kê của cả ngành (Outside View) để tính toán rủi ro thực tế.

### 3. False Positive (Dương tính giả) & Spam Filter
Tại sao email quan trọng đôi khi vào Spam?
*   Hệ thống chấp nhận sai sót: Thà giết nhầm (False Positive - Thư thật vào Spam) còn hơn bỏ sót (False Negative - Thư rác vào Inbox)? Không, thực tế ngược lại.
*   Trong bộ lọc Spam, **False Positive** (Chặn nhầm thư quan trọng) là lỗi nghiêm trọng hơn nhiều so với **False Negative** (Để lọt thư rác).
*   **Ứng dụng:** Khi thiết lập các quy tắc (trong code hoặc quản lý), hãy tự hỏi: Loại lỗi nào tôi chấp nhận được? (Thà mất tiền hay thà mất cơ hội?).
