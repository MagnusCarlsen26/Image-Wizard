import cv2
from ultralytics import YOLO
import modules as md
import numpy as np
model = YOLO('yolov8n-seg.pt')
cap = cv2.VideoCapture(0)


while cap.isOpened():
    success , frame = cap.read()

    if success:
        results = model(classes=0,source=frame)
        cv2.imshow("Results",results[0].plot())
        masks = results[0].masks
        if masks is not None and masks.xy is not None and len(masks.xy) > 0:
            boundary_pts = np.array(masks.xy[0] , dtype=np.int32)
            if(boundary_pts.size != 0):
                new_image1 = md.back_black(frame,boundary_pts)
                new_image2 = md.back_normal(frame,boundary_pts)
                new_image3 = md.back_white(frame,boundary_pts)
                new_image4 = md.alpha_blending(frame,boundary_pts,128)
                new_image5 = md.transparent_bg(frame,boundary_pts)
            else:
                new_image1 = frame
                new_image2 = frame
                new_image3 = frame
                new_image4 = frame
                new_image5 = frame
        cv2.imshow("New Image1",new_image1)
        cv2.imshow("New Image2",new_image2)
        cv2.imshow("New Image3",new_image3)
        cv2.imshow("New Image4",new_image4)
        cv2.imshow("New Image5",new_image5)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:

        break

cap.release()
cv2.destroyAllWindows()
