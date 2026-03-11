from ultralytics import YOLO

# Load trained model
model = YOLO("model/best.pt")

# Evaluate on validation dataset
metrics = model.val(data="data.yaml")

print("Evaluation Metrics:")
print(metrics)
