import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI(model="gpt-4")
st.header("Research assistant")
user_input=st.text_input("Enter your text")
if st.button('Summerize'):
    result= model.invoke(user_input)
    st.write(result.content)
    