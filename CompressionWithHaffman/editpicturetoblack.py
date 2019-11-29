import numpy as np
import cv2
img = cv2.imread("key-flat-128x128.png",0)
for i in range(128):
    for j in range(128):
        img[i][j] = (img[i][j]//20)*20
cv2.imwrite('key-flag-black.png', img)
