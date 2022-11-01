#найти canny edges на изображенни
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('images.jpg',0)
edges = cv.Canny(image,100,200)
plt.subplot(121),plt.imshow(image,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()