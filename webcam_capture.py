import cv2
import time

# Open the default camera
cam = cv2.VideoCapture(0)

img_counter = 0
img_width = 640
img_height = 640
while True:
    ret, frame = cam.read()
    # Display the captured frame
    frame = cv2.resize(frame, (img_width,img_height))
    cv2.imshow('Camera', frame)
    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break
    elif cv2.waitKey(256) == 32:
        # SPACE pressed
        img_name = "/captured_images/opencv_frame_" + str(img_counter) + ".jpg"
        cv2.imwrite(img_name, frame)  
        print("{} written!".format(img_name))
        img_counter += 1
    

# Release the capture and writer objects
cam.release()
cv2.destroyAllWindows()