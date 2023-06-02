import numpy as np
import cv2
from matplotlib import pyplot as plt

x1, y1 = -1, -1
x2, y2 = -1, -1
click, click2 = False, False

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)

def mousePass(event, x, y, flags, param):
    pass

def mouseCallback(event, x, y, flags, param):
    global x1, y1, x2, y2, click, click2

    if event == cv2.EVENT_FLAG_LBUTTON:
        click = True
        x1, y1 = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if click:
            cv2.rectangle(frame, (x1, y1), (x, y), (0, 0, 255), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        if click:
            x2, y2, = x, y
            cv2.rectangle(frame, (x1,y1), (x2, y2), (0,0,255), 2)
            click2 = True
            print('clicked!')


winName = "test"
winName2 = "template"

cv2.namedWindow(winName)
cv2.setMouseCallback(winName, mouseCallback)

status , frame = cam.read()
template = frame.copy()

while not click2:
    cv2.imshow(winName, frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    if click2:
        break

if not cam.isOpened():
    print('webcam error')
    exit()

template2 = template[y1:y2, x1: x2]
cv2.namedWindow(winName2)
cv2.imshow(winName2, template)

w, h = x2-x1 , y2-y1

while cam.isOpened():
    status, frame = cam.read()

    res = cv2.matchTemplate(frame, template2, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc
    bottom_right = top_left[0] + w, top_left[1] + h

    cv2.rectangle(frame, top_left, bottom_right, 0, 2)


    if status:
        cv2.imshow(winName, frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
