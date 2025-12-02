import streamlit as st
import tempfile

from src.retrieval_from_vectorDB import query_rag
from src.vector_db_embedding_initializing import create_or_update_chroma_db
from src.document_loader import load_document
from src.chunking_document import chunk_text

st.title("📘 RAG Chatbot (PDF / DOCX / TXT Upload)")
st.write("Upload your files → embeddings stored once → ask questions anytime.")

# Initialize session state
if "db_ready" not in st.session_state:
    st.session_state.db_ready = False

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    st.info("Checking for embeddings...")

    vectordb = create_or_update_chroma_db(file_path=file_path, load_only=False)
    
    st.session_state.db_ready = True

    st.success("Embeddings stored successfully!")

st.subheader("Ask a question")
query = st.text_input("Enter your question")

if st.button("Ask"):
    if not st.session_state.db_ready:
        st.error("Please upload a document first.")
    elif query.strip() == "":
        st.error("Please enter a question.")
    else:
        if query:
            st.info("Generating the answer.....")
            answer = query_rag(query)
            st.write("### Answer:")
            st.write(answer)
