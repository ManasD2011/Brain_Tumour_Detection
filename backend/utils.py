import numpy as np
from skimage.transform import resize
import base64
import cv2

IMG_SIZE = 128

def preprocess_slice(img):
    img = resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / (np.max(img) + 1e-8)
    return img

def encode_image(mask):
    mask = (mask * 255).astype("uint8")
    _, buffer = cv2.imencode(".png", mask)
    return base64.b64encode(buffer).decode()
    