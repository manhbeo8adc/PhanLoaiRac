# Attention trong CNN

## Tổng quan
Attention trong CNN là một cơ chế cho phép mô hình tập trung vào các vùng quan trọng trong hình ảnh. Nó tính toán trọng số cho mỗi vùng trong hình ảnh dựa trên mức độ quan trọng của nó, giúp mô hình nắm bắt được các đặc trưng quan trọng và bỏ qua các vùng không liên quan.

## Lợi ích
- **Tập trung vào vùng quan trọng**: Attention trong CNN giúp mô hình tập trung vào các vùng quan trọng trong hình ảnh, giúp tăng độ chính xác.
- **Giảm nhiễu**: Bỏ qua các vùng không liên quan, giúp giảm nhiễu và tăng độ robust.
- **Linh hoạt**: Attention trong CNN có thể được áp dụng cho nhiều loại bài toán khác nhau, như phân loại, phát hiện đối tượng, phân đoạn.

## Cách triển khai
- **Tính toán Attention Map**: Attention map được tính bằng cách áp dụng một mạng con (sub-network) lên feature map của CNN.
- **Áp dụng Attention Map**: Attention map được áp dụng lên feature map để tạo ra feature map mới, trong đó các vùng quan trọng được nhấn mạnh.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, Attention trong CNN có thể được áp dụng để tập trung vào các vùng quan trọng trong hình ảnh rác thải, giúp mô hình phân loại chính xác hơn.

## Tài liệu tham khảo
- [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507)
- [CBAM: Convolutional Block Attention Module](https://arxiv.org/abs/1807.06521) 