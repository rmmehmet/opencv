import cv2
import numpy as np
import matplotlib.pyplot as plt

#image reading
image_path = "image-color-histograms\histogram.jpg"
image = cv2.imread(image_path)

#separating the image into channels in bgr color format
b,g,r = cv2.split(image)

#creating histograms for b,g and r color channels
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

#showing graphic and picture
plt.show()
cv2.imshow("Canvas",image)

cv2.waitKey(0)
cv2.destroyAllWindows()