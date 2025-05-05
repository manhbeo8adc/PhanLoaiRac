# Backpropagation

## Tổng quan
Backpropagation là một thuật toán học máy được sử dụng để huấn luyện các mạng nơ-ron nhân tạo. Thuật toán này giúp mô hình học cách điều chỉnh các trọng số của nó để giảm thiểu hàm mất mát, từ đó cải thiện hiệu suất dự đoán.

## Đặc điểm
- **Lan truyền ngược**: Backpropagation hoạt động bằng cách lan truyền ngược lỗi từ lớp đầu ra về các lớp trước đó, giúp mô hình học cách điều chỉnh các trọng số.
- **Gradient Descent**: Thuật toán sử dụng gradient descent để cập nhật các trọng số, giúp mô hình tiến gần hơn đến điểm tối ưu.
- **Hiệu quả**: Backpropagation là một thuật toán hiệu quả, cho phép mô hình học từ dữ liệu lớn và phức tạp.

## Cách triển khai
- **Tính toán lỗi**: Lỗi được tính toán dựa trên sự khác biệt giữa giá trị dự đoán và giá trị thực tế.
- **Lan truyền ngược lỗi**: Lỗi được lan truyền ngược từ lớp đầu ra về các lớp trước đó, giúp mô hình học cách điều chỉnh các trọng số.
- **Cập nhật trọng số**: Các trọng số được cập nhật dựa trên gradient của hàm mất mát, giúp mô hình tiến gần hơn đến điểm tối ưu.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, Backpropagation có thể được sử dụng để huấn luyện mô hình phân loại rác thải, giúp mô hình học cách dự đoán chính xác nhãn của rác thải.

## Tài liệu tham khảo
- [Understanding Backpropagation](https://towardsdatascience.com/understanding-backpropagation-algorithm-7bb3aa2f95fd)
- [Backpropagation in Neural Networks](https://www.analyticsvidhya.com/blog/2020/01/fundamentals-deep-learning-backpropagation-algorithm/) 