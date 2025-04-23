# Converting rgb image to binary image using thresholding method

import cv2
import numpy as np
 
# Load the grayscale image
image = cv2.imread(r"C:\Users\admin\Desktop\KAMAL - 1045 (DO NOT DELETE)\char.png", cv2.IMREAD_GRAYSCALE)
 
# Apply thresholding
total = np.sum(image)
w, h = image.shape[:2]
avg = int(total/(w*h))

threshold_value = avg

#threshold_value = 150  # You can adjust this value
thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
 
# Display the thresholded image
cv2.imshow('Thresholded Image', thresholded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
 
 
