# 📊 Data Analytics & Business Intelligence Knowledge Audit: Thử thách "SwiftRetail Growth Lab"

> **Mục đích:** Đo lường năng lực trích xuất ý nghĩa từ dữ liệu, tư duy thống kê, thiết kế chỉ số kinh doanh (KPIs) và kỹ năng kể chuyện bằng dữ liệu (Data Storytelling).
> **Phiếu trả lời:** [Tải mẫu tại đây](../templates/data-analytics-answer-template.md)
> 
> **Kịch bản:** Bạn là **Senior Data Analyst** của "SwiftRetail" - một chuỗi cửa hàng bán lẻ đa kênh (Omnichannel). Doanh thu quý vừa qua sụt giảm 15% mà không rõ nguyên nhân. CEO yêu cầu bạn thực hiện một cuộc "kiểm toán dữ liệu" toàn diện để tìm ra "lỗ hổng" và đề xuất chiến lược tăng trưởng mới.

---

## 🛠️ Thử thách 1: SQL Mastery & Data Cleaning (Trích xuất & Làm sạch)
*Đo lường năng lực xử lý dữ liệu thô và kỹ thuật truy vấn nâng cao.*

**Tình huống:** Dữ liệu bán hàng từ hệ thống POS (tại cửa hàng) và Website đang bị lệch nhau. Bạn cần hợp nhất chúng và xử lý các dòng dữ liệu trùng lặp hoặc thiếu thông tin khách hàng.

**Câu hỏi:**
1.  Viết một truy vấn SQL (sử dụng **CTE** và **Window Functions**) để tìm ra Top 5 khách hàng có chi tiêu cao nhất trong mỗi tháng của năm 2025.
2.  Làm thế nào để xử lý các giá trị trống (**NULL**) trong cột `Customer_ID` mà không làm mất đi thông tin doanh thu tổng? Bạn chọn phương pháp **Imputation** (điền giá trị) hay **Filtering** (loại bỏ)? Tại sao?

**Thước đo:**
*   **🟢 Beginner:** Biết dùng `SELECT`, `WHERE`, `GROUP BY` cơ bản.
*   **🔴 Expert:** Thành thạo **Window Functions** (`RANK`, `PARTITION BY`), xử lý được dữ liệu phân mảnh (Fragmented data) và tối ưu hóa hiệu suất truy vấn trên tập dữ liệu hàng triệu dòng.

---

## 📈 Thử thách 2: Statistical Thinking & A/B Testing (Tư duy Thống kê)
*Đo lường khả năng đọc hiểu bản chất con số, tránh các bẫy thống kê.*

**Tình huống:** Team Marketing chạy một chiến dịch khuyến mãi mới và báo cáo rằng "Giá trị đơn hàng trung bình (AOV) đã tăng lên". Tuy nhiên, bạn nhận thấy có một vài đơn hàng cực lớn (Outliers) làm lệch con số này.

**Câu hỏi:**
1.  Trong trường hợp có **Outliers** lớn, bạn nên dùng chỉ số nào để đại diện cho "giá trị trung tâm": **Mean** (Trung bình cộng) hay **Median** (Trung vị)? Tại sao?
2.  Thiết kế một bài toán **A/B Testing** cho tính năng "Gợi ý sản phẩm liên quan" trên App. Làm thế nào để xác định kết quả tăng trưởng là **Statistically Significant** (có ý nghĩa thống kê) chứ không phải do ngẫu nhiên?

**Thước đo:**
*   **🟢 Beginner:** Hiểu các khái niệm cơ bản nhưng dễ bị đánh lừa bởi các con số trung bình.
*   **🔴 Expert:** Hiểu về **Distribution** (Phân phối), **P-value**, **Confidence Interval**, và biết cách xử lý nhiễu dữ liệu để đưa ra kết luận chính xác.

---

## 🎯 Thử thách 3: Business Metrics & KPI Design (Thiết kế chỉ số)
*Đo lường sự am hiểu về vận hành kinh doanh (Domain Knowledge).*

