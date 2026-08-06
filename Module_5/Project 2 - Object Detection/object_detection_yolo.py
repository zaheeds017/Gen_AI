"""
============================================================
 PROJECT 2 : OBJECT DETECTION with YOLO
 Module 5  : Deep Learning & Computer Vision
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
Uses YOLO (You Only Look Once) - a state-of-the-art deep-learning
object detector - to find and label objects (people, cars, buses,
dogs, ...) in an image. Unlike classification (which labels the WHOLE
image), detection also finds WHERE each object is, drawing a box
around it.

    1. LOAD a pre-trained YOLOv8 model (downloads once, ~6 MB).
    2. RUN detection on an image.
    3. PRINT every object found, with its confidence.
    4. SAVE the image with labelled boxes -> detected_objects.png.

HOW TO RUN
----------
1. Install once:  pip install ultralytics
   (this also installs PyTorch and OpenCV automatically)
2. In this folder:
       python object_detection_yolo.py
   or with your own image:
       python object_detection_yolo.py path/to/your_photo.jpg
3. Open `detected_objects.png`.

NOTE: the FIRST run downloads the model weights (needs internet, once).
After that it works offline.

CONCEPTS PRACTISED (Module 5)
-----------------------------
- Object detection vs image classification
- Using a PRE-TRAINED deep-learning model (transfer learning idea)
- Bounding boxes, class labels, confidence scores
- YOLO: a single fast pass over the image ("you only look once")

NOTE ON OUTPUT
--------------
Console text is plain ASCII; the annotated image is SAVED as a PNG
(no display window needed).
"""

import sys

import cv2
from ultralytics import YOLO

OUTPUT_FILE = "detected_objects.png"


def pick_image() -> str:
    """Use the image path given on the command line, or a bundled sample."""
    if len(sys.argv) > 1:
        return sys.argv[1]
    # ultralytics ships with sample images; 'bus.jpg' has people + a bus.
    try:
        from ultralytics.utils import ASSETS
        return str(ASSETS / "bus.jpg")
    except Exception:
        return "bus.jpg"


def main() -> None:
    print("=" * 52)
    print("        OBJECT DETECTION with YOLO")
    print("=" * 52)

    image_path = pick_image()
    print(f"Image: {image_path}")

    # STEP 1: load a small, fast, pre-trained YOLOv8 model.
    # 'yolov8n.pt' (n = nano) is the smallest; it already knows 80 common
    # object classes from being trained on the huge COCO dataset.
    print("Loading YOLOv8 model (downloads once on first run)...")
    model = YOLO("yolov8n.pt")

    # STEP 2: run detection. verbose=False keeps the console tidy.
    results = model(image_path, verbose=False)
    result = results[0]                      # results for our single image

    # STEP 3: report what was found.
    names = model.names                      # id -> class name (e.g. 0 -> 'person')
    counts = {}
    print("\n----- OBJECTS DETECTED -----")
    for box in result.boxes:
        label = names[int(box.cls)]
        confidence = float(box.conf)
        counts[label] = counts.get(label, 0) + 1
        print(f"   {label:<12} (confidence {confidence*100:.0f}%)")

    if counts:
        print("\nSummary (counts):")
        for label, n in sorted(counts.items(), key=lambda kv: -kv[1]):
            print(f"   {n} x {label}")
    else:
        print("   (No objects detected in this image.)")

    # STEP 4: save the image with boxes and labels drawn on it.
    # result.plot() returns the annotated image as a BGR NumPy array.
    annotated = result.plot()
    cv2.imwrite(OUTPUT_FILE, annotated)
    print(f"\n[OK] Annotated image saved to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
        print("Tip: make sure 'ultralytics' is installed (pip install "
              "ultralytics) and, on the first run, that you have internet "
              "to download the model weights.")
