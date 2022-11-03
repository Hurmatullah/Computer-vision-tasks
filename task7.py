#отразить изображение по нижней границе
import cv2 as cv

#Поиск изображения по источнику
image = cv.imread('images.jpg')
flipImageBottom = cv.flip(image, 0)
cv.imwrite('task7-image/new_flip_image.jpg', flipImageBottom)