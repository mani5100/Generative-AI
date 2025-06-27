from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.llms import OpenAI
from langchain_openai.embeddings import OpenAIEmbeddings

loader=TextLoader('6.Runnables\\PdfReader\\pdf.txt')
document=loader.load()
splitter=RecursiveCharacterTextSplitter()
docs=splitter.split_documents(document)
vector=FAISS.from_documents(docs,OpenAIEmbeddings())
retriever=vector.as_retriever()
query="What is written about babar azam"
retrieved_docs=retriever.get_relevant_documents(query)
print(retrieved_docs)

retrieved_text='\n'.join([doc.page_content for doc in retrieved_docs])
llm=OpenAI(temperature=0.7)
prompt=f"Based on the following text, awnser the question.\n{query}\n{retrieved_text}"
answer=llm.invoke(prompt)
print(answer)