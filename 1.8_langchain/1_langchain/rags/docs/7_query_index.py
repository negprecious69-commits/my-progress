import time

from langchain_chroma import chroma
from langchain_huggingface import HuggingFaceEmbeddings

# load persisted vector store
start = time.perf_counter()
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
reload_time = time.perf_counter() - start

# perform similar search
query_start = time.perf_counter() 
results = vector_store_similarity_search("how much is the seed web dev bootcamp?", k=3)
query_time = time.perf_counter() - query_start

# display results
print(f"Reloaded persisted index in {reload_time:.3f} seconds (no re-embedding of documents)")
print(f"Query took {query_time:.3f} seconds")
for doc in results:
    print(f"- {doc.page_contend[:100]}...")