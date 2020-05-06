# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:03:25 2019

@author: Felix
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()
hitarea = 50
target_x, target_y = 82,348

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    fgmask = cv2.GaussianBlur(fgmask,(5,5),0)

    #fgmask = cv2.medianBlur(fgmask,5)
    try:
        whites = np.where(fgmask == 255)
        y = int(np.median(whites[0]))
        x = int(np.median(whites[1]))
        #hitbox = fgmask[y-hitarea:y+hitarea,x-hitarea:x+hitarea]
        cv2.circle(frame, (x,y), hitarea, 180, thickness=5)
        #hitbox = frame[y-hitarea:y+hitarea,x-hitarea:x+hitarea]

        #hitbox[:,:] = 180
        
        if target_x < x+hitarea and target_x > x-hitarea and target_y < y+hitarea and target_y > y-hitarea:
            print('Treffer')
    except:
        print("Out of Bounds")
        
    #Fullscreen
    #cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    #cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow("window", frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

