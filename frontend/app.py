import streamlit as st
import requests
from fpdf import FPDF
import random

st.set_page_config(page_title="K12 Syllabus Reviser", layout="wide")

API_URL = "http://localhost:5000/generate_questions"

# Sidebar options
st.sidebar.title("K12 Reviser Settings")
subject = st.sidebar.selectbox("Choose Subject", ["Science", "English", "Hindi", "History", "Geology", "Others"])
custom_subject = ""
if subject == "Others":
    custom_subject = st.sidebar.text_input("Enter custom subject")

topic = st.sidebar.text_input("Enter Topic")
question_count = st.sidebar.slider("Number of Questions", 1, 20, 5)
mode = st.sidebar.selectbox("Study Format", ["MCQ", "Q&A", "Fill in the blanks", "Type Answer"])

if st.sidebar.button("Generate Questions", key="generate_btn"):
    with st.spinner("Generating questions..."):
        payload = {
            "subject": subject,
            "custom_subject": custom_subject,
            "topic": topic,
            "question_count": question_count,
            "mode": mode
        }

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            st.session_state.questions = response.json().get("questions", [])
            st.session_state.show_answers = False
            st.rerun()
        else:
            st.error("Failed to fetch questions")

# Display questions
if "questions" in st.session_state:
    st.title("🔍 Study Mode: " + mode)

    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}

    for idx, q in enumerate(st.session_state.questions):
        st.markdown(f"**Q{idx+1}. {q['question']}**")

        key = f"answer_{idx}"
        user_answer = None

        if q["mode"] == "MCQ":
            user_answer = st.radio("Options", q["options"], key=key)
        elif q["mode"] == "Fill in the blanks":
            user_answer = st.text_input("Your Answer:", key=key)
        elif q["mode"] == "Type Answer":
            user_answer = st.text_area("Your Answer:", key=key)
        elif q["mode"] == "Q&A":
            st.markdown(f"**Answer:** {q['answer']}")
            if q.get("explanation"):
                st.info(f"💡 Explanation: {q['explanation']}")

        st.session_state.user_answers[key] = user_answer

    if st.button("Check My Answers", key="check_answers_btn"):
        st.session_state.show_answers = True
        st.rerun()

    if st.session_state.get("show_answers", False):
        st.subheader("✅ Results")

        for idx, q in enumerate(st.session_state.questions):
            user_key = f"answer_{idx}"
            user_answer = st.session_state.user_answers.get(user_key, "").strip().lower()
            correct_answer = q["answer"].strip().lower()

            st.markdown(f"**Q{idx+1}. {q['question']}**")
            st.markdown(f"**Your Answer:** {st.session_state.user_answers.get(user_key, '')}**")

            if user_answer == correct_answer:
                st.success("Correct!")
            else:
                st.error(f"Incorrect. Correct Answer: {q['answer']}")

            if q.get("explanation"):
                st.info(f"💡 Explanation: {q['explanation']}")

    # Generate More Questions
    if st.button("Generate More Questions", key="generate_more_btn"):
        more_payload = {
            "subject": subject,
            "custom_subject": custom_subject,
            "topic": topic,
            "question_count": question_count,
            "mode": mode
        }

        with st.spinner("Generating more questions..."):
            response = requests.post(API_URL, json=more_payload)

            if response.status_code == 200:
                st.session_state.questions = response.json().get("questions", [])
                st.session_state.show_answers = False
                st.session_state.user_answers = {}
                st.rerun()
            else:
                st.error("❌ Failed to generate more questions.")

    # PDF Export
    if st.button("Download as PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for i, q in enumerate(st.session_state.questions):
            pdf.multi_cell(0, 10, f"Q{i+1}: {q['question']}")
            if q["mode"] == "MCQ":
                for opt in q["options"]:
                    pdf.multi_cell(0, 10, f" - {opt}")
            pdf.multi_cell(0, 10, f"Answer: {q['answer']}")
            if q.get("explanation"):
                pdf.multi_cell(0, 10, f"Explanation: {q['explanation']}")
            pdf.cell(0, 10, "", ln=True)

        pdf_file = "questions.pdf"
        pdf.output(pdf_file)
        with open(pdf_file, "rb") as f:
            st.download_button("📥 Download PDF", data=f, file_name="questions.pdf")
