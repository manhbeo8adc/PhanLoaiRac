# Stacking

## Tổng quan
Stacking (Stacked Generalization) là một phương pháp ensemble learning, trong đó một mô hình meta (meta-learner) được huấn luyện để kết hợp kết quả dự đoán của các mô hình base (base learners). Mục đích là tận dụng sức mạnh của nhiều mô hình khác nhau để tạo ra một mô hình tổng thể mạnh hơn.

## Lợi ích
- **Tận dụng đa dạng**: Kết hợp nhiều mô hình khác nhau, giúp bổ sung cho nhau.
- **Tăng độ chính xác**: Mô hình meta học cách kết hợp kết quả dự đoán của các mô hình base một cách tối ưu.
- **Linh hoạt**: Có thể sử dụng bất kỳ loại mô hình nào làm base learner hoặc meta-learner.

## Cách triển khai
- **Huấn luyện base learners**: Huấn luyện các mô hình base trên tập dữ liệu gốc.
- **Tạo tập dữ liệu meta**: Sử dụng kết quả dự đoán của các mô hình base trên tập validation để tạo ra tập dữ liệu meta.
- **Huấn luyện meta-learner**: Huấn luyện mô hình meta trên tập dữ liệu meta để kết hợp kết quả dự đoán của các mô hình base.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, stacking có thể được áp dụng bằng cách:
- Huấn luyện các mô hình ResNet, EfficientNet, MobileNet làm base learners.
- Sử dụng kết quả dự đoán của các mô hình này trên tập validation để tạo ra tập dữ liệu meta.
- Huấn luyện một mô hình meta (ví dụ: Logistic Regression, Random Forest) trên tập dữ liệu meta để kết hợp kết quả dự đoán của các mô hình base.

## Tài liệu tham khảo
- [Stacked Generalization](https://www.sciencedirect.com/science/article/abs/pii/S0893608005800231)
- [Ensemble Methods in Machine Learning](https://www.cs.cornell.edu/~caruana/ctp/ct.papers/caruana.icml04.icdm06long.pdf) 