import streamlit as st
import pandas as pd
import numpy as np

#------App Title and Description------
st.title("My first streamlit app ")
st.write(" This is a simple app to demonstrate the basic functionalities of streamlit.")

#------Interactive Widgets in the Sidebar------
st.sidebar.header("User Input Features")

#------Text Input------
user_name = st.sidebar.text_input("What is your name ?", "Avi ")

#------Slider Input------
age = st.sidebar.slider("Select your age", 0, 100, 25)

#------Selectbox Input------
favorite_color = st.sidebar.selectbox("What is  your favorite color ? ", ["Red", "Green", "Blue", "Yellow"])

#------------Main Page Content----------------
st.header("Welcome , ({user_name}) !")
st.write(f"Your age is {age} and your favorite color is {favorite_color}.")

#------Display a DataFrame------
st.subheader("Here's some random data : ")

# Create a sample DataFrame
data = pd.DataFrame( 
    np.random.randn(10,5),
    columns=('col %d ' % i for i in range(5))
)

st.dataframe(data)

#----------Checkbox to show/hide the content----------
if st.checkbox("Show raw data"):
    st.subheader("Raw")
    st.write("Hello There!")
else:
    st.write("Goodbye")