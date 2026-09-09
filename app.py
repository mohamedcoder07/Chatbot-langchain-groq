import streamlit as st

from chatbot import ask_llm


st.set_page_config(
    page_title="Chatbot Llama",
    page_icon="🤖"
)

st.title("🤖 Chatbot Llama")

question = st.text_input(
    "Posez votre question :"
)

if st.button("Envoyer"):
    if question.strip():
        with st.spinner("Le modèle réfléchit..."):
            answer = ask_llm(question)

        st.write(answer)
    else:
        st.warning("Veuillez entrer une question.")