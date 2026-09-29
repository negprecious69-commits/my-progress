from langchain_community.document_loaders import   PyPDFLoader, TextLoader
#from streamlit import pdf
pdf_loader = PyPDFLoader("docs/Artificial_intelligence.pdf")
pdf_docs = pdf_loader.load()
# one document per page, with page number in metadata

# text_laoder = TextLoader("module_note.txt")
# text_docs = text_loader.load()
print(f"Loaded {len(pdf_docs)} pages from the PDF")
print(pdf_docs[0].metadata)
print(f"printing the pdf doc: {pdf_docs}")