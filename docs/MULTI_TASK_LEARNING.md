# Multi-Task Learning

## Tổng quan
Multi-Task Learning (MTL) là một phương pháp học máy, trong đó một mô hình được huấn luyện để thực hiện nhiều nhiệm vụ khác nhau cùng một lúc. Mục đích là tận dụng các đặc trưng chung giữa các nhiệm vụ để cải thiện hiệu suất tổng thể của mô hình.

## Lợi ích
- **Tận dụng đặc trưng chung**: MTL giúp mô hình học được các đặc trưng chung giữa các nhiệm vụ, giúp tăng độ chính xác.
- **Giảm overfitting**: Huấn luyện nhiều nhiệm vụ cùng lúc giúp giảm thiểu overfitting, tăng độ robust.
- **Tiết kiệm tài nguyên**: Một mô hình có thể thực hiện nhiều nhiệm vụ, giúp tiết kiệm tài nguyên tính toán.

## Cách triển khai
- **Chia sẻ các lớp chung**: Các lớp đầu tiên của mô hình được chia sẻ giữa các nhiệm vụ, giúp học các đặc trưng chung.
- **Các lớp riêng biệt**: Các lớp cuối cùng của mô hình được tách riêng cho từng nhiệm vụ, giúp học các đặc trưng riêng.
- **Hàm mất mát tổng hợp**: Hàm mất mát tổng hợp được tính bằng tổng có trọng số của các hàm mất mát của từng nhiệm vụ.
- **Điều chỉnh trọng số**: Trọng số của các hàm mất mát có thể được điều chỉnh để cân bằng giữa các nhiệm vụ.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, MTL có thể được áp dụng để huấn luyện một mô hình thực hiện cả phân loại rác thải và phát hiện đối tượng rác thải. Các lớp đầu tiên của mô hình được chia sẻ để học các đặc trưng chung, trong khi các lớp cuối cùng được tách riêng cho từng nhiệm vụ.

## Tài liệu tham khảo
- [Multi-Task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics](https://arxiv.org/abs/1705.07115)
- [An Overview of Multi-Task Learning in Deep Neural Networks](https://arxiv.org/abs/1706.05098) 