from langchain.output_parsers import ResponseSchema


problem_template = """
I am an English language learner aiming to improve my English proficiency from CEFR {current_cefr} to CEFR {objective_cefr}, focusing on {english_test_target} {problem_type} preparation.

{format_instructions}
I would like to improve my English proficiency through {english_test_target} {problem_type} preparation, ensuring that the topic is randomly chosen and not limited to a specific theme 
topic's examples include {topic_examples}.
Please submit a single question:
"""

problem_support_prompts = {
    "reading": "",
    "listening": "",
    "writing": ""
}

# 出題トピック
topics = [
    "Environmental issues",
    "Education",
    "Technology",
    "Health and medicine",
    "Globalization",
    "Employment and job market",
    "Urban and rural life",
    "Cultural differences",
    "Social issues",
    "Economics",
    "Politics and government",
    "Travel and tourism",
    "Arts and entertainment",
    "Science and research",
    "Communication and media",
    "Ethics and morality",
    "Family and relationships",
    "Climate change",
    "Sports and recreation",
    "Personal development",
]

# e.g. TOEFL, IELTS, Duolingo English Test
# TOEFLとか特定のテストを指定すると特定のトピックに偏るので一般的なワードを入れてる
english_test_target = "English Test" 

reading_response_schemas = [
    ResponseSchema(name="content", description="100-word or more sentences of 100 words or more on the subject matter in question"),
    ResponseSchema(name="question", description="Questions about problematic content"),
    ResponseSchema(name="answer_options", description="List format answer options of question"),
    ResponseSchema(name="correct_index", description="An int index (≥0) indicating the correct answer choice of answer_options"),
    ResponseSchema(name="commentary", description="Explanation of why this is the correct answer"),
    ResponseSchema(name="difficulty", description="Float type difficulty of this problem from 0.0~9.0, similar to IELTS score"),
    ResponseSchema(name="topic", description="Nouns that indicate what this question is a sentence against.")
]

listening_response_schemas = [
    ResponseSchema(name="content", description="A description of a listening situation related to listening preparation, excluding conversations"),
    ResponseSchema(name="passage", description="A listening passage related to the described situation"),
    ResponseSchema(name="question", description="Questions about problematic content"),
    ResponseSchema(name="answer_options", description="List format answer options for the question"),
    ResponseSchema(name="correct_index", description="An int index (≥0) indicating the correct answer choice of answer_options"),
    ResponseSchema(name="commentary", description="Explanation of why this is the correct answer"),
    ResponseSchema(name="difficulty", description="Float type difficulty of this problem from 0.0~9.0, similar to IELTS score"),
    ResponseSchema(name="topic", description="A noun indicating the subject matter of the content")
]

writing_response_schemas = [
    ResponseSchema(name="content", description="A writing prompt for writing preparation"),
    ResponseSchema(name="question", description="A brief explanation of the writing task"),
    ResponseSchema(name="answer_example", description="An example of a well-written response to the prompt"),
    ResponseSchema(name="commentary", description="Explanation of what makes the example response effective"),
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
    ResponseSchema(name="feedback", description="Feedback describing the strengths, weaknesses, and suggestions for improvement"),
    ResponseSchema(name="corrected", description="Suggested corrected version of the original sentence or paragraph"),
]