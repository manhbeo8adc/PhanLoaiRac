# Magnitude-based Pruning

## Tổng quan
Magnitude-based Pruning là một kỹ thuật trong học máy, thường được sử dụng để giảm kích thước của mô hình bằng cách loại bỏ các liên kết có giá trị tuyệt đối nhỏ nhất. Kỹ thuật này giúp cải thiện hiệu suất của mô hình mà không làm giảm đáng kể độ chính xác.

## Đặc điểm
- **Giảm kích thước mô hình**: Magnitude-based Pruning giúp giảm kích thước của mô hình bằng cách loại bỏ các liên kết không cần thiết.
- **Bảo toàn độ chính xác**: Mặc dù giảm kích thước, Magnitude-based Pruning vẫn đảm bảo rằng độ chính xác của mô hình không bị ảnh hưởng đáng kể.
- **Hiệu quả**: Kỹ thuật này giúp cải thiện hiệu suất của mô hình bằng cách giảm thời gian xử lý và tài nguyên cần thiết.

## Cách triển khai
- **Phân tích mô hình**: Mô hình được phân tích để xác định các liên kết có giá trị tuyệt đối nhỏ nhất.
- **Loại bỏ liên kết**: Các liên kết có giá trị tuyệt đối nhỏ nhất có thể được loại bỏ để thu nhỏ kích thước mô hình.
- **Huấn luyện lại**: Sau khi loại bỏ các liên kết, mô hình có thể được huấn luyện lại để đảm bảo hiệu suất.

## Ví dụ
Trong dự án Phân Loại Rác Thông Minh, Magnitude-based Pruning có thể được sử dụng để giảm kích thước của mô hình phân loại rác thải, giúp cải thiện hiệu suất mà không làm giảm độ chính xác.

## Tài liệu tham khảo
- [Model Pruning in Machine Learning](https://www.analyticsvidhya.com/blog/2017/03/model-pruning-in-machine-learning/)
- [Understanding Model Pruning](https://towardsdatascience.com/understanding-model-pruning-7a4b1a5c3c2) 