# Warehouse Object Detection using YOLOv9

## Project Overview

This project builds an AI computer vision model to detect objects commonly found in warehouse environments such as boxes, pallets, forklifts, robots, and workers.

The model is trained using the YOLOv9 object detection framework and a labeled warehouse dataset.

---

## Technologies Used

* Python
* YOLOv9 (Ultralytics)
* PyTorch
* Computer Vision
* Roboflow Dataset

---

## Dataset

The dataset contains labeled warehouse images with objects such as:

* Box
* Cart
* Forklift
* Pallets
* Person
* Robot
* White Roll

Only sample images are included in this repository.

---

## Model Training

Training command used:

yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=5 imgsz=320 batch=8

---

## Model Results

The trained model achieves object detection performance evaluated using:

* Precision
* Recall
* mAP (Mean Average Precision)

Example evaluation outputs are stored in the `results/` folder.

---

## Project Structure

warehouse-object-detection-yolo
│
├── dataset/sample_images
├── model/best.pt
├── results/
├── notebook/train.py
└── README.md

---

## Applications

Warehouse Automation
Inventory Monitoring
Robotics Vision Systems
Smart Logistics

---

## Author

**Vijay Gavvala**
B.Tech Data Science Graduate
Hyderabad, India
