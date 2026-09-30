import streamlit as st
import ollama
st.set_page_config(page_title="AI Assistant")
st.markdown("""
<style>
.stApp {
    background: #f7f3ed;
}
.block-container {
    max-width: 900px;
    padding-top: 55px;
}
h1 {
    text-align: center;
    color: #29251f;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}
.subtitle {
    text-align: center;
    color: #8b8175;
    font-size: 14px;
    margin-bottom: 40px;
}
[data-testid="stChatMessage"] {
    background: transparent;
    border: none;
    padding: 10px 5px;
    margin: 8px 0;
}
[data-testid="stChatMessageContent"] {
    color: #3b362f;
    font-size: 15px;
    line-height: 1.7;
}
[data-testid="stChatInput"] {
    background: #fffdf9;
    border: 1px solid #d8d0c5;
    border-radius: 22px;
    box-shadow: 0 5px 20px rgba(70,60,50,0.08);
}
[data-testid="stChatInput"]:focus-within {
    border-color: #a69a8c;
    box-shadow: 0 5px 25px rgba(70,60,50,0.12);
}
[data-testid="stChatInput"] textarea {
    color: #3b362f;
    font-size: 15px;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: #aaa095;
}
.footer {
    text-align: center;
    color: #aaa095;
    font-size: 11px;
    margin-top: 25px;
}
</style>
""", unsafe_allow_html=True)

st.title("AI Assistant")
st.markdown('<div class="subtitle">A simple and intelligent conversational assistant</div>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Message AI Assistant...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    response = ollama.chat(model="llama3.2", messages=st.session_state.messages)
    bot_response = response["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.write(bot_response)

st.markdown('<div class="footer">Powered by Ollama</div>', unsafe_allow_html=True)