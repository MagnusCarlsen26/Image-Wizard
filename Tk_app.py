import cv2
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import modules_tk as md
from ultralytics import YOLO
from tkinter import colorchooser ,  Scale
model = YOLO('yolov8n-seg.pt')
mode = 0
alpha = 128
color = "#00ff00"

def show_video1():
    ret, frame = camera.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_p = frame.copy()
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(frame)
        video_frame.imgtk = frame
        video_frame.config(image=frame)
        frame1 = process_frame(frame_p)
        if frame1 is not None:
            frame1 = Image.fromarray(frame1)
            frame1 = ImageTk.PhotoImage(frame1)
            video_frame_1.imgtk = frame1
            video_frame_1.config(image=frame1)
        # show_video2(frame)  # Pass the frame to show_video2
    video_frame.after(10, show_video1)

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
    
def update_brightness(value):
    global alpha
    alpha = int(value)
    print("Selected brightness:", value)

def get_rgb_from_hex(hex_color):
  
  # Remove the leading "#" if present
  hex_color = hex_color.lstrip("#")
  # Check for valid hex length (6 digits)
  if len(hex_color) != 6:
      raise ValueError("Invalid hex color format. Please use #RRGGBB format.")
  # Convert each hex digit to integer and multiply by 16 for proper base conversion
  rgb_values = [int(hex_color[i:i+2], 16) for i in range(0, len(hex_color), 2)]
  return rgb_values

def process_frame(frame):
    frame_1 = frame .copy()
    boundary = fetch_boundary(frame)
    global color
    global alpha
    rgb_hex = get_rgb_from_hex(color)
    if boundary is not None:
        if mode == 1:
            return md.back_black(frame_1,boundary,rgb_hex)
        if mode == 2:
            return md.back_white(frame_1,boundary,rgb_hex)
        if mode == 3:
            return md.back_normal(frame_1,boundary,rgb_hex)
        if mode == 4:
            return md.alpha_blending(frame_1,boundary,alpha,rgb_hex)
        if mode == 5:

            return md.transparent_bg(frame_1,boundary,rgb_hex)
        if mode == 6:
            return md.lower_contrast(frame_1,boundary)
        if mode == 7:
            return md.non_linear_lower(frame_1,boundary)
        if mode == 8:
            return md.invert(frame_1,boundary)

        else:
            return frame
    else:
        return None

def toggle_camera():
    global camera, camera_on
    if camera_on:
        camera.release()
        camera_button.config(text="Turn Camera On")
    else:
        camera = cv2.VideoCapture(0)
        camera_button.config(text="Turn Camera Off")
    camera_on = not camera_on

app = tk.Tk()
app.title("Live Video App")

video_frame = tk.Label(app)
video_frame_1 = tk.Label(app)
video_frame.pack(side="left")
video_frame_1.pack(side="right")

camera = cv2.VideoCapture(0)

camera_button = tk.Button(app, text="Turn Camera Off", command=toggle_camera)
camera_button.pack()



def pick_color():
    global color
    color = colorchooser.askcolor()[1]  # Get the selected color in hexadecimal format
    color_button.config(bg=color)

def set_mode(mode_value):
    global mode
    mode = mode_value

mode_button_0 = tk.Button(app, text="Reset", command=lambda: set_mode(0))
mode_button_0.pack()

mode_button_1 = tk.Button(app, text="BG Black", command=lambda: set_mode(1))
mode_button_1.pack()

mode_button_2 = tk.Button(app, text="BG White", command=lambda: set_mode(2))
mode_button_2.pack()

mode_button_3 = tk.Button(app, text="BG Normal", command=lambda: set_mode(3))
mode_button_3.pack()

mode_button_4 = tk.Button(app, text="Alpha Blend", command=lambda: set_mode(4))
mode_button_4.pack()

mode_button_5 = tk.Button(app, text="Custom BG", command=lambda: set_mode(5))
mode_button_5.pack()

mode_button_6 = tk.Button(app, text="Low Contrast", command=lambda: set_mode(6))
mode_button_6.pack()

mode_button_7 = tk.Button(app, text="Non Linear Low", command=lambda: set_mode(7))
mode_button_7.pack()

mode_button_8 = tk.Button(app, text="Invert", command=lambda: set_mode(8))
mode_button_8.pack()

color_button = tk.Button(app, text="Pick Color", command=pick_color)
color_button.pack()

brightness_slider = Scale(app, from_=0, to=255, orient=tk.HORIZONTAL, command=update_brightness)
brightness_slider.set(alpha)
brightness_slider.pack()

camera_on = True

show_video1()
app.mainloop()
