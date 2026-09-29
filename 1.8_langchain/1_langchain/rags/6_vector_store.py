import time

from langchain_chroma import chroma
from langchain_huggingface import HuggingFaceEmbeddings

# load and split document
start = time.perf_counter()
chunks = load_and_split_folder("docs")

# initialize embegging model
embedding=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# create and persist vector store
vector_store = chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

elapsed = time.perf_counter() - start
print(f"Built and persisted index with {len(chunks)} chunks in {elapsed:.2f} seconds")