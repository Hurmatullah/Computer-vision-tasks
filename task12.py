#изменить контрасть изображения
import cv2 as cv
import numpy as np

img = cv.imread('images.jpg', 1)
# преобразование в цветовое пространство ЛАБ
lab= cv.cvtColor(img, cv.COLOR_BGR2LAB)
l_channel, a, b = cv.split(lab)

# Применение CLAHE к L-каналу
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl = clahe.apply(l_channel)

# объедините улучшенный L-канал CLAHE с каналами a и b
limg = cv.merge((cl,a,b))

#Преобразование изображения из лабораторной цветовой модели в цветовое пространство BGR
enhanced_img = cv.cvtColor(limg, cv.COLOR_LAB2BGR)

# Наложение исходного изображения на улучшенное изображение
result = np.hstack((img, enhanced_img))
cv.imshow('Result', result)
cv.imwrite('task12-image/enhanced_image.jpg', result)
cv.waitKey(0)
