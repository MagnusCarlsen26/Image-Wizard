import streamlit as st
import cv2
import numpy as np 
# Define hardcoded_image_path globally
global hardcoded_image_path, uploaded_image, updated_image, update_widget, uploaded_widget

# Rest of your code

hardcoded_image_path = None
uploaded_image = None
updated_image = None
# update_widget,uploaded_widget = st.columns()
update_widget = None #st.empty() 
uploaded_widget = None #st.empty()
from ultralytics import YOLO
from backend import modules as md
model = YOLO('yolov8n-seg.pt')


def file_2_image(img_file):
    if img_file is not None:

        file_bytes = np.asarray(bytearray(img_file.read()) , dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        # image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
        return image
    else:
        None

def fetch_boundary(image):
    results = model(classes=0,source=image)
    masks = results[0].masks
    if masks is not None and masks.xy is not None and len(masks.xy) > 0:
        boundary_pts = np.array(masks.xy[0] , dtype=np.int32)
        if(boundary_pts.size != 0):
            update = md.back_black(image,boundary_pts)
        else:
            update = image
    else:
        update = np.zeros_like(image)
    return update

def main():
    global hardcoded_image_path, uploaded_image, updated_image, update_widget, uploaded_widget

    st.markdown("<h1 style='text-align: center;'>CV Project</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.title("Options")
    run = st.sidebar.checkbox('Run')
    color_picker = st.sidebar.color_picker("Choose a color", "#ff0000")  # Add a color picker
    print(color_picker)
    st.sidebar.title("Upload Image")
    uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file:
                # if uploaded_file is not None:
        uploaded_widget.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        uploaded_image = file_2_image(uploaded_file)
        print(uploaded_image)
        if uploaded_image is not None:
            updated_image = fetch_boundary(uploaded_image)
            update_widget.image(updated_image, caption="Hardcoded Image", use_column_width=True)
    
    col1, col2 = st.columns(2)
    

    def f0():
        if run:
            return r'C:\Users\Mic\Desktop\CV\CV_Project\Image-Wizard\frontend\download (1).jpeg'
        else:
            return r'C:\Users\Mic\Desktop\CV\CV_Project\Image-Wizard\frontend\download.jpeg'
    def f1():
        if run:
            return r'C:\Users\Mic\Desktop\CV\CV_Project\Image-Wizard\frontend\download (2).jpeg'
        else:
            return r'C:\Users\Mic\Desktop\CV\CV_Project\Image-Wizard\frontend\download (1).jpeg'
    def f2():
        if run:
            return r'C:\Users\Mic\Desktop\CV\CV_Project\Image-Wizard\frontend\download (3).jpeg'
        else:
            return r'C:\Users\Mic\Desktop\CV\CV_Project\Image-Wizard\frontend\download (2).jpeg'
    def f3():
        if run:
            return r'C:\Users\Mic\Desktop\CV\CV_Project\Image-Wizard\frontend\download (4).jpeg'
        else:
            return r'C:\Users\Mic\Desktop\CV\CV_Project\Image-Wizard\frontend\download (3).jpeg'
    def f4():
        if run:
            return r'C:\Users\Mic\Desktop\CV\CV_Project\Image-Wizard\frontend\download (5).jpeg'
        else:
            return r'C:\Users\Mic\Desktop\CV\CV_Project\Image-Wizard\frontend\download (4).jpeg'
    def f5():
        if run:
            return r'C:\Users\Mic\Desktop\CV\CV_Project\Image-Wizard\frontend\download.jpeg'
        else:
            return r'C:\Users\Mic\Desktop\CV\CV_Project\Image-Wizard\frontend\download (5).jpeg'
    functions = [f0,f1,f2,f3,f4,f5]

    i = 0
    cols = st.columns(6)
    for j in cols:
        with j:
            if st.button(f'f{i}'):
              
            
                print("f0 clicked")
                print(updated_image)
                if uploaded_image is not None:
                    updated_image = fetch_boundary(uploaded_image)
                    cv2.imshow("test",updated_image )
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    update_widget.image(updated_image, caption="Hardcoded Image", use_column_width=True)
            
                else:
                    updated_image = None
                    update_widget.empty()

                st.write(f'f{i} is clicked')
        i += 1
    
    with col2:
        # Create empty placeholder for updated image
        update_widget = st.empty()
        if uploaded_image is not None:
            update_widget.image(updated_image, caption="Hardcoded Image", use_column_width=True)
        # if updated_image:
           
        #     update_widget = st.image(updated_image, caption="Hardcoded Image", use_column_width=True)
        # else:
        #     updated_widget = st.text("No Data Available")

    with col1:
        uploaded_widget = st.empty()
        if run:
            st.sidebar.text("Live video is ON")
         
            FRAME_WINDOW = st.image([])
            camera = cv2.VideoCapture(0)
            while run:
                _, frame = camera.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                uploaded_image = frame
                FRAME_WINDOW.image(frame)
            else:
                st.write('Stopped')
        else:
            st.sidebar.text("Live video is OFF")

        st.subheader("Uploaded an Image")
        upload_demo = cv2.imread("demopic.png")
        uploaded_widget.image(upload_demo, caption="Uploaded Image", use_column_width=True)
        # if uploaded_file is not None:
        #     st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        #     uploaded_image = file_2_image(uploaded_file)
        #     print(uploaded_image)
        #     if uploaded_image is not None:
        #         updated_image = fetch_boundary(uploaded_image)
        #         update_widget.image(updated_image, caption="Hardcoded Image", use_column_width=True)

           

if __name__ == "__main__":
    main()
