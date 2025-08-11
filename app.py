import streamlit as st
import utils
from model.model import build_model, get_device

st.title("♻️ RecycleAI")
st.write("Upload a picture of trash and we'll tell you how to dispose of it!")
img_file = st.file_uploader("Upload your trash here!", type=["png", "jpeg", "jpg"])
if img_file is not None:
    try: 
            img_processed = utils.load_image_for_user(img_file)
            st.image(img_processed, use_container_width=True)
            st.write("Image loaded Successfully!")
    except Exception:
        st.write("Image did not loaded successfully.")
    
device = get_device()
model = build_model()
model.to(device)
    




