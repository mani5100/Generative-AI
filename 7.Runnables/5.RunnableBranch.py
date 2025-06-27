from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda, RunnableBranch
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI()
parser=StrOutputParser()
template=PromptTemplate(
    template="Write a note on {topic}",
    input_variables=['topic']
)
template2=PromptTemplate(
    template="Summerize this text in one para: {text}",
    input_variables=['text']
)
chian=template|model|parser
con_chain=RunnableBranch(
    (lambda x: len(x.split())>200,template2|model|parser),
    RunnablePassthrough()
)
main_chain=chian|con_chain
res=main_chain.invoke({"topic":"pakistan Forign Policy"})
print(res)