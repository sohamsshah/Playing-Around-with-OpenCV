# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:21:49 2020

@author: Soham Shah
"""

#image operations

import cv2
img = cv2.imread('1.png')
print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
