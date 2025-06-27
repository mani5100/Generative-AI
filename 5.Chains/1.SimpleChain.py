from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model= ChatOpenAI()
template=PromptTemplate(
    template="Write a note on this topic. \n Topic: {topic}",
    input_variables=['topic']
)
parser=StrOutputParser()
chain=template|model|parser
result=chain.invoke({'topic':'Pakistan'})
print(result)