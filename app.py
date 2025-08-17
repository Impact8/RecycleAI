import streamlit as st
import utils
from model.model import build_model, get_device, classes
import torch

st.title("♻️ RecycleAI")
st.write("Upload a picture of trash and we'll tell you how to dispose of it!")
device = get_device()
model = build_model()
img_file = st.file_uploader("Upload your trash here!", type=["png", "jpeg", "jpg"])
if img_file is not None:
    try:
        img_processed = utils.load_image_for_user(img_file)
        st.image(img_processed, use_container_width=True)
        with torch.no_grad():
            img_tensor = utils.load_image_for_model(img_file)
            model.to(device)
            outputs = model(img_tensor.to(device))
            predicted_class = outputs.argmax(dim=1).item()
            st.write("Predicted class index:", predicted_class)
            st.write("Predicted label:", classes[predicted_class])
    except Exception as e:
        st.exception(e) 
        st.write("Type of Error:", type(e).__name__)
    




