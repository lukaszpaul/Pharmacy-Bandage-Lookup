import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

header = st.container()
lookup = st.container()

image = Image.open('image.png')

if lookup:
    primary_clr = st.get_option('theme.primaryColor')
    txt_clr = st.get_option('theme.textColor')
    second_clr = '#004dbb'

else:
    primary_clr = '#1515f1'
    txt_clr = '#004dbb'
    second_clr = '#004dbb' 

with header: 
    st.image(image)
    st.markdown("<h2 style='text-align: center; color: DarkBlue;'>Bandage Lookup Resource</h2>", unsafe_allow_html=True)

with lookup: 
    title = st.text_input('Lookup', 'Search...')


