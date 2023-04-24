import asyncio

import streamlit as st

from logic.mock import (
    mock_reading_problem,
    mock_listening_problem,
    mock_writing_problem
)
from logic.generate_problem import (
    async_generate_problem_by_llm
)


def get_problems(current_cefr_level: str, objective_cefr_level: str):
    # TODO: Logic を分けられるようにする
    config = st.session_state["config"]

    if config == "debug":
        problem_reading = mock_reading_problem()
        problem_listening = mock_listening_problem()
        problem_writing = mock_writing_problem()
    else:
        problem_reading, problem_listening, problem_writing = async_generate_problem_by_llm(
            current_cefr_level, objective_cefr_level, ["reading", "listening", "writing"]
        )
    
    return problem_reading, problem_listening, problem_writing