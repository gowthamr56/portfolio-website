import requests
from urllib import request
from PIL import Image

# getting page icon 
def get_page_icon(icon_url: str):
    request.urlretrieve(url=icon_url, filename="page_icon")
    return Image.open("page_icon")

# function that loads lottiefiles through url
def load_lottie_url(lottie_url: str):
    r = requests.get(lottie_url)
    if r.status_code != 200:
        return None
    return r.json()