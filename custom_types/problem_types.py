from typing import TypedDict

class ChoiceQuestionProblem(TypedDict):
    content: str
    question: str
    answer_options: list[str]
    correct: int
    commentary: str
    difficulty: float
    category: str

class FreeDescriptionProblem(TypedDict):
    content: str
    question: str
    answer_example: str
    commentary: str
    difficulty: float
    topic: str
