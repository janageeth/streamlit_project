# Importing all the libraries needed

import streamlit as st
from PIL import Image

##############################
# Page Title
##############################

image = Image.open('DNA.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!
""")

##############################
# Input Text Box
##############################

st.header('Enter DNA sequence')
sequence_input = ">DNA Query 2\nGAACAGTGGAGGCTAGGCAGTAGGGCTAGCTAAGCTAGCTAGCTAG"

sequence = st.text_area('Please enter the DNA Sequence here:', sequence_input, height=25)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

# print input DNA
st.header('INPUT (DNA Query)')
sequence

## DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')


##
def DNA_counter(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d


X = DNA_counter(sequence)

X_label = list(X)
x_values = list(X.values())

X
