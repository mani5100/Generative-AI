from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda
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
para_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'words':RunnableLambda(lambda x:len(x.split()))
})
main=RunnableSequence(chain,para_chain)
res=main.invoke({"topic":"Pakistan Cricket Team"})
print(res)