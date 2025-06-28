import os
import argparse
import logging
import sys
from PIL import Image

# Standard crop box from find_crop_box.py output
STANDARD_CROP_BOX = (593, 77, 2205, 1209)

parser = argparse.ArgumentParser(description="Crop images in a directory.")
parser.add_argument("--source_dir", type=str, default="../../../Labeling/Screenshots", help="Directory containing source images")
parser.add_argument("--output_dir", type=str, default="../../../Labeling/Cropped", help="Directory to save cropped images")
parser.add_argument("--crop_box", type=int, nargs=4, default=STANDARD_CROP_BOX, help="Crop box coordinates (left, upper, right, lower)")

SOURCE_DIR = ""
OUTPUT_DIR = ""
CROP_BOX = ()

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def crop_image(input_path, output_path, crop_box):
    try:
        with Image.open(input_path) as img:
            width, height = img.size
            adjusted_crop_box = (
                max(0, min(crop_box[0], width)),  # left
                max(0, min(crop_box[1], height)),  # upper
                max(0, min(crop_box[2], width)),  # right
                max(0, min(crop_box[3], height))  # lower
            )
            if adjusted_crop_box != crop_box:
                logging.warning(f"Adjusted crop box for {os.path.basename(input_path)}: {crop_box} -> {adjusted_crop_box}")
            cropped = img.crop(adjusted_crop_box)
            logging.info(f"Cropped: {os.path.basename(input_path)} -> {output_path}")
            cropped.save(output_path)
    except OSError as e:
        logging.error(f"File error processing {os.path.basename(input_path)}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error processing {os.path.basename(input_path)}: {e}")

def main():
    for filename in os.listdir(SOURCE_DIR):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(SOURCE_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, f"{os.path.splitext(filename)[0]}-cropped.png")
            if os.path.exists(output_path):
                logging.info(f"Skipped: {filename} -> {output_path} (already cropped)")
                continue  # Skip if already cropped
            crop_image(input_path, output_path, CROP_BOX)

if __name__ == "__main__":
    args = parser.parse_args()

    SOURCE_DIR = args.source_dir
    OUTPUT_DIR = args.output_dir
    CROP_BOX = args.crop_box

    # Ensure the output directory exists
    if not os.path.exists(SOURCE_DIR):
        logging.error(f"Source directory '{SOURCE_DIR}' does not exist.")
        sys.exit(1)
     os.makedirs(OUTPUT_DIR, exist_ok=True)

     main()
