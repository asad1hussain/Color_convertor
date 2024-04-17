import cv2
import numpy as np

# Load the image
image = cv2.imread('input_image.jpg')

# Define the lower and upper bounds for black color in HSV
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 30])

# Convert image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Threshold the image to get a mask for black areas
black_mask = cv2.inRange(hsv, lower_black, upper_black)

# Define the RGB color for black replacement
black_replace_rgb = (133, 43, 255)

# Replace black pixels with the specified RGB color
image[black_mask > 0] = black_replace_rgb

# Save the output image
cv2.imwrite('output_image.jpg', image)
