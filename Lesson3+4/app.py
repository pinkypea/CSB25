import streamlit as st
import numpy as np
from tensorflow.keras.saving import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import os

MODEL_PATH = "model.keras"
TRAIN_DIR = "./asl-alphabet/asl_alphabet_train/asl_alphabet_train"
IMG_SIZE = (128, 128)

st.title("ASL Alphabet Classifier")
st.write("Upload một ảnh thủ ngữ để model dự đoán chữ cái")

model = load_model(MODEL_PATH)

# Load classname
class_names = sorted([
    d for d in os.listdir(TRAIN_DIR)
    if os.path.isdir(os.path.join(TRAIN_DIR, d))
])

# Upload ảnh
uploaded_file = st.file_uploader(
    "Chọn ảnh", type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    # Hiển thị ảnh gốc
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Ảnh đã được tải lên", width=200)

    # Tiền xử lý ảnh
    img = img.resize(IMG_SIZE)
    img_array = image.img_to_array(img)

    # Chuẩn hóa ảnh
    img_array = (img_array - img_array.mean()) / img_array.std()
    img_array = np.expand_dims(img_array, axis=0)

    # Dự đoán
    prediction = model.predict(img_array)
    predicted_index = np.argmax(prediction)
    predicted_class = class_names[predicted_index]

    # Hiển thị kết quả
    st.subheader("Kết quả dự đoán:")
    st.write(f"Ký tự: {predicted_class}")

