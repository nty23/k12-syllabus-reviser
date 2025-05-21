# K12 Syllabus Reviser - High-Level Design & Architecture

## 1. Overview

The **K12 Syllabus Reviser** is an AI-powered study assistant application designed to generate custom study questions and answers across various subjects and formats. It aims to help K-12 students revise effectively through an interactive user interface and AI-driven backend.

---

## 2. System Components

### 2.1 Frontend (Streamlit App)

- Provides a clean, interactive user interface for students to:
  - Select subjects and topics
  - Choose question format (MCQ, Q&A, Fill in the blanks, Type Answer)
  - Input answers and receive feedback with explanations
  - Download question sets as PDFs
- Communicates with backend via HTTP POST requests to fetch AI-generated questions.
- Manages user state (questions, answers, and results) locally using Streamlit's session state.

---

### 2.2 Backend (Flask API Server)

- Exposes a RESTful API endpoint `/generate_questions` for question generation requests.
- Receives user parameters (subject, topic, question count, mode) and interacts with the Groq LLaMA 3 API.
- Processes AI responses, formats questions with:
  - Question text
  - Options (for MCQ, ensuring correct answer included)
  - Correct answer
  - Explanation (optional)
  - Mode/type of question
- Returns JSON responses with structured question data.

---

### 2.3 AI Model (Groq LLaMA 3 API)

- A large language model accessed via Groq API.
- Generates high-quality, contextually relevant questions and answers based on prompts created dynamically by backend.
- Supports multiple question formats.
- Provides explanations to aid understanding.

---

## 3. Data Flow Diagram

```mermaid
flowchart TD
    User -->|Interacts via UI| Frontend
    Frontend -->|POST /generate_questions| Backend
    Backend -->|API request| Groq LLaMA 3 API
    Groq LLaMA 3 API --> Backend
    Backend --> Frontend
    Frontend -->|Displays questions & explanations| User


## 4. Technology Stack

Component	Technology
Frontend	Streamlit (Python)
Backend API	Flask (Python)
AI Model	Groq LLaMA 3 API
PDF Generation	FPDF (Python)

## 5. Hardware Requirements

Development Machine:
Minimum: 2 CPU cores, 4GB RAM, Internet connection
OS: Windows/macOS/Linux with Python 3.8+
Deployment:
Cloud VM or server with similar or higher specs for reliable uptime
API key for Groq LLaMA 3 (requires internet)

## 6. Future Enhancements

User authentication and personalized study profiles
More subjects and languages support
Enhanced analytics to track learning progress
Mobile-friendly frontend version
Integration with school LMS platforms

## 7. Conclusion

The design ensures modularity with clear separation of concerns between frontend, backend, and AI services, enabling easy maintenance and future scalability. The chosen tech stack balances ease of development with performance for a seamless user experience.

