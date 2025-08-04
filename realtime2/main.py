import cv2
from yolov8_detector import detect_people
from speaker import speak_async
from database import initialize_database, log_count, close_connection

def main():
    initialize_database()
    cap = cv2.VideoCapture(0)  # USB webcam assumed at index 0

    if not cap.isOpened():
        print("❌ Camera read failed.")
        return

    spoken_count = -1
    print("[INFO] Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))
        frame_with_boxes, boxes = detect_people(frame)
        person_count = len(boxes)

        if person_count != spoken_count:
            speak_async(f"{person_count} people detected")
            log_count(person_count)
            spoken_count = person_count

        cv2.putText(frame_with_boxes, f"People: {person_count}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("YOLOv8 Detection", frame_with_boxes)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    close_connection()

if __name__ == "__main__":
    main()
