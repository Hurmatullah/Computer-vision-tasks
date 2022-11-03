#сделать размытие изображения
import cv2 as cv

img = cv.imread('images.jpg')
blur = cv.blur(img,(5,5))
cv.imshow('Original',img)
cv.imshow('Blurred', blur)
cv.imwrite('task21-image/Original_image.jpg', img)
cv.imwrite('task21-image/Blur_image.jpg', blur)
cv.waitKey(0)