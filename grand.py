import streamlit as st
import pandas as pd
import numpy as np
import csv
from csv import writer
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

#ADD TO CSV FUNCTION
def add_function():
  st.text("")
  st.text("")
  st.text("")
  st.markdown("<h3 style='color:rgb(0, 77, 187); font-weight:bold';>Add An Item</h3>", unsafe_allow_html=True)


  col4, col5, col6, col7, col8 = st.columns(5)
  NDC = col4.text_input('NDC/SCAN')
  Name = col5.text_input('Name')
  Box = col6.text_input('Box Price')
  Single = col7.text_input('Single Price')
  Kinray = col8.text_input('Kinray #')

  if st.button("Finalize Add"):
    List = [NDC, Name, Box, Single, Kinray]
    with open('bandagesheet.csv', 'a') as file:
      file.write(List)
      

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
    search_term = st.text_input('Lookup', placeholder = 'Enter Here...')
    if st.button("Search"):
     result = search_csv(search_term)
     st.write(result)
    st.text("")
    st.text("")
    st.text("")

    
with dataset:
    col1, col2, col3 = st.columns(3)

    col1.button("Add", on_click = add_function())
      

    col2.button("Edit")
    if col3.button("Raw Data"):
      st.text("")
      st.text("")
      st.text("")
      st.markdown("<h3 style='color:rgb(0, 77, 187); font-weight:bold';>Raw Bandage Data</h3>", unsafe_allow_html=True)
      bandage_data = pd.read_csv('bandagesheet.csv')
      st.write(bandage_data)





