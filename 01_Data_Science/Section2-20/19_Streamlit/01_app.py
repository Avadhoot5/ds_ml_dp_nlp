import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('Hello Streamlit')

# Display a text
st.write('Sample Text')

# creating a df
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

# display the df

st.write('Here is the dataframe')
st.write(df)

st.space()

# charting - line chart

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a','b','c']
)

st.write('Line Chart: ')

st.line_chart(chart_data)
