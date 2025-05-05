# Gradient Descent

## Tổng quan
Gradient Descent là một thuật toán tối ưu hóa được sử dụng để tìm giá trị tối thiểu của một hàm mất mát. Thuật toán này hoạt động bằng cách di chuyển theo hướng ngược lại của gradient (đạo hàm) của hàm mất mát, giúp mô hình tiến gần hơn đến điểm tối ưu.

## Đặc điểm
- **Hướng di chuyển**: Gradient Descent di chuyển theo hướng ngược lại của gradient, giúp mô hình tiến gần hơn đến điểm tối ưu.
- **Tốc độ học**: Tốc độ học (learning rate) là một tham số quan trọng, quyết định kích thước bước di chuyển trong mỗi lần cập nhật.
- **Điểm dừng**: Thuật toán dừng lại khi đạt đến điểm tối ưu hoặc khi số lần lặp đạt đến giới hạn.

## Cách triển khai
- **Tính toán gradient**: Gradient của hàm mất mát được tính toán để xác định hướng di chuyển.
- **Cập nhật tham số**: Các tham số của mô hình được cập nhật dựa trên gradient và tốc độ học.
- **Lặp lại**: Quá trình này được lặp lại cho đến khi đạt đến điểm tối ưu hoặc khi số lần lặp đạt đến giới hạn.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, Gradient Descent có thể được sử dụng để tối ưu hóa hàm mất mát của mô hình phân loại rác thải, giúp mô hình học cách dự đoán chính xác nhãn của rác thải.

## Tài liệu tham khảo
- [Understanding Gradient Descent](https://towardsdatascience.com/understanding-gradient-descent-7b9533c4d6e7)
- [Gradient Descent in Machine Learning](https://www.analyticsvidhya.com/blog/2017/03/introduction-to-gradient-descent-algorithm-along-its-variants/) 