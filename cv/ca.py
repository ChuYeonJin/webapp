import cv2, time

video=cv2.VideoCapture(0)

d=0
while True:
    d += 1
    check, frame = video.read()

    print(check)
    print(frame)

    cv2.imshow("capturing",frame)

    key = cv2.waitKey(1)

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows

print(d)