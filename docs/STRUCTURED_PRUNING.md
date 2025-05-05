# Structured Pruning

## Tổng quan
Structured Pruning là một kỹ thuật trong học máy, thường được sử dụng để giảm kích thước của mô hình bằng cách loại bỏ toàn bộ các khối hoặc lớp của mô hình. Kỹ thuật này giúp cải thiện hiệu suất của mô hình mà không làm giảm đáng kể độ chính xác.

## Đặc điểm
- **Giảm kích thước mô hình**: Structured Pruning giúp giảm kích thước của mô hình bằng cách loại bỏ toàn bộ các khối hoặc lớp không cần thiết.
- **Bảo toàn độ chính xác**: Mặc dù giảm kích thước, Structured Pruning vẫn đảm bảo rằng độ chính xác của mô hình không bị ảnh hưởng đáng kể.
- **Hiệu quả**: Kỹ thuật này giúp cải thiện hiệu suất của mô hình bằng cách giảm thời gian xử lý và tài nguyên cần thiết.

## Cách triển khai
- **Phân tích mô hình**: Mô hình được phân tích để xác định các khối hoặc lớp không cần thiết.
- **Loại bỏ khối hoặc lớp**: Các khối hoặc lớp không cần thiết có thể được loại bỏ để thu nhỏ kích thước mô hình.
- **Huấn luyện lại**: Sau khi loại bỏ các khối hoặc lớp, mô hình có thể được huấn luyện lại để đảm bảo hiệu suất.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, Structured Pruning có thể được sử dụng để giảm kích thước của mô hình phân loại rác thải, giúp cải thiện hiệu suất mà không làm giảm độ chính xác.

## Tài liệu tham khảo
- [Model Pruning in Machine Learning](https://www.analyticsvidhya.com/blog/2017/03/model-pruning-in-machine-learning/)
- [Understanding Model Pruning](https://towardsdatascience.com/understanding-model-pruning-7a4b1a5c3c2) 