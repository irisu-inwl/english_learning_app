from typing import TypedDict

class ChoiceQuestionReadingProblem(TypedDict):
    content: str
    question: str
    answer_options: list[str]
    correct_index: int
    commentary: str
    difficulty: float
    topic: str

class ChoiceQuestionListeningProblem(TypedDict):
    content: str
    passage: str
    question: str
    answer_options: list[str]
    correct_index: int
    commentary: str
    difficulty: float
    topic: str

class FreeDescriptionProblem(TypedDict):
    content: str
    question: str
    answer_example: str
    commentary: str
    difficulty: float
    topic: str
