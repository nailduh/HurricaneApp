import streamlit as st
import pandas as pd
from deep_translator import GoogleTranslator

# Mapping for language abbreviations
LANGUAGE_MAP = {
    'English': 'en',
    'Spanish': 'es',
    'Vietnamese': 'vi',
    'Portuguese': 'pt'  # pl
}

# Translate the text based on user language preference
def translateText(textBox, target_language):
    translated_text = [
        GoogleTranslator(source='auto', target=target_language).translate(text)
        for text in textBox
    ]
    return translated_text

# Array of text to be translated
textBox = [
    "Produced by Jr and Nelda", 
    "Information", 
    "We want to know what your location is to be able to give you the most accurate data", 
    "State: ",
    "ZIP Code: ",
    "County: ",
    "Street Address:"
]

# Initialize app
st.title("Hurricane App")

# Language preference selection
languagePref = st.selectbox("Language Preference", ("English", "Spanish", "Vietnamese", "Portuguese"), index=0)
languageAbbr = LANGUAGE_MAP.get(languagePref, 'en')

# Only translate if the language preference has changed
if 'current_language' not in st.session_state or st.session_state.current_language != languageAbbr:
    st.session_state.current_language = languageAbbr
    st.session_state.translated_textBox = translateText(textBox, languageAbbr)

# Display the translated text
st.write(st.session_state.translated_textBox[0])
st.divider()
st.header(st.session_state.translated_textBox[1])
st.write(st.session_state.translated_textBox[2])

# User input for getting location
#State
user_state = st.text_input(st.session_state.translated_textBox[3])
#Zip
user_zip = st.text_input(st.session_state.translated_textBox[4])
#County
user_county = st.text_input(st.session_state.translated_textBox[5])
#Street Address
user_streetAddy = st.text_input(st.session_state.translated_textBox[6])
st.divider()
if user_state != "" and user_zip != "" and user_streetAddy != "" and user_county != "":
    st.write("Your address is " + user_streetAddy + ', ' + user_county +', '+ user_zip + ', ' + user_state)
