import streamlit as st

def init_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def add_user_message(text):
    st.session_state.messages.append(
        {"role": "user", "content": text}
    )

def add_ai_message(text):
    st.session_state.messages.append(
        {"role": "assistant", "content": text}
    )