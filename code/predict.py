from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("/home/tony/Projects/hands-seals-detection/yolo-model/models/best.pt")
results = model.predict(source="0", show=True)
print(results)