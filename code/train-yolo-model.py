# Author: Lucas Fernando
# Project: Hands Seals Detection
# Project repository: https://github.com/lucasfernandoprojects/hand-sign-detection
# This script trains a YOLOv8n model (nano version of the eighth version of YOLO)
# The model applies some augmentation techniques in order to make the training set
# more diverse and, therefore, avoid over-fitting

import os
from ultralytics import YOLO

# Paths
DATASET_BASE_PATH = ""
YOLO_CONFIG_PATH = ""

# Load YOLO model configuration
model = YOLO('yolov8n.yaml')

# Define training parameters with inline augmentation parameters
training_params = {
    'data': YOLO_CONFIG_PATH,
    'epochs': 50,
    'imgsz': 640,
    'degrees': 10.0,        # Rotation degrees
    'translate': 0.1,       # Translate (fraction)
    'scale': 0.5,           # Scale (fraction)
    'shear': 0.1,           # Shear (fraction)
    'perspective': 0.0,     # Perspective (fraction)
    'flipud': 0.0,          # Flip up-down (fraction)
    'fliplr': 0.5,          # Flip left-right (fraction)
    'mosaic': 1.0,          # Mosaic augmentation (fraction)
    'mixup': 0.0            # MixUp augmentation (fraction)
}

# Train the model with augmentation
results = model.train(**training_params)
