from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Train the model
model.train(
    data="data.yaml",
    epochs=5,
    imgsz=320,
    batch=8
)

# Run prediction on test images
model.predict(
    source="dataset/sample_images",
    save=True
)