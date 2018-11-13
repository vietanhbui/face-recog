import cv2
import sqlite3

cap = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier("D:\\Workspace\\Python\\Face Recognition\\haarcascade_frontalface_default.xml")
# detector = cv2.CascadeClassifier("D:\\Workspace\\Python\\Face Recognition\\lbpcascade_frontalface.xml")

def insertOrUpdate(id, name, age, gender):
    conn = sqlite3.connect("D:\\Workspace\\Python\\Face Recognition\\FaceBase.db")
    cmd = "SELECT * FROM People WHERE ID = " + str(id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if isRecordExist == 1:
        cmd = "UPDATE People SET Name = '" + str(name) + "', Age = " + str(age) + ", Gender = '" + str(gender) + "' WHERE ID = " + str(id)
    else:
        cmd = "INSERT INTO People(ID, Name, Age, Gender) VALUES(" + str(id) + ", '" + str(name) + "', " + str(age) + ", '" + str(gender) + "')"
    conn.execute(cmd)
    conn.commit()
    conn.close()

id = input("Enter your id: ")
name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
insertOrUpdate(id, name, age, gender)
sampleNum = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sampleNum = sampleNum + 1
        cv2.imwrite("D:\\Workspace\\Python\\Face Recognition\\dataSet\\User." + str(id) + "." + str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(frame, (x - 50, y - 50), (x + w + 50, y + h + 50), (255, 0, 0), 2)
    cv2.imshow("Frame", frame)
    cv2.waitKey(100)
    if sampleNum > 20:
        cap.release()
        cv2.destroyAllWindows()
        break