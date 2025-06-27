from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from typing import Literal
from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from langchain.schema.runnable import RunnableBranch,RunnableLambda
load_dotenv()
model=ChatOpenAI()

class Feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description="This is sentiment of feedback.")
    
    
pydantic_parser=PydanticOutputParser(pydantic_object=Feedback)


classification_template=PromptTemplate(
    template="""Identify the sentiment of feedback given below.
    Feedback: {feedback}
    {instructions}
    """,
    input_variables=['feedback'],
    partial_variables={'instructions':pydantic_parser.get_format_instructions()}
)
classification_chain=classification_template|model|pydantic_parser
# print(template.format(feedback="You are bad"))
str_parser=StrOutputParser()

positive_template=PromptTemplate(
    template="Give the appropriate answer of this positive feedback.\nFeedback:{feedback}",
    input_variables=['feedback']
)
negative_template=PromptTemplate(
    template="Give the appropriate answer of this negative feedback.\nFeedback:{feedback}",
    input_variables=['feedback']
)
branch_chain=RunnableBranch(
    (lambda x:x.sentiment=="positive",positive_template|model|str_parser),
    (lambda x:x.sentiment=="negative",negative_template|model|str_parser),
    RunnableLambda(lambda x:"No feedback found")
)
main_chain=classification_chain|branch_chain
feedback="""The product did not meet my expectations. The quality feels subpar, and it doesn’t function as advertised. I encountered several issues, including poor durability and an overall lack of reliability. Additionally, customer support was unhelpful when I reached out for assistance. I would not recommend this product unless significant improvements are made."""

result=main_chain.invoke({'feedback':feedback})
print(result)