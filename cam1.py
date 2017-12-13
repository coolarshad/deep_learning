import cv2
import os 
import numpy as np

cap=cv2.VideoCapture(0)

#font=cv2.FONT_HERSHEY_SIMPLEX
while True:
  ret, img=cap.read()
  cv2.imwrite('cap_image.jpg',img)  
  
  #cv2.imshow('image',img)
#  im=open('a','r+')
#  line1=im.readline()
# line2=im.readline()
# cv2.putText(img,line1,(0,30),font,1,(0,255,0),2,cv2.LINE_AA)
# cv2.putText(img,line2,(0,60),font,1,(0,255,0),2,cv2.LINE_AA)
  cv2.imshow('object',img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
