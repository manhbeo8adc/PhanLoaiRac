# Transfer Learning

## Tổng quan
Transfer Learning là một phương pháp học máy, trong đó kiến thức từ một mô hình đã được huấn luyện trên một nhiệm vụ nguồn (source task) được chuyển giao để cải thiện hiệu suất cho một nhiệm vụ đích (target task). Thay vì huấn luyện từ đầu, transfer learning tận dụng các đặc trưng đã học được từ dữ liệu lớn để áp dụng cho dữ liệu nhỏ hơn hoặc liên quan.

## Lợi ích
- **Tiết kiệm thời gian**: Giảm thời gian huấn luyện do không cần huấn luyện từ đầu.
- **Tận dụng kiến thức**: Sử dụng các đặc trưng đã học được từ dataset lớn (ví dụ: ImageNet).
- **Hiệu quả với dữ liệu ít**: Cải thiện hiệu suất cho các nhiệm vụ có ít dữ liệu huấn luyện.

## Cách triển khai
- **Pretrained models**: Sử dụng các mô hình đã được huấn luyện trước (ví dụ: ResNet, EfficientNet, MobileNet) làm backbone.
- **Fine-tuning**: Thay đổi lớp cuối cùng của mô hình pretrained để phù hợp với số lượng lớp của nhiệm vụ đích, sau đó huấn luyện lại (fine-tune) trên dataset đích.
- **Feature extraction**: Có thể chỉ sử dụng các lớp đầu của mô hình pretrained để trích xuất đặc trưng, sau đó huấn luyện một mô hình mới trên các đặc trưng này.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, transfer learning có thể được áp dụng bằng cách:
- Sử dụng ResNet hoặc EfficientNet đã được huấn luyện trên ImageNet làm backbone.
- Fine-tune mô hình trên dataset rác thải để phân loại các loại rác và dự đoán các thuộc tính vật liệu.

## Tài liệu tham khảo
- [A Survey on Transfer Learning](https://www.cse.ust.hk/~qyang/Docs/2009/tkde_transfer_learning.pdf)
- [How transferable are features in deep neural networks?](https://arxiv.org/abs/1411.1792) 