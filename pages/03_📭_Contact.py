import streamlit as st
from PIL import Image

# page configurations
page_icon = Image.open(r"icons\page_icon.png")
st.set_page_config(
    page_icon=page_icon,
    page_title="Gowtham - Contact",
    layout="wide"
)

st.markdown("""
    # Not yet developed,
    ### Try after sometime...
""")