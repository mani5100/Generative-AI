from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate
load_dotenv()
model=OpenAI(model="gpt-3.5-turbo-instruct")
schema=[
    ResponseSchema(name="name",description="Name of the person"),
    ResponseSchema(name="age",description="Age of the person"),
    ResponseSchema(name="height",description="Height of the person"),
    ResponseSchema(name="nationality",description="Nationality of the person"),
]
parser=StructuredOutputParser.from_response_schemas(schema)
template=PromptTemplate(
    template="Give me name, age and nationalty of {celeb}.\n{instructions}",
    input_variables=['celeb'],
    partial_variables={'instructions':parser.get_format_instructions()}
)
# prompt=template.format(celeb="Aamir Khan")
# print(prompt)
# res=model.invoke(prompt)
# result = parser.parse(res)
# print(result)

chain=template|model|parser
result=chain.invoke({'celeb':'Imran Khan'})
print(result)