#сделать гамма-перобразование
from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse

alpha = 1.0
alpha_max = 500
beta = 0
beta_max = 200
gamma = 1.0
gamma_max = 200

def gammaCorrection():
    ## [changing-contrast-brightness-gamma-correction]
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)

    res = cv.LUT(img_original, lookUpTable)
    ## [changing-contrast-brightness-gamma-correction]

    img_gamma_corrected = cv.hconcat([img_original, res])
    cv.imshow("Gamma correction", img_gamma_corrected)

def on_gamma_correction_trackbar(val):
    global gamma
    gamma = val / 100
    gammaCorrection()

parser = argparse.ArgumentParser(description='Code for Changing the contrast and brightness of an image! tutorial.')
parser.add_argument('--input', help='Path to input image.', default='images.jpg')
args = parser.parse_args()

img_original = cv.imread(cv.samples.findFile('images.jpg'))
if img_original is None:
    print('Could not open or find the image: ', img_original)
    exit(0)

img_gamma_corrected = np.empty((img_original.shape[0], img_original.shape[1]*2, img_original.shape[2]), img_original.dtype)

img_gamma_corrected = cv.hconcat([img_original, img_original])

cv.namedWindow('Gamma correction')

gamma_init = int(gamma * 100)
cv.createTrackbar('Gamma correction', 'Gamma correction', gamma_init, gamma_max, on_gamma_correction_trackbar)

on_gamma_correction_trackbar(gamma_init)

cv.waitKey()