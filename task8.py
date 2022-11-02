#повернуть изображение на 45 градусов
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('images.jpg')
(h, w) = image.shape[:2]
center = (w / 2, h / 2)
angle = 45
scale = 1

M = cv.getRotationMatrix2D(center, angle, scale)
rotated = cv.warpAffine(image, M, (w, h))
cv.imwrite('task8-image/45_degree_image.jpg', rotated)