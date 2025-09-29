import os 
import cv2

image = cv2.imread(os.path.join('.', 'data', 'howard.jpeg'))
# Resize image
print (image.shape)
#cv2.imshow('image', image)
#cv2.waitKey(0)
resized_image = cv2.resize(image, (750, 500))
#print (resized_image.shape)
cropped_image = image[0:400, 0:400]
print (cropped_image.shape)
cv2.imshow('cropped_image', cropped_image)
cv2.waitKey(0)