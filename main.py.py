import streamlit as st
import pandas as pd

# Portfolio Title and Headers
st.title("Welcome To Data Engineer World")
st.header("Python")
st.subheader("SQL")
st.subheader("Snowflake")
st.subheader("Big Data")
st.subheader("Microsoft Azure")
st.subheader("Pyspark")
st.markdown(
    "As a data engineer, I bring a strong foundation in programming, database management, and ETL processes. "
    "I am eager to apply my technical skills and contribute to building robust data pipelines and solutions."
)

# User Input Section
name = st.text_input("Enter your Name: ")
fname = st.text_input("Enter your Father Name: ")
adr = st.text_area("Enter Your Area:")
age = st.selectbox("Enter Your Age:", [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])
city = st.text_input("Enter your City: ")

# Submit Button
button = st.button("Done")

if button:
    st.markdown(f"""
    **Portfolio Details**
    - **Name:** {name}
    - **Father's Name:** {fname}
    - **Address:** {adr}
    - **Age:** {age}
    - **City:** {city}
    """)
