import streamlit as st

# Set page title and icon
st.set_page_config(
    page_title="SightScope: About",
    page_icon="./images/about.png",
    layout="wide"
)

# Display title and caption
st.title("About SightScope")
st.caption("A web application for detecting and tracking objects in images and videos.")

# Display About information
st.markdown("""
## What is SightScope?

SightScope is a web application that uses the YOLO V5 object detection model to automatically detect and track objects in images and videos. 

## How to use SightScope?

To use SightScope, simply upload an image, and the model will automatically detect objects and draw bounding boxes around them. 

SightScope also supports live video object detection, where you can use your webcam or other camera to detect objects in real-time. Simply click on the "Live Video" tab and allow the app to access your camera. 

## Who made SightScope?

SightScope was created by Kuldeep Singh, a software engineer with a passion for computer vision and machine learning.

## How to contact me?

You can reach me at kuldeepstechwork@gmail.com with any questions, feedback, or partnership inquiries. I'd love to hear from you! 
""")

# Add some space at the bottom
st.markdown("<br><br><br>", unsafe_allow_html=True)
