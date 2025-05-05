# Multi-Task Learning

## Tổng quan
Multi-Task Learning (MTL) là một phương pháp học máy, trong đó một mô hình được huấn luyện để thực hiện nhiều nhiệm vụ cùng lúc. Thay vì huấn luyện các mô hình riêng biệt cho từng nhiệm vụ, MTL tận dụng thông tin từ các nhiệm vụ liên quan để cải thiện hiệu suất tổng thể.

## Lợi ích
- **Chia sẻ kiến thức**: Các nhiệm vụ liên quan có thể chia sẻ đặc trưng, giúp mô hình học hiệu quả hơn.
- **Giảm overfitting**: Tận dụng dữ liệu từ nhiều nhiệm vụ giúp mô hình tránh được overfitting.
- **Tăng hiệu suất**: Cải thiện độ chính xác cho các nhiệm vụ có ít dữ liệu huấn luyện.

## Cách triển khai
- **Kiến trúc mạng**: Sử dụng kiến trúc mạng có nhiều đầu ra (multi-head), mỗi đầu ra tương ứng với một nhiệm vụ.
- **Loss function**: Kết hợp các loss function riêng cho từng nhiệm vụ, có thể cân bằng trọng số giữa các loss.
- **Backbone chung**: Sử dụng một backbone chung (ví dụ: ResNet, EfficientNet) để trích xuất đặc trưng, sau đó chia nhánh cho từng nhiệm vụ.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, MTL có thể được áp dụng để dự đoán đồng thời:
- Nhãn phân loại rác (carton, thủy tinh, kim loại, ...).
- Các thuộc tính vật liệu (metallic, smoothness, albedo, ...).

## Tài liệu tham khảo
- [Multi-Task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics](https://arxiv.org/abs/1705.07115)
- [An Overview of Multi-Task Learning in Deep Neural Networks](https://arxiv.org/abs/1706.05098) 