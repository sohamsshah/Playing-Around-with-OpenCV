# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 23:24:24 2019

@author: Soham Shah
"""
import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(1):
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
 

    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
 

    mask1 = mask1+mask2
    
    
    
    res = cv2.bitwise_and(frame,frame,mask=mask1)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask1)
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break
    
cap.release()
cv2.destroyAllWindows()
