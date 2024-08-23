import streamlit as st
import pandas as pd
import numpy as np
 
# Title of the dashboard
st.title('Exploratory Data Analysis for Solar Installation in Benin, Sierra Leone, and Togo,')
 
# Sidebar for user input
st.sidebar.header('Countries')
option = st.sidebar.selectbox('Select country:', ["Benin", "Sierra Leone", "Togo0"])
 
# Display the selected option
st.write('You selected:', option)
 
# Generate some random data
data = np.random.randn(100, 3)
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
 
# Display the dataframe
st.write('Random Data:', df)
 
# Plot the data
st.line_chart(df)