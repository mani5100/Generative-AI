from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv
load_dotenv()
openai_model= ChatOpenAI()
google_model=ChatGoogleGenerativeAI(model="gemini-1.5-pro")
parser=StrOutputParser()
template_notes=PromptTemplate(
    template="""
    Generate notes from the given text. 
    Text: 
    {text}
    """,
    input_variables=['text']
)
template_quiz=PromptTemplate(
    template="""
    Generate 5 MCQs from the given text. Each msqs have the 4 options from which nly one is correct. and by the end of each question there should be the crrect answer of it. 
    Text: 
    {text}
    """,
    input_variables=['text']
)
parallel_chains=RunnableParallel({
    'notes':template_notes|openai_model|parser,
    'quiz':template_quiz|google_model|parser
})

template_merge=PromptTemplate(
    template="""
    I am going to give you notes and MSQs. You have to merge it.
    Notes: {notes}
    Quiz: {quiz}
    """,
    input_variables=['notes','quiz']
)
merge_chain=template_merge|openai_model|parser
chain=parallel_chains|merge_chain
text="""
Deep learning is a subset of machine learning that utilizes artificial neural networks to model and solve complex problems. Inspired by the structure and function of the human brain, deep learning algorithms consist of multiple layers of interconnected nodes, or neurons, that process data hierarchically. Each layer extracts higher-level features from the input, allowing the model to recognize patterns, classify data, and make predictions. The most common architecture used in deep learning is the deep neural network (DNN), which includes variations like convolutional neural networks (CNNs) for image processing and recurrent neural networks (RNNs) for sequential data. Training deep learning models requires vast amounts of data and computational power, as they rely on backpropagation and gradient descent optimization to adjust weights and minimize errors over multiple iterations.

One of the key advantages of deep learning is its ability to automatically learn feature representations from raw data without the need for explicit feature engineering. This has led to significant breakthroughs in various fields, including computer vision, natural language processing (NLP), and speech recognition. For example, deep learning models power applications like facial recognition, autonomous vehicles, medical diagnosis, and AI-driven chatbots. However, the success of deep learning models depends on factors such as the availability of labeled datasets, computational resources like GPUs and TPUs, and the choice of hyperparameters like learning rate, batch size, and activation functions. Transfer learning and pre-trained models, such as OpenAI's GPT and Google's BERT, have further accelerated progress by enabling models to leverage knowledge from previously trained networks.

Despite its impressive achievements, deep learning also presents challenges and limitations. Training deep networks is computationally expensive and often requires specialized hardware, making it inaccessible to smaller organizations. Additionally, deep learning models are sometimes seen as "black boxes" because of their lack of interpretability, meaning it is difficult to understand why they make certain decisions. This can raise ethical concerns, particularly in high-stakes domains like healthcare and finance. Overfitting is another issue, where models perform well on training data but fail to generalize to new, unseen examples. Researchers are actively exploring solutions such as explainable AI (XAI), regularization techniques, and more efficient neural network architectures to address these challenges. As deep learning continues to evolve, it is expected to drive further advancements in artificial intelligence and redefine industries through its capabilities.
"""

result=chain.invoke({'text':text})
print(result)

chain.get_graph().print_ascii()