# HOME PAGE
import streamlit as st
from streamlit_lottie import st_lottie
from generalize import load_lottie_url, get_page_icon

# getting page icon
page_icon = get_page_icon(icon_url="https://raw.githubusercontent.com/gowthamr56/portfolio-website/master/icons/page_icon.png")

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
        div.css-keje6w.e1tzin5v1{
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
    </style>
""", unsafe_allow_html=True)

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
