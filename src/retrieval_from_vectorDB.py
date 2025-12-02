import os

from utils.logging import logger_func

from src.vector_db_embedding_initializing import create_or_update_chroma_db, CHROMA_DB_PATH
from src.reading_prompt import prompt_reader

# LLM (Groq)
from langchain_groq import ChatGroq

from dotenv import load_dotenv

## Defining the logger
logger = logger_func()

## Loading the environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
base_url = os.getenv("base_url")
cohere_api_key = os.getenv("cohere_api_key")

# -------------------------------------------------------
# RAG Query
# -------------------------------------------------------
def query_rag(question):
    """
    This function takes the user question and gives the relevant response retrieving data from the vector db.

    parameter: user query
    output: retrieved answer of the user query
    """
    """
    Retrieves context and generates LLM answer
    """
    try:
        # Load vectordb without recomputing embeddings. Because we need the vectordb here for the retrieval only
        vectordb = create_or_update_chroma_db(file_path=None, load_only=True)
        
        retriever = vectordb.as_retriever(search_kwargs={"k": 3})
        retreieved_docs = retriever.invoke(question)

        logger.info("*** Relevant document retrieval is completed ***")
            
        context = "\n\n".join([single_data.page_content for single_data in retreieved_docs])

        logger.info("*** context has been generated from the retrieved docs ***")

        ## Starting the LLM action
        logger.info("*** LLM initiation staring and answer generation is in progress... ***")
        llm = ChatGroq(
            api_key=api_key,
            model="openai/gpt-oss-120b",
        )
        my_prompt = prompt_reader(context, question)
        response = llm.invoke(my_prompt)
        answer = response.content

        logger.info("*** Answer is generated and stored into 'answer' variable ***\n\n")
        return answer
    
    except Exception as e:
        logger.error("Error occured in query_rag method")
        print(e) 