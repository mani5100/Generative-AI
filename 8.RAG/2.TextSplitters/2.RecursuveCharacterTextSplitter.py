from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load PDF
loader = PyPDFLoader('Data/Pdf/DiscreteMathematics.pdf')
docs = list(loader.lazy_load())

# Split text into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
text_chunks = splitter.split_documents(docs)

# Output info
print(f"Total chunks: {len(text_chunks)}")
print(text_chunks[0].page_content)
