from ultralytics import YOLO

# Load trained model
model = YOLO("model/best.pt")

# Run detection on sample images
results = model.predict(
    source="dataset/sample_images",
    save=True
)

print("Prediction completed. Check runs/detect folder for results.")
