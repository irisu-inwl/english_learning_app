import json
import logging
import uuid
from typing import get_type_hints

import yaml
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper
from langchain.output_parsers import StructuredOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

from logic.prompts import (
    reading_listening_problem_template,
    reading_listening_response_schemas,
)
from custom_types.problem_types import ChoiceQuestionProblem, FreeDescriptionProblem

ProblemType = ChoiceQuestionProblem | FreeDescriptionProblem
chat_model = ChatOpenAI(temperature=0)


def _transform_problem(problem: dict, transform_type: ProblemType):
    # FIXME: pydantic parser使えば良いと思う
    output: ProblemType = {}
    type_hints = get_type_hints(transform_type)
    
    for key, var_type in type_hints.items():
        output[key] = var_type(problem[key])
    
    return output


def _save_problem_file(problem: dict, problem_type: str):
    # TODO: fileに出すのはあれなので、リリース時はDBに出す
    save_file_name = uuid.uuid4().hex
    with open(f"data/{problem_type}_problem/{save_file_name}.yaml", "w") as fw:
        fw.write(
            yaml.dump(problem, default_flow_style=False, Dumper=Dumper)
        )


def generate_problem_by_llm(current_cefr: str, objective_cefr: str, problem_type: str):
    if problem_type in ["reading", "listening"]:
        response_schemas = reading_listening_response_schemas
        template = reading_listening_problem_template
        transform_type = ChoiceQuestionProblem

    # OutputParserの準備
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()
    
    # ChatLLM に送るプロンプトのテンプレート
    prompt = ChatPromptTemplate(
        messages=[
            HumanMessagePromptTemplate.from_template(template) 
        ],
        input_variables=["current_cefr", "objective_cefr", "problem_type"],
        partial_variables={"format_instructions": format_instructions}
    )

    # プロンプトの作成
    _input = prompt.format_prompt(
        current_cefr=current_cefr, objective_cefr=objective_cefr, problem_type=problem_type)
    
    # 実行
    output = chat_model(_input.to_messages())

    # parse output
    try:
        problem = output_parser.parse(output.content)
    except IndexError:
        logging.warning(output.content)
        problem = json.loads(output.content)
    
    problem = _transform_problem(problem, transform_type)

    # save
    _save_problem_file(problem, problem_type)

    return problem
