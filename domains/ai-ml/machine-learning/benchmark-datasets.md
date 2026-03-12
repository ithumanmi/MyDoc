## 📊 Classic ML Benchmark Datasets

> [← Back to AI/ML Roadmap](../README.md)

Danh sách dataset chuẩn giúp luyện tập và benchmark các kỹ thuật Classic ML.

---

## 1. Regression

| Dataset | Mô tả | Link |
| --- | --- | --- |
| **California Housing** | Dự đoán giá nhà theo vùng. | [Scikit-learn](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset) |
| **Boston Housing** *(legacy)* | Dự đoán giá nhà Boston. (Cẩn trọng bias) | [UCI](https://archive.ics.uci.edu/ml/datasets/housing) |
| **Bike Sharing** | Dự đoán lượng thuê xe đạp theo giờ. | [UCI](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset) |
| **NYC Taxi Fare** | Dự đoán giá taxi, tập lớn để thử feature engineering. | [Kaggle](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction) |

---

## 2. Classification

| Dataset | Mô tả | Link |
| --- | --- | --- |
| **Titanic Survival** | Bài toán kinh điển phân loại sống/chết. | [Kaggle](https://www.kaggle.com/c/titanic) |
| **Credit Card Default** | Dự đoán khách hàng vỡ nợ. | [UCI](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients) |
| **Telco Customer Churn** | Dự đoán khách hàng rời mạng. | [Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn) |
| **MNIST (Classic)** | Nhận diện chữ số viết tay. | [Yann LeCun](http://yann.lecun.com/exdb/mnist/) |
| **Bank Marketing** | Phân loại khách hàng phản hồi chiến dịch. | [UCI](https://archive.ics.uci.edu/ml/datasets/bank+marketing) |

---

## 3. Unsupervised & Anomaly

| Dataset | Mô tả | Link |
| --- | --- | --- |
| **Mall Customers** | Phân cụm khách hàng theo thu nhập/chi tiêu. | [Kaggle](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python) |
| **Wholesale Customers** | Clustering B2B theo category mua hàng. | [UCI](https://archive.ics.uci.edu/ml/datasets/wholesale+customers) |
| **KDD Cup 99 / NSL-KDD** | Anomaly detection trong network traffic. | [Kaggle](https://www.kaggle.com/datasets/galaxyh/kddcup99-data) |
| **Credit Card Fraud Detection** | Imbalanced dataset phát hiện gian lận. | [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud) |

---

## 4. Time-Series / Forecasting

| Dataset | Mô tả | Link |
| --- | --- | --- |
| **M4, M5 Competition** | Chuỗi thời gian đa ngành (retail, macro). | [Kaggle](https://www.kaggle.com/c/m5-forecasting-accuracy) |
| **Electricity Load Diagrams** | Dự đoán nhu cầu điện (15 phút). | [UCI](https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014) |
| **Air Quality / PM2.5** | Forecast ô nhiễm. | [UCI](https://archive.ics.uci.edu/ml/datasets/Beijing+PM2.5+Data) |

---

## 5. Tools & Tips

*   **Datasets hub:** Hugging Face Datasets, Kaggle, UCI ML Repository.
*   **Data Versioning:** DVC, LakeFS.
*   **Evaluation:** Luôn chia train/validation/test chuẩn, kiểm tra imbalance.
*   **Ethics:** Cân nhắc bias trong dataset (Boston Housing, Adult Income...).

> 🧠 Tip: Khi luyện tập, hãy ghi lại notebook + metric baseline để so sánh giữa các thuật toán và feature set.
