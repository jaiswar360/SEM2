# Low Filter (Computer Vision)

import cv2
import numpy as np
import matplotlib.pyplot as plt 
 
def apply_average_filter(image_path, kernel_size):
    # Read the image
    image = cv2.imread(image_path)
 
    # Apply the average filter
    filtered_image = cv2.blur(image, (kernel_size, kernel_size))
 
    return filtered_image
 
if __name__ == "__main__":
    # Input image path and kernel size
    input_image_path = r"C:\Users\admin\Desktop\KAMAL - 1045\ffff.jpg"
    kernel_size = 10  # You can adjust the kernel size as needed.
 
    # Apply the average filter
    filtered_image = apply_average_filter(input_image_path, kernel_size)
 
    # Display the original and filtered images
    # cv2.imshow("Original Image", cv2.imread(input_image_path))
    # cv2.imshow("Filtered Image", filtered_image)

    plt.subplot(1, 2, 1) 
    plt.imshow(input_image_path)
    plt.title("Original Image")
    plt.axis("off")
 
    plt.subplot(1, 2, 2) 
    plt.imshow(filtered_image)
    plt.title("Filtered Image")
    plt.axis("off")
 
    plt.show()
    
    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
