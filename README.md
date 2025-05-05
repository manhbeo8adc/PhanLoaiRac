# Phân Loại Rác Thông Minh

Ứng dụng phân loại rác thải sử dụng Deep Learning, được xây dựng với Python và TensorFlow.

## Tính năng

- Phân loại 6 loại rác thải: Carton, Thủy tinh, Kim loại, Giấy, Nhựa, Rác thông thường
- Giao diện đồ họa thân thiện với người dùng
- Độ chính xác cao nhờ sử dụng mô hình MobileNetV2

## Cài đặt

1. Clone repository:
```bash
git clone https://github.com/yourusername/PhanLoaiRac.git
cd PhanLoaiRac
```

2. Tạo môi trường ảo và cài đặt dependencies:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3. Train mô hình (tùy chọn):
```bash
python src/models/train.py
```

## Sử dụng

1. Chạy ứng dụng:
```bash
python src/app.py
```

2. Hoặc sử dụng file thực thi đã build:
- Chạy file `dist/app.exe`
- Đảm bảo thư mục `models` chứa file `waste_classifier.h5` nằm cùng thư mục với `app.exe`

## Cấu trúc thư mục

```
PhanLoaiRac/
├── data/
│   ├── raw/          # Dữ liệu thô
│   └── processed/    # Dữ liệu đã xử lý
├── models/           # Thư mục chứa mô hình
├── src/
│   ├── data/        # Code xử lý dữ liệu
│   ├── models/      # Code mô hình
│   └── app.py       # Giao diện người dùng
├── requirements.txt  # Dependencies
└── README.md        # Tài liệu hướng dẫn
```

## Yêu cầu hệ thống

- Python 3.8 trở lên
- Windows 10/11
- RAM: 4GB trở lên
- GPU (tùy chọn) để tăng tốc độ xử lý

## License

MIT License 