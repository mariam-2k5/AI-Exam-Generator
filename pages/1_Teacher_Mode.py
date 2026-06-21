from file_utils import extract_text_from_pdf, extract_text_from_txt, extract_text_from_url
import streamlit as st
from question_generator import ExamGenerator
from pdf_generator import create_pdf

st.set_page_config(layout="wide")
st.title("🧑‍🏫 Teacher Mode – Section Based Exam Paper Generator")

generator = ExamGenerator()

# ---------------- HEADER DETAILS ----------------

college_name = st.text_input("🏫 College Name", "ABC College of Engineering")
subject_name = st.text_input("📘 Subject Name", "Computer Fundamentals")
exam_title = st.text_input("📝 Examination Title", "Internal Examination")
exam_time = st.text_input("⏰ Duration", "3 Hours")

st.markdown("---")

# ---------------- STUDY MATERIAL ----------------

study_content = st.text_area("📚 Paste Study Material", height=200)

uploaded_file = st.file_uploader(
    "📄 Upload Study Material (PDF or TXT)",
    type=["pdf", "txt"]
)

url_input = st.text_input("🔗 Or Enter Study Material URL")

# Convert uploaded content into text
if uploaded_file is not None:

    if uploaded_file.type == "application/pdf":
        study_content = extract_text_from_pdf(uploaded_file)

    elif uploaded_file.type == "text/plain":
        study_content = extract_text_from_txt(uploaded_file)

if url_input.strip() != "":
    study_content = extract_text_from_url(url_input)

st.markdown("---")

# ---------------- SECTION CONFIGURATION ----------------

st.subheader("📑 Section Configuration")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Section A")
    a_type = st.selectbox("Question Type (A)", ["MCQ", "Theory"])
    a_bloom = st.selectbox("Bloom Level (A)", ["Remember", "Understand", "Apply", "Analyze", "Evaluate"])
    a_count = st.number_input("No. of Questions (A)", 1, 20, 5)
    a_marks = st.number_input("Marks per Question (A)", 1, 20, 1)

with col2:
    st.markdown("### Section B")
    b_type = st.selectbox("Question Type (B)", ["MCQ", "Theory"])
    b_bloom = st.selectbox("Bloom Level (B)", ["Remember", "Understand", "Apply", "Analyze", "Evaluate"])
    b_count = st.number_input("No. of Questions (B)", 1, 20, 3)
    b_marks = st.number_input("Marks per Question (B)", 1, 20, 5)

with col3:
    st.markdown("### Section C")
    c_type = st.selectbox("Question Type (C)", ["MCQ", "Theory"])
    c_bloom = st.selectbox("Bloom Level (C)", ["Remember", "Understand", "Apply", "Analyze", "Evaluate"])
    c_count = st.number_input("No. of Questions (C)", 1, 20, 2)
    c_marks = st.number_input("Marks per Question (C)", 1, 20, 10)

st.markdown("---")

include_answers = st.checkbox("☑ Include Answer Key")

# ---------------- GENERATE EXAM ----------------

if st.button("🚀 Generate Exam Paper"):

    if study_content.strip() == "":
        st.warning("Please paste study material before generating the paper.")

    else:

        total_marks = (
            (a_count * a_marks) +
            (b_count * b_marks) +
            (c_count * c_marks)
        )

        header_text = f"""
{college_name}
{exam_title}
Subject: {subject_name}
Time: {exam_time}
Max Marks: {total_marks}
"""

        st.markdown("## 📄 Generated Question Paper")

        st.markdown(f"""
**{college_name}**  
**{exam_title}**  
**Subject:** {subject_name}  
**Time:** {exam_time}  
**Max Marks:** {total_marks}

---
""")

        st.markdown(f"### Section A ({a_count} × {a_marks})")
        section_a = generator.generate_question(
            text=study_content,
            difficulty=a_bloom,
            num_questions=a_count,
            question_type=a_type,
            marks=a_marks,
            include_answer=include_answers
        )
        st.text(section_a)

        st.markdown("---")

        st.markdown(f"### Section B ({b_count} × {b_marks})")
        section_b = generator.generate_question(
            text=study_content,
            difficulty=b_bloom,
            num_questions=b_count,
            question_type=b_type,
            marks=b_marks,
            include_answer=include_answers
        )
        st.text(section_b)

        st.markdown("---")

        st.markdown(f"### Section C ({c_count} × {c_marks})")
        section_c = generator.generate_question(
            text=study_content,
            difficulty=c_bloom,
            num_questions=c_count,
            question_type=c_type,
            marks=c_marks,
            include_answer=include_answers
        )
        st.text(section_c)

        st.success("✅ Exam Paper Generated Successfully!")

        full_text = header_text + "\n\nSection A\n" + section_a + "\n\nSection B\n" + section_b + "\n\nSection C\n" + section_c

        pdf_file = create_pdf(full_text)

        with open(pdf_file, "rb") as f:
            st.download_button(
                label="📥 Download Exam Paper (PDF)",
                data=f,
                file_name="exam_paper.pdf",
                mime="application/pdf"
            )