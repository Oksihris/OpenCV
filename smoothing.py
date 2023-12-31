import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

#Averaging
average = cv.blur(img, (3,3))
cv.imshow('Averaged', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilatural
bilatural = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilatural Blur', bilatural)

cv.waitKey(0)