**Tình huống:** CEO muốn biết "Sức khỏe thực sự" của tệp khách hàng hiện tại thay vì chỉ nhìn vào doanh số tổng.

**Câu hỏi:**
1.  Hãy phân tích sự khác biệt và mối liên hệ giữa **CAC** (Chi phí thu hút khách hàng) và **LTV** (Giá trị vòng đời khách hàng). Tỉ lệ **LTV/CAC** bao nhiêu là lý tưởng cho một doanh nghiệp bán lẻ?
2.  Thiết kế một bộ chỉ số để đo lường **Retention Rate** (Tỉ lệ giữ chân) theo từng nhóm khách hàng (Cohort Analysis). Bạn sẽ định nghĩa một "Khách hàng rời bỏ" (Churned Customer) như thế nào trong ngành bán lẻ?

**Thước đo:**
*   **🟢 Beginner:** Chỉ quan tâm đến các chỉ số bề nổi (Vanity metrics) như số lượt click, doanh thu tổng.
*   **🔴 Expert:** Thiết kế được hệ thống chỉ số tác động trực tiếp đến dòng tiền (Actionable metrics), hiểu sâu về **Unit Economics**.

---

## 🎨 Thử thách 4: Data Visualization & Storytelling (Kể chuyện bằng dữ liệu)
*Đo lường khả năng giao tiếp và thuyết phục thông qua hình ảnh.*

**Tình huống:** Bạn phải trình bày kết quả phân tích cho Hội đồng quản trị trong 10 phút. Bạn có một dashboard với 20 biểu đồ khác nhau.

**Câu hỏi:**
1.  Nguyên tắc **Data-to-Ink Ratio** là gì? Làm thế nào để loại bỏ các chi tiết thừa (Chart junk) để làm nổi bật thông điệp chính?
2.  Nếu muốn so sánh thị phần của 5 dòng sản phẩm chính theo thời gian, bạn sẽ chọn biểu đồ nào: **Pie Chart**, **Stacked Bar Chart**, hay **Line Chart**? Giải thích lựa chọn của bạn.

**Thước đo:**
*   **🟢 Beginner:** Dashboard lòe loẹt, nhiều màu sắc, biểu đồ không phù hợp với loại dữ liệu.
*   **🔴 Expert:** Áp dụng tốt tâm lý học thị giác (**Gestalt Principles**), dẫn dắt người xem từ "Dữ liệu" đến "Insight" và cuối cùng là "Hành động" (Actionable Insights).

---

## 🐍 Thử thách 5: Python & Automation (Lập trình & Tự động hóa)
*Đo lường năng lực xử lý nâng cao và tự động hóa quy trình báo cáo.*

**Tình huống:** Mỗi sáng bạn phải tốn 2 tiếng để tải 10 file Excel từ các nguồn khác nhau, gộp lại và gửi báo cáo qua email cho các trưởng phòng.

**Câu hỏi:**
1.  Bạn sẽ dùng thư viện nào trong Python (ví dụ: **Pandas**, **Openpyxl**) để tự động hóa quy trình này? Mô tả các bước chính trong code.
2.  Làm thế nào để thực hiện một phân tích dự báo cơ bản (ví dụ: **Linear Regression**) để ước tính doanh số cho tháng tới dựa trên dữ liệu lịch sử?

**Thước đo:**
*   **🟢 Beginner:** Vẫn làm thủ công hoặc chỉ biết dùng Excel Macro đơn giản.
*   **🔴 Expert:** Xây dựng được **Data Pipeline** tự động, biết sử dụng các mô hình học máy cơ bản để hỗ trợ ra quyết định dự báo (Predictive Analytics).

---

## 📊 Bảng tự chấm điểm (Scoring Rubric)

