import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()
model=ChatOpenAI(model="gpt-4")
st.header("Research Assistant")
paper_input=st.selectbox("Select a Research Paper",["attention is all you need","BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding","GPT: Language models are few-shot learners","Cbam: Convolutional block attention module"])
exp_style=st.selectbox("Select Explanation Style",["Code Oriented","Technical","Beginner-Friendly","Mathemetical"])
exp_length=st.selectbox("Select Explanation Length",["Short {1-2 paragraphs}","Medium {3-4 paragraphs}","Long {5-6 paragraphs}"])

prompt_template=load_prompt("D:\\LangChain\Tutorials\\2.Prompts\\PromptTemplate.json")
prompt=prompt_template.invoke(
    {'user_input_paper':paper_input,
    'user_exp_style':exp_style,
    'user_exp_length':exp_length}
)

if st.button("Summerize"):
    result=model.invoke(prompt)
    st.write(result.content)