# Module 5 — Hands-on Projects 👁️

**AI Powered Engineering Upskilling Program · Deep Learning & Computer Vision**

This is where you make computers **see**. Three projects span the computer-vision stack: a **neural network** that reads digits, **YOLO** object detection, and core **OpenCV** image processing.

> 📖 Full theory for each project is in
> [`Course_Notes/Module_05_Deep_Learning_and_Computer_Vision.md`](../../Course_Notes/Module_05_Deep_Learning_and_Computer_Vision.md) (sections 12–14).

---

## ⚙️ One-time setup

```bash
pip install -r requirements.txt
# or:  pip install numpy matplotlib scikit-learn opencv-python ultralytics
```

Check Python first with `python --version` (need **3.10+**).

> **Note on TensorFlow:** the notes teach neural networks/CNNs with **Keras/TensorFlow** (the industry standard), which needs **Python 3.10–3.13** or **Google Colab**. So the *runnable* Digit Recognition project uses scikit-learn's neural network (works on any Python), and the Keras version is shown in the notes. OpenCV and YOLO work on current Python.

---

## 📁 Projects

| # | Project | Focus | Libraries | Syllabus link |
|---|---|---|---|---|
| 1 | **Digit Recognition** ✍️ | Neural network / image classification | scikit-learn | **Digit Recognition** |
| 2 | **Object Detection (YOLO)** 🎯 | Deep-learning detection | ultralytics (YOLOv8) | **Object Detection** |
| 3 | **OpenCV Image Processing** 🖼️ | Vision fundamentals | OpenCV | *OpenCV* (reinforcement) |

Projects 1 & 2 are the **two syllabus activities**. Project 3 builds the **OpenCV** foundations that underpin all computer vision.

---

## ▶️ How to run any project

1. Do the one-time `pip install` above.
2. Open a terminal **inside that project's folder**.
3. Run the `.py` file, e.g.:
   ```bash
   python digit_recognition.py
   ```
4. Open the generated **`*.png`** image.

> Project 2 (YOLO) downloads a ~6 MB model on its first run (needs internet once), then works offline.

---

## 🔗 The computer-vision journey

```
Project 3  →  PROCESS : an image is just an array (grayscale, edges, contours)
Project 1  →  CLASSIFY: a neural network reads WHAT a small image shows (a digit)
Project 2  →  DETECT  : YOLO finds WHAT and WHERE (people, cars, buses)
```

**Recommended order: 3 → 1 → 2** — understand images, then classify them, then detect objects within them.

---

## ✅ Everything is tested

All three programs were run end-to-end and their output images verified: 98% digit accuracy, a real YOLO detection on a street scene, and a full OpenCV processing montage.
