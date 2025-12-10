# railway-track-fault-detection
Railway tracks require continuous monitoring, but manual inspection is slow, costly, and prone to human error. This project builds an AI-powered solution that analyzes images or video frames of railway tracks and detects any potential faults in real time.
# 🚆 Railway Track Fault Detection Using YOLOv8
An AI-powered system for detecting railway track faults such as cracks, misalignments, missing fasteners, and obstacles using **YOLOv8**. This project focuses **only on image-based fault detection**.

---

## ⭐ Overview
Railway tracks require frequent inspection to maintain safety, but manual inspection is slow and prone to errors. This project provides an automated **Computer Vision + Deep Learning** solution that analyzes **static images** of railway tracks and detects different types of defects with high accuracy.

---

## 🎯 Objectives
- Detect multiple types of railway track defects from images  
- Automate track inspection using YOLOv8  
- Provide accurate detections under different lighting and environmental conditions  
- Enable a fast, scalable inspection workflow using images only  

---

## 🧠 Features
- 🎯 **High-accuracy detection** using YOLOv8  
- 🖼️ Works **only with images** 
- 📦 Easy-to-train using custom annotated images  
- 🔧 Simple and modular project structure  
- ⚡ Fast inference on CPU or GPU  

---

## 📂 Dataset
The dataset contains railway track images annotated for:
- Cracks  
- Track misalignment  
- Missing or loose fasteners  
- Foreign obstacles  

Annotations were created with **LabelImg / Roboflow**, including augmentation (brightness, rotation, blur, noise).

> Add your dataset link here once available.

---

## 🏗️ System Architecture
```
Input Image  
      ↓  
Preprocessing (Resize, Normalize)  
      ↓  
YOLOv8 Model  
      ↓  
Fault Detection + Bounding Boxes  
      ↓  
Output Image with Labels
```

---

## 🚀 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/railway-track-fault-detection.git
cd railway-track-fault-detection
```

### 2️⃣ Install Dependencies
```bash
pip install ultralytics opencv-python torch numpy
```

---

## 🏋️‍♂️ Model Training

### Create your `data.yaml` file
```yaml
train: path/to/train/images
val: path/to/val/images

nc: 4
names: ['crack', 'misalignment', 'fastener_missing', 'obstacle']
```

### Train YOLOv8
```bash
yolo detect train \
    data=track_fault.yaml \
    model=yolov8n.pt \
    epochs=50 \
    imgsz=640 \
    batch=16
```

---

## 🧪 Run Inference (Images Only)

### Predict on a Single Image
```bash
yolo detect predict model=best.pt source="image.jpg"
```

### Predict on a Folder of Images
```bash
yolo detect predict model=best.pt source="test_images/"
```

---

## 📊 Results
- High precision and recall across defect categories  
- Strong performance in varied lighting  
- Outputs bounding boxes with class labels and confidence scores  

> Add your sample result images here.

---

## 🛠️ Tech Stack
- Python 3.10+  
- YOLOv8 (Ultralytics)  
- PyTorch  
- OpenCV  
- NumPy  
- Roboflow / LabelImg  

---

## 🌟 Applications
- Railway inspection automation  
- Maintenance planning and analysis  
- Research on railway infrastructure safety  
- Dataset creation for advanced models  

---

## 📌 Future Enhancements
- Add segmentation-based crack detection  
- Add severity scoring for faults  
- Create an image-based inspection dashboard  
- Expand dataset with more track variations  

---

## 🤝 Contribution
Contributions are welcome!  
Feel free to open an issue or submit a pull request.

---







