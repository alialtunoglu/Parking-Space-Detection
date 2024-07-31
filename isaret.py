# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:48:30 2024
@author: alial
"""

import cv2
import pickle

# Constants
PARKING_SPACE_WIDTH = 26
PARKING_SPACE_HEIGHT = 15

try:
    with open("noktalar", "rb") as f:
        liste = pickle.load(f)
except FileNotFoundError:
    liste = []

def mouse(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        liste.append((x, y))
    elif events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(liste):
            x1, y1 = pos
            if x1 < x < x1 + PARKING_SPACE_WIDTH and y1 < y < y1 + PARKING_SPACE_HEIGHT:
                liste.pop(i)
    with open("noktalar", "wb") as f:
        pickle.dump(liste, f)

while True:
    img = cv2.imread("first_frame.png")
    
    for l in liste:
        cv2.rectangle(img, l, (l[0] + PARKING_SPACE_WIDTH, l[1] + PARKING_SPACE_HEIGHT), (255, 0, 0), 2)
    
    cv2.imshow("pen", img)
    cv2.setMouseCallback("pen", mouse)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cv2.destroyAllWindows()
