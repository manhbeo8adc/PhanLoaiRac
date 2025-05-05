# Hàm Mất Mát Tổng Hợp (Combined Loss Function)

## Tổng quan
Hàm mất mát tổng hợp là tổng có trọng số của các hàm mất mát của từng nhiệm vụ trong mô hình Multi-Task Learning. Mục đích của hàm mất mát tổng hợp là giúp mô hình học cách cân bằng giữa các nhiệm vụ khác nhau, đảm bảo rằng mô hình không bỏ qua bất kỳ nhiệm vụ nào.

## Đặc điểm
- **Cân bằng nhiệm vụ**: Hàm mất mát tổng hợp giúp mô hình học cách cân bằng giữa các nhiệm vụ khác nhau, đảm bảo rằng mô hình không bỏ qua bất kỳ nhiệm vụ nào.
- **Trọng số**: Mỗi hàm mất mát trong hàm mất mát tổng hợp được gán một trọng số, thể hiện mức độ quan trọng của nhiệm vụ đó.
- **Tối ưu hóa**: Hàm mất mát tổng hợp được tối ưu hóa để giảm thiểu tổng lỗi của tất cả các nhiệm vụ.

## Cách triển khai
- **Tính toán hàm mất mát tổng hợp**: Hàm mất mát tổng hợp được tính bằng cách nhân mỗi hàm mất mát với một trọng số tương ứng và cộng tất cả lại với nhau.
- **Điều chỉnh trọng số**: Trọng số của các hàm mất mát có thể được điều chỉnh để cân bằng giữa các nhiệm vụ, tùy thuộc vào mức độ quan trọng của từng nhiệm vụ.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, hàm mất mát tổng hợp có thể được sử dụng để huấn luyện mô hình thực hiện cả phân loại rác thải và phát hiện đối tượng rác thải. Các hàm mất mát của từng nhiệm vụ được gán trọng số tương ứng và cộng lại để tạo ra hàm mất mát tổng hợp.

## Tài liệu tham khảo
- [Multi-Task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics](https://arxiv.org/abs/1705.07115)
- [An Overview of Multi-Task Learning in Deep Neural Networks](https://arxiv.org/abs/1706.05098) 