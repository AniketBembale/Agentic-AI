from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from langchain_community.document_loaders import TextLoader


load_dotenv()




embedding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
loader = TextLoader("doc.txt")
docs = loader.load()   
documents = [
    "Virat Kohli is an Indian cricketer and former captain of the India national team. He is widely regarded as one of the best batsmen in the world and has numerous records to his name.",
    "Kohli made his debut for India in 2008 and quickly established himself as a key player in the team. He is known for his aggressive batting style, consistency, and ability to chase down targets.",
    "Under his captaincy, India achieved significant success, including a historic Test series win against Australia in Australia in 2018-2019.",
    "Kohli has received several awards and accolades throughout his career, including the Sir Garfield Sobers Trophy for ICC Cricketer of the Year multiple times.",
    "He is also known for his fitness and dedication to the sport, often setting high standards for his teammates.",
    "Off the field, Kohli is involved in various philanthropic activities and has a significant following on social media.",
    "In 2021, Kohli stepped down as the captain of the T20I format, focusing more on his batting and contributing to the team in other ways.",
    "Kohli continues to be a vital part of the Indian cricket team and is expected to play a crucial role in upcoming tournaments and series.",
    "rohit sharma is the current captain of the indian cricket team in t20 format",
    "sachin tendulkar is a former indian cricketer and one of the greatest batsmen in the history of cricket",
    "m.s dhoni is a former captain of the indian cricket team and is known for his calm demeanor and finishing abilities",
    "rahul dravid is a former indian cricketer and captain, known for his solid technique and reliability as a batsman",
    "anil kumble is a former indian cricketer and captain, known for his leg-spin bowling and leadership skills",
    "jasprit bumrah is a current indian cricketer and one of the best fast bowlers in the world",
    "hardik pandya is a current indian cricketer known for his all-round abilities and explosive batting",
    "ravindra jadeja is a current indian cricketer known for his all-round abilities and exceptional fielding",
    "yuzvendra chahal is a current indian cricketer and one of the best leg-spinners in the world",]
# print(docs)   
query = "tell me about virat kohli"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
# most_similar_doc_index = np.argmax(similarities)
index,score = sorted(list(enumerate(similarities)),key=lambda x:x[1])[-1]
print(documents[index])
print(f"similarity score: {score}")