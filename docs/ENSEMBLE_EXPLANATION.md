# Ensemble trong Học Máy

## Tổng quan
Ensemble (tập hợp) trong học máy là một phương pháp kết hợp nhiều mô hình (các "base learners") để tạo ra một mô hình tổng thể mạnh hơn. Thay vì dựa vào một mô hình duy nhất, ensemble tận dụng sức mạnh của nhiều mô hình khác nhau, giúp giảm thiểu sai số, tăng độ chính xác, và tăng độ robust.

## Lợi ích
- **Giảm sai số**: Kết hợp nhiều mô hình giúp giảm thiểu sai số, tăng độ chính xác tổng thể.
- **Tăng độ robust**: Mô hình ensemble ít bị ảnh hưởng bởi nhiễu hoặc dữ liệu bất thường.
- **Tận dụng đa dạng**: Các mô hình khác nhau có thể học được các đặc trưng khác nhau, giúp bổ sung cho nhau.

## Cách triển khai
- **Bagging (Bootstrap Aggregating)**: Huấn luyện nhiều mô hình trên các tập dữ liệu con được lấy mẫu ngẫu nhiên từ tập dữ liệu gốc, sau đó lấy kết quả trung bình hoặc voting.
- **Boosting**: Huấn luyện các mô hình theo thứ tự, mỗi mô hình sau tập trung vào các mẫu mà mô hình trước dự đoán sai.
- **Stacking**: Huấn luyện một mô hình meta để kết hợp kết quả dự đoán của các mô hình base.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, ensemble có thể được áp dụng bằng cách:
- Huấn luyện nhiều mô hình khác nhau (ResNet, EfficientNet, MobileNet) trên dataset rác thải.
- Kết hợp kết quả dự đoán của các mô hình này để tạo ra kết quả cuối cùng.

## Tài liệu tham khảo
- [Ensemble Methods in Machine Learning](https://www.cs.cornell.edu/~caruana/ctp/ct.papers/caruana.icml04.icdm06long.pdf)
- [A Survey of Ensemble Learning Methods](https://arxiv.org/abs/1902.01975) 