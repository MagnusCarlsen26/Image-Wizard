import streamlit as st
import cv2

def main():
    st.markdown("<h1 style='text-align: center;'>CV Project</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.title("Options")
    run = st.sidebar.checkbox('Run')
    st.sidebar.title("Upload Image")
    uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    col1, col2 = st.columns(2)
    
    with col2:
        st.subheader("Output Image")
        hardcoded_image_path = r"C:\Users\Mic\Desktop\cv\$R3Y837B.jpg"
        hardcoded_image = open(hardcoded_image_path, "rb").read()
        st.image(hardcoded_image, caption="Hardcoded Image", use_column_width=True)

    with col1:
        if run:
            st.sidebar.text("Live video is ON")
            # OpenCV code to capture live video from webcam
            FRAME_WINDOW = st.image([])
            camera = cv2.VideoCapture(0)
            while run:
                _, frame = camera.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FRAME_WINDOW.image(frame)
            else:
                st.write('Stopped')
        else:
            st.sidebar.text("Live video is OFF")

        st.subheader("Uploaded an Image")
        if uploaded_file is not None:
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    


    
    

if __name__ == "__main__":
    main()
