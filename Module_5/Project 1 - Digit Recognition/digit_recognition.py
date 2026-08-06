"""
============================================================
 PROJECT 1 : DIGIT RECOGNITION  (Neural Network)
 Module 5  : Deep Learning & Computer Vision
 AI Powered Engineering Upskilling Program (2026 Edition)
============================================================

WHAT THIS PROGRAM DOES
----------------------
Trains a NEURAL NETWORK to recognize handwritten digits (0-9) from
images - the classic first project of computer vision. Each image is
a tiny 8x8 grid of pixel brightness values; the network learns to map
those 64 numbers to the correct digit.

    1. LOAD the built-in 'digits' dataset (1,797 labelled 8x8 images).
    2. PREPARE: flatten each image to 64 features, scale, split.
    3. TRAIN a Multi-Layer Perceptron (MLPClassifier) - a real neural
       network with hidden layers.
    4. EVALUATE: accuracy + a confusion matrix.
    5. VISUALIZE sample predictions -> digit_predictions.png.

WHY scikit-learn (not TensorFlow) HERE?
---------------------------------------
scikit-learn's MLPClassifier IS a neural network and runs instantly on
any machine with no heavy install. The Module 5 NOTES show the same
idea as a Keras/TensorFlow CNN (the industry tool) - use that once you
have a TensorFlow-compatible setup. The concepts are identical.

HOW TO RUN
----------
1. Install once:  pip install scikit-learn matplotlib numpy
2. In this folder:  python digit_recognition.py
3. Open `digit_predictions.png`.

CONCEPTS PRACTISED (Module 5)
-----------------------------
- Images as arrays of pixel numbers
- Neural networks (input -> hidden layers -> output)
- Flattening an image; feature scaling
- Multiclass classification (10 classes, digits 0-9)
- Confusion matrix for image classification

NOTE ON OUTPUT
--------------
Console text is plain ASCII; the chart is SAVED as a PNG.
"""

import numpy as np

import matplotlib
matplotlib.use("Agg")            # save charts to a file instead of a window
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

CHART_FILE = "digit_predictions.png"


def main() -> None:
    print("=" * 52)
    print("        DIGIT RECOGNITION (Neural Network)")
    print("=" * 52)

    # --- STEP 1: load the images -------------------------------------------
    # Each sample is an 8x8 image (64 pixels). images = the 8x8 grids,
    # data = the same pixels flattened to a row of 64, target = the digit.
    digits = load_digits()
    print(f"Loaded {len(digits.images)} images, each 8x8 pixels, "
          f"labelled 0-9.")

    X = digits.data          # shape (1797, 64) - one row of 64 pixels per image
    y = digits.target        # the true digit for each image (0-9)

    # --- STEP 2: split and scale -------------------------------------------
    X_train, X_test, y_train, y_test, img_train, img_test = train_test_split(
        X, y, digits.images, test_size=0.2, random_state=42)

    # Neural networks train better when inputs are on a similar scale.
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # --- STEP 3: build & train the neural network --------------------------
    # Two hidden layers (64 then 32 neurons). The network learns weights
    # that turn 64 pixels into a digit, using gradient descent (Module 4).
    print("\nTraining a neural network (2 hidden layers: 64 -> 32)...")
    model = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500,
                          random_state=42)
    model.fit(X_train_scaled, y_train)

    # --- STEP 4: evaluate --------------------------------------------------
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    print(f"\n----- RESULTS (on unseen test images) -----")
    print(f"Test accuracy: {acc:.3f}  ({acc*100:.1f}% of digits correct)")
    print("\nClassification report (per digit):")
    print(classification_report(y_test, y_pred))

    # --- STEP 5: visualize sample predictions ------------------------------
    # Show the first 10 test images with the model's prediction.
    fig, axes = plt.subplots(2, 5, figsize=(12, 6))
    fig.suptitle("Digit Recognition - Sample Predictions",
                 fontsize=16, fontweight="bold")
    for ax, image, true_label, pred in zip(
            axes.ravel(), img_test, y_test, y_pred):
        ax.imshow(image, cmap="gray")
        correct = (true_label == pred)
        ax.set_title(f"Pred: {pred}  (true {true_label})",
                     color="green" if correct else "red")
        ax.axis("off")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(CHART_FILE, dpi=100)
    plt.close(fig)
    print(f"\n[OK] Sample predictions saved to '{CHART_FILE}'.")

    # A quick confusion-matrix summary in text (which digits get confused).
    cm = confusion_matrix(y_test, y_pred)
    errors = cm.sum() - np.trace(cm)
    print(f"Total misclassified: {errors} out of {len(y_test)} test images.")


if __name__ == "__main__":
    main()
