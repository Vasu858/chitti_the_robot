import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key=os.getenv("OPENAI")

client = OpenAI(api_key=api_key)
st.title("Human Resource chatbot")

if "messages" not in  st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

input_text=st.chat_input("Ask me anything about human resources")
if input_text:
    st.session_state.messages.append({
        "role": "user",
        "content": input_text
    })
    with st.chat_message("user"):
        st.write(input_text)
   
    response= client.responses.create(
        model="gpt-4.1",
        instructions = "You are a helpful and friendly HR chatbot. Answer only questions related to Human Resources. If the user asks an unrelated question, politely explain that you can help only with HR-related topics and encourage them to ask an HR question.",
        input = st.session_state.messages,
        temperature = 0.5
    )
    st.session_state.messages.append({"role": "assistant",
    "content": response.output_text})
    with st.chat_message("assistant"):
        st.write(response.output_text)   
        
