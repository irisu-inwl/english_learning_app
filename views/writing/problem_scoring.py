import streamlit as st


def view(problem: dict):
    st.subheader("Problem")
    content = problem["content"]
    st.write(content)

    question = problem["question"]
    st.write(question)

    answer_example = problem["answer_example"]
    answer = st.session_state["writing_answer"]
    commentary = problem["commentary"]
    st.text_area("Your answer", value=answer, disabled=True)

    st.subheader("System Scoring")
    system_score = st.session_state["system_score"]
    system_comments = st.session_state["system_comments"]
    st.write(f"Score: {system_score}")
    st.write(f"Comment: {system_comments}")

    st.subheader("Answer Example")
    st.write(answer_example)

    st.subheader("Commentary")
    st.write(commentary)
    