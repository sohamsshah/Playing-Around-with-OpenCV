# -*- coding: utf-8 -*-
"""
@author: Soham Shah
"""
import cv2,time
import datetime
from imutils.video import VideoStream
import argparse
import imutils
s(ap.parse_args())
vs = VideoStream(src=0).start()

time.sleep(2.0)

firstFrame = None
a=[]
b=[]
c=[]
d=[]

while True:
    frame = vs.read()
    text = "Unoccupied"
    b.append([datetime.datetime.now(),text])
    
    if frame is None:
        break
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    if firstFrame is None:
        firstFrame = gray
        continue
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=0)
    cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    for c in cnts:
        
        if cv2.contourArea(c) < 500:
            continue
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Occupied"
        b.append([datetime.datetime.now(),text])
           
    cv2.putText(frame, "Room Status: {}".format(text), (10, 20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if key == ord("u"):
        firstFrame = gray
    
vs.stop()

cv2.destroyAllWindows()


   
        
    
