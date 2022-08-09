import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

# page configurations
page_icon = Image.open(r"icons\page_icon.png")
st.set_page_config(
    page_icon="""<?xml version="1.0" standalone="no"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN" "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd"><svg version="1.0" xmlns="http://www.w3.org/2000/svg" width="40.000000pt" height="40.000000pt" viewBox="0 0 40.000000 40.000000" preserveAspectRatio="xMidYMid meet"><g transform="translate(0.000000,40.000000) scale(0.100000,-0.100000)" fill="#000000" stroke="none"><path d="M144 269 c-13 -15 -19 -36 -19 -69 0 -62 23 -90 77 -90 45 0 78 28 78 65 0 22 -4 25 -35 25 -19 0 -35 -4 -35 -10 0 -5 11 -10 25 -10 28 0 29 -3 15 -31 -13 -24 -72 -26 -91 -3 -17 21 -17 87 0 108 18 21 77 21 89 0 5 -9 15 -15 22 -12 10 3 8 10 -8 26 -30 30 -92 30 -118 1z"/></g></svg>""",
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

with col2:
    lottie_url = "https://assets9.lottiefiles.com/packages/lf20_SmywXC.json"
    st_lottie(load_lottie_url(lottie_url))