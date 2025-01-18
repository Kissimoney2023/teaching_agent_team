import streamlit as st

st.title("Hello Streamlit!")
st.write("This is a test app.")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")
