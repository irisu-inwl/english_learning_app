import streamlit as st


def view(problem: dict):
    st.subheader("Problem")
    
    content = problem["content"]
    st.write(content)

    listening_audio = st.session_state["listening_audio"]
    st.audio(listening_audio, format='audio/mp3')

    question = problem["question"]
    st.write(question)

    answer_options = problem["answer_options"]
    st.radio("Answer Options:", range(len(answer_options)), key="listening_answer_index", format_func=lambda x:answer_options[x])
