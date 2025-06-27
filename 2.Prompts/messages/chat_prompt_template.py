from langchain_core.prompts import ChatPromptTemplate

promptTemplate=ChatPromptTemplate([
    ('system',"You have to act as {domain} expert"),
    ('human','toy have to explain {topic} in simple and organized way.')
])

prompt=promptTemplate.invoke({
    "domain":"SEO",
    "topic":"Niche Research"
})

print(prompt)