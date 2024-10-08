import cv2

#image reading
image_path = "contour-analysis/triangle.jpg"
image = cv2.imread(image_path)

#converting the image from bgr color format to gray color format
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#converting received image to binary image
ret,thresh = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)

#contours are found on the binary image
#contours represent the boundaries of an object or shape and are often used for object detection in image processing and computer vision projects.
contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#Taking the first contour of the contours previously obtained using the cv2.findContours function
cnt = contours[0]

#calculation of the area of ​​the contour
area = cv2.contourArea(cnt)

#calculation of the perimeter of the contour
perimeter= cv2.arcLength(cnt,True)

#drawing the contour of the original image for visualization
cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2) 

#writing text over the image to show area and perimeter
cv2.putText(image, f'Area: {area:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(image, f'Perimeter: {perimeter:.2f}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Original İmage",image)
cv2.imshow("Thresholded İmage",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()