import cv2
 
# init Webcam
cam = cv2.VideoCapture(0)

# yellow
lower_yellow = (18, 60, 120) #(18, 100, 210)
upper_yellow = (48, 200, 245) #(40, 160, 245) 

while cam.isOpened():
    # get frame from webcam
    ret, frame = cam.read()
 
    # convert to HSV for better filtering
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    # filter frame
    mask = cv2.inRange(frame, lower_yellow, upper_yellow)
 
    # show frame
    cv2.imshow("threshold", mask)
  
    key = cv2.waitKey(1) & 0xff
 
    if key == 27:
        break
