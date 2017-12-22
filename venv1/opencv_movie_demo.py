import cv2

VIDEO_FILE_PATH = './sprite.mp4'

movie = cv2.VideoCapture(VIDEO_FILE_PATH)

cv2.namedWindow('Face Movie')

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml') #Haar

while(True):
    ret, frame = movie.read()

    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grayframe, 1.1,3,0,(10,10))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3, 4, 0)

    cv2.imshow('Face', frame)

    if cv2.waitKey(1) ==27: # ESC
        break;

cap.release()
cv2.destroyWindow('Face')

