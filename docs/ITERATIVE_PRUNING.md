# Iterative Pruning

## Tổng quan
Iterative Pruning là một kỹ thuật trong học máy, thường được sử dụng để giảm kích thước của mô hình bằng cách thực hiện Pruning theo từng bước, mỗi bước loại bỏ một số liên kết và huấn luyện lại mô hình. Kỹ thuật này giúp cải thiện hiệu suất của mô hình mà không làm giảm đáng kể độ chính xác.

## Đặc điểm
- **Giảm kích thước mô hình**: Iterative Pruning giúp giảm kích thước của mô hình bằng cách loại bỏ các liên kết không cần thiết theo từng bước.
- **Bảo toàn độ chính xác**: Mặc dù giảm kích thước, Iterative Pruning vẫn đảm bảo rằng độ chính xác của mô hình không bị ảnh hưởng đáng kể.
- **Hiệu quả**: Kỹ thuật này giúp cải thiện hiệu suất của mô hình bằng cách giảm thời gian xử lý và tài nguyên cần thiết.

## Cách triển khai
- **Phân tích mô hình**: Mô hình được phân tích để xác định các liên kết không cần thiết.
- **Loại bỏ liên kết**: Các liên kết không cần thiết có thể được loại bỏ theo từng bước để thu nhỏ kích thước mô hình.
- **Huấn luyện lại**: Sau mỗi bước loại bỏ, mô hình có thể được huấn luyện lại để đảm bảo hiệu suất.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, Iterative Pruning có thể được sử dụng để giảm kích thước của mô hình phân loại rác thải, giúp cải thiện hiệu suất mà không làm giảm độ chính xác.

## Tài liệu tham khảo
- [Model Pruning in Machine Learning](https://www.analyticsvidhya.com/blog/2017/03/model-pruning-in-machine-learning/)
- [Understanding Model Pruning](https://towardsdatascience.com/understanding-model-pruning-7a4b1a5c3c2) 