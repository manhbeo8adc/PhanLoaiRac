# Data Augmentation

## Tổng quan
Data Augmentation là một kỹ thuật tăng cường dữ liệu, trong đó các biến đổi được áp dụng lên dữ liệu gốc để tạo ra nhiều mẫu huấn luyện hơn. Mục đích là tăng độ đa dạng của dữ liệu, giúp mô hình học được các đặc trưng bất biến với các biến đổi của ảnh, từ đó tăng độ robust và giảm overfitting.

## Lợi ích
- **Tăng dữ liệu**: Tạo ra nhiều mẫu huấn luyện hơn từ dữ liệu gốc, giúp mô hình học hiệu quả hơn.
- **Tăng độ robust**: Giúp mô hình học được các đặc trưng bất biến với các biến đổi của ảnh (xoay, lật, thay đổi độ sáng, độ tương phản, ...).
- **Giảm overfitting**: Tăng độ đa dạng của dữ liệu giúp mô hình tránh được overfitting.

## Cách triển khai
- **Biến đổi hình học**: Xoay, lật, cắt, thay đổi kích thước, ...
- **Biến đổi màu sắc**: Thay đổi độ sáng, độ tương phản, độ bão hòa, ...
- **Biến đổi nhiễu**: Thêm nhiễu Gaussian, nhiễu muối tiêu, ...
- **Biến đổi kết hợp**: Kết hợp nhiều biến đổi khác nhau để tạo ra dữ liệu đa dạng hơn.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, data augmentation có thể được áp dụng bằng cách:
- Xoay ảnh rác thải với các góc khác nhau.
- Lật ảnh theo chiều ngang hoặc dọc.
- Thay đổi độ sáng, độ tương phản của ảnh.
- Thêm nhiễu để mô phỏng điều kiện ánh sáng khác nhau.

## Tài liệu tham khảo
- [Understanding Data Augmentation for Classification: When to Warp?](https://arxiv.org/abs/1609.08764)
- [Data Augmentation in Deep Learning](https://towardsdatascience.com/data-augmentation-in-deep-learning-5847bdd0e90c) 