# CONTACT PAGE
import streamlit as st
from streamlit_lottie import st_lottie
from google.cloud import firestore
from google.oauth2 import service_account
import json
from generalize import load_lottie_url, get_page_icon

# getting page icon 
page_icon = get_page_icon(icon_url="https://raw.githubusercontent.com/gowthamr56/portfolio-website/master/icons/page_icon.png")

# page configurations
st.set_page_config(
    page_icon=page_icon,
    page_title="Gowtham - Contact",
    layout="wide"
)

# Authenticate to Firestore with the JSON account key.
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="portfolio-website-aeedb")

# styling(CSS) for contact page
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
    # Ask Me Anything 📭
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# collects details and messages of the user
# and stores it in firestore database
with col1:
    with st.form(key="contact_form"):
        name = st.text_input("Name").strip()
        email = st.text_input("E-mail or Phone").strip()
        message = st.text_area("Message").strip()
        btn = st.form_submit_button(label="Send")

if btn:
    if all((name, email, message)):
        if ("@" in email) and ("." in email) and (not(email.startswith("@"))):
            # creating a NEW document reference for the users using their name
            doc_ref = db.collection("messages").document(name)
            # uploading details like email and message to the firestore DB
            doc_ref.set(
                {
                    "email/phone": email,
                    "message": message
                }
            )
            st.success("Your message is sent successfully")
        else:
            st.error("Please, enter a valid E-mail address")
    else:
        st.error("Please, fill out all the fields")

with col2:
    lottie_url = "https://assets1.lottiefiles.com/packages/lf20_dhcsd5b5.json"
    st_lottie(load_lottie_url(lottie_url))

# copyrights
st.markdown(
    """
        <hr>
        <div class="copyrights">
            <center>
                <p style="font-size: 18px;">
                    Made with ❤ by <a href="" style="text-decoration: none;">Gowtham</a>
                    <br>
                    ...
                </p>
            </center>
        </div>
        <hr>
    """, unsafe_allow_html=True
)
