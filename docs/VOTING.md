# Voting

## Tổng quan
Voting là một phương pháp kết hợp kết quả dự đoán của nhiều mô hình (các "base learners") để tạo ra kết quả cuối cùng. Có hai loại voting chính: hard voting (lấy kết quả dự đoán phổ biến nhất) và soft voting (lấy trung bình xác suất dự đoán của các mô hình).

## Lợi ích
- **Đơn giản**: Dễ triển khai, không cần huấn luyện thêm mô hình meta.
- **Tăng độ chính xác**: Kết hợp nhiều mô hình giúp tăng độ chính xác tổng thể.
- **Giảm sai số**: Giảm thiểu sai số do overfitting hoặc underfitting của từng mô hình riêng lẻ.

## Cách triển khai
- **Hard Voting**: Lấy kết quả dự đoán phổ biến nhất từ các mô hình (ví dụ: nếu 2 mô hình dự đoán lớp A và 1 mô hình dự đoán lớp B, kết quả cuối cùng là lớp A).
- **Soft Voting**: Lấy trung bình xác suất dự đoán của các mô hình (ví dụ: nếu 2 mô hình dự đoán lớp A với xác suất 0.7 và 0.8, 1 mô hình dự đoán lớp B với xác suất 0.6, kết quả cuối cùng là lớp A với xác suất trung bình 0.75).

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, voting có thể được áp dụng bằng cách:
- Huấn luyện các mô hình ResNet, EfficientNet, MobileNet trên dataset rác thải.
- Kết hợp kết quả dự đoán của các mô hình bằng hard voting hoặc soft voting để tạo ra kết quả cuối cùng.

## Tài liệu tham khảo
- [Ensemble Methods in Machine Learning](https://www.cs.cornell.edu/~caruana/ctp/ct.papers/caruana.icml04.icdm06long.pdf)
- [A Survey of Ensemble Learning Methods](https://arxiv.org/abs/1902.01975) 