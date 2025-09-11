from langchain_core.messages import (AIMessage, BaseMessage, ChatMessage, FunctionMessage, HumanMessage, SystemMessage)
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)
messages = [
    SystemMessage(content="You are a helpful assistant "),
    HumanMessage(content="Tell me about Astronomy")]
result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)
