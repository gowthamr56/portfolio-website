# BLOGS PAGE
import streamlit as st
from typing import Union
from generalize import get_page_icon

# getting page icon 
page_icon = get_page_icon(icon_url="https://raw.githubusercontent.com/gowthamr56/portfolio-website/master/icons/page_icon.png")

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
        .topic{
            border: 1px solid #dedcdc;
            border-radius: 20px;
            padding: 5px;
            background: #dedcdc;
        }
        .css-eczf16.e16nr0p31{
            text-decoration: none;
        }
        div.css-keje6w.e1tzin5v1>div{
            padding: 10px;
            border-radius: 10px;
            transition-property: all;
            transition-duration: 1s;
            transition-timing-function: ease;
        }
        div.css-keje6w.e1tzin5v1>div:hover{
            background: #E7E4E4;
            transform: scale(1.03);
        }
        </style>
        # 📰 Blogs
        <br>
    """, unsafe_allow_html=True
)

def blog_post(blog_title: str, blog_link: str, blog_caption: str, date: int, month: str, year: int, topics: Union[list, tuple]) -> None:
    st.markdown(
        f"""
            <p style="margin-bottom: -10px; color: grey;">{month} {date}, {year}</p>
            <h4>
                <a href="{blog_link}" style="text-decoration: none; color: black;">{blog_title}</a>
            </h4>
        """, unsafe_allow_html=True
    )
    st.caption(f"{blog_caption}")

    # considering only first two topics
    if len(topics) > 2:
        topics = topics[:2]

    st.markdown(
        f"""
            <p style="font-size: 14px; font-weight: bold; margin-top: -7px;">
                <span class="topic">{topics[0]}</span> <span class="topic">{topics[1]}</span>
            </p>
        """, unsafe_allow_html=True
    )

# ------------------------------------------------------ #

with  st.container():
    col2, col3 = st.columns(2)
    # with col1:
    #     ...
    with col2:
        blog_post(
            "Parallelism Vs Concurrency | Learn Python Stuffs with ChatGPT | #3",
            "https://medium.com/@gowtham180502/parallelism-vs-concurrency-learn-python-stuffs-with-chatgpt-3-165a14027db6",
            "This article in the series will walk you through “Parallelism vs Concurrency”",
            18,
            "Feb",
            2023,
            ["Python", "Parallelism/Concurrency"]
        )
    with col3:
        blog_post(
            "Is threading in Python parallel? | Learn Python Stuffs with ChatGPT | #2",
            "https://medium.com/towardsdev/is-threading-in-python-parallel-learn-python-stuffs-with-chatgpt-2-b51e95ccc71f",
            "This article in the series will walk you through “Is really threading in python parallel?”",
            6,
            "Feb",
            2023,
            ["Python", "Threading"]
        )

st.markdown(
    """<hr>""", unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        blog_post(
            "Understanding of join() function in threading module | Learn Python Stuffs with ChatGPT | #1",
            "https://medium.com/towardsdev/understanding-of-join-function-in-threading-module-learn-python-stuffs-with-chatgpt-1-3b384df7d0f1",
            "This article in the series will give you a clear understanding of the join() function in Python’s threading module.",
            3, 
            "Feb", 
            2023,
            ["Python", "Threading"]
        )
    with col2:
        blog_post(
            "Store images in MySQL using Python",
            "https://medium.com/towardsdev/store-images-in-mysql-using-python-b5762dc9d743",
            "This article will discuss how to store images/files in the MySQL database using Python. To perform storing images/files from the MySQL database, we have to create a database and a table to store them.",
            28, 
            "Jan", 
            2023,
            ["Python", "MySQL"]
        )
    with col3:
        blog_post(
            "Create 7 different files using Python",
            "https://medium.com/towardsdev/create-7-different-files-using-python-476b4644dc2d",
            "In this article, we will discuss how to create seven different files and how to read those created files using Python programming language. The seven file types are,",
            31, 
            "Dec", 
            2022,
            ["Python", "File Handling"]
        )

st.markdown(
    """<hr>""", unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        blog_post(
            "How to integrate ChatGPT with Python?",
            "https://medium.com/@gowtham180502/how-to-integrate-chatgpt-with-python-7dc61d471d8d",
            "In this article, we are going to discuss how to integrate ChatGPT with Python. Before that, we have to know what actually a ChatGPT is. We will discuss that in the following,",
            13, 
            "Dec", 
            2022,
            ["Python", "ChatGPT"]
        )
    with col2:
        blog_post(
            "Implementing RSA Algorithm using Python",
            "https://medium.com/@gowtham180502/implementing-rsa-algorithm-using-python-836f7da2a8e0",
            "This article explains what actually the RSA algorithm is in cryptography and shows how to implement the RSA algorithm for the encryption and decryption of data using Python. Here, data refers to numbers. You can also use string data for encryption and decryption using this algorithm.",
            9, 
            "Dec", 
            2022,
            ["Python", "Cryptography"]
        )
    with col3:
        blog_post(
            "How to deploy your CNN model in IBM Cloud?",
            "https://medium.com/@gowtham180502/how-to-deploy-your-cnn-model-in-ibm-cloud-19d49e4d0cf8",
            "This article clearly explains how to deploy your Convolutional Neural Network (CNN) model in IBM Cloud platform.",
            27, 
            "Nov", 
            2022,
            ["CNN Model Deployment", "IBM Cloud"]
        )

st.markdown(
    """<hr>""", unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        blog_post(
            "10 simple coding interview questions and their answers using Python",
            "https://www.isrgrajan.com/10-simple-coding-interview-questions-and-their-answers-using-python.html",
            "In this article, we are going to discuss 10 simple Python coding interview questions and answers that are entirely for freshers.",
            16, 
            "Nov", 
            2022,
            ["Python", "Interview Preparation"]
        )
    with col2:
        blog_post(
            "Text-to-Speech conversion using Python and IBM Watson.",
            "https://medium.com/@gowtham180502/text-to-speech-conversion-using-python-and-ibm-watson-c7356dc0a3ce",
            "In this article, I will take you to how to convert text to speech using IBM Watson Studio. Before that, I will show you how to convert text to speech using the Python module pyttsx3.",
            12,
            "Nov",  
            2022,
            ["Python", "IBM Watson"]
        )
    with col3:
        blog_post(
            "How to compare two images and get an accuracy level with Python?",
            "https://medium.com/@gowtham180502/how-to-compare-two-images-and-get-an-accuracy-level-with-python-61d8d953a942",
            "In this article, I am going to take you to how to compare two images and get an accuracy level between those images using Python, OpenCV and Face Recognition modules.",
            29, 
            "Oct", 
            2022,
            ["Python", "Computer Vision"]
        )

st.markdown(
    """<hr>""", unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        blog_post(
            "How to list all the attributes and methods available inside the Python class?",
            "https://medium.com/@gowtham180502/how-to-list-all-the-attributes-and-methods-available-inside-the-python-class-154067789b84",
            "In this blog, we are going to learn how to list all the attributes and methods available inside the python class/module.",
            21, 
            "Oct", 
            2022,
            ["Python", "OOPS"]
        )
    with col2:
        blog_post(
            "How can we replace background green screen using Python and Computer Vision?",
            "https://medium.com/@gowtham180502/how-can-we-replace-the-green-screen-background-using-python-4947f1575b1f",
            "In this blog, we are going to discuss how to replace a image which is having green screen background.",
            10, 
            "Oct", 
            2022,
            ["Python", "Computer Vision"]
        )
    with col3:
        blog_post(
            "Paranthesis checker using Python - Stack Application",
            "https://pynerds.blogspot.com/2022/02/paranthesis-checker-implementation.html",
            "In this blog, we are going to see one of the implementation of stack application which is a parenthesis checker.",
            24, 
            "Feb", 
            2022,
            ["Python", "Data Structures"]
        )

st.markdown(
    """<hr>""", unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        blog_post(
            "How do we detect and track motions using Python and Computer Vision?",
            "https://medium.com/@gowtham180502/motion-detection-and-tracking-using-opencv-python-ea75ef927e72",
            "In this blog, we are going to see how to detect and track movements using the OpenCV module.",
            23, 
            "Sep", 
            2021,
            ["Python", "Computer Vision"]
        )
    with col2:
        blog_post(
            "How to detect colors using Python and Computer Vision?",
            "https://medium.com/@gowtham180502/how-to-detect-colors-using-opencv-python-98aa0241e713",
            "In this blog, we are going to see how the colors are detected by the OpenCV module.",
            22,
            "Sep",
            2021,
            ["Python", "Computer Vision"]
        )
    with col3:
        blog_post(
            "How do we make an audio book using Python?",
            "https://pynerds.blogspot.com/2021/08/make-audio-book-from-pdf-file-using.html",
            "Here, you are going to know about making audio book from PDF file book using Python",
            15,
            "Aug",
            2021,
            ["Python", "Text to Speech"]
        )

st.markdown(
    """<hr>""", unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        blog_post(
            "Text to Speech converter using Python",
            "https://pynerds.blogspot.com/2021/08/converting-text-to-speech-using-python.html",
            "In this blog, you are going to learn about how to convert text to speech using python",
            2,
            "Aug",
            2021,
            ["Python", "Text to Speech"]
        )
    with col2:
        blog_post(
            "Learn how to recognize user's voice input using Python",
            "https://pynerds.blogspot.com/2021/08/speech-recognition-using-python.html",
            "This blog explains the implementation of the how we can recognize voice input from the user.",
            2,
            "Aug",
            2021,
            ["Python", "Speech Recognition"]
        )
    with col3:
        blog_post(
            "How do we handle files in Python? - File Handling",
            "https://pynerds.blogspot.com/2020/12/file-handling-python.html",
            "This blog explains about the file handling concept in Python",
            12, 
            "Dec",
            2020,
            ["Python", "File Handling"]
        )

st.markdown(
    """<hr>""", unsafe_allow_html=True)
