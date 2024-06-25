# Author: Lucas Fernando
# Project: Hands Seals Detection
# Project repository: https://github.com/lucasfernandoprojects/hand-sign-detection
# This script loads the object recognition model previously trained and make predictions.
# You need a webcam connected to your PC to run this code.

from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("YOUR_MODEL_PATH/best.pt")
results = model.predict(source="0", show=True)
print(results)
