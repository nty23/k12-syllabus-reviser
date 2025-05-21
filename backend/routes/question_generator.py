# backend/routes/question_generator.py

from flask import Blueprint, request, jsonify
from utils.groq_api import generate_questions_from_content

question_bp = Blueprint("questions", __name__)

@question_bp.route("/generate_questions", methods=["POST"])
def generate_questions():
    data = request.get_json()
    content = data.get("content", "")

    if not content.strip():
        return jsonify({"error": "Content is empty"}), 400

    questions = generate_questions_from_content(content)
    return jsonify({"questions": questions})
