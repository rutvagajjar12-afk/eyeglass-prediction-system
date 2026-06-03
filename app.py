
import streamlit as st

st.title("👓 Eyeglass Number Prediction System")

age = st.number_input("Enter Age")

if st.button("Predict"):
    st.success("Prediction Complete")
