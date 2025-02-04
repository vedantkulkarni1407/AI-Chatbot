import google.generativeai as genai
import streamlit as st

# Configure API key (Use your own generated api key)
genai.configure(api_key="AIzaSyDYB8KOlgtmZidCh3Nb0d6hDT2IZ-1L1O8")

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

# Streamlit UI
st.title("🤖 Vedant's Chatbot")
st.write("Chat with Google Gemini AI")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Get AI response
    response = model.generate_content(user_input)
    reply = response.text

    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
