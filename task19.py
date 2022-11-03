import cv2
import numpy as np

img = cv2.imread('iphone.jpg', cv2.IMREAD_UNCHANGED)

#преобразовать изображение в серый цвет
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#установите пороговое значение
thresh = 100
#получить пороговое изображение
ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
#найдите контуры
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#создайте пустое изображение для контуров
img_contours = np.zeros(img.shape)
# нарисуйте контуры на пустом изображении
cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)
cv2.imwrite('task19-image/contourIphone.jpg',img_contours)