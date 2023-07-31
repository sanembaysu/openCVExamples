import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (500, 500))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
    # scaleFactor (1.1) : Giriş görüntüsünün boyutunu küçültmek için kullanılır. %10
    # minNeighbors (5) : Görüntüdeki yüzleri algılamak iin görüntü boyunca kayan bir pencere uygular.

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (54, 85, 255), 4)


    cv2.imshow('Yuz Tanima', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect_faces('face1.jpg')


