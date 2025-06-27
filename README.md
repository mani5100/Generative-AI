# LangChain Tutorials 📚

A curated collection of **hands‑on notebooks and mini‑projects** that demonstrate how to build production‑ready Large Language‑Model (LLM) applications with the [LangChain](https://langchain.com/) framework.

> **Why this repo?** I created these tutorials while deep‑diving into LangChain so that recruiters and future teammates can review the breadth of concepts I am mastering—and the quality standards I follow when writing code.

---

## 🎯 Learning Objectives

| # | Topic | Skills Demonstrated |
|---|-------|--------------------|
| 1 | **Prompt Engineering** | Static & dynamic templates, prompt chaining, best‑practice formatting |
| 2 | **LLM Integration** | OpenAI GPT‑4o, Google Gemini, HuggingFace Inference API |
| 3 | **Embeddings & Similarity Search** | SentenceTransformers, FAISS & Chroma vector stores |
| 4 | **Retrieval‑Augmented Generation (RAG)** | Building RetrievalQA pipelines for PDFs & structured data |
| 5 | **Chains & Runnables** | Sequential / conditional / parallel chains, tool calling agents |
| 6 | **Structured Output** | Pydantic & TypedDict parsers for JSON / tabular responses |
| 7 | **Deployment Hygiene** | Environment‑variable management, lightweight Dockerfile, Makefile targets |

---

## 🗂 Project Layout

```text
LangChain-Tutorials/
├── notebooks/            # Jupyter & Colab notebooks (step‑by‑step walkthroughs)
├── src/                  # Re‑usable Python modules (prompt utils, loaders, chains)
├── data/                 # Sample PDFs / plain‑text docs for RAG examples
├── requirements.txt      # Pinned versions for full reproducibility
├── Dockerfile            # Optional container setup (Python 3.10‑slim)
├── .env.example          # Template for API keys & secrets
└── README.md             # Project documentation (this file)
```

---

## 🚀 Quick Start

```bash
# 1 – Clone the repo
$ git clone https://github.com/mani5100/Generative-AI.git
$ cd Generative-AI

# 2 – Create & activate a virtual environment
$ python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate

# 3 – Install dependencies
$ pip install -r requirements.txt

# 4 – Set your API keys
$ cp .env.example .env
# ↳ paste keys for OpenAI / Gemini / HF_API_TOKEN

# 5 – Run a notebook or execute an example script
$ jupyter lab         # or `python src/example_rag_pipeline.py`
```

---



## 👋 About Me

I’m **Abdul Rehman**, a CS undergrad passionate about applied AI, ML, DL and generative AI. I built this repository as evidence of my practical skills and to land an internship where I can contribute to real‑world generative‑AI products. 

* 💌 Reach me on [LinkedIn](https://www.linkedin.com/in/mani5100/) or via email m.abdulrehman.shoukat@gmail.com
* 🗂 View other experiments in my [Generative‑AI portfolio](https://github.com/mani5100/Generative-AI)

