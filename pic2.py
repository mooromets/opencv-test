import cv2

frame = cv2.imread("lego.png")
 
lower_yellow = (18, 30, 30) #(18, 100, 210)
upper_yellow = (48, 255, 255) #(40, 160, 245) 

frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(frame, lower_yellow, upper_yellow)

cv2.imshow("threshold", mask)

cv2.waitKey(0)
