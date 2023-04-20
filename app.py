import os

import streamlit as st

from views import (
    problem_setting,
    problem_answer,
    problem_scoring,
)


def initialize():
    st.session_state["current_cefr_level"] = "A1"
    st.session_state["objective_cefr_level"] = "A1"
    st.session_state["problem_reading"] = None
    st.session_state["problem_listening"] = None
    st.session_state["problem_writing"] = None

    st.session_state["reading_answer_index"] = 0
    st.session_state["listening_answer_index"] = 0
    st.session_state["writing_answer"] = ""

    st.session_state["page_state"] = "setting" # setting, answer, score

    st.session_state["config"] = os.getenv("CONFIG", "debug") # debug, develop, production


if "init" not in st.session_state:
    st.session_state["init"] = True
    initialize()


def view():
    st.title("English Problem Generator")
    page_state = st.session_state["page_state"]
    match page_state:
        case "setting":
            problem_setting.view()
        case "answer":
            problem_answer.view()
        case "score":
            problem_scoring.view()
        case _:
            problem_setting.view()


if __name__ == "__main__":
    view()
