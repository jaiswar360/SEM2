import cv2
import numpy as np
import matplotlib.pyplot as plt  # Importing matplotlib to display images
 
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
 
    if filtered_image is None:
        exit()
 
    # Display the original and filtered images using OpenCV
    # cv2.imshow("Original Image", cv2.imread(input_image_path))
    # cv2.imshow("Filtered Image", filtered_image)
 
    # Display images using matplotlib
    original_image = cv2.imread(input_image_path)
    original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    filtered_image_rgb = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)
 
    plt.subplot(1, 2, 1) 
    plt.imshow(original_image_rgb)
    plt.title("Original Image")
    plt.axis("off")
 
    plt.subplot(1, 2, 2) 
    plt.imshow(filtered_image_rgb)
    plt.title("Filtered Image")
    plt.axis("off")
 
    plt.show()
 
    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
