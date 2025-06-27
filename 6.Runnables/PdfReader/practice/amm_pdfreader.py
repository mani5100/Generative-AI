from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai.llms import OpenAI
loader=TextLoader('6.Runnables\\PdfReader\\pdf.txt')
document=loader.load()
splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
splitted_document=splitter.split_documents(document)
vector_store=FAISS.from_documents(splitted_document,OpenAIEmbeddings())
retriever=vector_store.as_retriever()
query="What is nature of pakistan. Give me one word answer.?"
retrieved_docs=retriever.invoke(query)
retrieved_text="\n".join([docs.page_content for docs in retrieved_docs])
prompt=f"Based on this text \n Text: {retrieved_text} \n Give the answer of this Query.\n Query: {query}\n Note: Use only the knowledge that is given in upper Text"
model=OpenAI(temperature=0.7)
output=model.invoke(prompt)
print(output)