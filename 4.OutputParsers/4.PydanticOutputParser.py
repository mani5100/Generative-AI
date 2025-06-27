from langchain_openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()
model=OpenAI()
class person(BaseModel):
    name:str=Field(description="Name of Person")
    age:int=Field(description="Age of Person",gt=18)
    city:str=Field(description="City of Person where he belongs")
parser=PydanticOutputParser(pydantic_object=person)
template=PromptTemplate(
    template="Give me name, age and city of {celeb}.\n{instructions}",
    input_variables=['celeb'],
    partial_variables={'instructions':parser.get_format_instructions()}
)
chain=template|model|parser
result=chain.invoke({'celeb':'Imran Khan'})
print(result)