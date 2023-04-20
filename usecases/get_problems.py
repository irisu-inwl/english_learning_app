import asyncio

import streamlit as st

from logic.mock import (
    mock_reading_problem,
    mock_listening_problem,
    mock_writing_problem
)
from logic.generate_problem import (
    generate_problem_by_llm,
    async_generate_problem_by_llm
)


async def generate_problem_concurrently():
    tasks = []
    problems = await asyncio.gather(*tasks)


def get_problems(current_cefr_level: str, objective_cefr_level: str):
    # TODO: Logic を分けられるようにする
    config = st.session_state["config"]

    if config == "debug":
        problem_reading = mock_reading_problem()
        problem_listening = mock_listening_problem()
        problem_writing = mock_writing_problem()
    else:
        # problem_reading = generate_problem_by_llm(current_cefr_level, objective_cefr_level, "reading")
        # problem_listening = generate_problem_by_llm(current_cefr_level, objective_cefr_level, "listening")
        # problem_writing = generate_problem_by_llm(current_cefr_level, objective_cefr_level, "writing")
        problem_reading, problem_listening, problem_writing = async_generate_problem_by_llm(
            current_cefr_level, objective_cefr_level, ["reading", "listening", "writing"]
        )
    
    return problem_reading, problem_listening, problem_writing