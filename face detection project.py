import cv2

detect=cv2.CascadeClassifier(r"C:\Users\harsh\OneDrive\Desktop\FACE DETECT\haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)

while True:
    ret,image=cap.read()
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    face=detect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow('Camera',gray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


    
    
