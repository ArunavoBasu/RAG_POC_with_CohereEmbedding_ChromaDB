from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
base_url = os.getenv("base_url")

llm = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model="openai/gpt-oss-120b"
)

# ---- Run ----
response = llm.invoke("What is RAG?")
print(response.content)
