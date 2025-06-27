from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
load_dotenv()
parser=JsonOutputParser()
model=OpenAI(model="gpt-3.5-turbo-instruct")
template=PromptTemplate(
    template="""
    Give me age, height and where they started there career of {actor}.
    {instructions}
    """,
    input_variables=['actor'],
    partial_variables={'instructions':parser.get_format_instructions()}
)
# prompt=template.format(actor="Amir Khan")
# chain=prompt|model|parser
chain=template|model|parser
res = chain.invoke({"actor": "Amir Khan"})
print(res)
