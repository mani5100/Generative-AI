from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableParallel,RunnableSequence,RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

template=PromptTemplate(
    template="Tell me a joke about {topic}",
    input_variables=['topic']
)
template2=PromptTemplate(
    template="Tell me explaination of joke: {joke}",
    input_variables=['joke']
)
model=ChatOpenAI()
parser=StrOutputParser()
chain=RunnableSequence(template,model,parser)
chain_parallel=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explaination':RunnableSequence(template2,model,parser)
})
main_chain=RunnableSequence(chain,chain_parallel)
res=main_chain.invoke({"topic":"Pakistan Cricket Team"})
print(res)