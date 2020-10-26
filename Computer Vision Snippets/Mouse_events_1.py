# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:56:08 2020

@author: Soham Shah
"""

import cv2
import numpy as np
cap = cv2.VideoCapture(0)

# Getting size of captured frame
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# CAP_PROP_FRAME_WIDTH -> 3
# CAP_PROP_FRAME_WIDTH -> 4

# Altering the size of captured frame
cap.set(3,1200)
cap.set(4,480)
print(cap.get(3))
print(cap.get(4))

#get different events
events = [i for i in dir(cv2) if 'EVENT' in i]

def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x," ",y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x) + ' ' + str(y)
        cv2.putText(frame,text,(x,y), font,0.5,(0,255,255),2)
        cv2.imshow('image', frame)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = frame[y,x,0]
        green = frame[y,x,1]
        red = frame[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(blue) + ' ' + str(green) + ' ' + str(red)
        cv2.putText(frame,text,(x,y), font,0.5,(0,0,255),2)
        cv2.imshow('image', frame)
        
        
        

while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
#        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Width: "+ str(cap.get(3))+ " Height: "+ str(cap.get(4))
        frame = cv2.putText(frame, text, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow('image',frame)
        cv2.setMouseCallback('image',click_event)
            
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
