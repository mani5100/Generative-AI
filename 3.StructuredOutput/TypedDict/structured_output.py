from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Annotated,Optional,TypedDict,Literal

model=ChatOpenAI(model="gpt-4")
class Review(TypedDict):
    key_theme:Annotated[list[str],"Write down all the key theme of the review."]
    summary:Annotated[str,"Give me brief description of the review."]
    sentiment:Annotated[Literal['pos','neg'],"For positive give pos and for negative give neg."]
    pros:Annotated[Optional[list[str]],"Write down the pros in the list."]
    cons:Annotated[Optional[list[str]],"Write down the cons in the list."]
    name: Annotated[Optional[str], "Extract the reviewer's name **only if explicitly mentioned as a person’s name**. If no person's name is given, return `None`. **Do not infer a name from the product title or review heading.**"]
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