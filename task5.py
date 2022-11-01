#перевести изорбражение в hsv
import cv2 as cv
import numpy as np

image = cv.imread('images.jpg')
cvtHsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow("Original Image", image)
cv.imshow('Converted to HSV', cvtHsv)
cv.waitKey(0)