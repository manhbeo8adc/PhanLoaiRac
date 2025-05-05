# Attention Map

## Tổng quan
Attention Map là một bản đồ trọng số (weight map) được tạo ra bởi cơ chế Attention, cho biết mức độ quan trọng của mỗi vùng trong dữ liệu đầu vào. Nó giúp mô hình tập trung vào các vùng quan trọng và bỏ qua các vùng không liên quan, từ đó cải thiện hiệu suất của mô hình.

## Đặc điểm
- **Trọng số**: Mỗi vùng trong Attention Map được gán một trọng số, thể hiện mức độ quan trọng của vùng đó.
- **Độ phân giải**: Attention Map có thể có độ phân giải khác nhau, tùy thuộc vào kích thước của dữ liệu đầu vào và mô hình.
- **Tính toán**: Attention Map được tính toán dựa trên các đặc trưng (features) của dữ liệu đầu vào, thông qua các phép biến đổi và chuẩn hóa.

## Cách triển khai
- **Tính toán Attention Scores**: Attention scores được tính bằng cách nhân các đặc trưng của dữ liệu đầu vào với các trọng số học được.
- **Chuẩn hóa**: Attention scores được chuẩn hóa bằng softmax để tạo ra Attention Map.
- **Áp dụng Attention Map**: Attention Map được áp dụng lên dữ liệu đầu vào để tạo ra dữ liệu mới, trong đó các vùng quan trọng được nhấn mạnh.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, Attention Map có thể được sử dụng để tập trung vào các vùng quan trọng trong hình ảnh rác thải, giúp mô hình phân loại chính xác hơn.

## Tài liệu tham khảo
- [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507)
- [CBAM: Convolutional Block Attention Module](https://arxiv.org/abs/1807.06521) 