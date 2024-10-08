import cv2
import numpy as np


image_balls_path = "hough-transform/balls.jpg"
image_coins_path = "hough-transform/coins.jpg"

#image reading
image_ball = cv2.imread(image_balls_path)
image_coins = cv2.imread(image_coins_path)

#converting the image from bgr color format to gray color format
gray_image_ball = cv2.cvtColor(image_ball, cv2.COLOR_BGR2GRAY)
gray_image_coins = cv2.cvtColor(image_coins, cv2.COLOR_BGR2GRAY)

#applying median filter to gray format images
#median filter helps reduce noise on images
image_ball_blur = cv2.medianBlur(gray_image_ball, 5)
image_coins_blur = cv2.medianBlur(gray_image_coins, 5)



#using houghcircles for circle detection
circles_image_ball = cv2.HoughCircles(
    image_ball_blur,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=image_ball_blur.shape[0] / 32,  #adjusted minDist
    param1=120,  #canny upper threshold
    param2=30,   #for high accuracy
    minRadius=10,  #smaller minimum radius
    maxRadius=100   #larger maximum radius
)

circles_image_coins = cv2.HoughCircles(
    image_coins_blur,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=image_coins_blur.shape[0] / 8,  #adjusted minDist
    param1=120,  #canny upper threshold
    param2=30,   #for high accuracy
    minRadius=20,  #smaller minimum radius
    maxRadius=60   #larger maximum radius
)

#drawing the detected circles
if circles_image_ball is not None:
    circles_image_ball = np.uint16(np.around(circles_image_ball))
    for i in circles_image_ball[0, :]:
        cv2.circle(image_ball, (i[0], i[1]), i[2], (0, 255, 0), 2)  #draw the circle in green

if circles_image_coins is not None:
    circles_image_coins = np.uint16(np.around(circles_image_coins))
    for i in circles_image_coins[0, :]:
        cv2.circle(image_coins, (i[0], i[1]), i[2], (255, 0, 0), 2)  #draw the circle in blue

#displaying the results
cv2.imshow("Image Ball", image_ball)
cv2.imshow("Image Coins", image_coins)
cv2.waitKey(0)
cv2.destroyAllWindows()
