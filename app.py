import streamlit as st

# Title and text
st.title("My First Streamlit App")
st.header("Welcome to Streamlit")
st.write("This is a basic Streamlit web app.")

# Input
name = st.text_input("Enter your name:")

# Button and output
if st.button("Greet"):
    st.success(f"Hello, {name}! Welcome to Streamlit.")
