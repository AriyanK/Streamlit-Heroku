import streamlit as st
import pandas as pd
import numpy as np
from itertools import count
from datetime import datetime
import csv
st.title('Counter Example')

if 'key' not in st.session_state:
    st.session_state.key = 'value'

if 'count' not in st.session_state:
    st.session_state.count = 0
increment = st.button('Increment')
if increment:
    st.session_state.count += 1
st.write('Count = ', st.session_state.count)
bikeData = pd.read_csv('housing.csv')
st.write(bikeData.describe())

st.markdown('## Comments')

userList = []
commentList = []
with open('comments.csv') as f:
    for line in f:
        commentList.append(line)
with st.form("my_form"):
    text = st.text_input("Comments")
# Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Comment submitted")
        with open('comments.csv', 'a') as f:
            f.write(f'\n{text}')
            commentList.append(text)
st.write("Previous comments")
print("-------------------------------")
for i in commentList:
    st.write(i)
    st.write("--------------------")