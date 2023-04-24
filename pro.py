import cv2
img = cv2.imread('solar-system.jpg')

cv2.putText(img,'EARTH',(400,200),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,255))
cv2.imshow('output',img)
cv2.waitKey(0)