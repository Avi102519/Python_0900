import streamlit as st

st.title("My Application")
st.write("This app calculates the square of a number!")
st.header("Select a Number")
number = st.slider("pick a number",0,100,5)
st.subheader("Result")
squared_number = number ** 2
st.write(f"The square of {number} is {squared_number}")