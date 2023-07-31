import cv2

face_classifier = cv2.CascadeClassifier\
    (cv2.data.haarcascades + "haarcascade_frontalface_default.xml")    # Haar Cascade modeli

video_capture = cv2.VideoCapture(0)     #web kamerası erişimi


def detect_faces(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY) # yüz algılanmadan önce çevreyi gri tonlamaya dönüştür

    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))   # yüzü tespit etme
    # scaleFactor (1.1) : Giriş görüntüsünün boyutunu küçültmek için kullanılır. %10
    # minNeighbors (5) : Görüntüdeki yüzleri algılamak iin görüntü boyunca kayan bir pencere uygular.

    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (255, 255, 255), 4)     # yüz için sınırlayıcı
    return faces

while True:
    result, video_frame = video_capture.read()  # videodan kareleri oku
    if result is False:
        break  # başarılı değilse döngüyü sonlandır

    faces = detect_faces(video_frame)  # oluşan fonksiyonu videoya uygula

    cv2.imshow("Yuz Algilama", video_frame)  # pencereyi görüntüle

    if cv2.waitKey(1) & 0xFF == ord("c"):
        break

video_capture.release()
cv2.destroyAllWindows()