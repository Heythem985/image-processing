import os 
import cv2
#threshold is for making an image just two color (after using gray color space)
#it's useful in object traking .
image = cv2.imread(os.path.join('.','data','image.jpg'))
image_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
ret,threshold_image = cv2.threshold(image_gray,80,255,cv2.THRESH_BINARY)

#adaptive_thresold useful when we need to separate a shadow for example like the paper
adaptive_threshold = cv2.adaptiveThreshold(image_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY ,11, 2)



cv2.imshow('adaptive_threshold',adaptive_threshold)
cv2.imshow('image_gray',image_gray)
cv2.imshow('threshold_image',threshold_image)
cv2.imshow('image',image)
cv2.waitKey(0)