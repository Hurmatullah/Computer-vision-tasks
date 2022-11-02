#изменить баланс белого, сделать более "теплую" картинку
from __future__ import (division, absolute_import, print_function, unicode_literals)
import cv2 as cv
import numpy as np


def show(final):
    cv.imshow('Temple', final)
    cv.waitKey(0)
    cv.destroyAllWindows()

# Insert any filename with path
img = cv.imread('download.jpg')

def white_balance_loops(img):
    result = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    for x in range(result.shape[0]):
        for y in range(result.shape[1]):
            l, a, b = result[x, y, :]
            # fix for CV correction
            l *= 100 / 255.0
            result[x, y, 1] = a - ((avg_a - 128) * (l / 100.0) * 1.1)
            result[x, y, 2] = b - ((avg_b - 195) * (l / 100.0) * 1.1)
    result = cv.cvtColor(result, cv.COLOR_LAB2BGR)
    return result

final = np.hstack((img, white_balance_loops(img)))
show(final)
cv.imwrite('task15-image/result.jpg', final)