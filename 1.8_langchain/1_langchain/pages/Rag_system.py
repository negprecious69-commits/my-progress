import os
import tempfile

import streamlit as st
from langchain_community.document_loaders import TextLoader, PyPDFLoader, UnstructuredMarkdownLoader, UnstructuredWordDocumentLoader, WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

st.set_page_config(page_title="RAG Ingestion", page_icon="📄" )
st.title("RAG Ingestion")

@st.cache_resource(show_spinner="Loading embedding model...") # cache_re:Streamlit decoder, loads resource once and reuse
def get_embedding(): # loads and return embedding system
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") # creates embedding model using huggingface,  sentence-transformers: converts text to vectors


def load_uploaded_file(uploaded):
    """Streamlit uploads live in memory, so write to the temp files for the loaders."""
    suffix=os.path.splitext(uploaded.name)[1].lower()
    if suffix not in (".pdf", ".txt", ".docx", ".md", "URL"):
        raise ValueError(f"Unsupported file type: {uploaded.name}")


    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded.getvalue())
        path = tmp.name

    try:
        if suffix == ".pdf":
            docs = PyPDFLoader(path).load()
        elif suffix == ".docx":
            docs =  UnstructuredWordDocumentLoader(path).load()
        elif suffix == ".md":
            docs = UnstructuredMarkdownLoader(path).load()        
        elif suffix == "URL":
            docs = WebBaseLoader      
        else:
            docs = TextLoader(path, encoding="utf-8").load()
    finally:
        os.remove(path)

    for doc in docs:
        doc.metadata["source"] = uploaded.name
    return docs

# sidebar settings
st.sidebar.header("Chunking")
chunk_size = st.sidebar.slider("Chunk size", 200, 2000, 1000, step=100)
chunk_overlap = st.sidebar.slider("Chunk overlap", 0, 500, 100, step=50)

# Upload
files = st.file_uploader(
    "Upload PDF, TXT, Markdown, DOCX files", type=["pdf", "txt", "md", "docx"], accept_multiple_files=True
)

if st.button("Ingest", type="primary", disabled=not files):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    all_chunks=[]

    with st.spinner("Loading the splitter..."):
        for f in files:
            try:
                docs = load_uploaded_file(f)
                all_chunks.extend(splitter.split_documents(docs))
            except Exception as e:
                st.warning(f"Skipped {f.name}: {e}")
    if all_chunks:
        with st.spinner(f"Embedding {len(all_chunks)} chunks..."):
            store = InMemoryVectorStore(get_embedding())
            store.add_documents(all_chunks)
        st.session_state.store = store
        st.session_state.chunks = all_chunks
        st.success(f"Ingested {len(files)} file(s) into {len(all_chunks)} chunks.")

# Results
if "chunks" in st.session_state:
    chunks = st.session_state.chunks
    col1, col2 = st.columns(2)
    col1.metric("chunks", len(chunks))
    col2.metric("Avg chunk length", sum(len(c.page_content) for c in chunks) // len(chunks))

    with st.expander("Preview first 5 chunks"):
        for i, c in enumerate(chunks[:5], 1):
            st.caption(f"chunk {i} | {c.metadata.get('source')} | {c.metadata.get("page", "-")}")
            st.text(c.page_content) 

    st.subheader("Test retrieval")
    query = st.text_input("Ask somrthing about your documents")
    if query:
        results = st.session_state.store.similarity_search(query, k=3)
        for r in results:
            st.caption(f"{r.metadata.get("source")} | page {r.metadata.get('page', '-')}")
            st.write(r.page_content)                 
            st.divider()                  

