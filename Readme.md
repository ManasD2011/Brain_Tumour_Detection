# Brain Tumor Detection System

A full-stack AI-powered web application for detecting and visualizing brain tumors from MRI scans using deep learning.

---

## Features

- U-Net based tumor segmentation
- Multi-slice prediction for improved accuracy
- Tumor coverage percentage calculation
- MRI and mask overlay visualization
- Saved output images (mask and overlay)
- FastAPI backend for real-time inference
- Next.js frontend with modern UI
- Interactive visualization

---

## Tech Stack

### Backend
- Python
- FastAPI
- TensorFlow / Keras
- OpenCV
- Nibabel
- NumPy

### Frontend
- Next.js (React)
- TypeScript
- Tailwind CSS
- Framer Motion

---

## Model Details

- Architecture: U-Net (2D)
- Input: MRI slices (.nii / .nii.gz)
- Output: Segmentation mask
- Enhancement: Multi-slice prediction for improved stability

---

## Project Structure

Brain_Tumor_Detection/
├── backend/
│ ├── main.py
│ ├── predict.py
│ ├── utils.py
│ ├── config.py
│ └── requirements.txt
│
├── frontend/
│ ├── app/
│ ├── components/
│ ├── lib/
│ └── package.json
│
└── README.md


## Setup Instructions

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload


##Frontend

```bash
cd frontend
npm install
npm run dev
```


## How to Use

1. Upload a brain MRI file (.nii or .nii.gz)
2. Backend processes the file and detects tumors
3. Frontend displays the segmentation mask overlay on the MRI
4. View tumor coverage percentage and visualization


## Architectural Diagram



          ┌───────────────────────────┐
          │        Next.js UI         │
          │  (Upload + Visualization)│
          └────────────┬──────────────┘
                       │ HTTP Request
                       ▼
          ┌───────────────────────────┐
          │        FastAPI Backend     │
          │       (/predict API)       │
          └────────────┬──────────────┘
                       │
                       ▼
          ┌───────────────────────────┐
          │     Preprocessing Layer    │
          │ - Load .nii using nibabel  │
          │ - Extract slices           │
          │ - Resize & normalize       │
          └────────────┬──────────────┘
                       │
                       ▼
          ┌───────────────────────────┐
          │      U-Net Model (.h5)     │
          │   (Multi-slice inference)  │
          └────────────┬──────────────┘
                       │
                       ▼
          ┌───────────────────────────┐
          │     Post-processing        │
          │ - Generate mask            │
          │ - Compute tumor %          │
          │ - Create overlay image     │
          └────────────┬──────────────┘
                       │
                       ▼
          ┌───────────────────────────┐
          │        Response JSON       │
          │ - tumor_percentage         │
          │ - mask (base64)            │
          │ - original image           │
          └────────────┬──────────────┘
                       │
                       ▼
          ┌───────────────────────────┐
          │       Frontend UI          │
          │ - Overlay visualization    │
          │ - Slider control           │
          │ - Result display           │
          └───────────────────────────┘


          