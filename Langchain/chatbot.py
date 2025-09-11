from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (AIMessage, BaseMessage, ChatMessage, FunctionMessage, HumanMessage, SystemMessage)
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv


load_dotenv()

# model = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
#     # other params...
# )
model = ChatOpenAI(model = "gpt-3.5-turbo", temperature=0)

chat_history = [
    SystemMessage(content="You are a helpful assistant ")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print("AI Message: ",result.content)
print("Chat Ended")
print(chat_history)
    