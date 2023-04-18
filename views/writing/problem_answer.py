import streamlit as st


def view(problem: dict):
    st.subheader("Problem")
    content = problem["content"]
    st.write(content)

    question = problem["question"]
    st.write(question)

    st.text_area("Input your answer", key="writing_answer")
    