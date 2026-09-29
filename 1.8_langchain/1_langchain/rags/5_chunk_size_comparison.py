from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

docs = PyPDFLoader("docs/docs.pdf").load()
embeddings=HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")
query="what is mindset?"

for chunk_size in [300, 800, 1500]:
    # calculate the overlap size
    overlap=int(chunk_size*0.15)
    splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    chunks=splitter.split_documents(docs)
    # avg_length=sum(len(c.page_content) for c in chunks))
    len_content=[len(c.page_content) for c in chunks]
    print(f"Length for {chunk_size} is {len(len_content)}")
    average_lenght=sum(len_content)/len(len_content)
    print(f"Average length of chunks for chunk_size={chunk_size} is {average_lenght:.2f}")
    store=InMemoryVectorStore(embeddings)
    store.add_documents(chunks)

    top_results=store.similarity_search(query, k=1)[0]
    print(f"\n===Chunk size {chunk_size} (overlap {overlap})===")
    print(f"Total chunks: {len(chunks)}")
    print(f"Average length of chunks: {average_lenght:.0f} characters")
    print(f"Top match for: '{query}:\n {top_results.page_content[:200]}...")# summarize the content of the top match