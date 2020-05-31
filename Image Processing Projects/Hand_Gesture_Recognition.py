# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 00:45:48 2019

@author: Soham Shah
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 22:48:13 2019

@author: Soham Shah
"""

import cv2
import numpy as np
import imutils

firstFrame = None



def run_avg(image, aWeight):
    global firstFrame
    # initialize the background
    if firstFrame is None:
        firstFrame = image.copy().astype("float")
        return

    # compute weighted average, accumulate it and update the background
    cv2.accumulateWeighted(image, firstFrame, aWeight)

def segment(image,threshold = 25):
    global firstFrame
    diff = cv2.absdiff(firstFrame.astype("uint8"),image)
    thresholded = cv2.threshold(diff,threshold,255,cv2.THRESH_BINARY)[1]
    cnts,_ = cv2.findContours(thresholded.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) == 0:
        return
    else:
        segmented = max(cnts,key = cv2.contourArea)
        
        return (thresholded,segmented)
        


from sklearn.metrics import pairwise



def count(thresholded,segmented):
    chull = cv2.convexHull(segmented)
    extreme_top = tuple(chull[chull[:,:,1].argmin()][0])
    extreme_bottom = tuple(chull[chull[:,:,1].argmax()][0])
    extreme_left = tuple(chull[chull[:,:,0].argmin()][0])
    extreme_right = tuple(chull[chull[:,:,0].argmax()][0])
    
    cX = (extreme_left[0] + extreme_right[0])/2
    cY = (extreme_top[0] + extreme_bottom[0])/2
    distance = pairwise.euclidean_distances([(cX,cY)],Y = [extreme_left,extreme_right,extreme_top,extreme_bottom])[0]
    maximum_distance = distance[distance.argmax()]
    radius = int(0.8*maximum_distance)
    circumference = (2* np.pi * radius)
    circular_roi = np.zeros(thresholded.shape[:2],dtype = "uint8")
    cv2.circle(circular_roi, (int(cX),int(cY)),int(radius),255,1)
    circular_roi = cv2.bitwise_and(thresholded,thresholded,mask=circular_roi)
    
    cnts,_ = cv2.findContours(circular_roi.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    count = 0
    for c in cnts:
        (x,y,w,h) = cv2.boundingRect(c)
        if ((cY + (cY*0.25)) > (y + h)) and ((circumference * 0.25) > c.shape[0]):
            print(count)
            count += 1
    return count



aWeight = 0.5
camera = cv2.VideoCapture(0)

top,right,bottom,left = 120,250,400,590
num_frame = 0



while True:
    grabbed,frame = camera.read()
    
    
    frame = imutils.resize(frame,width=700)
    
    frame = cv2.flip(frame,1)
    
    clone = frame.copy()
    height,width = frame.shape[:2]
    roi = frame[top:bottom,right:left]
    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(7,7),0)
    if num_frame < 30:
        run_avg(gray,aWeight)
    else:
    
        hand = segment(gray)
        
        if hand is not None:
            thresholded,segmented = hand
            cv2.drawContours(clone,[segmented + (right,top)], -1,(0,0,255))
            cv2.imshow("Thresholded",thresholded)
        
    cv2.rectangle(clone, (left,top),(right,bottom),(0,255,0),2)
    a = str(count(thresholded,segmented))
    #print(a)
    num_frame += 1
    
    
    cv2.putText(clone, a , (600,50), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
        
    cv2.imshow("Video Feed",clone)
    
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('u'):
        run_avg(gray,aWeight)
    
    if key == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()


    
    
            
            
            