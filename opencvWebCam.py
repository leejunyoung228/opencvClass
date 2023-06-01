import cv2
import numpy as np

def nothing():
    pass

CAMERA_ID = 0

cam = cv2.VideoCapture(CAMERA_ID)
if cam.isOpened() == False:
    print('Cannot Open the Camera %d' % (CAMERA_ID))
    exit()

cv2.namedWindow('Blur track bar')
cv2.createTrackbar('blur', 'Blur track bar', 1, 10, nothing)
# cv2.createTrackbar('green color', 'RGB track bar', 0, 10, nothing)
# cv2.createTrackbar('blue color', 'RGB track bar', 0, 10, nothing)

cv2.setTrackbarPos('blur', 'Blur track bar', 5)
# cv2.setTrackbarPos('green color', 'RGB track bar', 5)
# cv2.setTrackbarPos('blue color', 'RGB track bar', 5)
img = np.zeros((512, 512, 3), np.uint8)

while True:
    ret, frame = cam.read()
    # cv2.imshow('Blur track bar', frame)

    blurVal = cv2.getTrackbarPos('blur', 'Blur track bar')
    res = cv2.blur(frame, (blurVal, blurVal))
    cv2.imshow('Blur track bar', res)
    # greenVal = cv2.getTrackbarPos('green color', 'RGB track bar')
    if cv2.waitKey(10) > 0:
        break
cam.release()
cv2.destroyAllWindows()
