import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2,img.shape[0]//2), 150, 255, -1)
rectangle = cv.rectangle(blank.copy(),(250,50), (400,400), 255, thickness= -1)
bitwise_or = cv.bitwise_or(rectangle, circle)


masked = cv.bitwise_and(img,img, mask=bitwise_or)
cv.imshow('Masked', masked)


cv.waitKey(0)