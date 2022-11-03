# повернуть изображение на 30 градусов
import cv2 as cv

#Поиск изображения по источнику
image = cv.imread('images.jpg')
(h, w) = image.shape[:2]
center = (w / 2, h / 2)
angle = 30
scale = 1
#Поворот изображения на 30 градусов
M = cv.getRotationMatrix2D(center, angle, scale)
rotated = cv.warpAffine(image, M, (w, h))
cv.imwrite('task9-image/30_degree_image.jpg', rotated)