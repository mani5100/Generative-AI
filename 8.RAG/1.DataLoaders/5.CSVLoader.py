from langchain_community.document_loaders import CSVLoader
loader=CSVLoader(file_path="Data\csv\iris.csv")
docs=loader.load()
res=docs[0].page_content
meta=docs[0].metadata
print(res)
print(meta)