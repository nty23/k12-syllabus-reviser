# backend/utils/groq_api.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = os.getenv("GROQ_API_URL")
GROQ_MODEL = os.getenv("GROQ_MODEL")

def generate_questions_from_content(content):
    prompt = f"""
You are an educational assistant. Generate 5 diverse K-12 level questions (MCQs, Fill-in-the-blanks, and True/False) from this content:

Content:
{content}
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error generating questions: {str(e)}"
