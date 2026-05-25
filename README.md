# FaceGuard — Deepfake Detection & Face Analysis System

> Originally developed as a team project for the **National College Students' Innovation and Entrepreneurship Training Program (大学生创新创业训练计划)**. As team leader, I was responsible for the overall system architecture and core algorithm integration. The team was awarded the **National First Prize (国家级一等奖)**. The code has been revisited and reorganized in 2026.

A desktop application for real-time deepfake detection and face recognition in video files, built with PySide6 and deep learning models running in parallel background threads.

---

## Features

- **Deepfake Detection** — Accumulates 68-point facial landmarks across a configurable video window, stabilizes them with Lucas-Kanade optical flow + Kalman filtering, then classifies them using a dual Bidirectional GRU model. Returns a Real/Fake verdict with a confidence score.
- **Face Recognition** — Detects faces with a Haar Cascade classifier, extracts 512-dimensional ArcFace embeddings via InsightFace (using MTCNN for alignment), and matches identities against a reference image folder using cosine similarity.
- **Real-time Overlay** — Bounding boxes are drawn over detected faces during playback via a transparent `QWidget` overlay.
- **Multi-threaded Architecture** — Detection and recognition each run in a dedicated `QObject` worker thread, communicating with the UI through Qt signals and slots.
- **Model Switching** — Supports pre-trained weights from Deeperforensics 1.0 and FaceForensics++; custom `.h5` model files can be loaded at runtime.

> **Note:** Face anonymization (face swap via SAEHD/DeepFaceLab) is included as a partial implementation — frame extraction and face alignment work, but video re-encoding is not completed in the current version.

---

## Architecture

```
MainWindow.py (PySide6 UI + QMediaPlayer)
│
├── module/deepfake_detector.py    ← landmark extraction + dual Bi-GRU inference
├── module/landmark_utils.py       ← Dlib detection, LK optical flow, Kalman tracking
├── module/face_recognition.py     ← recognition entry point (Haar Cascade + ArcFace)
├── module/face_rec_util.py        ← MTCNN alignment + InsightFace embedding extraction
├── module/my_thread.py            ← Detect_Thread / Face_Recog_Thread / Anonymize_Thread
├── module/video_prober.py         ← FFprobe-based video metadata extraction
├── module/image_util.py           ← QImage ↔ OpenCV (BGR ndarray) conversion
│
└── module/DeepFaceLab/
    └── VideoProcessing.py         ← Cut / ExtractFace / MergeSADE (partial)
```

### Deepfake Detection Pipeline

1. Sample frames from the loaded video over the configured detection window (1–30 s).
2. For each frame, detect the face with Dlib's frontal face detector and extract 68 facial landmarks.
3. Stabilize the landmark sequence across frames using **Lucas-Kanade optical flow** (forward + backward pass) combined with a **Kalman filter** to suppress jitter and handle frames where detection fails.
4. Feed the aligned landmark sequence (shape `[60, 136]`) into **g1.h5** (raw landmarks) and the frame-to-frame difference sequence (shape `[59, 136]`) into **g2.h5** (temporal differences). Both are Bidirectional GRU networks (64 units, dropout 0.5).
5. Average the two softmax outputs; threshold at 0.5 to produce the final **Real / Fake** label and confidence score.

### Face Recognition Pipeline

1. On each new video frame, detect the face region using an **OpenCV Haar Cascade** classifier (`haarcascade_frontalface_alt2.xml`). The detected crop is shown in the UI panel and used for bounding box overlay.
2. In parallel, extract the **512-dimensional embedding** of the target frame using **MTCNN** (PNet → RNet → ONet) for landmark-based alignment followed by **InsightFace** (ResNet-50 + ArcFace, TF 1.x checkpoint). The embedding of the horizontally flipped crop is summed with the original for robustness.
3. For each image in `images/known/`, extract its embedding and compute **cosine similarity** with the target embedding.
4. The best-matching identity and its similarity score (scaled to 0–100) are displayed; results below a threshold of 50 are suppressed.

---

## Project Structure

