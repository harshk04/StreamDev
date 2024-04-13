import cv2
import numpy as np

# Load the input image
image = cv2.imread("Figure_1.png")

# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for the purple color
lower_purple = np.array([125, 50, 50])
upper_purple = np.array([160, 255, 255])

# Threshold the HSV image to get only purple colors
mask = cv2.inRange(hsv, lower_purple, upper_purple)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get the largest contour (assuming it corresponds to the purple rectangle)
largest_contour = max(contours, key=cv2.contourArea)

# Get the bounding box of the largest contour
x, y, w, h = cv2.boundingRect(largest_contour)

# Crop the region inside the bounding box
cropped_image = image[y:y+h, x:x+w]

# Save or display the cropped image
cv2.imwrite("cropped_image.jpg", cropped_image)
# Or to display
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
