import cv2
import numpy as np

video_path = "hough-transform/line.mp4"

#starting the video source (we enter the parameter as 0 for webcam. If you have an external camera, you can enter it as 1)
cap = cv2.VideoCapture(video_path)

while True:
    #taking images from webcam
    #It returns two values ​​(ret returns whether the image can be received or not, while frame retrieves the image source).
    ret, frame = cap.read()

    if not ret:
        print("could not connect to camera")
        break
    
    #converting the image from bgr color format to gray color format
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detecting edges of gray format image
    edges = cv2.Canny(gray_image, 75, 150)

    #detecting straight lines in the edge image using the hough transform algorithm
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=200)

    #starting a loop for each line in the lines list
    #in the lines list, there is coordinate information for each line detected with hough transform.
    if lines is not None:  
        for line in lines:

            #getting the start (x1, y1) and end (x2, y2) coordinates of the line for each line
            x1, y1, x2, y2 = line[0]

            #drawing lines detected on the original image
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.imshow("Original Image", frame)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
