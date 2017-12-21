#coding: euc-kr
# *opencv 이용
# - google api사용하지 않고
# https://opencv.org/
#
# https://github.com/opencv/opencv/tree/master/data/haarcascades
# https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html
# http://prologos.tistory.com/1
#
# * package 3개 설치
# opencv-python
# opencv-contrib-python
# numpy - 수학 계산
#
# 머신러닝/딥러닝
import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

image = cv2.imread('./2016090911081720022.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30),
)

print  "Found {0} faces!".format(len(faces))
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w, y+h), (0,255,0),2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)



