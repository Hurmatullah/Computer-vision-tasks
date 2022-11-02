#найти все sift features точки на изображении
import cv2 as cv

image = cv.imread('images.jpg')
gray= cv.cvtColor(image,cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp = sift.detect(gray,None)
image=cv.drawKeypoints(gray,kp,image)
cv.imwrite('task2-image/sift_keypoints.jpg',image)