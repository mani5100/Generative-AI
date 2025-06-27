from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI(model="gpt-4")
chat_history=[SystemMessage(content="Act as an Helpful AI Assistant and you are developed by Abdul Rehman")]
while(True):
    user_ask=input("You: ")
    chat_history.append(HumanMessage(content=user_ask))
    if(user_ask=="exit"):
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AT: '+result.content)
print(chat_history)