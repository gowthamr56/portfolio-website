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


one = st.container()
with one:
    col1, col2, col3 = st.columns(3)
    with col1:
        blog_post(
            blog_title="Text-to-Speech conversion using Python and IBM Watson.",
            blog_link="https://medium.com/@gowtham180502/text-to-speech-conversion-using-python-and-ibm-watson-c7356dc0a3ce",
            blog_caption="In this article, I will take you to how to convert text to speech using IBM Watson Studio. Before that, I will show you how to convert text to speech using the Python module pyttsx3."
        )
    with col2:
        blog_post(
            blog_title="How to list all the attributes and methods available inside the Python class?",
            blog_link="https://medium.com/@gowtham180502/how-to-list-all-the-attributes-and-methods-available-inside-the-python-class-154067789b84",
            blog_caption="In this blog, we are going to learn how to list all the attributes and methods available inside the python class/module."
        )
    with col3:
        blog_post(
            blog_title="How to detect colors using Python and Computer Vision?",
            blog_link="https://medium.com/@gowtham180502/how-to-detect-colors-using-opencv-python-98aa0241e713",
            blog_caption="In this blog, we are going to see how the colors are detected by the OpenCV module."
        )


two = st.container()
with two:
    col1, col2, col3 = st.columns(3)
    with col1:
        blog_post(
            blog_title="How do we detect and track motions using Python and Computer Vision?",
            blog_link="https://medium.com/@gowtham180502/motion-detection-and-tracking-using-opencv-python-ea75ef927e72",
            blog_caption="In this blog, we are going to see how to detect and track movements using the OpenCV module."
        )
    with col2:
        blog_post(
            blog_title="How to compare two images and get an accuracy level with Python?",
            blog_link="https://medium.com/@gowtham180502/how-to-compare-two-images-and-get-an-accuracy-level-with-python-61d8d953a942",
            blog_caption="In this article, I am going to take you to how to compare two images and get an accuracy level between those images using Python, OpenCV and Face Recognition modules."
        )
    with col3:
        blog_post(
            blog_title="Paranthesis checker using Python - Stack Application",
            blog_link="https://pynerds.blogspot.com/2022/02/paranthesis-checker-implementation.html",
            blog_caption="In this blog, we are going to see one of the implementation of stack application which is a parenthesis checker."
        )


three = st.container()
with three:
    col1, col2, col3 = st.columns(3)
    with col1:
        blog_post(
            blog_title="How can we replace background green screen using Python and Computer Vision?",
            blog_link="https://medium.com/@gowtham180502/how-can-we-replace-the-green-screen-background-using-python-4947f1575b1f",
            blog_caption="In this blog, we are going to discuss how to replace a image which is having green screen background."
        )
    with col2:
        blog_post(
            blog_title="Learn how to recognize user's voice input using Python",
            blog_link="https://pynerds.blogspot.com/2021/08/speech-recognition-using-python.html",
            blog_caption="This blog explains the implementation of the how we can recognize voice input from the user."
        )
    with col3:
        blog_post(
            blog_title="10 simple coding interview questions and their answers using Python",
            blog_link="https://www.isrgrajan.com/10-simple-coding-interview-questions-and-their-answers-using-python.html",
            blog_caption="In this article, we are going to discuss 10 simple Python coding interview questions and answers that are entirely for freshers."
        )


four = st.container()
with four:
    col1, col2, col3 = st.columns(3)
    with col1:
        blog_post(
            blog_title="How do we handle files in Python? - File Handling",
            blog_link="https://pynerds.blogspot.com/2020/12/file-handling-python.html",
            blog_caption="This blog explains about the file handling concept in Python"
        )
    with col2:
        blog_post(
            blog_title="Text to Speech converter using Python",
            blog_link="https://pynerds.blogspot.com/2021/08/converting-text-to-speech-using-python.html",
            blog_caption="In this blog, you are going to learn about how to convert text to speech using python"
        )
    with col3:
        blog_post(
            blog_title="How do we make an audio book using Python?",
            blog_link="https://pynerds.blogspot.com/2021/08/make-audio-book-from-pdf-file-using.html",
            blog_caption="Here, you are going to know about making audio book from PDF file book using Python"
        )
