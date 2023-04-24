from langchain.output_parsers import ResponseSchema
from pydantic import BaseModel, Field


problem_template = """
I am an English language learner aiming to improve my English proficiency from CEFR {current_cefr} to CEFR {objective_cefr}, focusing on {english_test_target} {problem_type} preparation.

{format_instructions}
Please submit single problem and question related to the topic {main_topic} and subtopic {sub_topic}:
"""


# e.g. TOEFL, IELTS, Duolingo English Test
# TOEFLとか特定のテストを指定すると特定のトピックに偏るので一般的なワードを入れてる
english_test_target = "English Test" 


class ReadingProblem(BaseModel):
    content: str = Field("About 500~800-word sentences on the subject matter in question")
    question: str = Field("Questions about problematic content")
    answer_options: list[str] = Field("List format answer options of question")
    correct_index: int = Field("An int index (≥0) indicating the correct answer choice of answer_options")
    commentary: str = Field("Explanation of why this is the correct answer")
    difficulty: float = Field("Float type difficulty of this problem from 0.0~9.0, similar to IELTS score")


class ListeningProblem(BaseModel):
    content: str = Field("A description of a listening situation related to listening preparation, excluding conversations")
    passage: str = Field("A listening passage related to the described situation")
    question: str = Field("Questions about problematic content")
    answer_options: list[str] = Field("List format answer options of question")
    correct_index: int = Field("An int index (≥0) indicating the correct answer choice of answer_options")
    commentary: str = Field("Explanation of why this is the correct answer")
    difficulty: float = Field("Float type difficulty of this problem from 0.0~9.0, similar to IELTS score")


class WritingProblem(BaseModel):
    content: str = Field("A writing prompt for writing preparation")
    question: str = Field("A brief explanation of the writing task")
    answer_example: str = Field("An example of a well-written response to the prompt")
    commentary: str = Field("Explanation of what makes the example response effective")
    difficulty: float = Field("Float type difficulty of this problem from 0.0~9.0, similar to IELTS score")


writing_scoring_template = """You are an English exam grader.
Please grade and point out the user's answers given below:
Content: {content}
Question: {question}
Answer Example: {answer_example}
User Answer: {user_answer}

{format_instructions}
"""

writing_scoring_schemas = [
    ResponseSchema(name="score", description="Score from 0.0 to 10.0 for the user answer"),
    ResponseSchema(name="feedback", description="Feedback describing the strengths, weaknesses, and suggestions for improvement"),
    ResponseSchema(name="corrected", description="Suggested corrected version of the original sentence or paragraph"),
]