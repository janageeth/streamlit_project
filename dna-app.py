# Importing all the libraries needed

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

##############################
# Page Title
##############################

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!
""")


##############################
# Input Text Box
##############################

#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')
sequence_input = ">DNA Query 2\nGAACAGTGGAGGCTAGGCAGTAGGGCTAGCTAAGCTAGCTAGCTAG"

sequence = st.text_area("sequence_input", sequence_input, height=25)


st.header('INPUT (DNA Query)')
sequence



