import os
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau

from src.data.prepare_data import prepare_dataset

def create_model(num_classes, input_shape=(224, 224, 3)):
    """
    Create a model using MobileNetV2 as the base.
    
    Args:
        num_classes (int): Number of classes to classify
        input_shape (tuple): Input shape of the images
    
    Returns:
        tensorflow.keras.models.Model: Compiled model
    """
    # Load the base model
    base_model = MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=input_shape
    )
    
    # Freeze the base model
    base_model.trainable = False
    
    # Add custom layers
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    
    # Create the model
    model = Model(inputs=base_model.input, outputs=predictions)
    
    # Compile the model
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

def train_model(data_dir, model_save_path, batch_size=32, epochs=20):
    """
    Train the model.
    
    Args:
        data_dir (str): Directory containing the dataset
        model_save_path (str): Path to save the trained model
        batch_size (int): Batch size for training
        epochs (int): Number of epochs to train
    """
    # Prepare the dataset
    X_train, X_val, X_test, y_train, y_val, y_test, class_names = prepare_dataset(data_dir)
    
    # Create and compile the model
    model = create_model(len(class_names))
    
    # Create callbacks
    callbacks = [
        ModelCheckpoint(
            model_save_path,
            monitor='val_accuracy',
            save_best_only=True,
            mode='max',
            verbose=1
        ),
        EarlyStopping(
            monitor='val_loss',
            patience=5,
            restore_best_weights=True
        ),
        ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.2,
            patience=3,
            min_lr=1e-6
        )
    ]
    
    # Train the model
    history = model.fit(
        X_train, y_train,
        batch_size=batch_size,
        epochs=epochs,
        validation_data=(X_val, y_val),
        callbacks=callbacks
    )
    
    # Evaluate the model
    test_loss, test_accuracy = model.evaluate(X_test, y_test)
    print(f"\nTest accuracy: {test_accuracy:.4f}")
    print(f"Class names (label order): {class_names}")
    
    return model, history, class_names

if __name__ == "__main__":
    # Example usage
    data_dir = "data/raw"
    model_save_path = "models/waste_classifier.h5"
    
    # Create models directory if it doesn't exist
    os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
    
    # Train the model
    model, history, class_names = train_model(data_dir, model_save_path) 