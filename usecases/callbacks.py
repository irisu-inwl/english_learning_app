import streamlit as st

from usecases.get_problems import get_problems
from usecases.transform_text_to_speech import transform_text_to_speech
from logic.score_problem import score_problem_by_llm


def callback_problem_answer():
    st.session_state["page_state"] = "score"
    writing_answer = st.session_state["writing_answer"]
    writing_problem = st.session_state["problem_writing"]

    writing_scoring = score_problem_by_llm(writing_answer, writing_problem)
    st.session_state["system_score"] = writing_scoring["score"]
    st.session_state["system_feedback"] = writing_scoring["feedback"]
    st.session_state["system_corrected"] = writing_scoring["corrected"]


def callback_go_back_generate():
    st.session_state["page_state"] = "setting"


def callback_problem_generate():
    st.session_state["page_state"] = "answer"
    current_cefr_level = st.session_state["current_cefr_level"]
    objective_cefr_level = st.session_state["objective_cefr_level"]

    # usecases内でusecases呼ぶことで森羅万象ディレクトリになりそうだけどそうなったら考える
    problem_reading, problem_listening, problem_writing = get_problems(current_cefr_level, objective_cefr_level)

    st.session_state["problem_reading"] = problem_reading
    st.session_state["problem_listening"] = problem_listening
    st.session_state["problem_writing"] = problem_writing

    listening_passage = problem_listening["passage"]
    listening_audio = transform_text_to_speech(listening_passage)

    st.session_state["listening_audio"] = listening_audio
