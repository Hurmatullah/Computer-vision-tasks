# сделать фильтрацию изображения при помощи Фурье преобразоваия, оставить только быстрые частоты
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('images.jpg',0)

img_float32 = np.float32(img)

dft = cv.dft(img_float32, flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('High frequence'), plt.xticks([]), plt.yticks([])
plt.show()
cv.imwrite('task22-image/Original_image.jpg', img)
cv.imwrite('task22-image/HighFrequency.jpg', magnitude_spectrum)