import cv2 as cv
import numpy as np
import os

haar_cascade=cv.CascadeClassifier('haar_face.xml')

p =[]
for i in os.listdir(r'D:\Tutorials\Faces\train'):
    p.append(i)

# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img =cv.imread(r'D:\Tutorials\Faces\val\jerry_seinfeld\4.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)


# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)

    print(f'Label = {p[label]} with a confidence of {confidence}')

    cv.putText(img, str(p[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), thickness=2)
    cv.rectangle(img,(x,y), (x+w,y+h), (33,125,75), thickness=2)

cv.imshow('Detected face', img)


cv.waitKey(0)


