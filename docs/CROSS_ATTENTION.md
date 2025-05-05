# Cross-Attention

## Tổng quan
Cross-Attention là một cơ chế cho phép mô hình xem xét mối quan hệ giữa hai chuỗi dữ liệu khác nhau. Nó tính toán trọng số cho mỗi phần tử trong chuỗi thứ nhất dựa trên mối quan hệ của nó với các phần tử trong chuỗi thứ hai, giúp mô hình nắm bắt được các phụ thuộc giữa hai chuỗi.

## Lợi ích
- **Nắm bắt phụ thuộc giữa hai chuỗi**: Cross-Attention cho phép mô hình xem xét mối quan hệ giữa hai chuỗi dữ liệu, giúp nắm bắt được các phụ thuộc giữa chúng.
- **Tính toán song song**: Các phép tính trong Cross-Attention có thể được thực hiện song song, giúp tăng tốc độ huấn luyện.
- **Linh hoạt**: Cross-Attention có thể được áp dụng cho nhiều loại dữ liệu khác nhau, như văn bản, hình ảnh, âm thanh.

## Cách triển khai
- **Tính toán Query, Key, Value**: Mỗi phần tử trong chuỗi thứ nhất được biến đổi thành các vector Query, mỗi phần tử trong chuỗi thứ hai được biến đổi thành các vector Key và Value.
- **Tính toán Attention Scores**: Attention scores được tính bằng cách nhân Query với Key, sau đó chuẩn hóa bằng softmax.
- **Tính toán Output**: Output được tính bằng cách nhân Attention scores với Value.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, Cross-Attention có thể được áp dụng trong các mô hình dịch máy để nắm bắt mối quan hệ giữa câu nguồn và câu đích, giúp mô hình dịch chính xác hơn.

## Tài liệu tham khảo
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Transformer: A Novel Neural Network Architecture for Language Understanding](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html) 