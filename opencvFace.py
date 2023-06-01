import cv2

img1 = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)
img3 = cv2.absdiff(img1, img2)
ret, thresh2 = cv2.threshold(img3, 127, 255, cv2.THRESH_TOZERO_INV)
img5 = cv2.bitwise_not(thresh2)
cv2.imshow("image",img5)
cv2.waitKey(0)
cv2.destroyAllWindows()