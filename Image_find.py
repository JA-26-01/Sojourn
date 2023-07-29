import base64
import matplotlib.pyplot as plt
from io import BytesIO
import requests
from PIL import Image
import streamlit as st
import plotly.express as px

def new_img(txt):
    txt='?'+ txt
    response = requests.get("https://source.unsplash.com/random{0}".format(txt))
    bites = BytesIO(base64.b64decode(response.content))
    aux_im = Image.open(BytesIO(response.content))
    st.image(aux_im)