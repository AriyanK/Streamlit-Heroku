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
path = "C:/Users/skay9/Documents/Ary's_Stuff/MachineLearning/"
bikeData = pd.read_csv(path + 'housing.csv')
st.write(bikeData.describe())