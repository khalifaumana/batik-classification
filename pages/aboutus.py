import streamlit as st
from PIL import  Image
import numpy as np

def app():
    st.header("About Us")
    st.write("")
    st.write("")

    profPic1 = Image.open('images/profil_khalifa.jpg')
    profPic1 = np.array(profPic1)

    col1, col2 = st.columns(2)
    col1.image(profPic1, width = 350)
    col2.header("Muhammad Khalifa Umana\nIlmu Komputer - Universitas Gadjah Mada ")

    profPic2 = Image.open('images/profil_ais.jpeg')
    profPic2 = np.array(profPic2)

    col3, col4 = st.columns(2)
    col3.header("Aisya Nugrafitra Murti\nAktuaria - Universitas Gadjah Mada")
    col4.image(profPic2, width = 350)

    profPic3 = Image.open('images/profil_hanifa.jpeg')
    profPic3 = np.array(profPic3)

    col5, col6 = st.columns(2)
    col5.image(profPic3, width = 350)
    col6.header("Hanifa Reygina Fajrin\nMatematika - Universitas Gadjah Mada")