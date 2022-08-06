import cv2
import numpy as np

img = cv2.imread("frame_ROS_camera.jpeg")
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([175,0,0])
upper_red = np.array([255,255,255])
mask_red = cv2.inRange(imghsv, lower_red, upper_red)
_, contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

im = np.copy(img)
cv2.drawContours(im, contours, -1, (0, 255, 0), 2)
cv2.imshow("im", im)

#waits for user to press any key 
cv2.waitKey(0) 

#closing all open windows 
cv2.destroyAllWindows()