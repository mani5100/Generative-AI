from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate

template=ChatPromptTemplate([
    ('system',"You are a customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human'),('{query}')
])
chat_history=[]
with open("Prompts\\messages\\chat_history.txt") as f:
    chat_history.extend(f.readlines())
prompt=template.invoke({
    'chat_history':chat_history,
    'query':"where is my refund"
})
print([prompt])