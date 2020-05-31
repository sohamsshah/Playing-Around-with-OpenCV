# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:46:16 2019

@author: Soham Shah
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:29:56 2019

@author: Soham Shah
"""

import numpy as np
import cv2
#Making a list of all classes that MobileNet SSD(single Shot Display) includes
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat","chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3)) 
#random colors for our bounding boxes. We need 20 different colors for each box

net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")
"""The net is being loaded by the above code. We need the caffemodel file and the txt file to pass as params in the function.
It is for deployment for our detection.

"""


image = cv2.imread("img2.jfif") #reads image
(h, w) = image.shape[:2] #taking image's height and width 

blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
#making blob of (300,300) 


net.setInput(blob)
#inputing the blob
detections = net.forward()
#computations and detections and feeding it forward in the net
confidence_vals = []
THRESH = 0.03
detections_idx = []
detections_overall = []
detections_box = []


for i in np.arange(0,detections.shape[2]):
    confidence = detections[0,0,i,2]
    confidence_vals.append(confidence)
    detections_idx.append(detections[0,0,i,1])
    
    
    if confidence > THRESH:
        idx = int(detections[0,0,i,1])
        #getting the index of the detection
        box = detections[0,0,i, 3:7] * np.array([w,h,w,h])
        #finding dimensions of the box by multiplying the values of dimensions of the detected image and the width&height of the image 
    
        detections_idx.append(detections[0,0,i, 3:7])
        detections_overall.append(box)
        
        (startX, startY, endX, endY) = box.astype("int")
        #getting the dimensions of the box
        
        label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
        print("[INFO] {}".format(label))
        cv2.rectangle(image, (startX, startY),(endX, endY), COLORS[idx], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(image,label, (startX,y), cv2.FONT_HERSHEY_SIMPLEX,0.5, COLORS[idx],2)
cv2.imshow("OUTPUT", image)
cv2.waitKey(0)
        
                
