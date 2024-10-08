import cv2
import numpy as np

image_path = "hough-transform/h_line.png"

#reading the image
image = cv2.imread(image_path)

#converting the image from bgr color format to gray color format
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#detecting edges of gray format image
edges = cv2.Canny(gray_image,75,150)

#detecting straight lines in the edge image using the hough transform algorithm
lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200)

#starting a loop for each line in the lines list
#in the lines list, there is coordinate information for each line detected with hough transform.
for line in lines:

    #getting the start (x1, y1) and end (x2, y2) coordinates of the line for each line
    x1,y1,x2,y2 = line[0]

    #drawing lines detected on the original image
    cv2.line(image,(x1,y1),(x2,y2),(255,0,0),2)

#printing the information (coordinates) of the detected lines to the console
print(lines)

cv2.imshow("Original İmage",image)
cv2.imshow("Edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
