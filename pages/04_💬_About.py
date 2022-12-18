# ABOUT PAGE
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
    page_title="Gowtham - About",
    layout="wide"
)

# styling(CSS) for about page
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
        .links{
            display: flex;
            justify-content: center;
        }
        .links>a{
            margin: 10px;
        }
        .links>a:hover{
            transform: scale(1.1);
        }
    </style>
    # 💬 About
""", unsafe_allow_html=True)

# function that loads lottiefiles through url
def load_lottie_url(lottie_url: str):
    r = requests.get(lottie_url)
    if r.status_code != 200:
        return None
    return r.json()

# title of the page
# st.title("💬 About")

st.markdown(
    """
        #### As you know before,
        ### I'm Gowtham Ravichandran🤓
    """, unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    lottie_url = "https://assets2.lottiefiles.com/packages/lf20_wthp1bbd.json"
    st_lottie(load_lottie_url(lottie_url))

# details
with col2:
    st.markdown(
        """
        <p style="font-size: 18px">
            📌 I'm from Dharmapuri(Dt), Tamil Nadu, India.<br>
            📌 I did my high schooling in <b>Sri Vinayaga Matric Higher Secondary School</b> in Pennagaram(Tk), Dharmapuri(Dt) with <b>94.4%</b><br>
            📌 I have done my higher secondary studies in <b> Paramveer Matric Higher Secondary School</b> in papparapatti, Dharmapuri(Dt) with <b>77.2%</b><br>
            📌 Currently, I'm pursuing <b>final year</b> in <b>B.E - Computer Science</b> in <b>The Kavery Engineering College</b>, Salem(Dt).<br>
            📌 I love programming in <b>Python</b>. After I got clear in the basics of Python, I moved to work with <b>Computer Vision</b> and I have completed my couple of projects with that. I'm also having knowledge about <b>HTML, CSS,</b> and <b>MySQL</b>.<br>
            📌 Scroll down to visit my <b>social profiles</b>.
        </p>
        """, unsafe_allow_html=True
    )

# social profiles
st.markdown(
    """
        <hr>
        <div class="links">
            <a href="https://www.linkedin.com/in/gowtham-ravichandran-0889a2190?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B1usFymDfRj68%2BPhMJWJTDw%3D%3D"><svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 48 48" width="60" height="60"><path fill="#0078d4" d="M42,37c0,2.762-2.238,5-5,5H11c-2.761,0-5-2.238-5-5V11c0-2.762,2.239-5,5-5h26c2.762,0,5,2.238,5,5	V37z"/><path d="M30,37V26.901c0-1.689-0.819-2.698-2.192-2.698c-0.815,0-1.414,0.459-1.779,1.364	c-0.017,0.064-0.041,0.325-0.031,1.114L26,37h-7V18h7v1.061C27.022,18.356,28.275,18,29.738,18c4.547,0,7.261,3.093,7.261,8.274	L37,37H30z M11,37V18h3.457C12.454,18,11,16.528,11,14.499C11,12.472,12.478,11,14.514,11c2.012,0,3.445,1.431,3.486,3.479	C18,16.523,16.521,18,14.485,18H18v19H11z" opacity=".05"/><path d="M30.5,36.5v-9.599c0-1.973-1.031-3.198-2.692-3.198c-1.295,0-1.935,0.912-2.243,1.677	c-0.082,0.199-0.071,0.989-0.067,1.326L25.5,36.5h-6v-18h6v1.638c0.795-0.823,2.075-1.638,4.238-1.638	c4.233,0,6.761,2.906,6.761,7.774L36.5,36.5H30.5z M11.5,36.5v-18h6v18H11.5z M14.457,17.5c-1.713,0-2.957-1.262-2.957-3.001	c0-1.738,1.268-2.999,3.014-2.999c1.724,0,2.951,1.229,2.986,2.989c0,1.749-1.268,3.011-3.015,3.011H14.457z" opacity=".07"/><path fill="#fff" d="M12,19h5v17h-5V19z M14.485,17h-0.028C12.965,17,12,15.888,12,14.499C12,13.08,12.995,12,14.514,12	c1.521,0,2.458,1.08,2.486,2.499C17,15.887,16.035,17,14.485,17z M36,36h-5v-9.099c0-2.198-1.225-3.698-3.192-3.698	c-1.501,0-2.313,1.012-2.707,1.99C24.957,25.543,25,26.511,25,27v9h-5V19h5v2.616C25.721,20.5,26.85,19,29.738,19	c3.578,0,6.261,2.25,6.261,7.274L36,36L36,36z"/></svg></a>
            <a href="https://github.com/gowthamr56"><?xml version="1.0"?><svg fill="#000000" xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 30 30" width="60" height="60">    <path d="M15,3C8.373,3,3,8.373,3,15c0,5.623,3.872,10.328,9.092,11.63C12.036,26.468,12,26.28,12,26.047v-2.051 c-0.487,0-1.303,0-1.508,0c-0.821,0-1.551-0.353-1.905-1.009c-0.393-0.729-0.461-1.844-1.435-2.526 c-0.289-0.227-0.069-0.486,0.264-0.451c0.615,0.174,1.125,0.596,1.605,1.222c0.478,0.627,0.703,0.769,1.596,0.769 c0.433,0,1.081-0.025,1.691-0.121c0.328-0.833,0.895-1.6,1.588-1.962c-3.996-0.411-5.903-2.399-5.903-5.098 c0-1.162,0.495-2.286,1.336-3.233C9.053,10.647,8.706,8.73,9.435,8c1.798,0,2.885,1.166,3.146,1.481C13.477,9.174,14.461,9,15.495,9 c1.036,0,2.024,0.174,2.922,0.483C18.675,9.17,19.763,8,21.565,8c0.732,0.731,0.381,2.656,0.102,3.594 c0.836,0.945,1.328,2.066,1.328,3.226c0,2.697-1.904,4.684-5.894,5.097C18.199,20.49,19,22.1,19,23.313v2.734 c0,0.104-0.023,0.179-0.035,0.268C23.641,24.676,27,20.236,27,15C27,8.373,21.627,3,15,3z"/></svg></a>
            <a href="https://medium.com/@gowtham180502"><svg fill="#000000" xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 30 30" width="60" height="60"><path d="M8.5 7A8.5 8.5 0 108.5 24 8.5 8.5 0 108.5 7zM22 8A4 7.5 0 1022 23 4 7.5 0 1022 8zM28.5 9A1.5 6.5 0 1028.5 22 1.5 6.5 0 1028.5 9z"/></svg></a>
            <a href="https://pynerds.blogspot.com"><svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 48 48" width="60" height="60"><path fill="#ff6f00" d="M37,42H11c-2.761,0-5-2.239-5-5V11c0-2.761,2.239-5,5-5h26c2.761,0,5,2.239,5,5v26 C42,39.761,39.761,42,37,42z"/><path fill="#fff" d="M33.5,22h-1c-0.828,0-1.5-0.672-1.5-1.5V20c0-3.866-3.134-7-7-7h-4c-3.866,0-7,3.134-7,7v8 c0,3.866,3.134,7,7,7h8c3.866,0,7-3.134,7-7v-4.5C35,22.672,34.328,22,33.5,22z M20,19h5c0.553,0,1,0.448,1,1s-0.447,1-1,1h-5 c-0.553,0-1-0.448-1-1S19.447,19,20,19z M28,29h-8c-0.553,0-1-0.448-1-1s0.447-1,1-1h8c0.553,0,1,0.448,1,1S28.553,29,28,29z"/></svg></a>
            <a href="https://www.youtube.com/channel/UCZnc1SkBudQPzbOnYo3FWQA"><svg xmlns="http://www.w3.org/2000/svg" height="30px" width="30px" viewBox="-35.20005 -41.33325 305.0671 247.9995"><path d="M229.763 25.817c-2.699-10.162-10.65-18.165-20.748-20.881C190.716 0 117.333 0 117.333 0S43.951 0 25.651 4.936C15.553 7.652 7.6 15.655 4.903 25.817 0 44.236 0 82.667 0 82.667s0 38.429 4.903 56.85C7.6 149.68 15.553 157.681 25.65 160.4c18.3 4.934 91.682 4.934 91.682 4.934s73.383 0 91.682-4.934c10.098-2.718 18.049-10.72 20.748-20.882 4.904-18.421 4.904-56.85 4.904-56.85s0-38.431-4.904-56.85" fill="red"/><path d="M93.333 117.559l61.333-34.89-61.333-34.894z" fill="#fff"/></svg></a>
        </div>
        <hr>
    """, unsafe_allow_html=True
)


