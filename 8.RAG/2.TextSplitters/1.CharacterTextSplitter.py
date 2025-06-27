from langchain.text_splitter import CharacterTextSplitter
text="""The evolution of artificial intelligence has led to transformative applications across industries, from healthcare diagnostics to autonomous vehicles. Among the most groundbreaking developments is the integration of real-time data analysis with adaptive learning models, enabling systems to respond dynamically to complex environments. For instance, reinforcement learning, when coupled with human feedback, allows machines to refine their actions based on contextual relevance rather than static programming. Additionally, edge computing through devices like Raspberry Pi enhances system responsiveness by reducing latency and reliance on centralized servers. These innovations not only improve efficiency but also open up ethical considerations regarding autonomy, accountability, and the future of human-machine collaboration."""

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator=""
)
data=splitter.split_text(text)
print(data)