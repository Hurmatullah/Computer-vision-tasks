# сделать гистограмную эквайлизацию
from __future__ import print_function
import cv2 as cv

#Поиск изображения по источнику
original_image = cv.imread("images.jpg")
# преобразование цвета изображения из BGR в серый
cvtGray = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
dst = cv.equalizeHist(cvtGray)
cv.imshow('Source image', cvtGray)
cv.imshow('Equalized Image', dst)
cv.waitKey()