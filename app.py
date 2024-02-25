import streamlit as st
from langchain.llms import OpenAI

OPENAI_API_KEY = "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"

llm = OpenAI(openai_api_key=OPENAI_API_KEY)

st.title("ChatGPT Clone")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.chat_message("assistant"):
    st.write("Hello 👋")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Enter your message")

if(prompt):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = llm.predict(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
