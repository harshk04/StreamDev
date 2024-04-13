import cv2

# Path to the image file
frame_path = 'frame_0.jpg'

# Read the image
image = cv2.imread(frame_path)

# Define the four coordinates (x, y) of the points
point1 = (804, 198)  # Top-left corner
point2 = (1620, 343)  # Top-right corner
point3 = (1620, 531)  # Bottom-right corner
point4 = (290, 722)  # Bottom-left corner

# Calculate the bounding box
x_values = [point1[0], point2[0], point3[0], point4[0]]
y_values = [point1[1], point2[1], point3[1], point4[1]]
x_min, x_max = min(x_values), max(x_values)
y_min, y_max = min(y_values), max(y_values)

# Crop the image
cropped = image[y_min:y_max, x_min:x_max]

# Generate a new file path for the cropped image
cropped_path = 'cropped_frame.jpg'

# Save the cropped image with the new file path
cv2.imwrite(cropped_path, cropped)

print(f"Cropped image saved as {cropped_path}")
