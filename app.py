
import logging

import sys
sys.path.append(r"C:\Users\aresa\OneDrive\Desktop\Gemini AI\env\Lib\site-packages")

import absl.logging

# Set log level before TensorFlow loads
logging.getLogger('absl').setLevel(logging.ERROR)
absl.logging.set_verbosity(absl.logging.ERROR)
import streamlit as st
import google.generativeai as genai


f = open(r"C:\Users\aresa\OneDrive\Desktop\Gemini AI\Gemini AI API KEY.txt")
key = f.read()
genai.configure(api_key=key)
model = genai.GenerativeModel(model_name='gemini-1.5-flash')
chat = model.start_chat(history=[])
st.title("💬 Welcome to the ChatBot")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "ai", "content": "I am your assistant. How can I help you today?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
prompt = st.chat_input("Say Something")
if prompt:
    # Store user message
    st.session_state.messages.append({"role": "Human", "content": prompt})
    st.chat_message("Human").write(prompt)

    # Generate AI response
    res = chat.send_message(prompt)

    # Store AI response
    ai_response = res.text if hasattr(res, "text") else str(res)
    st.session_state.messages.append({"role": "ai", "content": ai_response})
    st.chat_message("ai").write(ai_response)