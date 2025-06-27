from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
url="https://sleeperbuildbody.com/"
loader=WebBaseLoader(url)
docs=loader.load()
template=PromptTemplate(
    template="""On the basis of following text:
    {text}
    answer the following question: {question}
    """,
    input_variables=['text','question']
)
model=ChatOpenAI()
parser=StrOutputParser()
chain=template|model|parser
result=chain.invoke({
    'text':docs[0].page_content,
    'question':"What is this page about"
})
print(result)