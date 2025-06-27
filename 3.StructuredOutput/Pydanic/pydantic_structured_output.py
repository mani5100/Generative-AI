from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Annotated,Optional,TypedDict,Literal
from pydantic import BaseModel,Field
load_dotenv()
model=ChatOpenAI(model="gpt-4o")
class Review(BaseModel):
    key_theme:list[str]=Field(description="Write down all the key theme of the review.")
    summary:str=Field(description="Give me brief description of the review.")
    sentiment:Literal['pos','neg']=Field(description="For positive give pos and for negative give neg.")
    pros:Optional[list[str]]=Field(description="Write down the pros in the list.",default=None)
    cons:Optional[list[str]]=Field(description="Write down the cons in the list.",default=None)
    name:Optional[str]=Field(default=None,description="Extract the reviewer's name **only if explicitly mentioned as a person’s name**. If no person's name is given, return `None`. **Do not infer a name from the product title or review heading.**")
structured_model=model.with_structured_output(Review)
result=structured_model.invoke("""
                        Product Review: XYZ Wireless Headphones
⭐ Rating: 4.5/5


"I recently bought the XYZ Wireless Headphones, and I must say, they exceeded my expectations! The sound quality is crisp and immersive, with deep bass and clear treble. The battery life is amazing—I can go nearly two days without recharging.

The noise cancellation is decent, but it could be better in very noisy environments. The ear cushions are super comfortable, making long listening sessions a breeze. Bluetooth connectivity is seamless, with no noticeable lag or dropouts.

The only downside? The touch controls can be a bit too sensitive, leading to accidental pauses or skips. But overall, for the price, these are an excellent choice for music lovers and casual listeners alike! Highly recommend!"

✅ Pros:
✔️ Excellent sound quality
✔️ Long battery life
✔️ Comfortable for extended use
✔️ Strong Bluetooth connectivity

❌ Cons:
❌ Noise cancellation could be better
❌ Sensitive touch controls""")


print(result)