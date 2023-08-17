import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# BGR to Grayscale
gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx= cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely= cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel =cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel x',sobelx)
cv.imshow('Sobel y', sobely)
cv.imshow('Sobel', combined_sobel)

canny = cv.Canny(gray,150, 175)
cv.imshow('Canny', canny)


combined_lc =cv.bitwise_and(lap, canny)
cv.imshow('Lap and canny', combined_lc)

cv.waitKey(0)