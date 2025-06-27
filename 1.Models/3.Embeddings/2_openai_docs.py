from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings=OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
text=[
    "My name is AbdulRehman",
    "I live in Sargodha",
    "Sargodha is the most beautifull place and it is famous for its oranges"
]
res=embeddings.embed_documents(text)
print(res)