| Lĩnh vực | Thang điểm (1-10) | Gợi ý tự vấn |
| :--- | :---: | :--- |
| **SQL & Data Cleaning** | ____ / 10 | Bạn có thể lấy được dữ liệu chính xác từ một database "hỗn loạn" không? |
| **Statistical Thinking** | ____ / 10 | Bạn có phân biệt được "Tương quan" (Correlation) và "Nhân quả" (Causation) không? |
| **Business Domain** | ____ / 10 | Bạn có hiểu ngôn ngữ của các sếp (Doanh thu, Lợi nhuận, Chi phí) không? |
| **Visualization** | ____ / 10 | Dashboard của bạn có giúp người xem ra quyết định trong 30 giây không? |
| **Python & Auto** | ____ / 10 | Bạn có đang "bóc lột" sức lao động của chính mình cho những việc lặp đi lặp lại không? |

### 🏆 Xếp hạng năng lực Data Analyst:
*   **0 - 15 điểm:** **Data Junior / Excel User**. Bạn mới làm quen với công cụ. Hãy học lộ trình tại `domains/data-analytics/`.
*   **16 - 30 điểm:** **Proficient Data Analyst**. Bạn xử lý tốt các yêu cầu báo cáo định kỳ.
*   **31 - 45 điểm:** **Senior Data & BI Architect**. Bạn có khả năng tư vấn chiến lược dựa trên dữ liệu.
*   **46 - 50 điểm:** **Head of Data / Decision Scientist**. Bạn biến dữ liệu thành lợi thế cạnh tranh cốt lõi của doanh nghiệp.

---

## 🔑 Answer Key: Góc nhìn Chuyên gia (Expert Guidelines)

### Thử thách 1: SQL & Cleaning
*   **CTE:** Giúp code sạch, dễ đọc và bảo trì.
*   **Window Functions:** Dùng `DENSE_RANK()` để xếp hạng khách hàng.
*   **Handling Nulls:** Nếu `Customer_ID` thiếu, có thể gán nhãn "Guest" để vẫn tính được doanh thu tổng mà không làm sai lệch báo cáo định danh khách hàng.

### Thử thách 2: Statistics
*   **Mean vs Median:** Luôn kiểm tra phân phối dữ liệu. Nếu dữ liệu bị lệch (Skewed), Median là chỉ số đáng tin cậy hơn.
*   **A/B Test:** Cần xác định **Sample Size** trước khi chạy và dùng kiểm định giả thuyết (**T-test/Z-test**) để xác định mức ý nghĩa.

### Thử thách 3: Business Metrics
*   **Retention:** Phải dựa trên hành động tạo ra giá trị (Value-added action) chứ không chỉ là đăng nhập.
*   **Unit Economics:** LTV/CAC > 3 là dấu hiệu của một mô hình kinh doanh bền vững.

### Thử thách 4: Visualization
*   **Lựa chọn biểu đồ:** Line Chart là tốt nhất để xem xu hướng (Trend) theo thời gian. Stacked Bar Chart chỉ dùng khi muốn xem tỉ trọng trong tổng thể. Tránh Pie Chart khi có quá nhiều hạng mục.

### Thử thách 5: Python & Auto
*   **Pandas:** Dùng `pd.concat()` hoặc `pd.merge()` để gộp dữ liệu.
*   **Automation:** Thiết lập **Cron job** hoặc dùng **Airflow** để chạy script tự động hàng ngày.

---

## 🚀 Tài liệu bổ trợ để "Level Up"
*   **Lộ trình kỹ thuật:** [Data Analytics Roadmap](../../domains/data-analytics/README.md)
*   **Tư duy phân tích:** [Data Analytics Thinking](../../domains/data-analytics/data-analytics-thinking.md)
*   **Học SQL thực chiến:** [SQLZoo](https://sqlzoo.net/) hoặc [HackerRank SQL](https://www.hackerrank.com/domains/sql)
*   **Cộng đồng dữ liệu:** [Kaggle](https://www.kaggle.com/) (Học qua các cuộc thi và Dataset thật)
