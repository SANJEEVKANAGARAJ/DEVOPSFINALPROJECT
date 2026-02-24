import streamlit as st
import requests

st.title("Student App")

name = st.text_input("Enter student name")

if st.button("Submit"):
    response = requests.get(f"http://localhost:8000/student/{name}")
    st.write(response.json())