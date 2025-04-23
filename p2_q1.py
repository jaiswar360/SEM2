import cv2
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

# Load the image (use raw string for file path to avoid issues with backslashes)
image = cv2.imread(r"C:\Users\admin\Desktop\KAMAL - 1045\OIP.jpg")

# Increase Brightness
image_float = image.astype(float)

# Increase the brightness
brightness_factor = 2.0  
brightened_image = image_float * brightness_factor

# Decrease the Brightness
brightness_factor1 = 0.4  
dark_image = image_float * brightness_factor1

# Clip the pixel values to the valid range [0, 255]
brightened_image = np.clip(brightened_image, 0, 255)
dark_image = np.clip(dark_image, 0, 255)

# Convert the image back to unsigned 8-bit integers
brightened_image = brightened_image.astype(np.uint8)
dark_image = dark_image.astype(np.uint8)

# Image Rotation using OpenCV
image_rotate = ndimage.rotate(image, 45)

# Image Translation
height, width = image.shape[:2]  # Store height and width
T = np.float32([[1, 0, 100], [0, 1, 200]])  # Translation matrix
img_trans = cv2.warpAffine(image, T, (width, height))

# Show images
# cv2.imshow("Original Image", image)
# cv2.imshow("Brightened Image", brightened_image)
# cv2.imshow("Dark Image", dark_image)
# cv2.imshow("Rotated Image", image_rotate)
# cv2.imshow("Translated Image", img_trans)


plt.figure(figsize=(10, 5))

plt.subplot(2, 3, 1)  
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 3, 2)  
plt.imshow(brightened_image)
plt.title("Brightened Image")
plt.axis("off")

plt.subplot(2, 3, 3) 
plt.imshow(dark_image)
plt.title("Dark Image")
plt.axis("off")

plt.subplot(2, 3, 4)  
plt.imshow(image_rotate)
plt.title("Rotated Image")
plt.axis("off")

plt.subplot(2, 3, 5) 
plt.imshow(img_trans)
plt.title("Translated Image")
plt.axis("off")

plt.show()

