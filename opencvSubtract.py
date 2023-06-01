import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('images/img3.jpg')
img2 = cv2.imread('images/img4.jpg')

img3 = cv2.subtract(img1, img2)

img4 = cv2.absdiff(img1, img2)

titles = ['src', 'map', 'sub', 'absDiff']
imgs = [img1, img2, img3, img4]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(imgs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()