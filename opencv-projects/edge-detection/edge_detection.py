import cv2

# empty function definition for trackbar
def nothing(x):
    pass

#starting the video source (we enter the parameter as 0 for webcam. If you have an external camera, you can enter it as 1)
cap = cv2.VideoCapture(0)

#creating the window
cv2.namedWindow("Webcam")

#creating trackbars
cv2.createTrackbar("Threshold", "Webcam", 127, 255, nothing)
cv2.createTrackbar("Canny Min", "Webcam", 100, 255, nothing)
cv2.createTrackbar("Canny Max", "Webcam", 200, 255, nothing)

while True:
    #taking images from webcam
    #It returns two values ​​(ret returns whether the image can be received or not, while frame retrieves the image source).
    ret, frame = cap.read()

    if not ret:
        print("could not connect to camera")
        break
    
    #projection of the image relative to the x-axis
    frame = cv2.flip(frame, 1)

    #converting the image from bgr color format to gray color format
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    #assigning the values ​​set in the trackbar to variables
    threshold_value = cv2.getTrackbarPos("Threshold", "Webcam")
    canny_min_value = cv2.getTrackbarPos("Canny Min", "Webcam")
    canny_max_value = cv2.getTrackbarPos("Canny Max", "Webcam")

    #converting received image to binary image
    threshold_ret, threshold = cv2.threshold(grayscale_frame, threshold_value, 255, cv2.THRESH_BINARY)

    #contours are found on the binary image
    #contours represent the boundaries of an object or shape and are often used for object detection in image processing and computer vision projects.
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #contours on the image are drawn
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    #edges are detected
    edges = cv2.Canny(grayscale_frame, canny_min_value, canny_max_value)

    cv2.imshow("Webcam", frame)
    cv2.imshow("Webcam-Threshold", threshold)
    cv2.imshow("Webcam-Canny", edges)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
