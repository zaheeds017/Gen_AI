"""
============================================================
 PROJECT 3 : OPENCV IMAGE PROCESSING TOOLKIT
 Module 5  : Deep Learning & Computer Vision
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
Computer Vision starts with IMAGE PROCESSING - the classic OpenCV
operations that every vision system uses before any deep learning.
This toolkit creates a sample image, then applies and displays the
core operations side by side:

    1. Original
    2. Grayscale        (color -> shades of gray)
    3. Gaussian Blur    (smooth out noise)
    4. Canny Edges      (find outlines)
    5. Threshold        (turn gray into pure black/white)
    6. Contour Detection (find & count the shapes/objects)

The result is saved as one montage image `processing_steps.png`.

HOW TO RUN
----------
1. Install once:  pip install opencv-python numpy matplotlib
2. In this folder:  python opencv_image_processing.py
3. Open `processing_steps.png`.

CONCEPTS PRACTISED (Module 5)
-----------------------------
- An image is a NumPy array of pixels (Module 3 pays off here!)
- Color spaces: BGR (OpenCV's order) vs RGB vs Grayscale
- Blurring / smoothing (Gaussian)
- Edge detection (Canny)
- Thresholding (binary images)
- Contours: detecting and counting objects

NOTE ON OUTPUT
--------------
Console text is plain ASCII; the montage is SAVED as a PNG (we use
cv2.imwrite / matplotlib, never cv2.imshow), so it runs without a
display and works on any machine.
"""

import cv2
import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUTPUT_FILE = "processing_steps.png"


# ----------------------------------------------------------------------
# STEP 0 : create a sample image with a few shapes (so processing is visible)
# ----------------------------------------------------------------------
def create_sample_image() -> np.ndarray:
    """Draw some colored shapes on a white canvas (a BGR image = NumPy array)."""
    # A blank white image: height 400, width 600, 3 color channels (BGR).
    img = np.full((400, 600, 3), 255, dtype=np.uint8)

    # OpenCV uses BGR order, not RGB. Colors below are (Blue, Green, Red).
    cv2.rectangle(img, (50, 50), (180, 180), (255, 0, 0), -1)     # blue square
    cv2.circle(img, (330, 115), 70, (0, 0, 255), -1)             # red circle
    cv2.ellipse(img, (490, 115), (80, 45), 0, 0, 360, (0, 200, 0), -1)  # green
    triangle = np.array([[150, 350], [80, 250], [220, 250]], np.int32)
    cv2.fillPoly(img, [triangle], (0, 165, 255))                 # orange triangle
    cv2.circle(img, (380, 300), 60, (200, 0, 200), -1)           # purple circle
    return img


def to_rgb(bgr):
    """OpenCV is BGR; Matplotlib expects RGB. Convert for correct display."""
    return cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)


def main() -> None:
    print("=" * 52)
    print("        OPENCV IMAGE PROCESSING TOOLKIT")
    print("=" * 52)

    # STEP 0: get an image to work on.
    img = create_sample_image()
    print(f"Sample image created: {img.shape[1]}x{img.shape[0]} pixels, "
          f"{img.shape[2]} color channels (an array of shape {img.shape}).")

    # STEP 1: GRAYSCALE - drop color, keep brightness (1 channel).
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # STEP 2: GAUSSIAN BLUR - average nearby pixels to smooth noise.
    blurred = cv2.GaussianBlur(gray, (9, 9), 0)

    # STEP 3: CANNY EDGE DETECTION - highlight where brightness changes fast.
    edges = cv2.Canny(blurred, 50, 150)

    # STEP 4: THRESHOLD - every pixel becomes pure black or white.
    # THRESH_BINARY_INV makes the shapes white on a black background.
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    # STEP 5: CONTOURS - find the outlines of the shapes and count them.
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
    contour_img = img.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 0, 0), 3)  # outline in black
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(contour_img, (x, y), (x + w, y + h), (0, 0, 0), 1)
    print(f"Contour detection found {len(contours)} object(s) in the image.")

    # --- Save all steps as one labelled montage ---------------------------
    steps = [
        ("1. Original", to_rgb(img)),
        ("2. Grayscale", gray),
        ("3. Gaussian Blur", blurred),
        ("4. Canny Edges", edges),
        ("5. Threshold", thresh),
        (f"6. Contours ({len(contours)} objects)", to_rgb(contour_img)),
    ]
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    fig.suptitle("OpenCV Image Processing Steps", fontsize=16, fontweight="bold")
    for ax, (title, image) in zip(axes.ravel(), steps):
        # 2-D arrays (gray/edges/thresh) use a gray colormap.
        cmap = "gray" if image.ndim == 2 else None
        ax.imshow(image, cmap=cmap)
        ax.set_title(title)
        ax.axis("off")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUTPUT_FILE, dpi=100)
    plt.close(fig)
    print(f"\n[OK] Montage saved to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()
