import numpy as np
import cv2

# Capture video from file
cap = cv2.VideoCapture('solidWhiteRightVideo.mp4')

while True:
    # 영상 읽기
    ret, frame = cap.read()
    # ret : 영상이 정상적으로 읽힌 경우 true, 그렇지 않으면 false
    # frame : 불러온 영상 저장 버퍼

    if ret:
        # 흑백 이미지로 변환
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 영상 출력
        cv2.imshow('frame',gray)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    else:
        break

# Release
cap.release()
cv2.destroyAllWindows()

