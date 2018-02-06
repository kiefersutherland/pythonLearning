import numpy
import cv2
#strulr='1.jpg'
strulr=r'F:\pic\1.jpg'
img=cv2.imread(strulr)
win = cv2.namedWindow('test win', flags=0)  
  
cv2.imshow('test win', img)  


cv2.waitKey(0)  
cv2.destroyAllWindows() 