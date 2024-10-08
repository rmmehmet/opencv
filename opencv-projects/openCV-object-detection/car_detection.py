import cv2

haar_cascade_car = cv2.CascadeClassifier("openCV-object-detection/haar-cascade/car.xml")
video_path = "openCV-object-detection/images-and-videos/car.mp4"

#starting the video source (we enter the parameter as 0 for webcam. If you have an external camera, you can enter it as 1)
cap = cv2.VideoCapture(video_path)

while True:
    #taking images from webcam
    #It returns two values ​​(ret returns whether the image can be received or not, while frame retrieves the image source).
    ret_frame,frame = cap.read()

    if ret_frame == 0:
        print("Video Acilamadi")

    #get coordinates of detected objects
    grayscale_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #get coordinates of detected objects    
    cars = haar_cascade_car.detectMultiScale(grayscale_frame,1.1,3)

    #loop is started for detected objects
    for (x,y,w,h) in cars:
        #rectangle is drawn for detected objects
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("Cars Video",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()