from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # You can use yolov8s.pt for better accuracy

def detect_people(frame):
    results = model(frame)
    boxes = []

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            if model.names[cls_id] == 'person':
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                boxes.append((x1, y1, x2, y2))
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return frame, boxes
