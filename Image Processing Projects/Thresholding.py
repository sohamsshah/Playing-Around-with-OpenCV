# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:24:43 2020

@author: Soham Shah
"""
# Simple Thresholding

import cv2 
img = cv2.imread('post.jpg',0) #Take B/W Image

_,th1 = cv2.threshold(img, 50,255, cv2.THRESH_BINARY) #if pixel value is greater than X it is assigned 255
_,th2 = cv2.threshold(img, 50,255, cv2.THRESH_BINARY_INV) #if pixel value is lesser than X it is assigned 255
_,th3 = cv2.threshold(img, 200,255, cv2.THRESH_TRUNC) # Till pixel value X it doesnt change, and after X, pixel intesity remains X throughout
_,th4 = cv2.threshold(img, 127,255, cv2.THRESH_TOZERO) # Till pixel value X it changes to Zero and stays 
_,th5 = cv2.threshold(img, 127,255, cv2.THRESH_TOZERO_INV)

cv2.imshow('img',img)

cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)
cv2.imshow('th4',th4)
cv2.imshow('th5',th5)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Adaptive Thresholding

th6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 1) #blocksize and constant
th7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('th6',th6)
cv2.imshow('th7',th7)
cv2.waitKey(0)
cv2.destroyAllWindows()