# RESUME PAGE
import streamlit as st
from streamlit_lottie import st_lottie
import requests
from urllib import request
from PIL import Image

# getting page icon 
icon_url = "https://raw.githubusercontent.com/gowthamr56/portfolio-website/master/icons/page_icon.png"
request.urlretrieve(url=icon_url, filename="page_icon")
page_icon = Image.open("page_icon")

# page configurations
st.set_page_config(
    page_icon=page_icon,
    page_title="Gowtham - Blogs",
    layout="wide"
)

# styling(CSS) for resume page
st.markdown(
    """
        <style>
            header, footer{
                visibility: hidden;
            }
        </style>
        # 📜 Resume
    """, unsafe_allow_html=True
)

st.image("resume_image.jpg")