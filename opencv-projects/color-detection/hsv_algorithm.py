import cv2
import numpy as np

# empty function definition for trackbar
def empty_function(x):
    pass

#creating the window
cv2.namedWindow("Trackbar")

#starting the video source (we enter the parameter as 0 for webcam. If you have an external camera, you can enter it as 1)
cap = cv2.VideoCapture(0)

#creating trackbars
cv2.createTrackbar("Lower - H","Trackbar",0,180,empty_function)
cv2.createTrackbar("Lower - S","Trackbar",0,255,empty_function)
cv2.createTrackbar("Lower - V","Trackbar",0,255,empty_function)

cv2.createTrackbar("Upper - H","Trackbar",0,180,empty_function)
cv2.createTrackbar("Upper - S","Trackbar",0,255,empty_function)
cv2.createTrackbar("Upper - V","Trackbar",0,255,empty_function)

#assigning default trackbar values
cv2.setTrackbarPos("Upper - H","Trackbar",180)
cv2.setTrackbarPos("Upper - S","Trackbar",255) 
cv2.setTrackbarPos("Upper - V","Trackbar",255)

while True:
    #taking images from webcam
    #It returns two values ​​(ret returns whether the image can be received or not, while frame retrieves the image source).
    ret,frame = cap.read()

    if ret == 0:
        print("could not connect to camera")

    #projection of the image relative to the x-axis
    frame = cv2.flip(frame,1)

    #converting the image from bgr color format to hsv color format
    hsv_color_format_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #assigning the values ​​set in the trackbar to variables
    lower_h = cv2.getTrackbarPos("Lower - H","Trackbar")
    lower_s = cv2.getTrackbarPos("Lower - S","Trackbar")
    lower_v = cv2.getTrackbarPos("Lower - V","Trackbar")

    upper_h = cv2.getTrackbarPos("Upper - H","Trackbar")
    upper_s = cv2.getTrackbarPos("Upper - S","Trackbar")
    upper_v = cv2.getTrackbarPos("Upper - V","Trackbar")

    '''
    hsv values for blue color (Lower Blue):

    H: 100
    S: 150
    V: 0

    hsv values for blue color (Upper Blue):
    
    H: 140
    S: 255
    V: 255
    
    '''

    #converting hsv upper and lower values ​​to nump array for mask operation
    lower_color = np.array([lower_h,lower_s,lower_v])
    upper_color = np.array([upper_h,upper_s,upper_v])

    #with the inRange function, the colors between the entered values ​​in the trackbar are filtered.
    mask = cv2.inRange(hsv_color_format_frame,lower_color,upper_color)

    cv2.imshow("Trackbar",mask)
    cv2.imshow("Original Frame",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()