if __name__ == "__main__":

    from ultralytics import YOLO

    # Load a YOLOv8 model
    model = YOLO('yolov8n.pt')  # or yolov8s.pt

    # Train on your dataset
    results = model.train(
        data="rail_guard_data.yaml",
        epochs=80,                        # training for 80 epochs
        imgsz=640,
        batch=16,
        name="yolov8s_custom_training_gpu",
        device=0
    )


    print("Training complete!")
