from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("Data\\Pdf\\DiscreteMathematics.pdf")
docs=loader.lazy_load()
for doc in docs:
    print(doc.metadata)