import os
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
from src.data.prepare_data import load_and_preprocess_image
import sys

class WasteClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phân Loại Rác Thông Minh")
        self.root.geometry("800x600")
        
        # Hàm lấy đường dẫn thực tế khi chạy bằng PyInstaller hoặc script thường
        def resource_path(relative_path):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)
        
        model_path = resource_path("models/waste_classifier.h5")
        self.model = tf.keras.models.load_model(model_path)
        
        # Define class names
        self.class_names = [
            "Carton",        # cardboard
            "Thủy tinh",     # glass
            "Kim loại",      # metal
            "Giấy",          # paper
            "Nhựa",          # plastic
            "Rác thông thường" # trash
        ]
        
        self.setup_ui()
    
    def setup_ui(self):
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create widgets
        ttk.Label(
            main_frame, 
            text="Phân Loại Rác Thông Minh",
            font=("Helvetica", 16)
        ).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Upload button
        self.upload_btn = ttk.Button(
            main_frame,
            text="Tải ảnh lên",
            command=self.upload_image
        )
        self.upload_btn.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Image display
        self.image_label = ttk.Label(main_frame)
        self.image_label.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Results display
        self.result_label = ttk.Label(
            main_frame,
            text="Kết quả phân loại sẽ hiển thị ở đây",
            font=("Helvetica", 12)
        )
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Confidence display
        self.confidence_label = ttk.Label(
            main_frame,
            text="",
            font=("Helvetica", 10)
        )
        self.confidence_label.grid(row=4, column=0, columnspan=2, pady=5)
    
    def upload_image(self):
        # Open file dialog
        print("[LOG] Bắt đầu upload_image")
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"),
                ("All files", "*.*")
            ]
        )
        print(f"[LOG] Đã chọn file: {file_path}")
        if file_path:
            # Load and preprocess image
            try:
                print("[LOG] Đọc và hiển thị ảnh bằng PIL")
                image = Image.open(file_path)
                image = image.resize((300, 300), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                self.image_label.configure(image=photo)
                self.image_label.image = photo
                print("[LOG] Đã hiển thị ảnh lên giao diện")
                # Preprocess image for model
                print("[LOG] Tiền xử lý ảnh cho model")
                img_array = load_and_preprocess_image(file_path)
                img_array = np.expand_dims(img_array, axis=0)
                print(f"[LOG] img_array shape: {img_array.shape}")
                # Make prediction
                print("[LOG] Dự đoán với model")
                predictions = self.model.predict(img_array)
                predicted_class = np.argmax(predictions[0])
                confidence = predictions[0][predicted_class]
                print(f"[LOG] Kết quả: class={predicted_class}, confidence={confidence}")
                # Update results
                self.result_label.configure(
                    text=f"Loại rác: {self.class_names[predicted_class]}"
                )
                self.confidence_label.configure(
                    text=f"Độ tin cậy: {confidence:.2%}"
                )
            except Exception as e:
                print(f"[LOG] Lỗi: {str(e)}")
                self.result_label.configure(
                    text=f"Lỗi: {str(e)}"
                )

def main():
    root = tk.Tk()
    app = WasteClassifierApp(root)
    root.mainloop()

if __name__ == "__main__":
    sys.stdout = open("logfile.txt", "w", encoding="utf-8")
    sys.stderr = sys.stdout
    main() 