#Main Hurricane App file
import streamlit as st
import pandas as pd

st.title("Hurricane App")
st.html("<p>Produced by Jr and Nelda</span></p>")
st.divider()
st.header("Infomation")
st.write("We want to know what your location is to be able to give you the most accurate data")
user_location = st.text_input("Location: ")
st.divider()
