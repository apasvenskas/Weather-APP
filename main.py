import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days - st.slider("Forcast Days", min_value = 1, max_value=5)