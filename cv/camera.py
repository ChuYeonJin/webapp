import cv2

cam = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)
cam3 = cv2.VideoCapture(2)
print(cam)
print(cam2)
print(cam3)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cam.set(3, 360)
cam.set(4, 240)

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

