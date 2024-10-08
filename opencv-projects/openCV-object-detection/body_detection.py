import cv2

video_path = "openCV-object-detection/images-and-videos/body.mp4"
body_cascade = cv2.CascadeClassifier("openCV-object-detection/haar-cascade/fullbody.xml")

#starting the video source (we enter the parameter as 0 for webcam. If you have an external camera, you can enter it as 1)
cap = cv2.VideoCapture(video_path)

while True:
    #taking images from webcam
    #It returns two values ​​(ret returns whether the image can be received or not, while frame retrieves the image source).
    ret_frame,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #get coordinates of detected objects
    bodies = body_cascade.detectMultiScale(gray_frame,1.1,1)

    #loop is started for detected objects
    for (x,y,w,h) in bodies:
        #rectangle is drawn for detected objects
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("Webcam",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


