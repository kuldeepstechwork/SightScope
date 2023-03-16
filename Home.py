import streamlit as st

# Set page title, icon, and layout
st.set_page_config(
    page_title="SightScope: YOLO V5 Object Detection App",
    page_icon="./images/home.png",
    layout="wide"
)

# Display title and caption
st.title("SightScope")
st.caption("A web application for detecting and tracking objects in images and videos.")

# Display project overview
st.markdown("""
## About SightScope

SightScope is an object detection and tracking web application that uses the YOLO V5 algorithm to detect and track objects in images and videos. This application is designed to be easy to use and accessible to anyone, even those without any prior experience in computer vision or machine learning.

## How it Works

SightScope uses a deep learning model called YOLO V5 to detect and track objects in images and videos. YOLO (You Only Look Once) is a state-of-the-art object detection algorithm that can detect multiple objects in an image or video frame with high accuracy and speed.

## List of Objects

The model used in this app can detect the following objects:

1. Person
2. Car
3. Chair
4. Bottle
5. Sofa
6. Bicycle
7. Horse
8. Boat
9. Motorbike
10. Cat
11. TV monitor
12. Cow
13. Sheep
14. Airplane
15. Train
16. Dining table
17. Bus
18. Potted plant
19. Bird
20. Dog




""")

# Add some space at the bottom
st.markdown("<br><br><br>", unsafe_allow_html=True)
