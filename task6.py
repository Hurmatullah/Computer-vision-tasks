#отразить изображение по правой границе
import cv2 as cv

#Поиск изображения по источнику
image = cv.imread('images.jpg')
#Переворачивание изображения с помощью метода flip
flipImage = cv.flip(image, 1)
cv.imwrite('task6-image/new_flip_image.jpg', flipImage)