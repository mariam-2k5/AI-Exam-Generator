from file_utils import extract_text_from_pdf, extract_text_from_txt, extract_text_from_url
import streamlit as st
import pandas as pd
import re

from question_generator import ExamGenerator
from evaluation_engine import AnswerEvaluator

st.set_page_config(layout="wide")
st.title("👩‍🎓 Adaptive Learning Mode")

generator = ExamGenerator()
evaluator = AnswerEvaluator()

BLOOM_LEVELS = ["Remember", "Understand", "Apply", "Analyze", "Evaluate"]

# ---------------- SESSION STATE ----------------

if "student_name" not in st.session_state:
    st.session_state.student_name = ""

if "started" not in st.session_state:
    st.session_state.started = False

if "level_index" not in st.session_state:
    st.session_state.level_index = 0

if "question" not in st.session_state:
    st.session_state.question = None

if "content" not in st.session_state:
    st.session_state.content = ""

if "feedback" not in st.session_state:
    st.session_state.feedback = None

if "page" not in st.session_state:
    st.session_state.page = "question"

if "results" not in st.session_state:
    st.session_state.results = []

if "correct" not in st.session_state:
    st.session_state.correct = 0

if "incorrect" not in st.session_state:
    st.session_state.incorrect = 0


# ---------------- START SCREEN ----------------

if not st.session_state.started:

    name = st.text_input("👤 Enter Student Name")

    content_input = st.text_area(
        "📘 Paste Study Content",
        height=200
    )

    uploaded_file = st.file_uploader(
        "📄 Upload Study Material (PDF or TXT)",
        type=["pdf", "txt"]
    )

    url_input = st.text_input("🔗 Or Enter Study Material URL")

    if uploaded_file is not None:

        if uploaded_file.type == "application/pdf":
            content_input = extract_text_from_pdf(uploaded_file)

        elif uploaded_file.type == "text/plain":
            content_input = extract_text_from_txt(uploaded_file)

    if url_input.strip() != "":
        content_input = extract_text_from_url(url_input)

    if st.button("Start Adaptive Session"):

        if name.strip() == "":
            st.warning("Please enter your name.")

        elif content_input.strip() == "":
            st.warning("Please provide study content.")

        else:

            st.session_state.student_name = name
            st.session_state.started = True
            st.session_state.content = content_input
            st.session_state.level_index = 0
            st.session_state.question = None
            st.session_state.feedback = None
            st.session_state.page = "question"
            st.session_state.results = []
            st.session_state.correct = 0
            st.session_state.incorrect = 0

            st.rerun()


# ---------------- SESSION FLOW ----------------

if st.session_state.started:

    # -------- SESSION COMPLETE --------

    if st.session_state.level_index >= len(BLOOM_LEVELS):

        st.success("🎉 Adaptive Learning Session Completed!")

        st.markdown("### Session Summary")

        st.markdown(f"""
**Student:** {st.session_state.student_name}  

**Correct Answers:** {st.session_state.correct}  

**Incorrect Answers:** {st.session_state.incorrect}
""")

        df = pd.DataFrame(st.session_state.results)
        csv = df.to_csv(index=False)

        st.download_button(
            "📥 Download Result Report",
            csv,
            "adaptive_learning_results.csv",
            "text/csv"
        )

    else:

        current_level = BLOOM_LEVELS[st.session_state.level_index]

        if st.session_state.question is None:

            st.session_state.question = generator.generate_question(
                text=st.session_state.content,
                difficulty=current_level,
                num_questions=1,
                question_type="Theory",
                marks=5,
                include_answer=False
            )

        # -------- QUESTION PAGE --------

        if st.session_state.page == "question":

            st.subheader(f"📖 Bloom Level: {current_level}")

            st.markdown("### Question")
            st.write(st.session_state.question)

            answer = st.text_area("✍️ Your Answer", key="student_answer")

            if st.button("Submit Answer"):

                if answer.strip() == "":
                    st.warning("Please write your answer.")

                else:

                    feedback = evaluator.evaluate(
                        question=st.session_state.question,
                        student_answer=answer
                    )

                    st.session_state.feedback = feedback

                    # -------- SCORE DETECTION --------

                    score = 0
                    match = re.search(r"Score\s*[:\-]?\s*(\d+)",feedback, re.IGNORECASE)

                    if match:
                        score = int(match.group(1))

                    # -------- RESULT LOGIC --------

                    if score >= 2:
                        result = "Correct"
                        st.session_state.correct += 1
                    else:
                        result = "Incorrect"
                        st.session_state.incorrect += 1

                    st.session_state.results.append({
                        "Student": st.session_state.student_name,
                        "Level": current_level,
                        "Score": score,
                        "Result": result
                    })

                    st.session_state.page = "evaluation"

                    st.rerun()

        # -------- EVALUATION PAGE --------

        elif st.session_state.page == "evaluation":

            st.markdown("### 🧠 Evaluation Result")

            clean_feedback = st.session_state.feedback.replace("Evaluation:", "")
            st.markdown(clean_feedback)

            if st.button("Next Level ➡"):

                st.session_state.level_index += 1
                st.session_state.question = None
                st.session_state.feedback = None
                st.session_state.page = "question"

                st.rerun()

        st.markdown("---")

        if st.button("Reset Session"):

            st.session_state.started = False
            st.session_state.student_name = ""
            st.session_state.level_index = 0
            st.session_state.question = None
            st.session_state.feedback = None
            st.session_state.page = "question"
            st.session_state.results = []
            st.session_state.correct = 0
            st.session_state.incorrect = 0

            st.rerun()