from langchain_experimental.text_splitter import SemanticChunker
from dotenv import load_dotenv
from langchain_openai.embeddings import OpenAIEmbeddings
load_dotenv()
model=OpenAIEmbeddings()
text="""The evolution of artificial intelligence has led to transformative applications across industries, from healthcare diagnostics to autonomous vehicles. Among the most groundbreaking developments is the integration of real-time data analysis with adaptive learning models, enabling systems to respond dynamically to complex environments. For instance, reinforcement learning, when coupled with human feedback, allows machines to refine their actions based on contextual relevance rather than static programming. Additionally, edge computing through devices like Raspberry Pi enhances system responsiveness by reducing latency and reliance on centralized servers. These innovations not only improve efficiency but also open up ethical considerations regarding autonomy, accountability, and the future of human-machine collaboration."""
splitter=SemanticChunker(model,breakpoint_threshold_type="standard_deviation",breakpoint_threshold_amount=1)
data=splitter.split_text(text)
print(data)