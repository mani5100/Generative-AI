from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI(model="gpt-4")
query=input("Enter your Query")
result = model.invoke(query)
print(result.content)

# same as anthropic 
# from langchain_anthropic import ChatAnthropic 
# model=ChatAnthropic(model="claude-3-5-sonnet-20241022")