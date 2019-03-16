import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

#Using a gaussian adaptive threshold
gauss = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval2, otsu = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('original', img)
cv2.imshow('Threshold', threshold)
cv2.imshow('Gray', threshold2)
cv2.imshow('gauss', gauss)
#cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()