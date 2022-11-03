#найти все sift features точки на изображении
import cv2 as cv

# Поиск изображения по источнику
image = cv.imread('images.jpg')
# Преобразование цвета из BGR в серый
cvColor= cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# способ инициирования просеивания
sift = cv.SIFT_create()
# Обнаружение преобразованного цвета
siftDetect = sift.detect(cvColor,None)
image=cv.drawKeypoints(cvColor,siftDetect,image)
cv.imwrite('task2-image/sift_keypoints.jpg',image)
