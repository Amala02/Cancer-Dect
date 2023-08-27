import streamlit as st
from ultralytics import YOLO
import pandas as pd
import numpy as np
from io import StringIO
import PIL
from PIL import Image
import requests
from io import BytesIO


st.title("cancer-dect")
st.text("Upload image here:")
uploaded_file = st.file_uploader("Choose a file", type=['png', 'jpg'])
if uploaded_file is not None:
    

    st.write("filename:", uploaded_file.name)
    uploaded_image = PIL.Image.open(uploaded_file)
    st.image(uploaded_image, caption='Input', width=200)

    st.divider()

    type_=st.selectbox("Choose any one type of detection", (('Brain'), ('Skin')))
    conf = st.slider('Set confidence level percentage', 0, 100, 25)

    if type_=='Brain':
        model= YOLO("cd_detect.pt")
        confi=conf/100
        res=model(uploaded_image, conf=confi)
        img=res[0].plot()
        a=res[0]
        if a.masks is not None:
            st.image(img, caption='Output', width=600)
        else:
            st.write("No detections found")

    if type_=='Skin':
        # Load a model
        model = YOLO('yolov8n.pt')  # load an official model
        model= YOLO("skin_detect.pt")
        confi=conf/100
        res=model(uploaded_image, conf=confi)
        img=res[0].plot()
        a=res[0]
        if a.masks is not None:
            st.image(img, caption='Output', width=600)
        else:
            st.write("No detections found")
    
url="https://github.com/Amala02"
st.write("Made by: [@Amala02](%s)" % url)
