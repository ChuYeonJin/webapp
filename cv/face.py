#/usr/bin/env python

import numpy as np
import cv2

def clock():
    return cv2.getTickCount() / cv2.getTickFrequency()

def draw_str(dst, tup, s):
    x = tup[0]
    y = tup[1]
    cv2.putText(dst, s, (x+1, y+1), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness = 2, lineType=cv2.LINE_AA)
    cv2.putText(dst, s, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), lineType=cv2.LINE_AA)

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3, minSize=(80, 80), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:, 2:] += rects[:, :2]
    return rects


def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


if __name__ == '__main__':
    cascade_fn = "/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
    nested_fn = "/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml"
    profile_fn = "/usr/local/share/OpenCV/haarcascades/haarcascade_profileface.xml"

    cascade = cv2.CascadeClassifier(cascade_fn)
    nested = cv2.CascadeClassifier(nested_fn)
    profile = cv2.CascadeClassifier(profile_fn)

    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        t = clock()
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))

        pro = detect(gray, profile)
        draw_rects(vis, pro, (0, 0, 255))

        for x1, y1, x2, y2 in rects:
            roi = gray[y1:y2, x1:x2]
            vis_roi = vis[y1:y2, x1:x2]
            subrects = detect(roi.copy(), nested)
            draw_rects(vis_roi, subrects, (255, 0, 0))

        dt = clock() - t
        tup = (20, 20)
        draw_str(vis, tup, 'time: %.1f ms' % (dt * 1000))
        cv2.imshow('facedetect', vis)

        if 0xFF & cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()