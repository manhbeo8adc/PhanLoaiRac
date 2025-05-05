import os
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split

def load_and_preprocess_image(image_path, target_size=(224, 224)):
    """
    Load and preprocess a single image using PIL (hỗ trợ Unicode path tốt hơn).
    
    Args:
        image_path (str): Path to the image file
        target_size (tuple): Target size for the image (height, width)
    
    Returns:
        numpy.ndarray: Preprocessed image
    """
    img = Image.open(image_path).convert('RGB')
    img = img.resize(target_size)
    img = np.array(img).astype(np.float32) / 255.0
    return img

def prepare_dataset(data_dir, test_size=0.2, val_size=0.2):
    """
    Prepare the dataset for training.
    
    Args:
        data_dir (str): Directory containing the dataset
        test_size (float): Proportion of data to use for testing
        val_size (float): Proportion of training data to use for validation
    
    Returns:
        tuple: (X_train, X_val, X_test, y_train, y_val, y_test)
    """
    images = []
    labels = []
    class_names = sorted(os.listdir(data_dir))
    
    # Load images and labels
    for class_idx, class_name in enumerate(class_names):
        class_dir = os.path.join(data_dir, class_name)
        for img_name in os.listdir(class_dir):
            img_path = os.path.join(class_dir, img_name)
            try:
                img = load_and_preprocess_image(img_path)
                images.append(img)
                labels.append(class_idx)
            except Exception as e:
                print(f"Error processing {img_path}: {e}")
    
    # Convert to numpy arrays
    X = np.array(images)
    y = np.array(labels)
    
    # Split into train, validation, and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42, stratify=y
    )
    
    X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size=val_size, random_state=42, stratify=y_train
    )
    
    return X_train, X_val, X_test, y_train, y_val, y_test, class_names

if __name__ == "__main__":
    # Example usage
    data_dir = "data/raw"
    X_train, X_val, X_test, y_train, y_val, y_test, class_names = prepare_dataset(data_dir)
    print(f"Training set shape: {X_train.shape}")
    print(f"Validation set shape: {X_val.shape}")
    print(f"Test set shape: {X_test.shape}")
    print(f"Classes: {class_names}") 