from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableParallel,RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
tweet=PromptTemplate(
    template="Tell me a twitter's tweet about {topic}",
    input_variables=['topic']
)
post=PromptTemplate(
    template="Tell me a linkedIn post about {topic}",
    input_variables=['topic']
)
model=ChatOpenAI()
parser=StrOutputParser()
chian=RunnableParallel({
    'tweet':RunnableSequence(tweet,model,parser),
    'post':RunnableSequence(post,model,parser)
})
res=chian.invoke({'topic': "Transformers"})
print(res)