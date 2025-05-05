# Self-Attention

## Tổng quan
Self-Attention là một cơ chế cho phép mô hình xem xét mối quan hệ giữa các phần tử trong cùng một chuỗi dữ liệu. Nó tính toán trọng số cho mỗi phần tử dựa trên mối quan hệ của nó với các phần tử khác trong chuỗi, giúp mô hình nắm bắt được các phụ thuộc dài hạn và ngắn hạn.

## Lợi ích
- **Nắm bắt phụ thuộc dài hạn**: Self-Attention cho phép mô hình xem xét toàn bộ chuỗi dữ liệu, giúp nắm bắt được các phụ thuộc dài hạn.
- **Tính toán song song**: Các phép tính trong Self-Attention có thể được thực hiện song song, giúp tăng tốc độ huấn luyện.
- **Linh hoạt**: Self-Attention có thể được áp dụng cho nhiều loại dữ liệu khác nhau, như văn bản, hình ảnh, âm thanh.

## Cách triển khai
- **Tính toán Query, Key, Value**: Mỗi phần tử trong chuỗi được biến đổi thành các vector Query, Key, Value.
- **Tính toán Attention Scores**: Attention scores được tính bằng cách nhân Query với Key, sau đó chuẩn hóa bằng softmax.
- **Tính toán Output**: Output được tính bằng cách nhân Attention scores với Value.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, Self-Attention có thể được áp dụng trong các mô hình xử lý ngôn ngữ tự nhiên để nắm bắt mối quan hệ giữa các từ trong câu, giúp mô hình hiểu rõ hơn về ngữ cảnh của câu.

## Tài liệu tham khảo
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Transformer: A Novel Neural Network Architecture for Language Understanding](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html) 