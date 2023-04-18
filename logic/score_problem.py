import json
import logging

from langchain.output_parsers import StructuredOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

from logic.prompts import (
    writing_scoring_template,
    writing_scoring_schemas
)

chat_model = ChatOpenAI(temperature=0)


def score_problem_by_llm(user_answer: str, writing_problem: dict):
    content = writing_problem["content"]
    question = writing_problem["question"]
    answer_example = writing_problem["answer_example"]

    # OutputParserの準備
    output_parser = StructuredOutputParser.from_response_schemas(writing_scoring_schemas)
    format_instructions = output_parser.get_format_instructions()
    
    # ChatLLM に送るプロンプトのテンプレート
    prompt = ChatPromptTemplate(
        messages=[
            HumanMessagePromptTemplate.from_template(writing_scoring_template) 
        ],
        input_variables=["current_cefr", "objective_cefr", "problem_type"],
        partial_variables={"format_instructions": format_instructions}
    )

    # プロンプトの作成
    _input = prompt.format_prompt(
        user_answer=user_answer, content=content, question=question, answer_example=answer_example
    )
    
    # 実行
    output = chat_model(_input.to_messages())

    # parse output
    try:
        score_and_commentary = output_parser.parse(output.content)
    except IndexError:
        logging.warning(output.content)
        score_and_commentary = json.loads(output.content)
    
    # problem = _transform_problem(problem, transform_type)

    # save
    # _save_problem_file(problem, problem_type)

    return score_and_commentary