#перевести изорбражение в hsv
import cv2 as cv

#Поиск изображения по источнику
image = cv.imread('images.jpg')
#Преобразование цвета нашего изображения из BGR в HSV
cvtHsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
#Отображение изображения на экране
cv.imshow("Original Image", image)
cv.imshow('Converted to HSV', cvtHsv)
cv.imwrite('task5-image/original_image.jpg',image)
cv.imwrite('task5-image/converted_to_HSV.jpg',cvtHsv)
cv.waitKey(0)
cv.destroyAllWindows()