import streamlit as st
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

def show_desc(place):
    place='?'+ place
    response = requests.get(url="https://en.wikipedia.org/wiki/"+place, )
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find(id="bodyContent")
    st.write(content.string)