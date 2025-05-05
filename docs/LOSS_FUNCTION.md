# Hàm Mất Mát (Loss Function)

## Tổng quan
Hàm mất mát (loss function) là một hàm toán học được sử dụng để đánh giá mức độ sai lệch giữa giá trị dự đoán của mô hình và giá trị thực tế. Mục đích của hàm mất mát là cung cấp một thước đo để mô hình có thể học cách điều chỉnh các tham số của nó để giảm thiểu sai lệch này.

## Đặc điểm
- **Đánh giá hiệu suất**: Hàm mất mát giúp đánh giá hiệu suất của mô hình, cho biết mô hình dự đoán tốt đến mức nào.
- **Hướng dẫn học tập**: Hàm mất mát cung cấp thông tin về hướng điều chỉnh các tham số của mô hình để cải thiện hiệu suất.
- **Đa dạng**: Có nhiều loại hàm mất mát khác nhau, tùy thuộc vào loại bài toán và dữ liệu.

## Các loại hàm mất mát phổ biến
- **Mean Squared Error (MSE)**: Sử dụng cho bài toán hồi quy, tính trung bình bình phương sai lệch giữa giá trị dự đoán và giá trị thực tế.
- **Cross-Entropy Loss**: Sử dụng cho bài toán phân loại, đo lường sự khác biệt giữa phân phối xác suất dự đoán và phân phối xác suất thực tế.
- **Hinge Loss**: Sử dụng cho bài toán phân loại nhị phân, đo lường khoảng cách giữa giá trị dự đoán và ranh giới quyết định.

## Hàm mất mát tổng hợp
- **Định nghĩa**: Hàm mất mát tổng hợp là tổng có trọng số của các hàm mất mát của từng nhiệm vụ trong mô hình Multi-Task Learning.
- **Mục đích**: Hàm mất mát tổng hợp giúp mô hình học cách cân bằng giữa các nhiệm vụ khác nhau, đảm bảo rằng mô hình không bỏ qua bất kỳ nhiệm vụ nào.
- **Cách tính toán**: Hàm mất mát tổng hợp được tính bằng cách nhân mỗi hàm mất mát với một trọng số tương ứng và cộng tất cả lại với nhau.

## Cách triển khai
- **Tính toán hàm mất mát**: Hàm mất mát được tính toán dựa trên giá trị dự đoán của mô hình và giá trị thực tế.
- **Tối ưu hóa**: Mô hình được huấn luyện để tối thiểu hóa hàm mất mát, thông qua các thuật toán tối ưu hóa như gradient descent.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, hàm mất mát Cross-Entropy có thể được sử dụng để huấn luyện mô hình phân loại rác thải, giúp mô hình học cách dự đoán chính xác nhãn của rác thải.

## Tài liệu tham khảo
- [Understanding Loss Functions](https://towardsdatascience.com/understanding-loss-functions-in-machine-learning-7a4b1a5c3c2)
- [Loss Functions in Deep Learning](https://www.analyticsvidhya.com/blog/2019/08/detailed-guide-7-loss-functions-machine-learning-python-code/) 