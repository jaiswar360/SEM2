# Color model conversions

import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# Load the image
image = cv2.imread(r"C:\Users\admin\Downloads\images.png")
 
# Convert to HSV (Hue, Saturation, Value)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 
# Convert to LAB (CIELAB) color space
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
 
# Convert to YCbCr
ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
 
# Convert to CMYK
# cmyk_image = cv2.cvtColor(image, cv2.COLOR_BGR2CMYK)
 
# Convert to YIQ
yiq_image = np.zeros_like(image, dtype=np.float32)
 
yiq_image[:,:,0] = 0.299 * image[:,:,2] + 0.587 * image[:,:,1] + 0.114 * image[:,:,0]
yiq_image[:,:,1] = 0.596 * image[:,:,2] - 0.274 * image[:,:,1] - 0.322 * image[:,:,0]
yiq_image[:,:,2] = 0.211 * image[:,:,2] - 0.523 * image[:,:,1] + 0.312 * image[:,:,0]
 
yiq_image = np.clip(yiq_image, 0, 255).astype(np.uint8)
 
# Display the original and converted images
# cv2.imshow('Original Image', image)
# cv2.imshow('HSV Image', hsv_image)
# cv2.imshow('LAB Image', lab_image)
# cv2.imshow('YCbCr Image', ycbcr_image)
# cv2.imshow('CMYK Image', cmyk_image)
# cv2.imshow('YIQ Image', yiq_image)


plt.figure(figsize=(10, 5))

plt.subplot(1, 5, 1)
plt.title("Original Image")
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 5, 2)
plt.title("HSV Image")
plt.imshow(hsv_image)
plt.axis('off')

plt.subplot(1, 5, 3)
plt.title("LAB Image")
plt.imshow(lab_image)
plt.axis('off')

plt.subplot(1, 5, 4)
plt.title("YCbCr Image")
plt.imshow(ycbcr_image)
plt.axis('off')

plt.subplot(1, 5, 5)
plt.title("YIQ Image")
plt.imshow(yiq_image)
plt.axis('off')

plt.show()
 
# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
