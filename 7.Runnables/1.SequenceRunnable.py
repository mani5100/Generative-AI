from langchain.schema.runnable import RunnableSequence
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

template=PromptTemplate(
    template="Tell me a joke about {topic}",
    input_variables=['topic']
)
model=ChatOpenAI()
parser=StrOutputParser()
chain=RunnableSequence(template,model,parser)
res=chain.invoke({'topic':"Pakitan Cricket"})
print(res)