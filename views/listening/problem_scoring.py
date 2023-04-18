import streamlit as st


def view(problem: dict):
    answer_index = st.session_state["listening_answer_index"]

    st.subheader("Problem")
    listening_audio = st.session_state["listening_audio"]
    st.audio(listening_audio, format='audio/mp3')
    content = problem["content"]
    st.write(content)

    question = problem["question"]
    st.write(question)

    answer_options = problem["answer_options"]
    st.radio("Answer Options:", answer_options, index=answer_index, disabled=True)

    correct_answer = problem["correct"]
    commentary = problem["commentary"]
    st.write(f"Correct Answer: **{answer_options[correct_answer]}**")
    correct_incorrect = "Correct" if correct_answer == answer_index else "Incorrect"
    st.write(f"Correct/Incorrect: **{correct_incorrect}**")

    st.subheader("Commentary")
    st.write(commentary)
    