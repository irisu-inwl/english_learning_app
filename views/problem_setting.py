import streamlit as st

from usecases.callbacks import callback_problem_generate


def view():
    st.header("Setting Problem")
    with st.form(key="setting_form"):
        st.radio("Current CEFR Level:", [
            "A1", "A2", "B1", "B2", "C1", "C2"
        ], horizontal=True, key="current_cefr_level")
        st.radio("Objective CEFR Level:", [
            "A1", "A2", "B1", "B2", "C1", "C2"
        ], horizontal=True, key="objective_cefr_level")
        st.form_submit_button("Generate", on_click=callback_problem_generate)

    st.info("""CEFR stands for Common European Framework of Reference for Languages and is a set of guidelines used to describe the outcomes of foreign language learners.
- A1: Breakthrough level, corresponding IELTS score is about 2.0
- A2: Waystage level, corresponding IELTS score is about 3.0
- B1: Threshold level, corresponding IELTS score is about 4.0-5.0
- B2: Vantage level, corresponding IELTS score is about 5.5-6.5
- C1: Advanced level, corresponding IELTS score is about 7.0-8.0
- C2: Mastery level, corresponding IELTS score is about 8.5-9.0
"""
    )