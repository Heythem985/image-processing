import os 
import cv2

image = cv2.imread(os.path.join('.','data','howard.jpeg')) 
image_rgb= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_hsv= cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',image )
cv2.imshow('image_rgb',image_rgb)
cv2.imshow('image_hsv',image_hsv)
cv2.imshow('image_gray',image_gray)

cv2.waitKey(0)
