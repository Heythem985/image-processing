import os 
import cv2 

#Read image
img_path = os.path.join('.', 'data', 'howard.jpeg')
img = cv2.imread(img_path)
#Write image
cv2.imwrite(os.path.join( '.' , 'data', 'howard_out.jpeg') , img)
#Display image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



