from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
result = llm.embed_query("What is the capital of India")
print(result)

