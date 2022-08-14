# HOME PAGE
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
    page_title="Gowtham - Home",
    layout="wide"
)

# styling(CSS) for the home page
st.markdown("""
    <style>
        header, footer{
            visibility: hidden;
        }
        div.css-keje6w.e1tzin5v2{
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .resume-button{
            display: block;
            width: 70px;
            text-align: center;
            text-decoration: none;
            border: 2px solid #31333f;
            border-radius: 5px;
        }
        .resume-button:hover{
            text-decoration: underline;
            background-color: #E7E4E4;
            transform: scale(0.98);
        }
    </style>
""", unsafe_allow_html=True)

# function that loads lottiefiles through url
def load_lottie_url(lottie_url: str):
    r = requests.get(lottie_url)
    if r.status_code != 200:
        return None
    return r.json()

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        ## Hai👋🏻, I' am
        # Gowtham Ravichandran
        #### I'm a guy who mostly thinks about the solution in a pythonic🐍 way
    """, unsafe_allow_html=True)
    st.markdown("""
        <a href="https://resume.io/r/NkRLMzXwb" class="resume-button" style="color: black;">Resume</a>
    """, unsafe_allow_html=True)
    with open("Gowtham-Resume.pdf", "rb") as file:
        st.download_button("Resume", data=file, file_name="Gowtham-Resume.pdf")

with col2:
    lottie_url = "https://assets9.lottiefiles.com/packages/lf20_SmywXC.json"
    st_lottie(load_lottie_url(lottie_url))