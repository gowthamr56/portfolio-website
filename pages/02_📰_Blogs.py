# BLOGS PAGE
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

# styling(CSS) for blogs page
st.markdown(
    """
        <style>
        header, footer{
            visibility: hidden;
        }
        .css-eczf16.e16nr0p31{
            text-decoration: none;
        }
        div.css-ocqkz7.e1tzin5v4>div{
            padding: 10px;
            border-radius: 10px;
            transition-property: all;
            transition-duration: 1s;
            transition-timing-function: ease;
        }
        div.css-ocqkz7.e1tzin5v4>div:hover{
            background: #E7E4E4;
            transform: scale(1.03);
        }
        </style>
        # 📰 Blogs
    """, unsafe_allow_html=True
)


def blog_post(blog_title, blog_link, blog_caption):
    st.markdown(
        f"""
            <h4>
                <a href="{blog_link}" style="text-decoration: none; color: black;">{blog_title}</a>
            </h4>
        """, unsafe_allow_html=True
    )
    st.caption(f"{blog_caption}")


# row one
one = st.container()
with one:
    col1, col2, col3 = st.columns(3)
    with col1:
        blog_post(
            blog_title="How to detect colors using Python and Computer Vision",
            blog_link="https://pynerds.blogspot.com/2021/09/color-detection-using-opencv-and-python.html",
            blog_caption="In this blog, we are going to see how the colors are detected by the OpenCV module."
        )
    with col2:
        blog_post(
            blog_title="How do we detect and track motions using Python and Computer Vision",
            blog_link="https://pynerds.blogspot.com/2021/09/motion-detection-and-tracking-using.html",
            blog_caption="In this blog, we are going to see how to detect and track movements using the OpenCV module."
        )
    with col3:
        blog_post(
            blog_title="Paranthesis checker using Python - Stack Application",
            blog_link="https://pynerds.blogspot.com/2022/02/paranthesis-checker-implementation.html",
            blog_caption="In this blog, we are going to see one of the implementation of stack application which is a parenthesis checker."
        )

# row two
two = st.container()
with two:
    col1, col2, col3 = st.columns(3)
    with col1:
        blog_post(
            blog_title="How can we replace background green screen using Python and Computer Vision",
            blog_link="https://pynerds.blogspot.com/2022/06/replace-green-screen-using-opencv-and.html",
            blog_caption="In this blog, we are going to discuss how to replace a video which is having green screen background."
        )
    with col2:
        blog_post(
            blog_title="Learn how to recognize user's voice input using Python",
            blog_link="https://pynerds.blogspot.com/2021/08/speech-recognition-using-python.html",
            blog_caption="This blog explains the implementation of the how we can recognize voice input from the user."
        )
    with col3:
        blog_post(
            blog_title="How do we handle files in Python - File Handling",
            blog_link="https://pynerds.blogspot.com/2020/12/file-handling-python.html",
            blog_caption="This blog explains about the file handling concept in Python"
        )

# row three
three = st.container()
with three:
    col1, col2, col3 = st.columns(3)
    with col1:
        blog_post(
            blog_title="Text to Speech converter using Python",
            blog_link="https://pynerds.blogspot.com/2021/08/converting-text-to-speech-using-python.html",
            blog_caption="In this blog, you are going to learn about how to convert text to speech using python"
        )
    with col2:
        blog_post(
            blog_title="How do we make an audio book using Python",
            blog_link="https://pynerds.blogspot.com/2021/08/make-audio-book-from-pdf-file-using.html",
            blog_caption="Here, you are going to know about making audio book from PDF file book using Python"
        )
    with col3:
        pass