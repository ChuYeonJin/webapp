import cv2
import time

cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

time.sleep(1)

while True:
    ret,img = cam.read()
    print(ret)
    print(img)

    cv2.imshow('Video Capture', img)
    key = cv2.waitKey(10)

    if key == 27:
        break
    if key == ord(' '):
        cv2.imwrite('capture.jpg', img)

