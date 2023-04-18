import streamlit as st

from views.reading import problem_answer as reading_problem_answer
from views.writing import problem_answer as writing_problem_answer
from views.listening import problem_answer as listening_problem_answer
from usecases.callbacks import (
    callback_problem_answer,
    callback_go_back_generate,
)

def view():
    st.header("Answer Problem")
    # view reading problem
    problem_reading = st.session_state["problem_reading"]
    problem_listening = st.session_state["problem_listening"]
    problem_writing = st.session_state["problem_writing"]

    with st.form(key="answer_form"):
        reading_tab, listening_tab, writing_tab = st.tabs(["Reading", "Listening", "Writing"])
        
        with reading_tab:
            reading_problem_answer.view(problem_reading)

        with listening_tab:
            listening_problem_answer.view(problem_listening)

        with writing_tab:
            writing_problem_answer.view(problem_writing)

        st.form_submit_button("Answer", on_click=callback_problem_answer)
        st.form_submit_button("Go Back", on_click=callback_go_back_generate)