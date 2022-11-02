#отразить изображение по правой границе
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('images.jpg')
img_flip_ud = cv.flip(image, 0)
cv.imwrite('task7-image/new_flip_image.jpg', img_flip_ud)