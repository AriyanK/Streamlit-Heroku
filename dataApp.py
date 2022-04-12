import streamlit as st
import pandas as pd
import numpy as np
st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0
increment = st.button('Increment')
if increment:
    st.session_state.count += 1
st.write('Count = ', st.session_state.count)
bikeData = pd.read_csv('housing.csv')
st.write(bikeData.describe())