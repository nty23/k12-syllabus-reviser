from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from groq import Groq
import ast
import random
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def build_prompt(subject, custom_subject, topic, question_count, mode):
    final_subject = custom_subject if subject == "Others" else subject
    prompt = f"""
You are a K-12 teacher. Generate {question_count} questions in the format: {mode}.

Topic: {topic}
Subject: {final_subject}

Instructions:
- Provide structured output as a list of Python dicts.
- For each question, include:
  - "question"
  - "options" (only for MCQ)
  - "answer"
  - "explanation"

Example Output:
[
  {{
    "question": "What is the function of mitochondria?",
    "options": ["Energy storage", "Digestion", "Energy production", "DNA replication"],
    "answer": "Energy production",
    "explanation": "Mitochondria is the powerhouse of the cell."
  }}
]
If format is "Fill in the blanks", format like:
[
  {{
    "question": "Mitochondria is the ________ of the cell.",
    "answer": "powerhouse",
    "explanation": "Mitochondria produces energy, hence called the powerhouse."
  }}
]
Only return the list of questions. Do not explain or say anything else.
"""
    return prompt.strip()

def ensure_correct_mcq_options(questions):
    for q in questions:
        if q.get("mode") == "MCQ" or ("options" in q and isinstance(q["options"], list)):
            answer = q.get("answer")
            options = q.get("options", [])
            if answer and answer not in options:
                options.append(answer)
            q["options"] = random.sample(list(set(options)), k=len(set(options)))
    return questions

@app.route("/")
def home():
    return "K12 Reviser Backend Running"

@app.route("/generate_questions", methods=["POST"])
def generate_questions():
    try:
        data = request.get_json()

        subject = data.get("subject", "")
        custom_subject = data.get("custom_subject", "")
        topic = data.get("topic", "")
        question_count = int(data.get("question_count", 5))
        mode = data.get("mode", "MCQ")

        prompt = build_prompt(subject, custom_subject, topic, question_count, mode)

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )

        content = response.choices[0].message.content
        print("Groq Response:", content)

        questions = ast.literal_eval(content.strip())

        # Inject mode and fix MCQ options
        for q in questions:
            q["mode"] = mode

        if mode == "MCQ":
            questions = ensure_correct_mcq_options(questions)

        return jsonify({"questions": questions})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
