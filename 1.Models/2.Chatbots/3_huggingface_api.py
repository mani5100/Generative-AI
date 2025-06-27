import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
hf_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
if not hf_token:
    raise ValueError("HUGGINGFACE_ACCESS_TOKEN not found in environment variables!")
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=hf_token 
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of Pakistan?")
print(result.content)