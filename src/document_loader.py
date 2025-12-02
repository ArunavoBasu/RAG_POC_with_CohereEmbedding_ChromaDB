import os

from utils.logging import logger_func

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
)

## importing the logger
logger = logger_func()

# -------------------------------------------------------
# Load any document (PDF / DOCX / TXT)
# -------------------------------------------------------
def load_document(file_path):
    try:
        extention = os.path.splitext(file_path)[1].lower()

        logger.info("*** Extention detected for the input file ***")

        if extention == ".pdf":
            loader = PyPDFLoader(file_path)
        elif extention == ".docx":
            loader = Docx2txtLoader(file_path)
        elif extention == ".txt":
            loader = TextLoader(file_path)
        else:
            raise ValueError("Unsupported file type. Use PDF, DOCX, or TXT.")

        pages = loader.load()
        text = "\n".join([p.page_content for p in pages])
        print(f"[INFO] Loaded file with {len(text)} characters")

        logger.info("*** Text extraction completed from the input document ***")
        return text
    
    except Exception as e:
        print(e)
        logger.error("*** Error in load_document method ***")