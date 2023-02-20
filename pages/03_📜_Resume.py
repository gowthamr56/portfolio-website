# RESUME PAGE
import streamlit as st
from generalize import get_page_icon
import webbrowser

# getting page icon 
# page_icon = get_page_icon(icon_url="https://raw.githubusercontent.com/gowthamr56/portfolio-website/master/icons/page_icon.png")

# page configurations
st.set_page_config(
    # page_icon=page_icon,
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

def view_resume(link: str):
    webbrowser.open(url=link, new=2)

if st.button("View"):
    view_resume("https://resume.io/r/NkRLMzXwb")

with open("resume_pdf.pdf", "rb") as file:
    st.download_button(f"Click to download", data=file, file_name="Gowtham-Resume.pdf")