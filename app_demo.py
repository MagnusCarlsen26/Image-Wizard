import streamlit as st
import cv2
import numpy as np
from backend import modules as md
from ultralytics import YOLO
import base64
model = YOLO('yolov8n-seg.pt')
st.set_page_config(layout="wide")
if 'uploadedimage' not in st.session_state:
    st.session_state.uploadedimage = "demopic.png"

if 'updatedimage' not in st.session_state:
    st.session_state.updatedimage = "demopic.png"

def get_base64_of_bin_file(image):
    _, buffer = cv2.imencode('.png', image)
    return base64.b64encode(buffer).decode()

# Function to create a download link with base64 data
def create_download_link(image, file_label='Download Link', file_name='image.png'):
    encoded_image = get_base64_of_bin_file(image)
    href = f'<a href="data:image/png;base64,{encoded_image}" download="{file_name}">{file_label}</a>'
    return href


@st.cache_data
def file_2_image(img_file):
    if img_file is not None:
        file_bytes = np.asarray(bytearray(img_file.read()) , dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        return image
    else:
        return None

@st.cache_data
def fetch_boundary(image):
    results = model(classes=0,source=image)
    masks = results[0].masks
    if masks is not None and masks.xy is not None and len(masks.xy) > 0:
        boundary_pts = np.array(masks.xy[0] , dtype=np.int32)
        if boundary_pts.size != 0:
            return boundary_pts
        else:
            return None
    else:
        return None

project_title = st.title("CV Project")
col1,col2 = st.columns(2)

with col1:
    uploaded_widget = st.empty()
    uploaded_widget.image(st.session_state.uploadedimage,use_column_width=True)

with col2:
    updated_widget = st.empty()
    updated_widget.image(st.session_state.updatedimage,use_column_width=True)

run = st.sidebar.checkbox('Run')
if run:
    stop = st.sidebar.button("Stop")
color_picker = st.sidebar.color_picker("Choose a color", "#ff0000")  # Add a color picker
st.sidebar.title("Upload Image")
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg","png"])

if uploaded_file:
    image = file_2_image(uploaded_file)
    uploaded_widget.image(image,use_column_width=True)
    st.session_state.uploadedimage = image

col_b1 , col_b2 , col_b3 , col_b4, col_b5  = st.columns(5)
col_b7 , col_b8 , col_b9 = st.columns(3)

with col_b1:
    button1 = st.button("B_Black_F_Green",use_container_width=True)

with col_b2:
    button2 = st.button("B_White_F_Red",use_container_width=True)

with col_b3:
    button3 = st.button("B_Normal_F_Green",use_container_width=True)

with col_b4:
    button4 = st.button("Alpha_Blend",use_container_width=True)

with col_b5:
    button5 = st.button("Transparent_BG",use_container_width=True)



with col_b7:
    button7 = st.button("lower_contrast",use_container_width=True)

with col_b8:
    button8 = st.button("non_linear_lower",use_container_width=True)

with col_b9:
    button9 = st.button("invert",use_container_width=True)




if button1:
    if st.session_state.uploadedimage is not None:
        boundary = fetch_boundary(st.session_state.uploadedimage)
        if boundary is not None:
            updatedimage = md.back_black(st.session_state.uploadedimage,boundary)
            st.session_state.updatedimage = updatedimage
            updated_widget.image(st.session_state.updatedimage , use_column_width=True)

if button2:
    if st.session_state.uploadedimage is not None:
        boundary = fetch_boundary(st.session_state.uploadedimage)
        if boundary is not None:
            updatedimage = md.back_white(st.session_state.uploadedimage,boundary)
            updatedimage = cv2.cvtColor(updatedimage , cv2.COLOR_BGR2RGB)
            st.session_state.updatedimage = updatedimage
            updated_widget.image(st.session_state.updatedimage , use_column_width=True)

if button3:
    if st.session_state.uploadedimage is not None:
        boundary = fetch_boundary(st.session_state.uploadedimage)
        if boundary is not None:
            updatedimage = md.back_normal(st.session_state.uploadedimage,boundary)
            updatedimage = cv2.cvtColor(updatedimage , cv2.COLOR_BGR2RGB)
            st.session_state.updatedimage = updatedimage
            updated_widget.image(st.session_state.updatedimage , use_column_width=True)

if button4:
    if st.session_state.uploadedimage is not None:
        boundary = fetch_boundary(st.session_state.uploadedimage)
        if boundary is not None:
            updatedimage = md.alpha_blending(st.session_state.uploadedimage,boundary,128)
            updatedimage = cv2.cvtColor(updatedimage , cv2.COLOR_BGR2RGB)
            st.session_state.updatedimage = updatedimage
            updated_widget.image(st.session_state.updatedimage , use_column_width=True)

if button5:
    if st.session_state.uploadedimage is not None:
        boundary = fetch_boundary(st.session_state.uploadedimage)
        if boundary is not None:
            updatedimage = md.transparent_bg(st.session_state.uploadedimage,boundary)
            # updatedimage = cv2.cvtColor(updatedimage , cv2.COLOR_BGR2RGB)
            st.session_state.updatedimage = updatedimage
            updated_widget.image(st.session_state.updatedimage , use_column_width=True)



if button7:
    if st.session_state.uploadedimage is not None:
        boundary = fetch_boundary(st.session_state.uploadedimage)
        if boundary is not None:
            updatedimage = md.lower_contrast(st.session_state.uploadedimage,boundary)
            # updatedimage = cv2.cvtColor(updatedimage , cv2.COLOR_BGR2RGB)
            st.session_state.updatedimage = updatedimage
            updated_widget.image(st.session_state.updatedimage , use_column_width=True)

if button8:
    if st.session_state.uploadedimage is not None:
        boundary = fetch_boundary(st.session_state.uploadedimage)
        if boundary is not None:
            updatedimage = md.non_linear_lower(st.session_state.uploadedimage,boundary)
            # updatedimage = cv2.cvtColor(updatedimage , cv2.COLOR_BGR2RGB)
            st.session_state.updatedimage = updatedimage
            updated_widget.image(st.session_state.updatedimage , use_column_width=True)

if button9:
    if st.session_state.uploadedimage is not None:
        boundary = fetch_boundary(st.session_state.uploadedimage)
        if boundary is not None:
            updatedimage = md.invert(st.session_state.uploadedimage,boundary)
            # updatedimage = cv2.cvtColor(updatedimage , cv2.COLOR_BGR2RGB)
            st.session_state.updatedimage = updatedimage
            updated_widget.image(st.session_state.updatedimage , use_column_width=True)



if st.button("Download Image"):

  download_image = cv2.cvtColor(st.session_state.updatedimage, cv2.COLOR_BGR2RGB)
  download_link = create_download_link(download_image)
  st.markdown(download_link, unsafe_allow_html=True)


if run:
    cap = cv2.VideoCapture(0)
    while run:
        success, frame = cap.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        if success:
            st.session_state.uploadedimage = frame
            uploaded_widget.image(st.session_state.uploadedimage, use_column_width=True)
        if stop:
            run = False
            run = st.checkbox("Run", key="run",value=False)
            break

    cap.release()
    cv2.destroyAllWindows()
    







