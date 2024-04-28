import cv2
from ultralytics import YOLO


model = YOLO('yolov8n-seg.pt')

cap = cv2.VideoCapture(0)


while cap.isOpened():
    success , frame = cap.read()

    if success:
        results = model(frame)
        cv2.imshow("Results",results[0].plot())

        # print(model.predict(classes = 0))
        # break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:

        break

cap.release()
cv2.destroyAllWindows()
