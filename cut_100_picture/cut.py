import cv2
import numpy as np

columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
assure_path_exists("StudentDetails/")
assure_path_exists("TrainingImage/")
serial = 0
exists = os.path.isfile("StudentDetails\StudentDetails.csv")
if exists:
    with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            serial = serial + 1
    serial = (serial // 2)
    csvFile1.close()
else:
    with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
        writer = csv.writer(csvFile1)
        writer.writerow(columns)
        serial = 1
    csvFile1.close()
Id = (txt.get()) # Lấy ID từ ô nhập
name = (txt2.get()) # Lấy name từ ô nhập

if ((name.isalpha()) or (' ' in name)):
    cam = cv2.VideoCapture(0) # Bật camera
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
    sampleNum = 0
    while (True): 
        ret, img = cam.read() 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        faces = detector.detectMultiScale(gray, 1.3, 5) 
        for (x, y, w, h) in faces: 
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            sampleNum = sampleNum + 1
            cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                        gray[y:y + h, x:x + w])

            cv2.imshow('Taking Images', img)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

        elif sampleNum > 100:
            break
    cam.release() 
    cv2.destroyAllWindows() # Xóa cửa xổ
    res = "Images Taken for ID : " + Id
    row = [serial, '', Id, '', name]
    with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile: 
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    message1.configure(text=res)
else:
    if (name.isalpha() == False):
        res = "Enter Correct name"
        message.configure(text=res)


