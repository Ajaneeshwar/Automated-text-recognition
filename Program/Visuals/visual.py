#!/usr/bin/env python
# coding: utf-8

# # Extraction of character from Visuals

# In[ ]:


import pytesseract
import cv2
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open Camera")
    
    
cntr = 0;
while True:
    ret,frame = cap.read()
    if((cntr%2)==0):
        
        imgH,imgW,_ = frame.shape
        
        x1,y1,w1,h1 = 0,0,imgH,imgW
        
        imgchar = pytesseract.image_to_string(frame)
        
        imgboxes = pytesseract.image_to_boxes(frame)
        for boxes in imgboxes.splitlines():
            boxes = boxes.split(' ')
            x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
            cv2.rectangle(frame,(x,imgH-y),(w,imgH-h),(0,0,255),1)
        
        cv2.putText(frame, imgchar, (x1 + int(w1/50),y1 + int(h1/50)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        
        
        cv2.imshow('Character Extraction form Visuals - Batch 7', frame)
        
        if cv2.waitKey(2) == ord('e'):
            print(imgchar,"\n\n\n DEVELOPER @ RASHAD H")

        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()            
            break

            
cap.release()
cv2.destroyAllWindows()
