# simple bioinformatics DNA Count

import pandas as pd # used here to create the DataFrame
import streamlit as st # forms the core of the web application
import altair as alt # statistical visualization library to create charts and graphs
from PIL import Image # to load and display web app logo

# opening and displaying the image with a width of 450px
image = Image.open('app-DNA.jpg')
st.image(image, width=450)

# app title and description
st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of any query DNA!

***
""")

# taking DNA sequence input
st.header('Enter DNA sequence')

sequence_input = '''> DNA Query (enter DNA sequence below) - \n
GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG
ATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC
TGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT'''

# creating text area for users to input their DNA sequence
sequence = st.text_area("Sequence Input", sequence_input, height=150)

# splits the input text into lines
sequence = sequence.splitlines()

# removed the first line (header line) from the sequence
sequence = sequence[1:] # Skips the sequence name (first line)

# joining the remaining lines into a single string of DNA sequence
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

# printing the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

# function to count nucleotide
st.header('OUTPUT (DNA Nucleotide Count)')

def DNA_nucleotideCount(seq):
  d = dict([
            ('A', seq.count('A')),
            ('T', seq.count('T')),
            ('G', seq.count('G')),
            ('C', seq.count('C'))
            ])
  return d

X = DNA_nucleotideCount(sequence)

# nucleotide information in print text
st.subheader('1. Nucleotide Count Information')
st.write('There are  ' + str(X['A']) + ' Adenine (A)')
st.write('There are  ' + str(X['T']) + ' Thymine (T)')
st.write('There are  ' + str(X['G']) + ' Guanine (G)')
st.write('There are  ' + str(X['C']) + ' Cytosine (C)')

# nucleotide information in Pandas DataFrame
st.subheader('2. DataFrame Format')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

# create and display bar chart for the same
st.subheader('3. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(x='nucleotide', y='count')
p = p.properties(width=alt.Step(80))
st.write(p)
