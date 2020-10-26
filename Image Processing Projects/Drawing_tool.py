# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:13:27 2020

@author: Soham Shah
"""

import cv2
import numpy as np
import math

events = [i for i in dir(cv2) if 'EVENT' in i]

def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y), 3,(0,255,255),-1)
        points.append((x,y))
        if len(points) >=2:
            distance = math.sqrt((points[0][0]-points[-1][0])**2 + (points[0][1]-points[-1][1])**2) 
            NN = (points[0][0],points[0][1])
            for i in points[:-1]:
                if (distance) > math.sqrt((i[0]-points[-1][0])**2 + (i[1]-points[-1][1])**2):
                    NN = (i[0],i[1])
            
            cv2.line(img,points[-1], NN, (255,255,0),5)
        cv2.imshow('image',img)
        
points = []

img = np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
