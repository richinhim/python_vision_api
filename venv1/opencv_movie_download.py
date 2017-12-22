import cv2

VIDEO_FILE_PATH='./sprite.mp4'

cap = cv2.VideoCapture(VIDEO_FILE_PATH)
cv2.namedWindow('Original')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps   = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # - *MJPG
filename = 'sprite_face_detect.avi'

out = cv2.VideoWriter(filename, fourcc, fps, (int(width) , int(height)))

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
while(True):
    ret, frame = cap.read()

    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayframe, 1.1, 3, 0, (10, 10))

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3, 4, 0)

    cv2.imshow('Face', frame)
    out.write(frame)

    if cv2.waitKey(1) == 27:
        break;

cap.release()
out.release()
cv2.destroyAllWindows()