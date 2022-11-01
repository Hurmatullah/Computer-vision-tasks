#найти все orb features точки на изображении
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

image = cv.imread("images.jpg", 0)

#initiating orb
orb = cv.ORB_create()
# find the keypoints with ORB
kp = orb.detect(image,None)
# compute the descriptors with ORB
kp, des = orb.compute(image, kp)
# draw only keypoints location,not size and orientation
img2 = cv.drawKeypoints(image, kp, None, color=(0,255,0), flags=0)
plt.imshow(img2), plt.show()