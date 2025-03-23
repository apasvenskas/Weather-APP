import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value = 1, max_value=5, help = "Select the number of forcasted days")

option = st.selectbox("Select data to view.", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
temperature = [10, 11, 15]
temperature = [days * i for i in temperature]

figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y":"Temperature (C)"})
st.plotly_chart(figure)