from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import uuid
import cv2
import numpy as np

from predict import run_prediction
from utils import encode_image
from config import UPLOAD_DIR, OUTPUT_DIR

app = FastAPI(title="Brain Tumor Detection API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure folders exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Validate file type
        if not file.filename.endswith((".nii", ".nii.gz")):
            raise HTTPException(status_code=400, detail="Upload .nii or .nii.gz file")

        # Unique filename
        filename = f"{uuid.uuid4()}_{file.filename}"
        file_path = os.path.join(UPLOAD_DIR, filename)

        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Run inference
        mask, tumor_percentage, original = run_prediction(file_path)

        # Encode for frontend
        encoded_mask = encode_image(mask)
        encoded_original = encode_image(original)

        # =========================
        # SAVE FILES
        # =========================

        filename_base = filename.split(".")[0]

        # Save mask
        mask_path = os.path.join(OUTPUT_DIR, f"{filename_base}_mask.png")
        mask_img = (mask * 255).astype("uint8")
        cv2.imwrite(mask_path, mask_img)

        # Save overlay
        overlay = (original * 255).astype("uint8")
        overlay = cv2.cvtColor(overlay, cv2.COLOR_GRAY2BGR)

        mask_colored = np.zeros_like(overlay)
        mask_colored[:, :, 2] = mask_img  # red mask

        overlay = cv2.addWeighted(overlay, 0.7, mask_colored, 0.3, 0)

        overlay_path = os.path.join(OUTPUT_DIR, f"{filename_base}_overlay.png")
        cv2.imwrite(overlay_path, overlay)

        # =========================
        # RESPONSE
        # =========================

        return {
            "success": True,
            "tumor_percentage": tumor_percentage,
            "mask": encoded_mask,
            "original": encoded_original,
            "saved_mask": mask_path,
            "saved_overlay": overlay_path
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))