import cv2
import os
import pytesseract
from PIL import Image
import time

OUTPUT_FOLDER = "frames"
OUTPUT_TEXT_FILE = "output.txt"
SAVE_INTERVAL_SECONDS = 5

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def extract_frames_and_perform_ocr(video_url, output_folder, output_text_file, save_interval_seconds):
    cap = cv2.VideoCapture(video_url)
    if not cap.isOpened():
        print('!!! Unable to open URL')
        return

    # Retrieve FPS
    fps = cap.get(cv2.CAP_PROP_FPS)

    frame_count = 0
    while True:
        # Read one frame
        ret, frame = cap.read()

        # Save frame to folder at intervals
        if frame_count % (save_interval_seconds * fps) == 0:
            frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved frame {frame_count} to {frame_filename}")

            # Crop the saved frame
            crop_and_save_frame(frame_filename)

            # Perform OCR on the cropped frame
            extracted_text = ocr_image(frame_filename)
            # Write the extracted text to the output file
            write_text_to_file(extracted_text, output_text_file)

        frame_count += 1

        # Check if end of the video stream
        if not ret:
            break

        time.sleep(1 / fps)  # Adding a slight delay

    cap.release()

def ocr_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Perform OCR
        text = pytesseract.image_to_string(img)
    return text

def write_text_to_file(text, output_file):
    with open(output_file, 'a') as f:
        f.write(text)
        f.write('\n')  # Add a newline between texts for clarity

def crop_and_save_frame(frame_path):
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

    # Save the cropped image, replacing the original
    cv2.imwrite(frame_path, cropped)

    print(f"Cropped and saved {frame_path}")

def main():
    # Take video URL as input from the user
    video_url = input("Enter the video URL: ")
    # video_url = "https://cdn.videosdk.live/meetings-hls/cd8096f0-e0f5-44c8-b57c-514c0a004b80/index.m3u8"
    # Execute the function to extract frames and perform OCR
    extract_frames_and_perform_ocr(video_url, OUTPUT_FOLDER, OUTPUT_TEXT_FILE, SAVE_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
