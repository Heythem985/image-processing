import os 
import cv2 

image = cv2.imread(os.path.join('.' ,'data' ,'noisy_image.jpg'))
print(image.shape)
#resized_image = cv2.resize(image,(368,552))
#print(resized_image.shape)
image_average = cv2.blur(image,(5,5))
image_gaussian = cv2.GaussianBlur(image,(5,5),0)
image_median = cv2.medianBlur(image,3)

cv2.imshow('resized_image',image )
cv2.imshow('image_average ',image_average )
cv2.imshow('image_gaussian',image_gaussian )
cv2.imshow('image_median',image_median )
cv2.waitKey(0)

