# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:51:30 2020

@author: Soham Shah
"""


import cv2
import numpy as np
import math

events = [i for i in dir(cv2) if 'EVENT' in i]

def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        cv2.circle(img,(x,y), 3, (0,0,255),-1)
        myColorImage = np.zeros((512,512,3), np.uint8)
        myColorImage[:] = [blue,green,red]
        cv2.imshow('color',myColorImage)

img = cv2.imread('1.png')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
