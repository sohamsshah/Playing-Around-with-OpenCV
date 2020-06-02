# -*- coding: utf-8 -*-
"""
@author: Soham Shah
"""

import cv2
import numpy as np 
  
cap = cv2.imread('#image-path')
    
hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV) 

lower_red = np.array([30,150,50]) 

upper_red = np.array([255,255,180]) 

# create a red HSV colour boundary and
# threshold HSV image 
mask = cv2.inRange(hsv, lower_red, upper_red) 

# Bitwise-AND mask and original image 

res = cv2.bitwise_and(cap,cap, mask= mask) 
edges = cv2.Canny(cap,100,200) 
indices = np.where(edges != [0])
coordinates = np.array([indices[0], indices[1]])
print(coordinates)

cv2.imshow('#img-name',res)
cv2.imshow("#img-name",edges)
cv2.waitKey(2)
