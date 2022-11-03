#изменить контрасть изображения
import cv2 as cv2
import numpy as np

img = cv2.imread('images.jpg', 1)
# преобразование в цветовое пространство ЛАБ
lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l_channel, a, b = cv2.split(lab)

# Применение CLAHE к L-каналу
clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(9,9))
cl = clahe.apply(l_channel)

# объедините улучшенный L-канал CLAHE с каналами a и b
limg = cv2.merge((cl,a,b))

#Преобразование изображения из лабораторной цветовой модели в цветовое пространство BGR
enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

# Наложение исходного изображения на улучшенное изображение
result = np.hstack((img, enhanced_img))
cv2.imshow('Result', result)
cv2.waitKey(0)
