from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (AIMessage, BaseMessage, ChatMessage, FunctionMessage, HumanMessage, SystemMessage)
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt


from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

st.header("Research Tool Chatbot")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')





if st.button("Submit"):
    chain = template | model

    result = chain.invoke({'paper_input': paper_input, 
                          'style_input': style_input, 
                          'length_input': length_input})
    st.write(result.content)