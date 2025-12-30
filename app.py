import streamlit as st
from agent.conversation import handle_conversation
from config.prompts import SYSTEM_PROMPT

st.set_page_config(page_title="GoodFoods Reservation Agent")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

st.title("🍽️ GoodFoods Reservation Assistant")

for msg in st.session_state.messages:
    if not isinstance(msg, dict):
        continue

    if msg.get("role") == "user":
        st.chat_message("user").write(msg.get("content"))

    elif msg.get("role") == "assistant" and msg.get("content"):
        st.chat_message("assistant").write(msg.get("content"))


user_input = st.chat_input("Book a table, explore restaurants...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    reply = handle_conversation(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
