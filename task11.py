# изменить яркость изоббражения
from __future__ import print_function
from builtins import input
import cv2 as cv
import numpy as np

image = cv.imread("images.jpg")

new_image = np.zeros(image.shape, image.dtype)
alpha = 1.0 # Простое управление контрастностью
beta = 0    # Простое управление яркостью
try:
    alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
    beta = int(input('* Enter the beta value [0-100]: '))
except ValueError:
    print('Error, not a number')
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for c in range(image.shape[2]):
            new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
cv.imshow('Original Image', image)
cv.imshow('New Image', new_image)
cv.imwrite('task11-image/original_image.jpg', image)
cv.imwrite('task11-image/Changed_image.jpg', new_image)
cv.waitKey(0)
cv.destroyAllWindows()