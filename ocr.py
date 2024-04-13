import os
import pytesseract
from PIL import Image
import time

def ocr_images_in_folder_with_delay(input_folder, output_path):
    # Open or create the output text file in append mode
    with open(output_path, 'a') as f:
        # Iterate over each file in the input folder
        for filename in os.listdir(input_folder):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                # Construct the full path to the image file
                image_path = os.path.join(input_folder, filename)
                # Perform OCR on the image
                extracted_text = ocr_image(image_path)
                # Write the extracted text to the output file
                f.write(extracted_text)
                f.write('\n')  # Add a newline between texts for clarity
                f.flush()  # Flush the buffer to ensure immediate writing to the file
                time.sleep(2)  # Add a delay of 5 seconds after processing each image

def ocr_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Perform OCR
        text = pytesseract.image_to_string(img)
    return text

input_folder = "frames"  # Specify the folder containing the frames
output_path = "output.txt"  # Specify the output text file path
ocr_images_in_folder_with_delay(input_folder, output_path)
