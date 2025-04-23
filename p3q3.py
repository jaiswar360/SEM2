# Median Filter

import cv2
import numpy as np
import matplotlib.pyplot as plt 

 
# Load the image
image_path = r"C:\Users\admin\Desktop\KAMAL - 1045\ffff.jpg"
original_image = cv2.imread(image_path)
 
# Apply median filter with specified kernel size
kernel_size = 3  # Adjust this value to change the filter size

median_filtered_image = cv2.medianBlur(original_image, kernel_size)
 
# Display the original and filtered images
# cv2.imshow('Original Image', original_image)
# cv2.imshow('Median Filtered Image', median_filtered_image)

plt.subplot(1, 2, 1) 
plt.imshow(original_image)
plt.title("Original Image")
plt.axis("off")
 
plt.subplot(1, 2, 2) 
plt.imshow(median_filtered_image)
plt.title("Median Filtered Image")
plt.axis("off")
 
plt.show()
 
# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
 
