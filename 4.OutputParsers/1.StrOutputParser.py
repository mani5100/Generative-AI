import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


model = ChatOpenAI()
template1=PromptTemplate(
    template="""Give a detailed description about this topic.
    Topic: {topic}""",
    input_variables=['topic']
)
template2=PromptTemplate(
    template="Summerize this given text into 3 lines.\nText: {text}",
    input_variables=['text']
)
parser=StrOutputParser()
chain=template1|model|parser|template2|model|parser
result=chain.invoke({'topic':'Laravel'})
print(result)