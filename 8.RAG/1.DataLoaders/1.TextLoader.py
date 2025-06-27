from langchain_community.document_loaders import TextLoader
loader=TextLoader("Data\\text\\poem.txt",encoding="utf-8")
docs=loader.load()
print(docs[0].metadata)
print(docs[0].page_content)