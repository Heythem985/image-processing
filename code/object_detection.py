import os 
import cv2

img=cv2.imread(os.path.join('.','data','cats.png'))
resized_img=cv2.resize(img,(786,512))
img_gray=cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
ret,threshold = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
contours,hierarchy=cv2.findContours(threshold,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours :
    x1 , y1 , w , h = cv2.boundingRect(cnt)
    cv2.rectangle(resized_img,(x1,y1),(x1+w,y1+h),(0,255,0),2)


cv2.imshow('resized_img',resized_img)
cv2.imshow('threshold',threshold)
cv2.waitKey(0)
