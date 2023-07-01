import streamlit as st
from PIL import Image

with st.expander("Choose a file"):
    uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # start the camera
    camera_image = st.camera_input("Camera")
if uploaded_image:
    img1 = Image.open(uploaded_image)
    gray_img1 = img1.convert("L")
    st.image(gray_img1)

if camera_image:
    # Creat a pillow image instance
    img = Image.open(camera_image)


    # convert the pillow image to grayscale
    gray_img = img.convert("L")


    # Render the grayscale image on the webpage
    st.image(gray_img)
