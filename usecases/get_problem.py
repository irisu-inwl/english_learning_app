from logic.mock import (
    mock_reading_problem,
    mock_listening_problem,
    mock_writing_problem
)
from logic.generate_problem import (
    generate_problem_by_llm
)


def get_problem(current_cefr_level: str, objective_cefr_level: str):
    # TODO: Logic を分けられるようにする
    problem_reading = mock_reading_problem()
    # problem_reading = generate_problem_by_llm(current_cefr_level, objective_cefr_level, "reading")
    problem_listening = mock_listening_problem()
    problem_writing = mock_writing_problem()
    
    return problem_reading, problem_listening, problem_writing