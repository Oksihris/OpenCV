import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank image', blank)

# # Certain color
# blank[100:350, 160:480]=33,125,75
# cv.imshow('Green image', blank)

# Draw a rectangle
cv.rectangle(blank,(10,10),(blank.shape[1]//2, blank.shape[0]//2),(33,125,75), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# Draw a circle
cv.circle(blank,  (blank.shape[1]//2, blank.shape[0]//2), 55, (133,25,75),thickness=3)
cv.imshow('Circle', blank)

# Draw a line
cv.line(blank, (30,79), (300,370), (33,25,115), thickness=2)
cv.imshow('Line', blank)

# Write text
cv.putText(blank,'I like oranges',(260,420), cv.FONT_ITALIC ,1.0, (0,165,255),thickness=2)
cv.imshow('Text', blank)


cv.waitKey(0)
