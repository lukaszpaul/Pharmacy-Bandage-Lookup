import streamlit as st
import pandas as pd
import numpy as np
import csv
from PIL import Image

#SEARCH FUNCTION 
def search_csv(search_term):
  search_term = search_term.lower()
  rows = []
  with open('bandagesheet.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      if any(search_term in cell.lower() for cell in row):
        rows.append(row)
    if rows:
        st.table(rows)
    else:
     st.write("Not found")

#INITIALIZE ZONES
header = st.container()
lookup = st.container()
search = st.container()
dataset = st.container()

#LOGO PNG
image = Image.open('image.png')



with header: 
    st.image(image)
    st.markdown("<h2 style='text-align: center; color: rgb(0, 77, 187); font-weight:bold';>Bandage Lookup Resource</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: rgb(0, 77, 187); font-weight:bold';>By: Lukasz Paul 2022</h3>", unsafe_allow_html=True)

with lookup: 
    search_term = st.text_input('Lookup', 'Search...')
    if st.button("Search"):
     result = search_csv(search_term)
     st.write(result)
     st.markdown('#')
    
with dataset:
    st.markdown("<h3 style='color:rgb(0, 77, 187); font-weight:bold';>Raw Bandage Data</h3>", unsafe_allow_html=True)
    bandage_data = pd.read_csv('bandagesheet.csv')
    st.write(bandage_data)





