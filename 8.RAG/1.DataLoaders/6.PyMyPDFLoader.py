from langchain_community.document_loaders import PyMuPDFLoader

loader=PyMuPDFLoader("Data\\Pdf\\DiscreteMathematics.pdf")
pages=loader.load()
print(pages[0])