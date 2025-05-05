# Bagging (Bootstrap Aggregating)

## Tổng quan
Bagging (Bootstrap Aggregating) là một phương pháp ensemble learning, trong đó nhiều mô hình (các "base learners") được huấn luyện trên các tập dữ liệu con được lấy mẫu ngẫu nhiên từ tập dữ liệu gốc. Kết quả dự đoán cuối cùng được tạo ra bằng cách lấy trung bình (cho bài toán hồi quy) hoặc voting (cho bài toán phân loại) từ các mô hình con.

## Lợi ích
- **Giảm phương sai (variance)**: Giúp giảm thiểu sai số do overfitting, tăng độ robust.
- **Tăng độ chính xác**: Kết hợp nhiều mô hình giúp tăng độ chính xác tổng thể.
- **Dễ song song hóa**: Các mô hình con có thể được huấn luyện song song, giúp tăng tốc độ huấn luyện.

## Cách triển khai
- **Bootstrap sampling**: Lấy mẫu ngẫu nhiên có hoàn lại từ tập dữ liệu gốc để tạo ra các tập dữ liệu con.
- **Huấn luyện mô hình con**: Huấn luyện một mô hình riêng biệt trên mỗi tập dữ liệu con.
- **Aggregation**: Kết hợp kết quả dự đoán của các mô hình con bằng cách lấy trung bình hoặc voting.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, bagging có thể được áp dụng bằng cách:
- Tạo nhiều tập dữ liệu con từ dataset rác thải bằng bootstrap sampling.
- Huấn luyện các mô hình ResNet, EfficientNet, MobileNet trên các tập dữ liệu con này.
- Kết hợp kết quả dự đoán của các mô hình bằng voting để tạo ra kết quả cuối cùng.

## Tài liệu tham khảo
- [Bagging Predictors](https://link.springer.com/article/10.1007/BF00058655)
- [Ensemble Methods in Machine Learning](https://www.cs.cornell.edu/~caruana/ctp/ct.papers/caruana.icml04.icdm06long.pdf) 