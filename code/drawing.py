import os 
import cv2

img=cv2.imread(os.path.join('.','data','image.jpg')) 
resized_image = cv2.resize(img,(368,552))
#line 
cv2.line(resized_image,(100,100),(200,200),(0,255,0),2)
#rectangle 
cv2.rectangle(resized_image,(120,120),(280,280),(255,0,0),3)
#circle 
cv2.circle(resized_image,(300,300),30,(0,0,255),4)
#text 
cv2.putText(resized_image,'hello i am here ' ,(100,450),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),4)
cv2.imshow('resized_image',resized_image)
cv2.waitKey(0)