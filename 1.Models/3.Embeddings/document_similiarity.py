from langchain_openai import OpenAIEmbeddings # type: ignore
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
documents=[
    "Babar Azam is widely regarded as one of Pakistan's greatest cricketers, known for his elegant batting style and remarkable consistency across all formats.",
    "Atif Aslam has captivated audiences worldwide with his soulful voice, producing numerous hit songs in Pakistan and Bollywood.",
    "Mahira Khan gained immense popularity through her role in the drama Humsafar, and she later made her Bollywood debut alongside Shah Rukh Khan in Raees.",
    "Abdul Sattar Edhi dedicated his entire life to humanitarian work, establishing the Edhi Foundation, which operates Pakistan's largest ambulance service and countless charitable initiatives.",
    "Wasim Akram is celebrated as one of the greatest fast bowlers in cricket history, playing a crucial role in Pakistan's 1992 World Cup victory with his exceptional swing bowling."
]
query="Who is a bowler"
model=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=300)
documents_embeddings=model.embed_documents(documents)
query_embeddings=model.embed_query(query)
scores=cosine_similarity([query_embeddings],documents_embeddings)[0]
scores=[float(s) for s in scores]
index,similiarity=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print("User: "+query)
print(documents[index])
print("Similiarity: ", similiarity)