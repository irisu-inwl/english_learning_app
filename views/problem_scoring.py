import streamlit as st

from views.reading import problem_scoring as reading_problem_scoring
from views.writing import problem_scoring as writing_problem_scoring
from usecases.callbacks import (
    callback_go_back_generate,
)


def view():
    st.header("Scoring")
    problem_reading = st.session_state["problem_reading"]
    problem_listening = st.session_state["problem_listening"]
    problem_writing = st.session_state["problem_writing"]

    reading_tab, listening_tab, writing_tab = st.tabs(["Reading", "Listening", "Writing"])
    with reading_tab:
        reading_problem_scoring.view(problem_reading)

    with listening_tab:
        st.write("wip")

    with writing_tab:
        writing_problem_scoring.view(problem_writing)
    
    with st.form(key="score"):
        st.form_submit_button("Go Back", on_click=callback_go_back_generate)