import streamlit as st

st.title("Test App")

with st.sidebar:

    Exchange_Option = st.multiselect(
        'Choose Stock Exchange:', [1, 2, 3, 4])