import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "final_model.h5")
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

IMG_SIZE = 96
THRESHOLD = 0.5

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
