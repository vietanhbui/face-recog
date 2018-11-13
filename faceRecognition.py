import numpy as np
import cv2

faceDetect = cv2.CascadeClassifier("D:\\Workspace\\Python\\Face Recognition\\haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

id = input("enter user id: ")
sampleNum = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sampleNum = sampleNum + 1
        cv2.imwrite("D:\\Workspace\\Python\\Face Recognition\\dataSet\\User." + str(id) + "." + str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 250, 0), 2)
        cv2.waitKey(100)
    cv2.imshow("Face Recognition", frame)
    cv2.waitKey(1)
    if sampleNum > 20:
        break
cap.release()
cap.destroyAllWindows()