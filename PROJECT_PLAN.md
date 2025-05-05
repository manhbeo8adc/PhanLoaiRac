# Kế hoạch dự án Phân loại rác bằng AI

## 1. Mục tiêu dự án

Xây dựng một hệ thống sử dụng trí tuệ nhân tạo (AI) để tự động phân loại các loại rác thải dựa trên hình ảnh đầu vào.

## 2. Yêu cầu chi tiết

*   **Nguồn dữ liệu đầu vào:** Người dùng tải lên một ảnh.
*   **Các loại rác cần phân loại (Đề xuất ban đầu - 6 loại):**
    *   Giấy (Paper)
    *   Carton (Cardboard)
    *   Nhựa (Plastic)
    *   Thủy tinh (Glass)
    *   Kim loại (Metal)
    *   Rác thông thường (Trash/Landfill)
*   **Bộ dữ liệu (Dataset):** Chưa có. Sẽ tìm và sử dụng bộ dữ liệu công khai (VD: TrashNet, Kaggle Datasets).
*   **Yêu cầu về hiệu suất:**
    *   Độ chính xác: > 85% (Mục tiêu ban đầu)
    *   Tốc độ xử lý: ~33ms/ảnh (Ưu tiên mô hình nhẹ như MobileNetV2, EfficientNet)
*   **Triển khai:** Ban đầu là ứng dụng Desktop (Windows/Mac/Linux), có thể phát triển thành ứng dụng di động sau.
*   **Kinh nghiệm người thực hiện:** Người mới bắt đầu. Cần hướng dẫn chi tiết, tập trung vào tính dễ hiểu.

## 3. Công nghệ sử dụng

*   **Ngôn ngữ lập trình:** Python
*   **Framework Deep Learning:** TensorFlow/Keras (Phù hợp cho người mới bắt đầu và có TFLite để tối ưu sau này)
*   **Thư viện xử lý ảnh:** OpenCV (`cv2`)
*   **Thư viện tính toán:** NumPy
*   **Thư viện GUI (Desktop App):** Tkinter (Đề xuất ban đầu cho sự đơn giản)
*   **Web Framework (Nếu triển khai web):** Flask/Django (Tùy chọn trong tương lai)

## 4. Mô hình Neural Network

*   **Loại mô hình:** Convolutional Neural Network (CNN)
*   **Phương pháp:** Transfer Learning
*   **Kiến trúc cơ sở (Đề xuất ưu tiên):** MobileNetV2 / EfficientNet (Do yêu cầu tốc độ). ResNet50 là phương án dự phòng nếu cần độ chính xác cao hơn và chấp nhận chậm hơn.
*   **Quy trình huấn luyện:**
    *   Chuẩn bị & Tăng cường dữ liệu
    *   Chia dữ liệu (Train/Validation/Test)
    *   Xây dựng & Tinh chỉnh mô hình
    *   Biên dịch mô hình
    *   Huấn luyện
    *   Đánh giá
    *   Lưu mô hình

## 5. Kế hoạch triển khai

*   **Giai đoạn 1: Phát triển mô hình AI**
    1.  Thiết lập môi trường Python và cài đặt thư viện (TensorFlow, OpenCV, NumPy).
    2.  Tải và chuẩn bị bộ dữ liệu (TrashNet hoặc tương tự).
    3.  Khám phá dữ liệu (EDA - Exploratory Data Analysis): Xem số lượng ảnh mỗi loại, kích thước, v.v.
    4.  Tiền xử lý và tăng cường dữ liệu.
    5.  Xây dựng mô hình Transfer Learning (sử dụng Keras).
    6.  Huấn luyện và tinh chỉnh mô hình.
    7.  Đánh giá mô hình trên tập kiểm thử.
    8.  Lưu lại mô hình tốt nhất.
*   **Giai đoạn 2: Xây dựng ứng dụng Desktop (Sử dụng Tkinter)**
    1.  Thiết kế giao diện đơn giản: Nút "Tải ảnh lên", khu vực hiển thị ảnh, khu vực hiển thị kết quả phân loại.
    2.  Viết code để tải mô hình đã lưu.
    3.  Xử lý ảnh người dùng tải lên (resize, chuẩn hóa giống lúc huấn luyện).
    4.  Đưa ảnh qua mô hình để dự đoán.
    5.  Hiển thị kết quả lên giao diện.
*   **Giai đoạn 3 (Tương lai):**
    *   Cải thiện độ chính xác mô hình (thêm dữ liệu, thử kiến trúc khác).
    *   Tối ưu mô hình cho tốc độ (VD: dùng TensorFlow Lite).
    *   Phát triển ứng dụng di động.

## 6. Các bước thực hiện tiếp theo

1.  **Xác nhận danh sách các loại rác cuối cùng** (Dựa trên đề xuất 6 loại hoặc tùy chỉnh).
2.  **Tìm và chọn bộ dữ liệu cụ thể** (VD: Cung cấp link tải TrashNet).
3.  **Thiết lập môi trường phát triển:** Cài đặt Python, pip, và tạo môi trường ảo.
4.  **Cài đặt các thư viện cần thiết:** `tensorflow`, `opencv-python`, `numpy`, `matplotlib` (để trực quan hóa).
5.  **Tải bộ dữ liệu đã chọn.**
6.  Cập nhật file `PROJECT_PLAN.md` này.
7.  Thiết lập môi trường phát triển.
8.  Thu thập hoặc chuẩn bị bộ dữ liệu.
9.  ... 