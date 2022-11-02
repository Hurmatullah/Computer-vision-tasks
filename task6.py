#отразить изображение по правой границе
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('images.jpg')
img_flip_ud = cv.flip(image, 1)
cv.imwrite('task6-image/new_flip_image.jpg', img_flip_ud)