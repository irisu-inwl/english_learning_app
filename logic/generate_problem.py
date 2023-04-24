import json
import logging
import uuid
import asyncio
import random

import yaml
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper
from langchain.output_parsers import (
    PydanticOutputParser
)
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from logic.topics import csv_data

from logic.prompts import (
    problem_template,
    ReadingProblem,
    ListeningProblem,
    WritingProblem,
    english_test_target,
)
from custom_types.problem_types import (
    ChoiceQuestionReadingProblem, ChoiceQuestionListeningProblem, FreeDescriptionProblem
)

ProblemType = ChoiceQuestionReadingProblem | ChoiceQuestionListeningProblem | FreeDescriptionProblem
chat_model = ChatOpenAI(temperature=0)


def _save_problem_file(problem: dict, problem_type: str):
    # TODO: fileに出すのはあれなので、リリース時はDBに出す
    save_file_name = uuid.uuid4().hex
    with open(f"data/{problem_type}_problem/{save_file_name}.yaml", "w") as fw:
        fw.write(
            yaml.dump(problem, default_flow_style=False, Dumper=Dumper)
        )


def _build_prompt(
    current_cefr: str, objective_cefr: str, problem_type: str, main_topic: str, sub_topic: str
):
    template = problem_template

    if problem_type == "reading":
        response_schemas = ReadingProblem
    if problem_type == "listening":
        response_schemas = ListeningProblem
    if problem_type == "writing":
        response_schemas = WritingProblem

    # Parserの準備
    parser = PydanticOutputParser(pydantic_object=response_schemas)
    format_instructions = parser.get_format_instructions()
    
    # ChatLLM に送るプロンプトのテンプレート
    prompt = ChatPromptTemplate(
        messages=[
            HumanMessagePromptTemplate.from_template(template) 
        ],
        input_variables=[
            "current_cefr", "objective_cefr", "problem_type", 
            "english_test_target", "main_topic", "sub_topic"
        ],
        partial_variables={"format_instructions": format_instructions}
    )

    # プロンプトの作成
    _input = prompt.format_prompt(
        current_cefr=current_cefr, objective_cefr=objective_cefr, 
        problem_type=problem_type, english_test_target=english_test_target,
        main_topic=main_topic, sub_topic=sub_topic, 
    )
    
    return _input, parser


def generate_problem_by_llm(current_cefr: str, objective_cefr: str, problem_type: str):
    topic_data = random.choice(csv_data)
    main_topic = topic_data["main_topic"]
    sub_topic = topic_data["sub_topic"]
    _input, output_parser = _build_prompt(
        current_cefr, objective_cefr, problem_type, main_topic, sub_topic
    )

    # 実行
    output = chat_model(_input.to_messages())

    # parse output
    try:
        problem = output_parser.parse(output.content)
    except IndexError:
        logging.warning(output.content)
        problem = json.loads(output.content)
    

    # save
    _save_problem_file(problem, problem_type)

    return problem


def async_generate_problem_by_llm(current_cefr: str, objective_cefr: str, problem_types: list[str]):
    input_dicts = []
    for problem_type in problem_types:
        input_dict = {}
        input_dict["problem_type"] = problem_type

        topic_data = random.choice(csv_data)
        main_topic = topic_data["main_topic"]
        sub_topic = topic_data["sub_topic"]

        _input, parser = _build_prompt(
            current_cefr, objective_cefr, problem_type, main_topic, sub_topic
        )
        input_dict["prompt"] = _input
        input_dict["parser"] = parser
        input_dicts.append(input_dict)

    # 実行
    prompts = [input_dict["prompt"].to_messages() for input_dict in input_dicts]
    outputs = asyncio.run(chat_model.agenerate(prompts))
    outputs = [output_generate[0].text for output_generate in outputs.generations]
    logging.info(outputs)

    # parse output
    problems = []
    for output, input_dict in zip(outputs, input_dicts):
        problem_type = input_dict["problem_type"]
        parser = input_dict["parser"]
        problem = parser.parse(output).dict()
        
        problems.append(problem)

        # save
        _save_problem_file(problem, problem_type)

    return problems
