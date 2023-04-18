from logic.score_problem import score_problem_by_llm


def score_problem(writing_answer: str, writing_problem: dict):
    _ = score_problem_by_llm(writing_answer, writing_problem)
