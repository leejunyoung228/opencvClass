import cv2
import numpy as np
four_point = []
def move(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        four_point.append([x,y])
        print([x,y])
        # cv2.rectangle(img, (x,y), (x+50, y+50), (255,0,0), -1)

img = cv2.imread("./images/road.jpg", cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('image')
cv2.setMouseCallback('image', move)
h, w = img.shape

while True:
    cv2.imshow('image', img)
    if len(four_point) == 4:
        break
    cv2.waitKey(1)
point_src = np.float32(four_point)
point_dst = np.float32([[110,480],[110,120],[560,120],[560,480]])
per_mat = cv2.getPerspectiveTransform(point_src,point_dst)
img = cv2.warpPerspective(img, per_mat, (w,h))
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()