import os

from langchain_community.vectorstores import Chroma
from langchain_cohere import CohereEmbeddings

from dotenv import load_dotenv
from utils.logging import logger_func

from src.document_loader import load_document
from src.chunking_document import chunk_text

load_dotenv()
cohere_api_key = os.getenv("cohere_api_key")

os.makedirs("DB_folder", exist_ok=True)
CHROMA_DB_PATH = "DB_folder/others_chroma_store"

logger = logger_func()

def create_or_update_chroma_db(file_path, load_only):
    """
    If load_only=True → load DB only (no embedding compute)
    If file_path is provided and load_only = False → load file, chunk, embed, update DB
    """
    try:
        embedder = CohereEmbeddings(model="embed-english-v3.0")

        # If ONLY loading existing DB (query mode)
        if load_only == True and file_path == None:
            vectordb = Chroma(
                persist_directory=CHROMA_DB_PATH,
                embedding_function=embedder
            )
            logger.info("*** Embedding creation completed and vectordb has been returned ***")
            return vectordb

        # Normal flow for file upload
        else:
            # Extract and chunk
            text = load_document(file_path)
            docs = chunk_text(text)

            vectordb = Chroma(
                persist_directory=CHROMA_DB_PATH,
                embedding_function=embedder
            )
            vectordb.add_documents(docs)
            logger.info("*** Embedding creation completed and vectordb has been returned ***")
            return vectordb

    except Exception as e:
        logger.error("Error occured in create_or_update_chroma_db method")
        print(e)

