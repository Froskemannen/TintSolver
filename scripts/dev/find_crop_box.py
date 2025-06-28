import os
import numpy as np
from PIL import Image
import logging
import cv2

def quick_find_crop_box(orig_img, cropped_img):
    """
    Use OpenCV template matching for fast crop box detection.
    Returns (left, upper, right, lower) tuple.
    """
    orig = np.array(orig_img.convert('RGB'))
    crop = np.array(cropped_img.convert('RGB'))
    # Convert to BGR for OpenCV
    orig_bgr = cv2.cvtColor(orig, cv2.COLOR_RGB2BGR)
    crop_bgr = cv2.cvtColor(crop, cv2.COLOR_RGB2BGR)
    res = cv2.matchTemplate(orig_bgr, crop_bgr, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    x, y = min_loc
    h, w = crop_bgr.shape[:2]
    return (x, y, x + w, y + h)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)  # Reduce log verbosity
    screenshots_dir = '../Labeling/Screenshots'
    cropped_dir = '../Labeling/Cropped'
    crop_boxes = []
    for filename in os.listdir(screenshots_dir):
        if filename.lower().endswith('.png'):
            base = os.path.splitext(filename)[0]
            cropped_name = f'{base}-cropped.png'
            cropped_path = os.path.join(cropped_dir, cropped_name)
            orig_path = os.path.join(screenshots_dir, filename)
            img_exists = os.path.exists(cropped_path)
            if not img_exists:
                continue
            orig_img = Image.open(orig_path)
            cropped_img = Image.open(cropped_path)
            box = quick_find_crop_box(orig_img, cropped_img)
            if box:
                crop_boxes.append(box)
                # Debug output for crop box
                logging.debug(f'{filename}: quick match crop box {box}')
    if crop_boxes:
        crop_boxes = np.array(crop_boxes)
        avg_box = tuple(np.round(np.mean(crop_boxes, axis=0)).astype(int))
        print(f'\nAverage crop box for all pairs: {avg_box}')
    else:
        print('No crop boxes estimated.')

if __name__ == '__main__':
    main()

