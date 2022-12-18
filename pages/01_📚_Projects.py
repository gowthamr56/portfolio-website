# PROJECTS PAGE
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
    page_title="Gowtham - Projects",
    layout="wide"
)

# styling(CSS) for projects page
st.markdown(
    """
        <style>
            header, footer{
                visibility: hidden;
            }
            div.css-keje6w.e1tzin5v2{
                display: flex;
                justify-content: center;
                align-items: center;
            }
            div.css-znku1x.e16nr0p33>p>a{
                display: block;
                border: 2px solid #31333f;
                border-radius: 5px;
                text-decoration: none;
                color: black;
                text-align: center;
            }
            div.css-znku1x.e16nr0p33>p>a:hover{
                text-decoration: underline;
                background-color: #E7E4E4;
                transform: scale(0.99);
            }
        </style>
        # 📚 Projects
    """, unsafe_allow_html=True
)

# function that loads lottiefiles through url
def load_lottie_url(lottie_url: str):
    r = requests.get(lottie_url)
    if r.status_code != 200:
        return None
    return r.json()

# generalized method to dispaly the details about the project
def project_info(project_title, demo_link, github_link):
    st.markdown(f"""
        # {project_title}
    """, unsafe_allow_html=True)
    st.markdown(f"""
        <a href={demo_link}>Demo <?xml version="1.0" standalone="no"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN" "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd"><svg version="1.0" xmlns="http://www.w3.org/2000/svg"  width="30" height="30" viewBox="0 0 48.000000 48.000000" preserveAspectRatio="xMidYMid meet"><g transform="translate(0.000000,48.000000) scale(0.100000,-0.100000)" fill="#000000" stroke="none"><path d="M77 402 c-14 -16 -17 -43 -17 -164 0 -188 -10 -178 182 -178 188 0 178 -10 178 182 0 188 10 178 -182 178 -128 0 -147 -2 -161 -18z m308 -162 l0 -145 -145 0 -145 0 -3 134 c-1 74 0 141 2 148 4 11 37 13 148 11 l143 -3 0 -145z"/><path d="M220 345 c0 -11 11 -15 42 -15 l43 0 -78 -78 c-42 -42 -77 -83 -77 -90 0 -26 28 -9 102 65 l78 78 0 -43 c0 -31 4 -42 15 -42 12 0 15 14 15 70 l0 70 -70 0 c-56 0 -70 -3 -70 -15z"/></g></svg></a><br>
        <a href={github_link}>GitHub <?xml version="1.0"?><svg fill="#000000" xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 30 30" width="30px" height="30px">    <path d="M15,3C8.373,3,3,8.373,3,15c0,5.623,3.872,10.328,9.092,11.63C12.036,26.468,12,26.28,12,26.047v-2.051 c-0.487,0-1.303,0-1.508,0c-0.821,0-1.551-0.353-1.905-1.009c-0.393-0.729-0.461-1.844-1.435-2.526 c-0.289-0.227-0.069-0.486,0.264-0.451c0.615,0.174,1.125,0.596,1.605,1.222c0.478,0.627,0.703,0.769,1.596,0.769 c0.433,0,1.081-0.025,1.691-0.121c0.328-0.833,0.895-1.6,1.588-1.962c-3.996-0.411-5.903-2.399-5.903-5.098 c0-1.162,0.495-2.286,1.336-3.233C9.053,10.647,8.706,8.73,9.435,8c1.798,0,2.885,1.166,3.146,1.481C13.477,9.174,14.461,9,15.495,9 c1.036,0,2.024,0.174,2.922,0.483C18.675,9.17,19.763,8,21.565,8c0.732,0.731,0.381,2.656,0.102,3.594 c0.836,0.945,1.328,2.066,1.328,3.226c0,2.697-1.904,4.684-5.894,5.097C18.199,20.49,19,22.1,19,23.313v2.734 c0,0.104-0.023,0.179-0.035,0.268C23.641,24.676,27,20.236,27,15C27,8.373,21.627,3,15,3z"/></svg></a>
    """, unsafe_allow_html=True)

# title of the page
# st.title("📚 Projects")

# sixth project - handwritten digit recognition system
six = st.container()
with six:
    col1, col2 = st.columns(2)
    with col1:
        project_info(
            project_title="A Novel Method for Handwritten Digit Recognition System",
            demo_link="https://youtu.be/K_E4Gk10cmM",
            github_link="https://github.com/IBM-EPBL/IBM-Project-41956-1660646536"
        )
    with col2:
        project_info(
            project_title="Weather forecasting appliction\n",
            demo_link="https://check-weather-in-your-city.herokuapp.com",
            github_link="https://github.com/gowthamr56/weather-application-with-flask.git"
        )
        

# fifth project - weather forecasting application
five = st.container()
with five:
    col1, col2 = st.columns(2)
    with col1:
        project_info(
            project_title="YouTube video and audio downloader",
            demo_link="https://gowthamr56-youtube-video-downloader-using-python-main-cgb307.streamlitapp.com/",
            github_link="https://github.com/gowthamr56/Youtube-video-downloader-using-python.git"
        )
    with col2:
        project_info(
            project_title="QR CODE generator and scanner",
            demo_link="https://gowthamr56-scan-create-qr-main-s638mm.streamlitapp.com/",
            github_link="https://github.com/gowthamr56/scan-create-qr.git"
        )

# first project - youtube video/audio downloader
one = st.container()
with one:
    col1, col2 = st.columns(2)
    with col1:
        project_info(
            project_title="Hand gesture volume control using computer vision",
            demo_link="https://pynerds.blogspot.com",
            github_link="https://github.com/gowthamr56/Gesture-Volume-Control-using-OpenCV-with-Python.git"
        )
    with col2:
        project_info(
            project_title="Virtual mouse using computer vision",
            demo_link="https://pynerds.blogspot.com",
            github_link="https://github.com/gowthamr56/virtual-mouse-using-computer-vision.git"
        )
