import cv2
import numpy as np
import requests
import io
import pathlib
import torch
from ultralytics import YOLO
from pathlib import Path
pathlib.PosixPath = pathlib.WindowsPath

model = YOLO("model/yolo11n.pt")

# Open the default camera
cam = cv2.VideoCapture(0)
img_counter = 0
img_width = 640
img_height = 640

def run():
    while True:
        ret, frame = cam.read()
        # Display the captured frame
        frame = cv2.resize(frame, (img_width,img_height))
        anno_image = annotate_frame(frame)
        cv2.imshow('Camera', anno_image)
        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

def annotate_frame(image):
    image = cv2.resize(image, (640,640))
    results = model.predict(image)
    for res in results:
            for box in res.boxes:
                print(res.names[int(box.cls[0])])
                cv2.rectangle(image, (int(box.xyxy[0][0]), int(box.xyxy[0][1])),
                              (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (0, 255, 0), 2)
                cv2.putText(image, f"{res.names[int(box.cls[0])]}" + " " + str(int(box.conf * 100)) + " %",
                            (int(box.xyxy[0][0]), int(box.xyxy[0][1]) - 10),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    return image
# Release the capture and writer objects

if __name__ == "__main__":
    run()
     
cam.release()
cv2.destroyAllWindows()