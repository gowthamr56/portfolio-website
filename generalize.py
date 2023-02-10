import requests


# function that loads lottiefiles through url
def load_lottie_url(lottie_url: str):
    r = requests.get(lottie_url)
    if r.status_code != 200:
        return None
    return r.json()