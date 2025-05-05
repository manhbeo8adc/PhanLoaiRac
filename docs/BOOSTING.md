# Boosting

## Tổng quan
Boosting là một phương pháp ensemble learning, trong đó các mô hình (các "base learners") được huấn luyện theo thứ tự, mỗi mô hình sau tập trung vào các mẫu mà mô hình trước dự đoán sai. Mục đích là tạo ra một mô hình tổng thể mạnh hơn bằng cách kết hợp các mô hình yếu (weak learners) thành một mô hình mạnh (strong learner).

## Lợi ích
- **Tăng độ chính xác**: Boosting giúp cải thiện độ chính xác bằng cách tập trung vào các mẫu khó.
- **Giảm bias**: Giúp giảm thiểu sai số do underfitting, tăng độ chính xác tổng thể.
- **Tự động điều chỉnh**: Tự động điều chỉnh trọng số của các mẫu dựa trên kết quả dự đoán của các mô hình trước.

## Cách triển khai
- **Huấn luyện tuần tự**: Huấn luyện các mô hình theo thứ tự, mỗi mô hình sau tập trung vào các mẫu mà mô hình trước dự đoán sai.
- **Điều chỉnh trọng số**: Tăng trọng số cho các mẫu bị dự đoán sai, giảm trọng số cho các mẫu được dự đoán đúng.
- **Kết hợp kết quả**: Kết hợp kết quả dự đoán của các mô hình bằng cách lấy trung bình có trọng số hoặc voting.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, boosting có thể được áp dụng bằng cách:
- Huấn luyện các mô hình ResNet, EfficientNet, MobileNet theo thứ tự, mỗi mô hình sau tập trung vào các mẫu mà mô hình trước dự đoán sai.
- Kết hợp kết quả dự đoán của các mô hình bằng voting để tạo ra kết quả cuối cùng.

## Tài liệu tham khảo
- [A Short Introduction to Boosting](https://cseweb.ucsd.edu/~yfreund/papers/IntroToBoosting.pdf)
- [Gradient Boosting Machines](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3885826/) 