# Laplacian Filter

import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# Read the image in grayscale
image = cv2.imread(r"C:\Users\admin\Desktop\KAMAL - 1045\OIP.jpg", cv2.IMREAD_GRAYSCALE)
 
# Apply the Laplacian filter
laplacian = cv2.Laplacian(image, cv2.CV_64F)
 
# Convert the result to uint8
laplacian = np.uint8(np.absolute(laplacian))
 
# Display the original and filtered images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title("Laplacian Filtered Image")
plt.imshow(laplacian, cmap='gray')
plt.axis('off')
plt.show()
 
