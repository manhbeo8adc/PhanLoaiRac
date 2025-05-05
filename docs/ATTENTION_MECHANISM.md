# Attention Mechanism

## Tổng quan
Attention Mechanism là một kỹ thuật trong học sâu, cho phép mô hình tập trung vào các phần quan trọng của dữ liệu đầu vào, bỏ qua các phần không liên quan. Ban đầu được phát triển cho các bài toán xử lý ngôn ngữ tự nhiên (NLP), attention mechanism đã được áp dụng rộng rãi trong nhiều lĩnh vực khác, bao gồm thị giác máy tính (computer vision).

## Lợi ích
- **Tập trung vào thông tin quan trọng**: Giúp mô hình học được các đặc trưng quan trọng, bỏ qua các vùng nhiễu.
- **Tăng khả năng giải thích**: Mô hình có thể giải thích được tại sao đưa ra quyết định dựa trên các vùng được chú ý.
- **Cải thiện hiệu suất**: Tăng độ chính xác và độ robust của mô hình.

## Cách triển khai
- **Self-Attention**: Mô hình tự tính toán mức độ quan trọng của từng phần tử trong dữ liệu đầu vào.
- **Cross-Attention**: Mô hình tính toán mức độ quan trọng của từng phần tử trong một dữ liệu dựa trên một dữ liệu khác (ví dụ: trong bài toán dịch máy, tính toán mức độ quan trọng của từng từ trong câu nguồn dựa trên câu đích).
- **Attention trong CNN**: Sử dụng các lớp attention trong mạng CNN để tập trung vào các vùng quan trọng trong ảnh.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, attention mechanism có thể được áp dụng bằng cách:
- Sử dụng các lớp attention trong mạng CNN để tập trung vào các vùng chứa vật liệu, vùng có nhãn dán, v.v.
- Kết hợp attention với các kiến trúc khác như Transformer để cải thiện hiệu suất.

## Tài liệu tham khảo
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507) 