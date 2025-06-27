from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings=OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
text="The capital of Pakistan is Islamabad."
res=embeddings.embed_query(text)
print(res)