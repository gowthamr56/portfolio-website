# RESUME PAGE
import streamlit as st
from streamlit_lottie import st_lottie
import requests
from urllib import request
from PIL import Image
import webbrowser

# getting page icon 
icon_url = "https://raw.githubusercontent.com/gowthamr56/portfolio-website/master/icons/page_icon.png"
request.urlretrieve(url=icon_url, filename="page_icon")
page_icon = Image.open("page_icon")

# page configurations
st.set_page_config(
    page_icon=page_icon,
    page_title="Gowtham - Resume",
    layout="wide"
)

# styling(CSS) for resume page
st.markdown(
    """
        <style>
            header, footer{
                visibility: hidden;
            }
            div.row-widget.stDownloadButton,
            div.row-widget.stButton{
                text-align: center;
            }
        </style>
        # 📜 Resume
        <br>
    """, unsafe_allow_html=True
)

view = st.checkbox("View")
if view:
    resume_url = "https://resume.io/r/NkRLMzXwb"
    
    view_btn = st.button("Click to view")
    if view_btn:
        webbrowser.open_new_tab(resume_url)
else:
    with open("resume_pdf.pdf", "rb") as file:
        st.download_button(f"Click to download", data=file, file_name="Gowtham-Resume.pdf")