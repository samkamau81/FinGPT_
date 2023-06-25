#api accessible to the server
import os
#Framework supporting MLOps Apps
import streamlit as st 
#Large Language Model Library
from langchain.llms import OpenAI

#api keys
api_key = "sk-xxxxxxxxxxxxxxxxxxx"
os.environ['OPENAI_API_KEY'] = api_key

# Llms
llm = OpenAI(temperature=0.9) 

# App framework
st.title('💸 MoneyMentor')

st.markdown("-------")
st.markdown("<h2 style='text-align:center;'> Want to Advice on any Business Problem </h2>",unsafe_allow_html=True)
form = st.form(key="my_form", clear_on_submit=True)
que=form.text_input("Enter Question") 
b1=form.form_submit_button('Answer')

if b1:
    answ=llm(que)
    st.write(answ)

st.markdown("-------")
