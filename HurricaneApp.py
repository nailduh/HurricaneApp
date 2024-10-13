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
def translate_text(text_list, target_language):
    try:
        translated_text = [
            GoogleTranslator(source='auto', target=target_language).translate(text)
            for text in text_list
        ]
        return translated_text
    except Exception as e:
        st.error(f"Error during translation: {e}")
        return text_list  # Return original text on error

# Array of text to be translated
text_box = [
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
language_pref = st.selectbox("Language Preference", ("English", "Spanish", "Vietnamese", "Portuguese"), index=0)
language_abbr = LANGUAGE_MAP.get(language_pref, 'en')

# Only translate if the language preference has changed
if 'current_language' not in st.session_state or st.session_state.current_language != language_abbr:
    st.session_state.current_language = language_abbr
    st.session_state.translated_text_box = translate_text(text_box, language_abbr)

# Display the translated text
st.write(st.session_state.translated_text_box[0])
st.divider()
st.header(st.session_state.translated_text_box[1])
st.write(st.session_state.translated_text_box[2])

# User input for getting location
user_state = st.text_input(st.session_state.translated_text_box[3])
user_zip = st.text_input(st.session_state.translated_text_box[4])
user_county = st.text_input(st.session_state.translated_text_box[5])
user_street_address = st.text_input(st.session_state.translated_text_box[6])

st.divider()
if all([user_state, user_zip, user_street_address, user_county]):
    st.write(f"Your address is {user_street_address}, {user_county}, {user_zip}, {user_state}")

st.title("Counties Under Boil Notice")

# Use a relative path or a URL for the image
image_path = "/Users/jrsierra/Downloads/floridamap.jpg"  # Update this as necessary
st.image(image_path, caption="Counties Under Boil Notice", use_column_width=True)
