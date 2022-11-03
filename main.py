#найти все orb features точки на изображении
import cv2 as cv
from matplotlib import pyplot as plt

# Считывающее изображение
image = cv.imread("images.jpg", 0)
# Инициирующий ШАР
orb = cv.ORB_create()
# Обнаружение ключевых точек с помощью шара
kp = orb.detect(image,None)
# вычислите дескрипторы с помощью ORB
kp, des = orb.compute(image, kp)
# Рисование ключевых моментов
img2 = cv.drawKeypoints(image, kp, None, color=(0,255,0), flags=0)
plt.imshow(img2), plt.show()
cv.imwrite('task1-image/image1.jpg', img2)