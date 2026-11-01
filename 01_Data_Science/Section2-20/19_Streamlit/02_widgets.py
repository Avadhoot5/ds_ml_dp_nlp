import streamlit as st
import pandas as pd

# title
st.title('Streamlit Text Input')

# Take input
name = st.text_input('Enter your name:')

# Slider
age = st.slider('Enter your age: ', 10, 100, 25)

st.write(f'Your age is {age}')

# Dropbox
options = ['JavaScript', 'Python', 'C++', 'Java']
choice = st.selectbox('Choose your favourite language:', options)
st.write(f'You selected {choice}')

# DF
data = {
    'name': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Karan', 'Neha'],
    'age': [25, 28, 23, 30, 27, 24],
    'city': ['Mumbai', 'Delhi', 'Pune', 'Bangalore', 'Chennai', 'Hyderabad']
}

df = pd.DataFrame(data)
st.write(df)

st.space()

df.to_csv('sample_data.csv')

file_selector = st.file_uploader('Choose an csv file to upload: ', type='csv')

if file_selector:
    df_file = pd.read_csv(file_selector)
    st.write(df_file)

if name:
    st.write(f'Hello, {name}')
