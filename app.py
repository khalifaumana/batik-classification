import os
import streamlit as st
import numpy as np
from PIL import  Image

from multipage import MultiPage
from pages import predictWithPreprocess, predictWithoutPreprocess, aboutus

app = MultiPage()

display = Image.open('images/Logo.jpeg')
display = np.array(display)

col1, col2 = st.columns(2)
col1.image(display, width = 350)
col2.title("Batik Classification Using CNN")

st.text("Presented by Group 1 UGM04 \nA project for SPADADIKTI Associate Data Science Microcredential class")


app.add_page("Classification with image preprocessing", predictWithPreprocess.app)
app.add_page("Classification without image preprocessing", predictWithoutPreprocess.app)
app.add_page("About Us", aboutus.app)

app.run()


