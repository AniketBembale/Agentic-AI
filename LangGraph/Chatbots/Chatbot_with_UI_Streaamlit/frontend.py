# import streamlit as st
# from langchain_core.messages import BaseMessage, HumanMessage
# from backend import model,chatbot

# with st.chat_message("User",avatar="🧑"):
#     st.text("Hii")
# with st.chat_message("Assistant",avatar="🤖"):
#     st.text("How  can i help you")


# user_input = st.chat_input("Type here")

# if user_input:
#    with st.chat_message("User"):
#         st.text(user_input)
import streamlit as st
from backend import chatbot
from langchain_core.messages import HumanMessage
import time


st.title("Chatbot")
# st.session_state -> dict -> 
CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user',avatar="🧑"):
        st.text(user_input)

    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)
    
    ai_message = response['messages'][-1].content
    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
    with st.chat_message('assistant',avatar="🤖"):
        placeholder = st.empty()
        typed_text = ""
        for char in ai_message:
            typed_text += char
            placeholder.markdown(typed_text)
            time.sleep(0.01)  # Adjust typing speed here