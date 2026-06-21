from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

class ExamGenerator:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate_question(self, text, difficulty, num_questions, question_type, marks, include_answer=True):

        if include_answer:
            answer_instruction = """
Include answers.

For MCQs:
- Provide 4 options labeled A, B, C, D.
- After all questions, provide:

Answer Key:
1. Correct Option
2. Correct Option

For Theory:
- After each question, provide a short structured answer.
"""
        else:
            answer_instruction = """
Generate ONLY the questions.
DO NOT provide answers.
DO NOT mention anything about answers.
DO NOT mention include_answer.
"""

        prompt = f"""
You are a professional university exam paper generator.

STRICT FORMATTING RULES (VERY IMPORTANT):

If question type is MCQ:

- Each question must be numbered.
- The question must be on its own line.
- Each option MUST be on a NEW LINE.
- NEVER put options in the same line.
- Format EXACTLY like this:

1. Question text

A. Option 1
B. Option 2
C. Option 3
D. Option 4

Leave one blank line after each question.

If question type is Theory:

- Only write the question.
- Number properly.
- Do NOT write options.

Generate {num_questions} {question_type} questions
at Bloom's Taxonomy level: {difficulty}.
Each question carries {marks} marks.

{answer_instruction}

Study Material:
{text}
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return response.choices[0].message.content