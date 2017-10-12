import cv2
import os

cam = cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cam.set(3, 360)
cam.set(4, 240)
os.system('sudo modprobe bcm2835-v412')

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

