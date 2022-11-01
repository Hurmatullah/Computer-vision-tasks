#перевести в grayscale
import cv2 as cv
import numpy as np

image = cv.imread('images.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)
cv.waitKey(0)
cv.destroyAllWindows()
