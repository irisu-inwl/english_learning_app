import streamlit as st


def view(problem: dict):
    st.subheader("Problem")
    content = problem["content"]
    st.write(content)

    question = problem["question"]
    st.write(question)

    answer_options = problem["answer_options"]
    st.radio("Answer Options:", range(len(answer_options)), key="reading_answer_index", format_func=lambda x:answer_options[x])
