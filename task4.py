#перевести в grayscale
import cv2 as cv

#Поиск изображения по источнику
image = cv.imread('images.jpg')
#Преобразуйте цвет исходного изображения в серый цвет
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#Показ нашего изображения на экране
cv.imshow('Gray Image', gray)
cv.waitKey(0)
cv.destroyAllWindows()
