# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 17:35:47 2020

@author: Soham Shah
"""

# Morphological Transformation

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('smarties.png',0)
_,mask = cv2.threshold(img,200,255, cv2.THRESH_BINARY_INV)
kernel = np.ones((2,2),np.uint8)
dilation = cv2.dilate(mask,kernel, iterations=2) #adding dilation
erosion = cv2.erode(mask,kernel,iterations=2) #erosion
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) #erosion then dilation
closed = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel) #dilation then erosion
mg =cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel) #difference between Dilation and Erosion

titles = ['image','mask', 'dilation', 'erosion', 'opening', 'closed', 'mg']
images = [img,mask,dilation, erosion, opening, closed,mg]

for i in range(len(images)):    
    plt.subplot(3,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    