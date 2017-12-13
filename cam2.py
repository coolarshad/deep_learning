import cv2
from time import sleep

cap=cv2.VideoCapture(0)
count=0
font=cv2.FONT_HERSHEY_SIMPLEX

while True:
  _,img=cap.read()
  #cv2.imshow('img',img)
  if count<4:
    cv2.putText(img,str(count),(250,300),font,1,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow('img2',img)
  count+=1
  sleep(1)
  k=cv2.waitKey(1) & 0xFF
  if k==27:
    break
cap.release()
cv2.destroyAllWindows()
