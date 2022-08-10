# CONTACT PAGE

import streamlit as st
from urllib import request
from PIL import Image

# getting page icon 
icon_url = "https://raw.githubusercontent.com/gowthamr56/portfolio-website/master/icons/page_icon.png"
request.urlretrieve(url=icon_url, filename="page_icon")
page_icon = Image.open("page_icon")

# page configurations
st.set_page_config(
    page_icon=page_icon,
    page_title="Gowtham - Contact",
    layout="wide"
)

# styling(CSS) for contact page
st.markdown("""
    <style>
        header, footer{
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    # Not yet developed,
    ### Try after sometime...
""")