```
FaceGuard/
├── MainWindow.py               # Application entry point
├── requirements.txt            # Conda environment spec (win-64, Python 3.9)
│
├── design/                     # PySide6 UI files
│   ├── Ui_Main.py             # Auto-generated UI class
│   ├── resources_rc.py         # Compiled Qt resources (icons, images)
│   └── images/                # Icon and graphic assets
│
├── module/                     # Core Python modules
│   ├── deepfake_detector.py
│   ├── face_recognition.py
│   ├── face_rec_util.py
│   ├── landmark_utils.py
│   ├── my_thread.py
│   ├── image_util.py
│   ├── video_prober.py
│   ├── mtcnn/                  # PNet / RNet / ONet implementations
│   └── DeepFaceLab/            # Face swapping pipeline (partial)
│
├── model/                      # Pre-trained models (download separately — see below)
│   ├── shape_predictor_68_face_landmarks.dat   # Dlib landmark predictor
│   ├── pre_model/
│   │   ├── deeper/             # Deeperforensics 1.0 — g1.h5, g2.h5
│   │   └── ff/                 # FaceForensics++ — g1.h5, g2.h5
│   └── recognition_model/
│       ├── all_in_one/         # MTCNN checkpoints (PNet / RNet / ONet)
│       ├── ckpt_model_d/       # InsightFace checkpoint (710k iterations)
│       └── haarcascade_frontalface_alt2.xml
│
├── workspace/                  # Anonymization working directory
│   ├── data_src/              # Source video input
│   ├── data_dst/              # Extracted frames and aligned faces
│   └── model/                 # SAEHD model weights
│
└── images/known/               # Reference face images for recognition
```

---

## Environment

Requires **Python 3.9**, a **CUDA-enabled GPU**, and **FFmpeg** available on the system `PATH`.

```bash
conda create --name FaceGuard --file requirements.txt
conda activate FaceGuard
```

### Pre-trained Models

The following files are **included in this repository** (tracked by git):

| File | Purpose |
|---|---|
| `model/pre_model/deeper/g1.h5`, `g2.h5` | Deepfake detection — trained on Deeperforensics 1.0 |
| `model/pre_model/ff/g1.h5`, `g2.h5` | Deepfake detection — trained on FaceForensics++ |
| `model/recognition_model/all_in_one/` | MTCNN checkpoints (PNet / RNet / ONet) |
| `model/recognition_model/ckpt_model_d/*.ckpt.index`, `*.ckpt.meta` | InsightFace graph structure |
| `model/recognition_model/haarcascade_frontalface_alt2.xml` | OpenCV Haar Cascade for face detection |

The following two files exceed GitHub's 100 MB limit and must be **downloaded manually**:

#### 1. Dlib shape predictor (`shape_predictor_68_face_landmarks.dat`, ~95 MB)

Download from the official dlib model repository and place it at `model/`:

```
http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
```

Extract the `.bz2` archive; the resulting `.dat` file goes to:

```
model/shape_predictor_68_face_landmarks.dat
```

#### 2. InsightFace checkpoint weights (~333 MB)

Download `InsightFace_iter_best_710000.ckpt.data-00000-of-00001` from [Google Drive](https://drive.google.com/drive/folders/1BxAjIuqCGgLIo8oFAyReN_LCOoe0jQkQ?usp=sharing) and place it at:

```
model/recognition_model/ckpt_model_d/InsightFace_iter_best_710000.ckpt.data-00000-of-00001
```

---

## Usage

```bash
python MainWindow.py
```

1. Click **Open File** to load a video (`.mp4` or `.avi`).
2. Check **Face Detection** to enable real-time deepfake detection and face recognition simultaneously.
3. Select the **detection window** (1–30 s) from the dropdown. Longer windows improve accuracy at the cost of latency.
4. Check **Show Face** to display bounding boxes over detected faces during playback.
5. Add reference images to `images/known/` before launching to enable identity matching.

Detection results — face thumbnail, deepfake confidence score, and identity match — appear in real time in the right panel.

---

## Models

| Component | Model | Notes |
|---|---|---|
| Deepfake Detection | Bidirectional GRU × 2 | Trained on Deeperforensics 1.0 / FaceForensics++ |
| Facial Landmarks | Dlib shape predictor | 68 points; stabilized with LK optical flow + Kalman filter |
| Face Detection (UI / bbox) | OpenCV Haar Cascade | Fast CPU-side detection for bounding box display |
| Face Alignment | MTCNN (PNet / RNet / ONet) | 5-point landmark alignment to 112 × 112 crop |
| Face Recognition | InsightFace ResNet-50 + ArcFace | 512-dim embedding; TF 1.x compat mode checkpoint |

---

## Tech Stack

| Category | Library / Tool |
|---|---|
| GUI | PySide6 6.3.2 |
| Deep Learning | TensorFlow 2.10.0 (TF1 compat mode for InsightFace) |
| Computer Vision | OpenCV 4.6.0 |
| Facial Landmarks | Dlib 19.24.0 |
| Video Processing | FFmpeg / ffmpeg-python |
| Numerical Computing | NumPy 1.23.5, SciPy 1.10.1 |

---

*This README was drafted with the assistance of [Claude Code](https://claude.ai/code). Technical content was reviewed and verified by the author.*
