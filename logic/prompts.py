from langchain.output_parsers import ResponseSchema


reading_listening_problem_template = """I am an English language learner.
My current English proficiency level is about CEFR {current_cefr}.
I would like to improve my English proficiency level to CEFR {objective_cefr} through English study.
{format_instructions}
I would like to improve my English proficiency through TOEFL {problem_type} preparation.
Please submit question:
"""

reading_listening_response_schemas = [
    ResponseSchema(name="content", description="Put a text suitable for a reading comprehension question"),
    ResponseSchema(name="question", description="Questions about problematic content"),
    ResponseSchema(name="answer_options", description="List format answer options of question"),
    ResponseSchema(name="correct", description="Correct answer index starting from 0"),
    ResponseSchema(name="commentary", description="Explanation of why this is the correct answer"),
    ResponseSchema(name="difficulty", description="Float type difficulty of this problem from 0.0~9.0, similar to IELTS score"),
    ResponseSchema(name="topic", description="Nouns that indicate what this question is a sentence against.")
]


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
    ResponseSchema(name="comments", description="Comments on the user's answer"),
]