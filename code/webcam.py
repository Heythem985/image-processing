import os 
import cv2
# Access webcam  
webcam = cv2.VideoCapture(0)
# Read frames from webcam
while True :
    ret,frame = webcam.read()
    if ret :
        cv2.imshow('webcam', frame)
            # Press 'q' to exit the loop
        if cv2.waitKey(40) & 0xFF == ord('q'):
            break 
#        
webcam.release()
cv2.destroyAllWindows()        