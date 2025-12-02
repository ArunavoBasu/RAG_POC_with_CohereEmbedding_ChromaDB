from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from utils.logging import logger_func

## Defining the logger
logger = logger_func()

# -------------------------------------------------------
# Chunk the document
# -------------------------------------------------------
def chunk_text(text):
    """
    This function returns the chunks of the input text

    parameter: text extracted from the input document
    output: chunked texts
    """
    try:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = 5000,
            chunk_overlap = 200
        )
        chunks = splitter.split_text(text)
        logger.info("*** Text splitting done by RecursiveCharacterTextSplitter ***")

        docs = [Document(page_content=single_chunks) for single_chunks in chunks]  ## Chroma requires a list of Document objects
        
        logger.info("*** docs has been created from the splitted texts ***")
        return docs

    except Exception as e:
        print(e)
        logger.error("*** error in chunk_text method ***")
