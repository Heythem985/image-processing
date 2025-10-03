import os 
import cv2
import numpy as np

image = cv2.imread(os.path.join('.','data','image.jpg'))
#print(image.shape)
image_resized= cv2.resize(image,(368,552))
#print (image_resized.shape)
#edge detection is used to show the edges in an image الحواف
image_edge=cv2.Canny(image_resized,100,200)
image_d=cv2.dilate(image_edge,np.ones((5,5),dtype=np.int8))
image_e=cv2.erode(image_d,np.ones((3,3),dtype=np.int8))




cv2.imshow('image_edge',image_edge)
cv2.imshow('image_resized',image_resized)
cv2.imshow('image_d',image_d)
cv2.imshow('image_e',image_e)
cv2.waitKey(0)
