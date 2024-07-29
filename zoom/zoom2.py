import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    img1 = cv2.imread("D:\drag\zoom\pizza.jpg")

    img[0:250, 0:250]= img1
    cv2.imshow("Camera Feed", img)
    cv2.waitKey(1)
