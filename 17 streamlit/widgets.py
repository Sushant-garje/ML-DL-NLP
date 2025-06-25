import streamlit as st
import pandas as pd

st.title("Streamlit text input")

age = st.slider("select your Age", 0, 100,25)
name = st.text_input("Enter your name")

options=['C',"Java","C#","Python","Ruby"]
choice = st.selectbox("Choose your Favorite language",options)
st.write("you  Selected"+choice)

if name:
    st.write("hello "+ name)


data = {
    "name":["sushant","rahul","ayush","junaid","varad"],
    "age":[20,19,20,22,20],
    "city":["pune","sangli","nager","pandharput","sambhajinagar"]
}

df = pd.DataFrame(data)
df.to_html("sample.csv")
st.write(df)

uploaded_file = st.file_uploader("Upload your file",type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)