#сместить изображение но 10 пикселей вправо
import cv2
import numpy as np

#Поиск изображения по источнику
image = cv2.imread('images.jpg')
shift = 10

#Смещаем наше изображение на 10 пикселей вправо
for i in range(image.shape[1] -1, image.shape[1] - shift, -1):
    image = np.roll(image, 1, axis= 1)
    image[:, -1] = 0

cv2.imshow('image', image)
cv2.waitKey()