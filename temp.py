# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import cv2
import pickle
import numpy as np

# Constants
PARKING_SPACE_WIDTH = 26
PARKING_SPACE_HEIGHT = 15
THRESHOLD = 350

cap = cv2.VideoCapture("video.mp4")

def check(frame1):
    spaceCounter=0
    for pos in liste:
        x, y = pos
        crop = frame1[y:y + PARKING_SPACE_HEIGHT, x:x + PARKING_SPACE_WIDTH]
        #print(crop)
        count = cv2.countNonZero(crop)
        print(count)
        if count < THRESHOLD:
            color = (0, 255, 0)  # Green for empty
            spaceCounter+=1
        else:
            color = (0, 0, 255)  # Red for occupied
            
        cv2.rectangle(frame, pos, (pos[0] + PARKING_SPACE_WIDTH, pos[1] + PARKING_SPACE_HEIGHT), color, 2)
    
    cv2.putText(frame, f"bos:{spaceCounter}/{len(liste)}", (15,24),cv2.FONT_HERSHEY_SIMPLEX,1 ,(255,0,0),4)

with open("noktalar", "rb") as f:
    liste = pickle.load(f)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 1)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    median = cv2.medianBlur(thresh, 5)
    dilated = cv2.dilate(median, np.ones((3, 3)), iterations=4)
    
    check(dilated)
    
    cv2.imshow("Parking Status", frame)
    
    if cv2.waitKey(200) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
