# изменить цветовую палитру по заданному шаблону
import numpy as np
import cv2 as cv
def callbackFunction(x):
    pass
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('Color_Palette')
# create trackbars for color change
cv.createTrackbar('R','Color_Palette',0,255,callbackFunction)
cv.createTrackbar('G','Color_Palette',0,255,callbackFunction)
cv.createTrackbar('B','Color_Palette',0,255,callbackFunction)
# создать переключатель для включения / выключения функциональности
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'Color_Palette',0,1,callbackFunction)
while(1):
    cv.imshow('Color_Palette',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # получить текущие позиции четырех полос трека
    r = cv.getTrackbarPos('R','Color_Palette')
    g = cv.getTrackbarPos('G','Color_Palette')
    b = cv.getTrackbarPos('B','Color_Palette')
    s = cv.getTrackbarPos(switch,'Color_Palette')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
cv.destroyAllWindows()