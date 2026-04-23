import numpy as np
import nibabel as nib
import tensorflow as tf
from skimage.transform import resize

from config import MODEL_PATH, IMG_SIZE, THRESHOLD

# Load model once
model = tf.keras.models.load_model(MODEL_PATH, compile=False)


def preprocess(img):
    img = resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / (np.max(img) + 1e-8)
    return img


def run_prediction(file_path):
    img = nib.load(file_path).get_fdata()

    depth = img.shape[2]
    center = depth // 2

    slice_range = range(center - 1, center + 2)   # 3 slices

    preds = []
    original_slice = None

    for i in slice_range:
        if i < 0 or i >= depth:
            continue

        img_slice = img[:, :, i]

        if i == center:
            original_slice = preprocess(img_slice)

        processed = preprocess(img_slice)
        input_img = processed[np.newaxis, ..., np.newaxis]

        pred = model.predict(input_img)[0]
        preds.append(pred)

    # Average predictions
    avg_pred = np.mean(preds, axis=0)

    mask = (avg_pred > THRESHOLD).astype(np.uint8)

    tumor_percentage = float(np.sum(mask) / mask.size * 100)

    return mask, tumor_percentage, original_slice