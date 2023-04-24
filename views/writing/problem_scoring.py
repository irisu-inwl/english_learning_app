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
    system_feedback = st.session_state["system_feedback"]
    corrected_answer = st.session_state["system_corrected"]
    st.write(f"Score: {system_score}")
    st.write(f"Feedback: {system_feedback}")
    st.write(f"Corrected Answer: {corrected_answer}")

    st.subheader("Answer Example")
    st.write(answer_example)

    st.subheader("Commentary")
    st.write(commentary)
    