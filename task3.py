#найти canny edges на изображенни
import cv2 as cv
import matplotlib.pyplot as plt

# Поиск изображения по источнику
image = cv.imread('images.jpg',0)
#Используя метод хитрого изображения для нашего изображения
edges = cv.Canny(image,100,200)
#Сравнение исходного изображения с измененным состоянием нашего изображения с помощью canny image.
cv.imshow('Original image', image)
cv.imshow('Canny edges', edges)
cv.waitKey(0)