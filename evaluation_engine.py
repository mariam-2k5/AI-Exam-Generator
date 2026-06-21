from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

class AnswerEvaluator:

    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def evaluate(self, question, student_answer):

        prompt = f"""
You are an AI educational evaluator.

Evaluate the student's answer in a supportive academic way.

Question:
{question}

Student Answer:
{student_answer}

Evaluation Rules:
- Give a score between 0 and 5
- Even partially correct answers should receive 2 or 3
- Do not be overly strict
- Encourage the student

Return the evaluation EXACTLY in this format:

Score: X/5

Strength:
One short sentence about what the student did sorrectly

Improvement:
One short sentence about what could be improved.
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return response.choices[0].message.content