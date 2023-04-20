import json
import logging
import uuid
from typing import get_type_hints
import asyncio

import yaml
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper
from langchain.output_parsers import StructuredOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

from logic.prompts import (
    problem_template,
    reading_listening_response_schemas,
    writing_schemas,
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


def _build_prompt(current_cefr: str, objective_cefr: str, problem_type: str):
    template = problem_template

    if problem_type in ["reading", "listening"]:
        response_schemas = reading_listening_response_schemas
    if problem_type in ["writing"]:
        response_schemas = writing_schemas

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
    
    return _input, output_parser


def generate_problem_by_llm(current_cefr: str, objective_cefr: str, problem_type: str):
    if problem_type in ["reading", "listening"]:
        transform_type = ChoiceQuestionProblem
    if problem_type in ["writing"]:
        transform_type = FreeDescriptionProblem
    
    _input, output_parser = _build_prompt(current_cefr, objective_cefr, problem_type)

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


def async_generate_problem_by_llm(current_cefr: str, objective_cefr: str, problem_types: list[str]):
    input_dicts = []
    for problem_type in problem_types:
        input_dict = {}
        input_dict["problem_type"] = problem_type
        if problem_type in ["reading", "listening"]:
            input_dict["transform_type"] = ChoiceQuestionProblem
        if problem_type in ["writing"]:
            input_dict["transform_type"] = FreeDescriptionProblem
    
        _input, output_parser = _build_prompt(current_cefr, objective_cefr, problem_type)
        input_dict["prompt"] = _input
        input_dict["output_parser"] = output_parser
        input_dicts.append(input_dict)

    # 実行
    prompts = [input_dict["prompt"].to_messages() for input_dict in input_dicts]
    outputs = asyncio.run(chat_model.agenerate(prompts))
    outputs = [output_generate[0].text for output_generate in outputs.generations]
    logging.info(outputs)

    # parse output
    problems = []
    for output, input_dict in zip(outputs, input_dicts):
        transform_type = input_dict["transform_type"]
        problem_type = input_dict["problem_type"]
        output_parser = input_dict["output_parser"]
        try:
            problem = output_parser.parse(output)
        except IndexError:
            logging.warning(output)
            problem = json.loads(output)
        
        problem = _transform_problem(problem, transform_type)
        problems.append(problem)

        # save
        _save_problem_file(problem, problem_type)

    return problems
