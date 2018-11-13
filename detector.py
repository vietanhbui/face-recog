import os
import cv2
import numpy as np
import sqlite3
from PIL import Image

faceDetect = cv2.CascadeClassifier("D:\\Workspace\\Python\\Face Recognition\\haarcascade_frontalface_default.xml")
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("D:\\Workspace\\Python\\Face Recognition\\recognizer\\trainingData.yml")
# id = 0
# font = cv2.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL, 5, 1, 0, 4)

def getProfile(id):
    conn = sqlite3.connect("D:\\Workspace\\Python\\Face Recognition\\FaceBase.db")
    cmd = "SELECT * FROM People WHERE ID = " + str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        id, conf = rec.predict(gray[y:y+h, x:x+w])
        profile = getProfile(id)
        if profile != None:
            # cv2.cv.PutText(cv2.cv.fromarray(frame), str(id), (x, y + h), font, 255)
            cv2.putText(frame, str(profile[1]), (x, y + h), font, 1, (255, 255, 255))
            cv2.putText(frame, str(profile[2]), (x, y + h + 30), font, 1, (255, 255, 255))
            cv2.putText(frame, str(profile[3]), (x, y + h + 60), font, 1, (255, 255, 255))
    cv2.imshow("Face", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()