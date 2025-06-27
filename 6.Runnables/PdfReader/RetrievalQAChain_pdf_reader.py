#Mentos Zindigi
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai.llms import OpenAI
from langchain.chains import RetrievalQA
loader=TextLoader('6.Runnables\\PdfReader\\pdf.txt')
document=loader.load()
splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
splitted_document=splitter.split_documents(document)
vector_store=FAISS.from_documents(splitted_document,OpenAIEmbeddings())
retriever=vector_store.as_retriever()
model=OpenAI(temperature=0.7)
qa_chain=RetrievalQA.from_chain_type(llm=model,retriever=retriever)
query="What is nature of pakistan. Give me one word answer.?"
output=qa_chain.invoke(query)
print(output)